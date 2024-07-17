till_map()
goto_origin()
print("STARTING FARM")
while True:

    petals = []

    def farm_bush():


        if not num_items(Items.Sunflower_Seed)and not trade(Items.Sunflower_Seed, 2) :
            traverse_map(harvest)
            if num_items(Items.Carrot) < get_world_size():
                print("Not enough Carrots!")
        

        plant(Entities.Sunflower)
        petals.append(measure())
        water()
        fertilize()

    def harvest_sunflower():
        max_petals = max(petals)
        if can_harvest() and get_entity_type() == Entities.Sunflower and measure() == max_petals:
            harvest()

    traverse_map(farm_bush)


    traverse_map(harvest_sunflower)