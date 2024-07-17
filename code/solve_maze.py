clear()
print('finding maze')
def start_maze():
    clear()
    while not get_entity_type() == Entities.Hedge:

        if not plant(Entities.Bush): # treasure spawned below us
            harvest()
        while get_entity_type() == Entities.Bush:

            # pumpkins too low?
            while num_items(Items.Pumpkin) < get_world_size()*2:
                print("Not enough pumpkins!")
                do_a_flip(  )
                do_a_flip(  )   
                    
            trade(Items.Fertilizer)
            use_item(Items.Fertilizer)

    return True



def treasure():
# check if treasure is found
    if  get_entity_type() == Entities.Treasure:
        return True
    else:
        return False

def solve_maze():

    directions = [North,  East, South, West]
    dir_index = 0
    visited = []

    while not treasure():
        for i in range(3):
            forwards = directions[dir_index]
            if move(forwards):
                dir_index = (dir_index + 1) % 4 # turn right
            else:
                dir_index = (dir_index - 1) % 4 # turn left

    return True


while True:
    if start_maze():
        if solve_maze():

            harvest()
