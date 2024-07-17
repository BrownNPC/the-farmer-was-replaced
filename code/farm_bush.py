till_map()
goto_origin()
print("STARTING FARM")
while True:
    def farm_bush():
        if can_harvest() and get_entity_type() == Entities.Bush:
            harvest()
        plant(Entities.Bush)
        water()
        
    
    traverse_map(farm_bush)
