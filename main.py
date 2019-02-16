### main function to run our program
import init_pokedb
import sys
import low_level

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

class Input_Err(Exception):
    
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
        pokemon = word[0].upper() + word[1:len(word)].upper()
        if check_in_pokemon(pokemon)| word.lower() =='pokemon' | word.lower() == 'list' | word.lower() == 'exit':
            return True
    
    return False

def validate_word_two(word):
    table_dic = ['location','attacks','pokemon']
    if word.lower() in table_dic:
        return True
    return False

def validate_word_three(word):
    #there will be a word three in cases of 'pokemon location *location_name*'
    if check_in_location(word.lower()):
        return True
    return False

def has_special_chars(word):
    for letter in word:
        if letter == '?' | letter == ';' | letter == ',' | letter == '.' | letter == '/' | letter == ':' | letter == '"' | letter == "'" | letter == '{' | letter == '[' | letter == ']' | letter == '}' | letter=='\\' | letter == '|' \ letter == '=' | letter == '+' | letter == '-' | letter == '_' | letter == '!' | letter == '@' | letter == '#' | letter == '$' | letter == '%' | letter == '^' | letter == '&' | letter == '*' | letter == '(' | letter == ')' | letter == '~' | letter == '`':
            return True
    return False

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
