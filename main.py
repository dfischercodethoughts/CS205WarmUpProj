### main function to run our program
import init_pokedb
import sys
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



def validate_input(raw_dat):
    tables = ["pokemon", "attacks", "locations"]
    columns = {
            ""}
    #return true false, based on specific contents of input
    split = raw_dat.split(" ")
    for dat in split:


if sys.__name__ == '__main__':
    init_pokedb()
    main()

class Input_Err(Exception):
    """INPROPER INPUT. PLEASE TRY AGAIN."""
    pass

def main():
    user_raw = ""
    
    validated_input = ""

    while valiated_input != "exit":
        #get user input on loop
        user_raw = raw_input() 

        #validate user input
        
    #execute statement based on user input

    #get output

    #format output
