DATABASE_NAME = 'pokedb.db'

### main function to run our program
import os
if not os.path.isfile(DATABASE_NAME):
    import init_pokedb

import sys
import low_level
import validate

def execute(string):
    #assumes properly formatted input
    con = low_level.open_db(DATABASE_NAME)
    results =  low_level.execute_sql(string,con)
    con.close()
    return results

#INTERESTING POKEMON: MRMIME MIMEJR
def main():
    print("Welcom to the PokeDB!")
    user_raw = ""
    
    
    while True:
        try:
            print("Enter your command:")
    
            #get user input on loop
            user_raw = input() 
            user_words = user_raw.split(' ' )
            validate.check_size(user_words)
            validate.check_first_word(user_words[0])
            if "exit" in user_words:
                break
            if len(user_words) == 1:
                
                if user_words[0] == "exit":
                    break
                
                elif user_words[0] == 'list':
                    raise validate.Input_Error('When using list, please enter a table name as well.')
                
                elif user_words[0] == 'pokemon':
                    sql = 'select * from pokemon;'
                    results = execute(sql)
                    display_results(results,'pokemon_list')

                elif check_in_pokemon(user_words[0]):
                    #want to select pokemon's information
                    sql = "select * from pokemon where name = '" + user_words[0] + "';"
                    results = execute(sql)
                    display_results(results, 'pokemon_record')
            
            elif len(use_words) == 2:
                validate.validate_second_word(user_words[1])
                if user_words[0] == "list":
                    #select all records from a table
                    sql = "select * from " + user_words[1].lower() + ";"
                    results = execute(sql)
                    if results:
                        display_results(results,user_words[1].lower() + "_list")
                    else:
                        raise validate.Input_Error("Something went wrong. Could not find the table requested.")
                elif validate.check_in_pokemon(user_words[0]):
                    if (user_words[1].lower() == "locations"):
                        #select location data of pokemon specified
                        pokemon = user_words[0][0].upper() + user_words[0][1:-1].lower()
                        sql = "select * from location_reference where pokemon_name = '" + pokemon + "' left join pokemon on location_reference.pokemon_name = pokemon.name;"
                        results = execute(sql)
                        


            #validate user input will throw exception if it's invalid
            if validate.validate_input(user_raw):
                words = user_raw.split()
                if words[0] == "exit":
                    break
                elif words [0] == 'list':
                    # expect tablename in second word
                    #since input is validated, safe to assume second word has table name
                    sql = generate_sql(words,'list')
                    con = low_level.open_db('pokedb.db')
                    results = low_level.execute_sql(sql)
                    con.close()
                    disp_results('list',results)
                elif words[0] == 'pokemon':
                    sql = generate_sql(words,'pokemon_at_location')
                    con = low_level.open_db('pokedb.db')
                    results = low_level.execute_sql(sql,con)
                    con.close()
                    disp_results('pokemon_at_location',results)
                elif validate.check_in_pokemon(words[0]):
                    sql = generate_sql(words,'pokemon_info')
                    con = low_level.open_db('pokedb.db')
                    results = low_level.execute_sql(sql,con)
                    con.close()
                    disp_results('pokemon_info',results)

                else:
                    print("Flow should not get here. ERROR")
        except validate.Input_Error as e:
            print(e.msg)


if __name__ == '__main__':
   # init_pokedb()
    main()

