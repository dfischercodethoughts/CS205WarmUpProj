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

def display_attack(attack_dic):
    #test
    print("functionality to come")
    print("test")
    
def display_pokemon_evolutions(list_of_dics, poke_name):
    header = poke_name[0].upper() + poke_name[1:len(poke_name)] + " Evolutions"
    print("\n{:^50}".format(header))
    print("-" * 52)
    for dic in list_of_dics:
        print("-" * 52)
        #print(dic)
        if dic.get("is_parent"):
            display_key_and_value("Parent Poke"," " +dic.get('poke_name').upper(),20,30)
        if dic.get("is_child"):
            display_key_and_value("Child Poke", " " +dic.get("poke_name").upper(),20,30)
        if dic.get("is_item_used") != None and dic.get("is_item_used") != 0:
            display_key_and_value("Item used",dic.get("item_used"),20,30)
        if dic.get("is_bred") != None and dic.get("is_bred") != 0:
            display_key_and_value("","By breeding.",20,30)
        if dic.get("is_evolve") != None and dic.get("is_evolve") != 0:
            display_key_and_value("", "By evolution.",20,30)
        if dic.get("is_traded") != None and dic.get("is_traded") != 0:
            display_key_and_value("","By trading.",20,30)
        if dic.get("additional_requirements") != '0' and dic.get("additional_requirements") != 0 and dic.get("additional_requirements") != None and dic.get("additional_requirements") != "":
            display_key_and_value("Additional reqs",dic.get("additional_requirements"))
        print("-" * 52)
    print("No more associated evolutions")

def display_pokemon_attacks(dic,pokemon_name):
    header = pokemon_name[0].upper() + pokemon_name[1:len(pokemon_name)].lower()
    header = header + " Attacks"
    
    print("{:^50}".format(header))
    print(" " + "-" * 51)
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
    print(" " + "-"*51)
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
    print(" " + "-"*51)

def display_pokemon_locations(location_array,pokemon_name):
    print(" " + "_" * 40)
    if location_array:
        to_display = "|" + pokemon_name[0].upper() + pokemon_name[1:len(pokemon_name)] + " can be found in:"
        #display_key_and_value(to_display,"",20,20)
        print(to_display)
        for location in location_array:
            display_key_and_value("",location[0],7,33)
        
    else:
        to_display = "No locations found for that pokemon."
    print(" " + "_" * 40)

def display_pokemon_in_location(pokemon_array,location_name):
    
    if pokemon_array:
        to_display = "\n" + location_name[0].upper() + location_name[1:len(location_name)] + " contains the following pokemon:"
        print(to_display)
        print(" " + "_" * 40)
        for pokemon in pokemon_array:
            poke_name = pokemon[0][0].upper()
            poke_name += pokemon[0][1:len(pokemon[0])]
            display_key_and_value("",poke_name,5,35)
        print(" " + "_" * 40)
    else:
        print("No pokemon found for that location.")

def list_table(table_name):
    table_name = table_name.lower()
    to_return = {}
    if table_name == "attacks":
        sql = 'select name, damage, effect, targets, power_points, accuracy, location_name from attacks;'
        results = menu_options.execute(sql)
        if results:
            print("ATTACKS TABLE")
            
            for attack in results:
                print(" " + "_" * 51)
                pokename = attack[0][0].upper()
                pokename += attack[0][1:len(attack[0])]
                display_key_and_value("Name",pokename,10,40)
                if attack[1] != None and attack[1] != 0 and attack[1] != "":
                    display_key_and_value("Damage",str(attack[1]),10,40)
                else:
                    display_key_and_value("No damage","See effect",10,40)
                display_key_and_value("Targets", attack[3],10,40)
                display_key_and_value("PP",str(attack[4]),10,40)
                if attack[5] != 0 and attack[5] != "":
                    display_key_and_value("Accuracy", str(attack[5]),10,40)
                if attack[6] != None and attack[6] != 0 and attack[6] != "" and attack[6] != "none":
                    display_key_and_value("Found in",attack[6],10,40)
                if attack[2] != None and attack[2] !=0 and attack[2] != "":
                    display_key_and_value("Effect",attack[2],10,40)
                print(" " + "_" * 51)
                
        else:
            raise validate.Input_Error("No attacks. Perhaps the db has not been set up yet.")
    elif table_name == "locations":
        sql = "select name, description from locations;"
        results = menu_options.execute(sql)
        if results:
            print("{:^55}" . format("LOCATIONS"))
            print(" " + "_"*55)
            header_str = "\n|{:^25}:".format("name")
            header_str += "{:^30}|".format("description")
            print(header_str)
            print("|{:^56}|".format(""))
            for location in results:
                display_key_and_value(location[0],location[1],25,30)
            print(" " + "_"*55)
                
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

            for evolution in results:
                print("-"*45)
                display_key_and_value("Parent Poke",evolution[0],15,30)
                display_key_and_value("Child Poke", evolution[1],15,30)
                if evolution[2] == 1:
                    display_key_and_value("", "Evolves through level up",15,30)
                if evolution[3] == 1 and evolution[4] != None:
                    display_key_and_value("","Transforms by using " + evolution[4],15,30)
                if evolution[5] == 1:
                    display_key_and_value("","Transforms through trading", 15, 30)
                if evolution[6] == 1:
                    display_key_and_value("","Transforms through breeding",15,30)
                if evolution[7] != None and evolution[7] != 0 and evolution[7] != "":
                    display_key_and_value("Additional reqs",evolution[7],15,30)
                print("-"*45)

                
