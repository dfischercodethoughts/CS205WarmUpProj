import sys
import low_level

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


