import menu_options

def display_key_and_value(key,value):
    new_key = key[0].upper() + key[1:len(key)].lower()
    return_str = "|{:>25}:{:<25}|".format(new_key,value)
    print(return_str)
    return return_str

def display_pokemon(dictionary):
    if dictionary.get("name") == "":
        print("\nNo pokemon found.\n")
        return

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

def display_all_pokemon(list_of_dic):
    print("POKEMON")
    for dic in list_of_dic:
        display_pokemon(dic)
        

def display_attack(dic):
    if dic.get("name") == "":
        print("No attacks found.")
        return
    display_key_and_value("name",dic.get("name"))
    display_key_and_value("damage",str(dic.get("damage")))
    display_key_and_value("effects",dic.get("effects"))
    display_key_and_value("targets",dic.get("targets"))
    display_key_and_value("power Points",str(dic.get("power_points")))
    display_key_and_value("% Accuracy",str(dic.get("accuracy")))
    if dic.get("location_name") !="":
        display_key_and_value("locations found",dic.get("location_name"))
    display_key_and_value("primary attack",dic.get("primary_attack"))
    if dic.get("secondary_attack")!= "":
        display_key_and_value("secondary attack",dic.get("secondary_attack"))
    else:
        display_key_and_value("secondary attack","no secondary attack")

def display_pokemon_attacks(dic,pokemon_name):
    header = pokemon_name[0].upper() + pokemon_name[1:-1].lower()
    print(header + " Attacks")
    if dic.get("primary_att_name") != "":
        print("{:>16}:{:<25}".format("Primary attack",dic.get("primary_att_name")))
        print("{:>16}:{:<3}".format("Damage",dic.get("primary_att_damage")))
        print("{:>16}:{:<10}".format("Effect",dic.get("primary_att_damage")))
        print("{:>16}:{:<10}".format("Targets",dic.get("primary_att_damage")))
        print("{:>16}:{:<3}".format("PowerPoints",dic.get("primary_att_damage")))
        print("{:>16}:{:<3}".format("Accuracy",dic.get("primary_att_damage")))
        print("{:>16}:{:<10}".format("Att Location",dic.get("primary_att_damage")))
    else:
        print("No primary attack found.")
        
    if dic.get("secondary_att_name") != "":
        print("{:>16}:{:<25}".format("Primary attack",dic.get("primary_att_name")))
        print("{:>16}:{:<3}".format("Damage",dic.get("primary_att_damage")))
        print("{:>16}:{:<10}".format("Effect",dic.get("primary_att_damage")))
        print("{:>16}:{:<10}".format("Targets",dic.get("primary_att_damage")))
        print("{:>16}:{:<3}".format("PowerPoints",dic.get("primary_att_damage")))
        print("{:>16}:{:<3}".format("Accuracy",dic.get("primary_att_damage")))
        print("{:>16}:{:<10}".format("Att Location",dic.get("primary_att_damage")))
    else:
        print("No primary attack found.")

def display_pokemon_locations(location_array,pokemon_name):
    if location_array:
        to_display = pokemon_name[0].upper() + " can be found in:"
        for location in location_array:
            to_display += "\n\t{:<15}".format(location)
    else:
        to_display = "No locations found for that pokemon."
    print(to_display)

def display_pokemon_attacks(dic):
    if dic.get("primary_att_name") == "":
        print("Something went wrong. No primary attack found.")
    else:
        print("Primary Attack")
        display_key_and_value("name",dic.get("primary_att_name"))
        display_key_and_value("damage",str(dic.get("primary_att_damage")))
        display_key_and_value("effects",dic.get("primary_att_effects"))
        display_key_and_value("targets",dic.get("primary_att_targets"))
        display_key_and_value("power Points",str(dic.get("primary_att_pp")))
        display_key_and_value("% Accuracy",str(dic.get("primary_att_accuracy")))
        if dic.get("primary_att_location") !="":
            display_key_and_value("locations found",dic.get("primary_att_location"))
        

    if dic.get("secondary_att_name") == "":
        print("No secondary attack found.")
    else:
        print("Secondary Attack")
        display_key_and_value("name",dic.get("secondary_att_name"))
        display_key_and_value("damage",str(dic.get("secondary_att_damage")))
        display_key_and_value("effects",dic.get("secondary_att_effects"))
        display_key_and_value("targets",dic.get("secondary_att_targets"))
        display_key_and_value("power Points",str(dic.get("secondary_att_pp")))
        display_key_and_value("% Accuracy",str(dic.get("secondary_att_accuracy")))
        if dic.get("secondary_att_location") !="":
            display_key_and_value("locations found",dic.get("primary_att_location_name"))


def display_pokemon_evolutions(list_of_dics):
    for dic in list_of_dics:
        if dic.get("is_parent"):
            print("\nParent Pokemon\n")
            str_to_print = dic.get("parent_poke_name") + ": "
            if dic.get("is_transformed") == 1:
                str_to_print += " Can be transformed "
                str_to_print += "using " + dic.get("parent_item") + "."
            if dic.get("is_bred_from_parent") == 1:
                str_to_print += " Can be bred."
            if dic.get("parent_traded") == 1:
                str_to_print += " Can be traded."
            if dic.get("is_evolved"):
                str_to_print += " Can be evolved."
            if dic.get("parent_additional_requirements") != "":
                str_to_print += "\nAdditional requirements: " + dic.get("parent_additional_requirements") + "\n"
        else:
            print("\nChild Pokemon")
            str_to_print = dic.get("child_poke_name") + " is obtainable:\n"
            if dic.get("can_be_transformed") == 1:
                
                str_to_print += "\tBy using " + dic.get("item_used") + ".\n"
            if dic.get("can_be_bred") == 1:
                str_to_print += "\tBy breeding.\n"
            if dic.get("trade_to_evolve") == 1:
                str_to_print += "\tBy trading.\n"
            if dic.get("evolves"):
                str_to_print += "\tBy evolving.\n"
            if dic.get("child_additional_requirements") != "":
                str_to_print += "\tAdditional requirements: " + dic.get("child_additional_requirements") + "\n"
        
    
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
            print("-"*20)
            header_str = "\n|{:^10}|".format("name")
            header_str += "{:^20}|\n".format("description")
            print(header_str)
            for location in results:
                row = "|{:>10}|".format(location[0][0])
                row += "{:>20}|".format(location[0][1])
                print(row)
        else:
            raise validate.Input_error("No locations. Perhaps the db has not been set up yet.")
    
    elif table_name == "pokemon":
        
        results = menu_options.select_all_pokemon()
        display_all_pokemon(results)
                
    elif table_name == "evolutions":
        sql = 'select parent_poke,child_poke,evolved,item_used,item,traded,bred,notes from evolutions;'
        results = menu_options.execute(sql)
        if results:
            print("EVOLUTIONS TABLE")
            print("-"*40)
            header_str = "\n|{:^10}|\n".format("parent poke")
            header_str += "|{:^10}|\n".format("child poke")
            header_str += "{:^6}|".format("evolved?")
            header_str += "{:^4}|".format("item?")
            header_str+= "{:^8}|\n".format("item name")
            header_str+= "|{:^8}|".format("traded?")
            header_str += "{:^5}|\n".format("bred?")
            header_str+= "|{:^10}|\n".format("additional notes")
            print(header_str)
            print("-"*40)

            for evolution in results:
                row = "\n|Parent: {:<5}|\n".format(evolution[0])
                row += "|Child: {:<5}|\n".format(evolution[1])
                if evolution[2] != 0 and evolution[2] != "":
                    row += "|{:<6}|\n".format("Parent evolves")
                if evolution[3] != 0 and evolution[3] != "":
                    row += "|{:<3} ".format("Parent has")
                    row+= "item {:<16}|\n".format(evolution[4].strip() + " used")
                if evolution[5] != 0 and evolution[5] != "":
                    row+= "|{:<8}|\n".format("Parent is traded")
                if evolution[6] != 0 and evolution [6] != "":
                    row += "|{:<5}|\n".format("Parent is bred")
                if evolution[7] != "" and evolution[7] != 0 and evolution[7] != '0':
                    row+= "|Additional Notes: {:<10}|\n".format(evolution[7].strip())
                print(row)
