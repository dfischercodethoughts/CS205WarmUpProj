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
    sql += ", attacks.location_name, attacks from attacks left join pokemon on pokemon.primary_attack = attacks.name where pokemon.name = '" + \
           pokemon.lower() + "';"

    #primary_att_results = execute(sql)
    sql = "select * from attacks left join pokemon on pokemon.secondary_attack = attacks.name where pokemon.name = '" + \
          pokemon.lower() + "';"

    #secondary_att_results = execute(sql)
    sql = "select * from pokemon left join location_reference on location_reference.pokemon_name = pokemon.name where pokemon.name = '" + \
          pokemon.lower() + "';"

    results = execute(sql)

    #returns dictionary with keys and values
    dict_to_return = {
        'name': results[0][0],
        'damage': results[0][1],
        'effects': results[0][2],
        'targets': results[0][3],
        'power_points': results[0][4],
        'accuracy': results[0][5],
        'location_name': results[0][6],
        'primary attack': results[0][7],
        'secondary_attack': results[0][8]
        }
    return dict_to_return


def select_pokemon_evolutions(pokemon):
    #want evolution information for a specific pokemon
    #result has format:
        # poke name, child pokemon, (int 0/1) evolved, item_used, (str) item, (int 0/1) traded, bred, (str) notes
    parent_sql = "select pokemon.name, evolutions.child_poke, evolutions.evolved, evolutions.item_used, evolutions.item,evolutions.traded, evolutions.bred, evolutions.notes"
    parent_sql += " from pokemon left join evolutions on evolutions.parent_poke = pokemon.name where pokemon.name = '" + \
                  pokemon.lower() + "';"
    results = execute(parent_sql)
    child_sql = 'select pokemon.name, evolutions.child_poke, evolutions.evolved, evolutions.item_used, evolutions.item,evolutions.traded, evolutions.bred, evolutions.notes'
    child_sql += ' from pokemon left join evolutions on evolutions.child_poke = pokemon.name where pokemon.name = "' + \
                 pokemon.lower() + '";'
    results = execute(child_sql)

    # returns dictionary with keys and values
    dict_to_return = {
        'parent_poke_name': results[0][0],
        'child_poke_name': results[0][1],
        'is_transformed_from': results[0][2],
        'parent_item': results[0][3],
        'is_evolved_from': results[0][4],
        'evolves': results[0][5],
        'can_be_transformed': results[0][6],
        'item_used': results[0][7],
        'can_be_bred': results[0][8],
        'is_bred_from': results[0][9],
        'parent_traded': results[0][10],
        'traded_to_evolve': results[0][11],
        'parent_additional_requirements': results[0][12],
        'child_additional_requirements': results[0][13]
    }
    return dict_to_return


def select_pokemon_locations(pokemon):
    sql = 'select location'