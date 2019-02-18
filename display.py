import menu_options

def list_table(table_name):
    to_return= {}
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
        sql = 'select name, hp, type1, type2, primary_attack,secondary_attack, evolution_level from pokemon;'
        results = menu_options.execute(sql)
        if results:
            print("POKEMON TABLE")
            print("-"*40)
            header_str = "\n|{:^10}|\n".format("name")
            header_str += "|{^:6}|".format("health")
            header_str += "{^:10}|".format("type 1")
            header_str += "{^:10}|\n".format("type 2")
            header_str+= "|{^:10}|".format("primary attack")
            header_str+= "{^:10}|".format("secondary attack")
            header_str += "{^:12}|\n".format("evolve level")
            print(header_str)
            print("-"*20)
            
            for attack in results:
                row = "\n|{:>10}|\n".format(results[0][0])
                row += "|{>:6}|".format(results[0][1])
                row += "{>:10}|".format(results[0][2])
                row += "{>:10}|\n".format(results[0][3])
                row += "|{>:10}|".format(results[0][4])
                row += "{>:10}|".format(results[0][5])
                row += "{>:12}|\n".format(results[0][6])
                print(row)
                
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
