till_map()
goto_origin()
print("STARTING FARM")

occupied_tiles = list() # vaariable of int is passed by value, so we need to use a list instead.
while True:
    def farm_bush():
        

        if can_harvest():
            occupied_tiles.append(1)
        
        if not num_items(Items.Pumpkin_Seed)and not trade(Items.Pumpkin_Seed, get_world_size()**2):
            traverse_map(harvest)
            if num_items(Items.Carrot_Seed) < get_world_size()**2:
                print("Not enough Carrots!")
            if num_items(Items.Wood) < get_world_size()**2:
                print("Not enough Wood!")
        plant(Entities.Pumpkin)
        water()
        fertilize()
        if len(occupied_tiles) == get_world_size()**2:
            quick_print("occupied all tiles")
            harvest()
            while len(occupied_tiles) !=0:
                occupied_tiles.pop()
        else:
            quick_print("not occupied all tiles", len(occupied_tiles), get_world_size()**2)
        # water()
        
    
    traverse_map(farm_bush)
