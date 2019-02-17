DATABASE_NAME = 'pokedb.db'

import low_level
import validate


user_words = " "

def execute(string):
    #assumes properly formatted input
    print("\nExecuting: " + string)
    con = low_level.open_db(DATABASE_NAME)
    results =  low_level.execute_sql(string,con)
    con.close()
    print("Done.")
    return results


def display_results(results, type_of_output):
    #naive implementation simply prints out all results
    if results:
        for r in results:
            print(r)
    else:
        print("no results.")

def select_pokemon(pokemon):
    sql = 'select name, type1, type2, hp,primary_attack,secondary_attack,evolution from pokemon where name = "' + pokemon.lower() + '";'
    results = low_level.execute_sql(sql)
    #returns dictionary with keys and values
    dic_to_return = {
            'name': results[0][0],
            'type_1':results[0][1],
            'type_2' : results[0][2],
            'hp' : results[0][3],
            'primary_attack':results[0][4],
            'secondary_attack' : results[0][5],
            'evolution_level' : results[0][6]
            }
    return dic_to_return


def select_pokemon_attacks(attack):
    if user_words[1] == 'attacks':
        # input pokemon_name attacks to get attack info for a specific pokemon
        sql = "select attacks.name, attacks.damage,attacks.effects,attacks.targets,attacks.power_points,attacks.accuracy"
        sql += ", attacks.location_name, attacks from attacks left join pokemon on pokemon.primary_attack = attacks.name where pokemon.name = '" + \
               user_words[0].lower() + "';"
        primary_att_results = execute(sql)
        sql = "select * from attacks left join pokemon on pokemon.secondary_attack = attacks.name where pokemon.name = '" + \
              user_words[0].lower() + "';"
        secondary_att_results = execute(sql)

        print("Attack information for " + user_words[0])

        if primary_att_results:
            print("Primary attacks: ")
            display_results(primary_att_results, "")
        else:
            print("No information on primary attack.")
        if secondary_att_results:
            print("Secondary attacks: ")
            display_results(primary_att_results, "")
        else:
            print("No information on secondary attack.")

    elif user_words[1] == 'locations':
        # wants location information on a given pokemon
        sql = "select * from pokemon left join location_reference on location_reference.pokemon_name = pokemon.name where pokemon.name = '" + \
              user_words[0].lower() + "';"
        results = execute(sql)
        if results:
            print("Results: ")
            print(results)
        else:
            raise validate.Input_Error("Something went wrong. No results. Please try again.")

def select_pokemon_evolutions(evolution):
    #want evolution information for a specific pokemon
                        #result has format:
    # poke name, child pokemon, (int 0/1) evolved, item_used, (str) item, (int 0/1) traded, bred, (str) notes
    parent_sql = "select pokemon.name, evolutions.child_poke, evolutions.evolved, evolutions.item_used, evolutions.item,evolutions.traded, evolutions.bred, evolutions.notes"
    parent_sql += " from pokemon left join evolutions on evolutions.parent_poke = pokemon.name where pokemon.name = '" + \
                  user_words[0] + "';"
    parent_results = execute(parent_sql)
    child_sql = 'select pokemon.name, evolutions.child_poke, evolutions.evolved, evolutions.item_used, evolutions.item,evolutions.traded, evolutions.bred, evolutions.notes'
    child_sql += ' from pokemon left join evolutions on evolutions.child_poke = pokemon.name where pokemon.name = "' + \
                 user_words[0] + '";'
    child_results = execute(child_sql)
    if child_results:
        # print(child_results)
        # print(len(child_results))
        # print(child_results[0][1])
        if child_results[0][2] == 1:
            print(user_words[0] + " evolves from " + child_results[0][1])
        elif child_results[0][3] == 1:
            print(user_words[0] + " can be transformed from " + child_results[0][1] + " using: " + child_results[0][4])
        elif child_results[0][5] == 1:
            result_str = user_words[0] + " evolves from " + child_results[0][1] + " after trading"
            if child_results[0][7] != "":
                result_str += ", with additional requirements: " + child_results[0][7]
            print(result_str)

        elif child_results[0][6] == 1:
            print(user_words[0] + " can be bred from " + child_results[0][1])
    else:
        print(user_words[0] + " has no parents.")

    if parent_results:
        # print(parent_results)
        if parent_results[0][2] == 1:
            print(user_words[0] + " evolves into " + parent_results[0][1])
        elif parent_results[0][3] == 1:
            print(
                user_words[0] + " can be transformed into " + parent_results[0][1] + " using: " + parent_results[0][4])
        elif parent_results[0][5] == 1:
            result_str = user_words[0] + " can be traded to evolve into " + parent_results[0][1]
            if parent_results[0][7] != "":
                result_str += ", with additional requirements: " + parent_results[0][7]
            print(result_str)

        elif child_results[0][6] == 1:
            print(user_words[0] + " can be bred into " + parent_results[0][1])

    else:
        print(user_words[0] + " has no parents.")

def select_pokemon_locations(location):
    sql = 'select location'