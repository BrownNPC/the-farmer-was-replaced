


traverse_map(harvest)
clear()
traverse_map(till)
print("STARTING FARM")
prev_tile_occupied = False # used to space trees by 1 tile
def farm_tree():
    if can_harvest():
        harvest()
    plant(Entities.Tree)
    water()
while True:

        
        
    
    traverse_map(farm_tree, 2)
