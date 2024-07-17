def water():
    if get_water() < 0.5:
        use_item(Items.Water_Tank)

    
def traverse_map(func=None, step=1):
        for col in range(1, get_world_size()+1):
            
            #opposite direction we used last column
            Pdirection = North 
            if col % 2 == 0:
                Pdirection = South

            # iterate over all tiles in a column and run func
            for i in range(get_world_size()):
                if step and i % step == 0:
                    if func != None:
                        func()
                
                # stop moving in the X axis when at last tile, 
                # by moving east 1 more time we land on the first tile.
                if i+1 != get_world_size():
                    move(Pdirection)
                
            move(East)


def till_map():
    def clean_map():
        if can_harvest():
            harvest()
        if get_ground_type != Grounds.Soil:
            till()
    traverse_map(clean_map)

def reverse_list(lst):
    if not lst:
        return lst
    temp_list = []
    for i in range(len(lst),0, -1):
        temp_list.append(lst[i-1])
    return temp_list

def backwards(direction):
    if direction == North:
        return South
    elif direction == East:
        return West
    elif direction == South:
        return North
    elif direction == West:
        return East

def dict_keys(dictionary):
    temp = []
    for key in dictionary:
        temp.append(dictionary[key]) 
    return temp

def fertilize():
    if num_items(Items.Fertilizer) < get_world_size():
        trade(Items.Fertilizer, get_world_size()**2)
    use_item(Items.Fertilizer)

def goto_origin():
    while get_pos_x() != 0 or get_pos_y() != 0:
        if get_pos_x() != 0:
            if get_pos_x() < 0:
                move(West)
            else:
                move(East)
        if get_pos_y() != 0:
            if get_pos_y() < 0:
                move(South)
            else:
                move(North)