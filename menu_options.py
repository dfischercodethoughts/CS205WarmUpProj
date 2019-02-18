DATABASE_NAME = 'pokedb.db'

import low_level
import validate


user_words = ""

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
    sql = 'select name, type1, type2, hp,primary_attack,secondary_attack,evolution_level from pokemon where name = "' + pokemon.lower() + '";'
    results = execute(sql)
    #returns dictionary with keys and values
    dict_to_return = {
            'name': results[0][0],
            'type_1': results[0][1],
            'type_2': results[0][2],
            'hp': results[0][3],
            'primary_attack': results[0][4],
            'secondary_attack': results[0][5],
            'evolution_level': results[0][6]
            }
    return dict_to_return


#Want to return dictionary of attacks based on pokemon that is typed in
def select_pokemon_attacks(pokemon):
    # input pokemon_name attacks to get attack info for a specific pokemon
    sql = "select attacks.name, attacks.damage,attacks.effects,attacks.targets,attacks.power_points,attacks.accuracy"
    sql += ", attacks.location_name from attacks left join pokemon on pokemon.primary_attack = attacks.name where pokemon.name = '" + \
           pokemon.lower() + "';"

    primary_att_results = execute(sql)
    sql = "select attacks.name, attacks.damage,attacks.effects,attacks.targets,attacks.power_points,attacks.accuracy"
    sql += ", attacks.location_name from attacks left join pokemon on pokemon.secondary_attack = attacks.name where pokemon.name = '" + \
          pokemon.lower() + "';"

    secondary_att_results = execute(sql)
    #sql = "select * from pokemon left join location_reference on location_reference.pokemon_name = pokemon.name where pokemon.name = '" + \
    #      pokemon.lower() + "';"

    #results = execute(sql)

    #returns dictionary with keys and values
    if primary_att_results[0][0] != "":
        dict_to_return = {
            'primary_att_name': results[0][0],
            'primary_att_damage': results[0][1],
            'primary_att_effects': results[0][2],
            'primary_att_targets': results[0][3],
            'primary_att_pp': results[0][4],
            'primary_att_accuracy': results[0][5],
            'primary_att_location': results[0][6]
            }
    else:
        dict_to_return = {
            'primary_att_name': "",
            'primary_att_damage':0,
            'primary_att_effects': "",
            'primary_att_targets': "",
            'primary_att_pp': 0,
            'primary_att_accuracy': 0,
            'primary_att_location': ""
            }
    if primary_att_results[0][0] != "":
        dict_to_return['secondary_att_name'] = results[0][0]
        dict_to_return['secondary_att_damage'] = results[0][1]
        dict_to_return['secondary_att_effects'] = results[0][2]
        dict_to_return['secondary_att_targets'] = results[0][3]
        dict_to_return['secondary_att_pp'] = results[0][4]
        dict_to_return['secondary_att_accuracy'] = results[0][5]
        dict_to_return['secondary_att_location'] = results[0][6]
    else:
        dict_to_return['secondary_att_name'] = ""
        dict_to_return['secondary_att_damage'] = 0
        dict_to_return['secondary_att_effects'] = ''
        dict_to_return['secondary_att_targets'] = ''
        dict_to_return['secondary_att_pp'] = 0
        dict_to_return['secondary_att_accuracy'] = 0
        dict_to_return['secondary_att_location'] = ''
    
    return dict_to_return


def select_pokemon_evolutions(pokemon):
    #want evolution information for a specific pokemon
    #result has format:
        # poke name, child pokemon, (int 0/1) evolved, item_used, (str) item, (int 0/1) traded, bred, (str) notes
    parent_sql = "select pokemon.name, evolutions.child_poke, evolutions.evolved, evolutions.item_used, evolutions.item,evolutions.traded, evolutions.bred, evolutions.notes"
    parent_sql += " from pokemon left join evolutions on evolutions.parent_poke = pokemon.name where pokemon.name = '" + \
                  pokemon.lower() + "';"
    parent_results = execute(parent_sql)
    child_sql = 'select pokemon.name, evolutions.child_poke, evolutions.evolved, evolutions.item_used, evolutions.item,evolutions.traded, evolutions.bred, evolutions.notes'
    child_sql += ' from pokemon left join evolutions on evolutions.child_poke = pokemon.name where pokemon.name = "' + \
                 pokemon.lower() + '";'
    child_results = execute(child_sql)

    # returns dictionary with keys and values
    dict_to_return = {
        'parent_poke_name': "",
        'child_poke_name': "",
        'is_transformed': 0,
        'parent_item': "",
        'is_evolved': 0,
        'evolves': 0,
        'can_be_transformed': 0,
        'item_used': "",
        'can_be_bred': 0,
        'is_bred_from_parent': 0,
        'parent_traded': 0,
        'trade_to_evolve': 0,
        'parent_additional_requirements': "",
        'child_additional_requirements': ""
    }

    if parent_results:
        dict_to_return['parent_poke_name'] = parent_results[0][0]
        dict_to_return['parent_additional_requirements'] = parent_results[0][7]
        dict_to_return['is_transformed'] = parent_results[0][3]
        dict_to_return['parent_item'] = parent_results[0][4]
        dict_to_return['is_bred_from_parent'] = parent_results[0][6]
        dict_to_return['is_evolved'] = parent_results[0][2]
        dict_to_return['parent_traded'] = parent_results[0][5]

    if child_results:
        dict_to_return['child_poke_name'] = child_results[0][1]
        dict_to_return['child_additional_requirements'] = child_results[0][7]
        dict_to_return['can_be_transformed'] = child_results[0][3]
        dict_to_return['item_used'] = child_results[0][4]
        dict_to_return['can_be_bred'] = child_results[0][6]
        dict_to_return['evolves'] = child_results[0][2]
        dict_to_return['trade_to_evolve'] = child_results[0][5]

    return dict_to_return


def select_pokemon_locations(pokemon):
    sql = 'select location'
