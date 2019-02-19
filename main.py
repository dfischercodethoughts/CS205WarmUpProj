DATABASE_NAME = 'pokedb.db'

### main function to run our program
import os
if not os.path.isfile(DATABASE_NAME):
    import init_pokedb

import sys
import low_level
import validate
import menu_options
import display

#INTERESTING POKEMON: MRMIME MIMEJR
def main():
    print("Welcome to the PokeDB!")
    user_raw = ""

    while True:
        try:
            print("\nEnter command:")

            user_raw = input()
            #print("you input " + user_raw)

            if isinstance(user_raw,str):
                user_raw = validate.sanitize(user_raw)
                user_words = user_raw.split(' ' )
                validate.check_size(user_words)
                count = 0
                for word in user_words:
                    user_words[count] = word.lower().strip()
                    count += 1
            else:
                raise validate.Input_Error("Please enter 1-3 words: *pokemon_name* [table_name] eg. bulbasaur attacks.")
            if "exit" in user_words:
                break
            if user_words[0].lower() == 'list':
                if len(user_words) == 2:

                    if user_words[1].lower() == 'all':
                        display.display_all_tables()
                    
                    validate.check_table_name(user_words[1].lower())
                    display.list_table(user_words[1].lower())
                    
                else:
                    raise validate.Input_Error("Please input 'list' followed by a table name: attacks locations pokemon or evolutions.")
            elif validate.check_in_pokemon(user_words[0].lower()):
                #switch on second word
                if len(user_words) == 1:
                    #input just pokemon name; want information on just that pokemon
                    results = menu_options.select_pokemon(user_words[0].lower())
                    display.display_pokemon(results)
                    
                #if input 2 words, the first of which is a pokemon name
                elif len(user_words) == 2:
                    validate.check_table_name(user_words[1].lower())
                    if user_words[1].lower() == 'attacks':
                        results = menu_options.select_pokemon_attacks(user_words[0])
                        display.display_pokemon_attacks(results,user_words[0])
                        
                    elif user_words[1].lower() == 'location' or user_words[1].lower() == 'locations':
                        results = menu_options.select_pokemon_locations(user_words[0])
                        display.display_pokemon_locations(results,user_words[0])
                        
                    elif user_words[1].lower() == 'evolutions' or user_words[1].lower() == 'evolution':
                        results = menu_options.select_pokemon_evolutions(user_words[0])
                        display.display_pokemon_evolutions(results,user_words[0])
                    else:
                        print("Unrecognized second word")
                else:
                    print("\nWhen searching for pokemon attributes, please enter the pokemon name followed by the attribute name.")
            

            elif (validate.check_in_locations(user_words[0].lower())):
                if len(user_words) == 1:
                    #searching for all pokemon in a given location
                    results = menu_options.select_pokemon_from_location(user_words[0].lower())
                    #print(results)
                    display.display_pokemon_in_location(results,user_words[0])
                else:
                    print("If searching for all pokemon that can be found in a certain location, please just enter the location name.")
            elif (validate.check_in_attacks(user_words[0].lower())):
                if len(user_words) == 1:
                    result = menu_options.select_attack(user_words[0].lower())
                    display.display_attack(result)
                else:
                    print("If trying to get information on an attack, please enter just that attack's name.")
            else:
                err_msg = "Sorry, that is incorrect input.\n"
                err_msg += "Tables are attacks/locations/evolutions/pokemon.\n"
                err_msg += "options in '|...|' are optional:"
                err_msg += "\nPlease input either 'list [table]', '[pokemon_name] |[table_name]|', or '[location_name]'."
                raise validate.Input_Error(err_msg)

        except validate.Input_Error as e:
            print(e.msg)


if __name__ == '__main__':
   # init_pokedb()
    main()
