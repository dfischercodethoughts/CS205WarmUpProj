import sys
import low_level

class Input_Error(Exception):
    
    msg = ""
    def __init__(self,word):
        self.msg = word

    print(msg)


def check_in_pokemon(word):
    con = low_level.open_db('pokedb.db')
    pokemon = word[0].upper() + word[1:-1].lower()
    result = low_level.execute_sql('select * from pokemon where name = "' + pokemon + '";',con)
    con.close()
    if result:
        return True
    
    return False

def check_in_locations(word):
    con = low_level.open_db('pokedb.db')
    result = low_level.execute_sql('select * from locations where name = "' + word.lower() + '";',con)
    con.close()
    if result:
        return True
    
    return False

def validate_word_one(word):
    word_one_dic = ["pokemon", "list","exit"]
    #ensures that word one is nonempty and in the pokedb
    if len(word) > 4:
        pokemon = word[0].upper() + word[1:-1].upper()
        if check_in_pokemon(pokemon) or word.lower() in word_one_dic:
            return True
    err_msg = word + " is not a valid option. Please enter 'pokemon_name [attacks/locations]', 'pokemon [location_name]', 'list [pokemon/attacks/locations]', or 'exit'."

    raise Input_Error(err_msg)

def validate_word_two(word):
    table_dic = ['location','attacks','pokemon']
    if word.lower() in table_dic or check_in_locations(word.lower()):
        return True
    err_msg = "'" + word + "' is not a table name. Table names are:\n"
    for table in table_dic:
        err_msg += "\t" + table + "\n"
    raise Input_Error(err_msg)

def validate_word_three(word):
    #there will be a word three in cases of 'pokemon location *location_name*'
    if check_in_locations(word.lower()):
        return True
    raise Input_Error(word + " is not a location. Please type 'list locations' to see all locations.")

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


