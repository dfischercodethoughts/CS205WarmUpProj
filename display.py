import menu_options

def display_key_and_value(key,value,left_size=25,right_size=25):
    if value != "" and value != 0:
        if value == None:
            value = ""
        new_key = key
        if len(key) > 2:
            new_key = key[0].upper() + key[1:len(key)].lower()
        return_str = "|{:>" + str(left_size) + "}:{:<" + str(right_size) + "}|"
        return_str = return_str.format(new_key,value)
        print(return_str)
        return True
    return False

def display_pokemon(dictionary):
    first_last_str = " "
    first_last_str += "-" * 51
    print(first_last_str)
    display_key_and_value("name",dictionary.get("name"))
    display_key_and_value("type 1",dictionary.get("type1"))
    if dictionary.get("type_2") != "":
        display_key_and_value("type 2",dictionary.get("type2"))
    display_key_and_value("Health",dictionary.get("hp"))
    display_key_and_value("primary attack",dictionary.get("primary_attack"))
    display_key_and_value("secondary attack",dictionary.get("secondary_attack"))
    if dictionary.get("evolution_level") != 0:
        display_key_and_value("evolves at level",dictionary.get("evolution_level"))
    print(first_last_str)
    
def display_pokemon_evolutions(list_of_dics, poke_name):
    header = poke_name[0].upper() + poke_name[1:len(poke_name)] + " Evolutions"
    print("{:^50}".format(header))
    print("-" * 52)
    for dic in list_of_dics:
        print("-" * 52)
        #print(dic)
        if dic.get("is_parent"):
            display_key_and_value("Parent Poke"," " +dic.get('poke_name'),20,30)
        if dic.get("is_child"):
            display_key_and_value("Child Poke", " " +dic.get("poke_name"),20,30)
        if dic.get("is_item_used") != None and dic.get("is_item_used") != 0:
            display_key_and_value("Item used",dic.get("item_used"),20,30)
        if dic.get("is_bred") != None and dic.get("is_bred") != 0:
            display_key_and_value("","By breeding.",20,30)
        if dic.get("is_evolve") != None and dic.get("is_evolve") != 0:
            display_key_and_value("", "By evolution.",20,30)
        if dic.get("is_traded") != None and dic.get("is_traded") != 0:
            display_key_and_value("","By trading.",20,30)
        if dic.get("additional_requirements") != 0 and dic.get("additional_requirements") != None and dic.get("additional_requirements") != "":
            display_key_and_value("Additional reqs:",dic.get("additional_requirements"))
        print("-" * 52)
    print("No more associated evolutions")

def display_pokemon_attacks(dic,pokemon_name):
    header = pokemon_name[0].upper() + pokemon_name[1:len(pokemon_name)].lower()
    header = header + " Attacks"
    
    print("{:^50}".format(header))
    print("-" * 52)
    if dic.get("primary_att_name") != "":
        display_key_and_value("Primary attack",dic.get("primary_att_name"),20,30)
        if dic.get("primary_att_damage") != None and str(dic.get("primary_att_damage")) != "" and dic.get("primary_att_damage") != 0:
            display_key_and_value("Damage",str(dic.get("primary_att_damage")),20,30)
        else:
            display_key_and_value("No damage","see effect",20,30)
        display_key_and_value("Targets",dic.get("primary_att_targets"),20,30)
        display_key_and_value("Power points",dic.get("primary_att_pp"),20,30)
        if dic.get("primary_att_accuracy") != None and dic.get("primary_att_accuracy")!=0 and str(dic.get("primary_att_accuracy"))!="":
            display_key_and_value("Accuracy",dic.get("primary_att_accuracy"),20,30)
        else:
            display_key_and_value("No accuracy","See effect",20,30)
        display_key_and_value("Effect",dic.get("primary_att_effect"),20,30)
    else:
        print("No primary attack found.")
    print("\n")
    if dic.get("secondary_att_name") != "":
        display_key_and_value("Secondary attack",dic.get("secondary_att_name"),20,30)
        if dic.get("secondary_att_damage") != None and str(dic.get("secondary_att_damage")) != "" and dic.get("secondary_att_damage") != 0:
            display_key_and_value("Damage",str(dic.get("secondary_att_damage")),20,30)
        else:
            display_key_and_value("No damage","See effect",20,30)
        display_key_and_value("Targets",dic.get("secondary_att_targets"),20,30)
        display_key_and_value("Power points",dic.get("secondary_att_pp"),20,30)
        if dic.get("secondary_att_accuracy") != None and dic.get("secondary_att_accuracy")!=0 and str(dic.get("secondary_att_accuracy"))!="":
            display_key_and_value("Accuracy",dic.get("secondary_att_accuracy"),20,30)
        else:
            display_key_and_value("No accuracy","See effect",20,30)
        display_key_and_value("Effect",dic.get("secondary_att_effect"),20,30)
    else:
        print("No secondary attack found.")

def display_pokemon_locations(location_array,pokemon_name):
    if location_array:
        to_display = pokemon_name[0].upper() + " can be found in:"
        for location in location_array:
            to_display += "\n\t{:<15}".format(location)
    else:
        to_display = "No locations found for that pokemon."
    print(to_display)

def list_table(table_name):
    table_name = table_name.lower()
    to_return = {}
    if table_name == "attacks":
        sql = 'select name, damage, effect, targets, power_points, accuracy, location_name from attacks;'
        results = menu_options.execute(sql)
        if results:
            print("ATTACKS TABLE")
            print("-"*35)
            header_str = "\n|{:^10}|\n".format("name")
            header_str += "|{:^6}|".format("damage")
            header_str += "{:^10}|".format("targets")
            header_str += "{:^3}|\n".format("PP")
            header_str+= "|{:^8}|".format("accuracy")
            header_str += "{:^20}|\n".format("found in")
            header_str += "|{:^30}|\n".format("effect")
            print(header_str)
            print("-"*20)
            
            for attack in results:
                row = "\n|{:<15}|\n".format("Name: " + attack[0])
                row += "|{:<10}|".format("Damage: " + str(attack[1]))
                row += "{:<15}|".format("Targets: " + attack[3])
                row += "{:<5}|\n".format("PP: "+  str(attack[4]))
                row += "|{:<11}|".format("Acc: " + str(attack[5]))
                row += "{:<20}|\n".format("Found: " + attack[6])
                row += "|{:<30}|\n".format("Effect: " + attack[2])
                print(row)
        else:
            raise validate.Input_Error("No attacks. Perhaps the db has not been set up yet.")
    elif table_name == "locations":
        sql = "select name, description from locations;"
        results = menu_options.execute(sql)
        if results:
            print("LOCATIONS")
            print("-"*51)
            header_str = "\n|{:^25}:".format("name")
            header_str += "{:^30}|\n".format("description")
            print(header_str)
            for location in results:
                display_key_and_value(location[0],location[1],25,30)
                
        else:
            raise validate.Input_error("No locations. Perhaps the db has not been set up yet.")
    
    elif table_name == "pokemon":
        results = menu_options.select_all_pokemon()
        print("POKEMON")
        print(results)
        for pokemon in results:
            
            display_pokemon(pokemon)
                
    elif table_name == "evolutions":
        sql = 'select parent_poke,child_poke,evolved,item_used,item,traded,bred,notes from evolutions;'
        results = menu_options.execute(sql)
        if results:
            print("EVOLUTIONS TABLE")
            print("-"*40)
            header_str = "\n|{:^10}|\n".format("parent poke")
            header_str += "|{^:10}|".format("child poke")
            header_str += "{^:6}|".format("evolved?")
            header_str += "{^:6}|".format("item?")
            header_str+= "{^:16}|\n".format("item name")
            header_str+= "{^:8}|".format("traded?")
            header_str += "{^:5}|\n".format("bred?")
            header_str+= "|{^:25}|\n".format("additional notes")
            print(header_str)
            print("-"*20)

            for attack in results:
                header_str = "\n|{:^10}|\n".format(results[0][0])
                header_str += "|{^:10}|".format(results[0][1])
                header_str += "{^:6}|".format(str(results[0][2]))
                header_str += "{^:6}|".format(str(results[0][3]))
                header_str+= "{^:16}|\n".format(results[0][4])
                header_str+= "{^:8}|".format(str(results[0][5]))
                header_str += "{^:5}|\n".format(str(results[0][6]))
                header_str+= "|{^:25}|\n".format(results[0][7])
