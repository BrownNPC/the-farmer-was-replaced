from farm_tree import farm_tree
from farm_grass import farm_grass


till_map()

print("STARTING FARM")
while True:
    def farm_carrot():
        if can_harvest():
            harvest()
        if not num_items(Items.Carrot_Seed)and not trade(Items.Carrot_Seed, get_world_size()**2) :
            traverse_map(harvest)
            if num_items(Items.Wood) < (get_world_size()**5):
                print("Not enough Wood!")
                while num_items(Items.Wood) < (get_world_size()**5):
                    traverse_map(farm_tree, 2)
                    

            if num_items(Items.Hay) < (get_world_size()**5):
                print("Not enough Hay!")
                clear()
                while num_items(Items.Hay) < (get_world_size()**5):
                    traverse_map(farm_grass)    
                till_map()

        plant(Entities.Carrots)
        water()
        
    
    traverse_map(farm_carrot)
