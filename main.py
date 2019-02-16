### main function to run our program
import init_pokedb
import sys
import low_level
import validate

#################################### - UNSURE IF NECESSARY TO USE ARG_PARSE.... ####################
#import argparse

#parser = argparse.ArgumentParser()

#parser.add_argument("table_name", help = "Table to pull from.")
#parser.add_argument("columns_name", help = "Columns to pull from table.")
#parser.add_argument("--where_cols", help = "Columns of where clause.")
#parser.add_argument("--col_vals", help = "Values of where clause.")

#args = parser.parse_args()

#create sql query from columns, execute and return output

#want like : pokemon location 'route_1'
# : all locations
# : all pokemon
# : all attacks
# -- select *  from [table] order by name;
# : attacks pikachu
#

#so, first input gives all potential tables

class Input_Error(Exception):
    
    msg = ""
    def __init__(self,word):
        self.msg = word

    print(msg)


def check_in_pokemon(word):
    con = low_level.open_db('pokedb.db')
    result = low_level.execute_sql('select * from pokemon where name = "' + word + '";',con)
    con.close()
    if result:
        return True
    
    return False

def check_in_location(word):
    con = low_level.open_db('pokedb.db')
    result = low_level.execute_sql('select * from locations where name = "' + word + '";',con)
    con.close()
    if result:
        return True
    
    return False

def validate_word_one(word):
    #ensures that word one is nonempty and in the pokedb
    if len(word) > 2:
        pokemon = word[0].upper() + word[1:-1].upper()
        if check_in_pokemon(pokemon) or word.lower() =='pokemon' or word.lower() == 'list' or word.lower() == 'exit':
            return True
    
    raise Input_Error("Word one failed validation: " + word)

def validate_word_two(word):
    table_dic = ['location','attacks','pokemon']
    if word.lower() in table_dic:
        return True
    raise Input_Error("Word two is not a table name: " + word)

def validate_word_three(word):
    #there will be a word three in cases of 'pokemon location *location_name*'
    if check_in_location(word.lower()):
        return True
    raise Input_Error("Word three is not a location: " + word)

def has_special_chars(word):
    for letter in word:
        if letter == '?' or letter == ';' or letter == ',' or letter == '.' or letter == '/' or letter == ':' or letter == '"' or letter == "'" or letter == '{' or letter == '[' or letter == ']' or letter == '}' or letter=='\\' or letter == '|' or letter == '=' or letter == '+' or letter == '-' or letter == '_' or letter == '!' or letter == '@' or letter == '#' or letter == '$' or letter == '%' or letter == '^' or letter == '&' or letter == '*' or letter == '(' or letter == ')' or letter == '~' or letter == '`':
            raise Input_Error("Input word has special characters: " + word)
    return False

def check_size(word_arr):
    if len(word_arr) > 3:
        raise Input_Error("Too many words.")
    elif len(word_arr) < 1:
        raise Input_Error("Too few words.")
    
    return True

def validate_input(phrase):
    try:
        has_special_chars(phrase)
        words = phrase.split(" ")
        check_size(words)
        count = 1
        for word in words:
            if count == 1:
                validate_word_one(word)
                count += 1
            elif count == 2:
                validate_word_two(word)
                count += 1
            elif count == 3:
                validate_word_three(word)
                count += 1

        return True
    except Input_Error as e:
        print(e.msg)

if sys.__name__ == '__main__':
   # init_pokedb()
    main()

#def transform(raw):
#    #outputs sql statement
#    split = raw.split(" ")
#    count = 0
#    sql_statement = ""
#    for word in split:
#        if count == 0:
#            pokemon = upper(word[0]) + lower(word[1:len(word)-1])
#            if check_in_pokemon(pokemon):
#                
#                else:
#                if lower(word) == 'list':
#                    sql_statement = 

#INTERESTING POKEMON: MRMIME MIMEJR
def main():
    user_raw = ""
    
    validated_input = []

    while valiated_input != "exit":
        #get user input on loop
        user_raw = raw_input() 

        #validate user input
        if user_raw.validate():
            validated_input = transform(user_raw)
            


    #execute statement based on user input

    #get output

    #format output
