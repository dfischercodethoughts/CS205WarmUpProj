DATABASE_NAME = 'pokedb.db'

import low_level
import validate


#user_words = ""

def execute(string):
    #assumes properly formatted input
    #print("\nExecuting: " + string)
    con = low_level.open_db(DATABASE_NAME)
    results =  low_level.execute_sql(string,con)
    con.close()
    #print("Done.")
    return results

def select_pokemon(pokemon):
    sql = 'select name, type1, type2, hp,primary_attack,secondary_attack,evolution_level from pokemon where name = "' + pokemon.lower() + '";'
    results = execute(sql)
    #returns dictionary with keys and values
    dict_to_return = {
            'name': results[0][0],
            'type1': results[0][1],
            'type2': results[0][2],
            'hp': results[0][3],
            'primary_attack': results[0][4],
            'secondary_attack': results[0][5],
            'evolution_level': results[0][6]
            }
    return dict_to_return

def select_attack(attack):
    sql = 'select attacks.name, attacks.damage,attacks.effect,attacks.targets,attacks.power_points,attacks.accuracy'
    sql += ', attacks.location_name from attacks where name = "' + attack + '";'
    print("functionality to come")


#Want to return dictionary of attacks based on pokemon that is typed in
def select_pokemon_attacks(pokemon):
    # input pokemon_name attacks to get attack info for a specific pokemon
    sql = "select attacks.name, attacks.damage,attacks.effect,attacks.targets,attacks.power_points,attacks.accuracy"
    sql += ", attacks.location_name from attacks left join pokemon on pokemon.primary_attack = attacks.name where pokemon.name = '" + \
           pokemon.lower() + "';"
    primary_att_results = execute(sql)
    
    sql = "select attacks.name, attacks.damage,attacks.effect,attacks.targets,attacks.power_points,attacks.accuracy"
    sql += ", attacks.location_name from attacks left join pokemon on pokemon.secondary_attack = attacks.name where pokemon.name = '" + \
           pokemon.lower() + "';"
    secondary_att_results = execute(sql)

    #returns dictionary with keys and values
    
    if primary_att_results:
        dict_to_return = {
            'primary_att_name': primary_att_results[0][0],
            'primary_att_damage': primary_att_results[0][1],
            'primary_att_effect': primary_att_results[0][2],
            'primary_att_targets': primary_att_results[0][3],
            'primary_att_pp': primary_att_results[0][4],
            'primary_att_acc': primary_att_results[0][5],
            'primary_att_location': primary_att_results[0][6]
            }
    else:
        dict_to_return = {
            'primary_att_name': "",
            'primary_att_damage':0,
            'primary_att_effect': "",
            'primary_att_targets': "",
            'primary_att_pp': 0,
            'primary_att_accuracy': 0,
            'primary_att_location': ""
            }
    
    if secondary_att_results:
        dict_to_return['secondary_att_name'] = secondary_att_results[0][0]
        dict_to_return['secondary_att_damage'] = secondary_att_results[0][1]
        dict_to_return['secondary_att_effect'] = secondary_att_results[0][2]
        dict_to_return['secondary_att_targets'] = secondary_att_results[0][3]
        dict_to_return['secondary_att_pp'] = secondary_att_results[0][4]
        dict_to_return['secondary_att_acc'] = secondary_att_results[0][5]
        dict_to_return['secondary_att_location'] = secondary_att_results[0][6]
    else:
        dict_to_return['secondary_att_name'] = ''
        dict_to_return['secondary_att_damage'] = 0
        dict_to_return['secondary_att_effect'] = ''
        dict_to_return['secondary_att_targets'] = ''
        dict_to_return['secondary_att_pp'] = 0
        dict_to_return['secondary_att_acc'] = 0
        dict_to_return['secondary_att_location'] = ''

    return dict_to_return


def select_pokemon_evolutions(pokemon):
    #want evolution information for a specific pokemon
    #result has format:
        # poke name, child pokemon, (int 0/1) evolved, item_used, (str) item, (int 0/1) traded, bred, (str) notes
    child_sql = "select pokemon.name, evolutions.child_poke, evolutions.evolved, evolutions.item_used, evolutions.item,evolutions.traded, evolutions.bred, evolutions.notes"
    child_sql += " from pokemon inner join evolutions on evolutions.parent_poke = pokemon.name where pokemon.name = '" + \
                  pokemon.lower() + "';"
    child_results = execute(child_sql)
    parent_sql = 'select pokemon.name, evolutions.parent_poke, evolutions.evolved, evolutions.item_used, evolutions.item,evolutions.traded, evolutions.bred, evolutions.notes'
    parent_sql += ' from pokemon inner join evolutions on evolutions.child_poke = pokemon.name where pokemon.name = "' + \
                 pokemon.lower() + '";'
    parent_results = execute(parent_sql)

    # returns list of dictionaries with keys and values
    
    list_of_dics = []
    #print("parents")
    for parent in parent_results:
        dict_to_return = {}
        #print(parent)
        dict_to_return['poke_name'] = parent[1]
        dict_to_return['additional_requirements'] = parent[7]
        dict_to_return['is_item_used'] = parent[3]
        dict_to_return['item_used'] = parent[4]
        dict_to_return['is_bred'] = parent[6]
        dict_to_return['is_evolve'] = parent[2]
        dict_to_return['is_traded'] = parent[5]
        dict_to_return['is_parent'] = True
        dict_to_return['is_child'] = False
        list_of_dics.append(dict_to_return)
        
    #print("children")
    for child in child_results:
        dict_to_return = {}
        #print(child)
        dict_to_return['poke_name'] = child[1]
        dict_to_return['additional_requirements'] = child[7]
        dict_to_return['is_item_used'] = child[3]
        dict_to_return['item_used'] = child[4]
        dict_to_return['is_bred'] = child[6]
        dict_to_return['is_evolve'] = child[2]
        dict_to_return['is_traded'] = child[5]
        dict_to_return['is_child'] = True
        dict_to_return['is_parent'] = False
        list_of_dics.append(dict_to_return)
        
    #print(list_of_dics)
    return list_of_dics

def select_all_pokemon():
    sql = "select name, hp,type1, type2, primary_attack,secondary_attack, evolution_level from pokemon;"
    results = execute(sql)
    list_to_ret = []
    
    for pokemon in results:
        dic = {}
        dic['name'] = pokemon[0]
        dic['hp'] = pokemon[1]
        dic['type1'] = pokemon[2]
        dic['type2'] = pokemon[3]
        dic['primary_attack'] = pokemon[4]
        dic['secondary_attack'] = pokemon[5]
        dic['evolution_level'] = pokemon[6]
        list_to_ret.append(dic)
    return list_to_ret


def select_pokemon_locations(pokemon):
    sql = 'select location_name from location_reference where pokemon_name = "' + pokemon + '";'
    results = execute(sql)
    to_return = []
    for location in results:
        to_return.append(location)
    return to_return


def select_pokemon_from_location(location):
    #returns list of pokemon name
    sql = "select pokemon_name from location_reference where location_name = '" + location + "';"
    results = execute(sql)
    to_return = []
    if results:
        for pokemon in results:
            to_return.append(pokemon)
    return to_return
    
