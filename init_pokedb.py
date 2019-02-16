#code to read in .csv files and init sqlite3 db
import csv
import sqlite3
import low_level
import sys
def insert_locations(csv_file,con,columns):
#csv file is file opened with pythons built in csv file handler
#con is sqlite3 db connection
#table name is a string containing the table name
    table_name = 'locations'
    count = 0
    for record in csv_file:
        if record[0] != "name" and count != 0:
            
            if record[1] != "":
                sqlstring = "insert into " + table_name
                sqlstring +=" (" + columns + ") values ('"
                for i in record:
                    if i != "--" and i != "----" and i != "":
                        sqlstring += i
                        sqlstring += "','"
                    #for building location db, we just want to insert location name and description (other cols ommitted)
                    #else:
                        #sqlstring += "','"
                sqlstring = sqlstring[:-2]
                sqlstring += ");"
            else:
                sqlstring = "insert into locations (name) values ('" + record[0] + "');"
        
            print("executing " + sqlstring)
            outs = low_level.execute_sql(sqlstring,con)
            print("output: ")
            if outs != None:
                for o in outs:
                    print(o)
        else:
            count = 1

def insert_attacks(csv_file,con,columns):
#csv file is file opened with pythons built in csv file handler
#con is sqlite3 db connection
#table name is a string containing the table name
    table_name = 'attacks'
    count = 0
    for record in csv_file:
        if record[0] != "name" and count != 0:
            
            
            sqlstring = "insert into " + table_name
            sqlstring +=" (" + columns + ") values ('"
            for i in record:
                if i != "--" and i != "----" and i != "":
                    sqlstring += i.replace("'","").replace('"',"")
                    sqlstring += "','"
                #for building location db, we just want to insert location name and description (other cols ommitted)
                else:
                    sqlstring += "','"
            sqlstring = sqlstring[:-2]
            sqlstring += ");"
        
            print("executing " + sqlstring)
            outs = low_level.execute_sql(sqlstring,con)
            print("output: ")
            if outs != None:
                for o in outs:
                    print(o)
        else:
            count = 1


def insert_location_references(csv_file,con,columns):
#csv file is file opened with pythons built in csv file handler
#con is sqlite3 db connection
#table name is a string containing the table name
    table_name = 'location_reference'
    count = 0
    for record in csv_file:
        if record[0] != "name" and count != 0:
            
            
            sqlstring = "insert into " + table_name
            sqlstring +=" (" + columns + ") values ("
            
            sqlstring +='"'+ record[0].lower() + '","' + record[1].lower() + '");'
        
            print("executing " + sqlstring)
            outs = low_level.execute_sql(sqlstring,con)
            print("output: ")
            if outs != None:
                for o in outs:
                    print(o)
        else:
            count = 1

def insert_pokemon(csv_file,con,columns):
#csv file is file opened with pythons built in csv file handler
#con is sqlite3 db connection
#table name is a string containing the table name
    table_name = 'pokemon'
    count = 0
    for record in csv_file:
        if record[0] != "name" and count != 0:
            
            
            sqlstring = "insert into " + table_name
            sqlstring +=" (" + columns + ") values ("
            
            for i in record:
                if not low_level.is_number(i) and i!= "-----" and i != "FALSE" and i != "yes" and i != "no" and i != "use" and i != "bred" and i != "trade" and i != "NA":
                    sqlstring += "'" + i.replace("'","").replace('"',"").lower() + "',"

                elif i == "no":
                    sqlstring += "0,"
                elif i == "yes":
                    sqlstring += "1,"
                elif low_level.is_number(i):
                    sqlstring += i + ","
                else:
                    sqlstring += "'',"
            while sqlstring.endswith(','):   
                sqlstring = sqlstring[:-1]
            
            sqlstring += ");"
        
            print("executing " + sqlstring)
            outs = low_level.execute_sql(sqlstring,con)
            print("output: ")
            if outs != None:
                for o in outs:
                    print(o)
        else:
            count = 1

def insert_evolutions(evo_csv, con):
    print("\n\nSTARTING EVOLUTIONS IMPORT...")
    tablename = 'evolutions'
    count = 0
    for record in evo_csv:
        if count != 0:
            sql_string = 'insert into ' + tablename + '( parent_poke, child_poke, evolved, item_used, item, traded, bred, notes) values ('
            for r in record:
                if r == 'y':
                    sql_string += '1,'
                elif r == 'n':
                    sql_string += '0,'
                elif r == '':
                    sql_string+='0,'
                else:
                    sql_string +='"'+ r+'",'
            sql_string = sql_string[0:-1] + ');'
            
            print("executing : " + sql_string)
            outs = low_level.execute_sql(sql_string,con)
            print("done. output: ")
            if outs:
                for o in outs:
                    print(o)
        else:
            count += 1

    print("ENDING EVOLUTION IMPORT.")
                            
                            
def create_tables():      
    print("\n\nCREATING POKE DB...\n")

    exec_string = []

    exec_string.append("create table locations (name text primary key,\n " +
        "description text, \n"+
        "north_exit text, \n"+
        "east_exit text, \n"+
        "south_exit text, \n"+
        "west_exit text, \n"+
        "foreign key(north_exit) references locations(name),\n"+
        "foreign key(east_exit) references locations(name),\n"+
        "foreign key(south_exit) references locations(name),\n"+
        "foreign key(west_exit) references locations(name)"+
        ");")

    exec_string.append( "create table attacks (name text primary key, \n" +
        "damage integer, \n" +
        "effect text, \n" +
        "targets text, \n" +
        "power_points integer, \n"+
        "accuracy integer, \n"+
        "location_name text not null, \n"+
        "foreign key (location_name) references locations(name)" +
        ");")

    exec_string.append("create table pokemon (" +
            "name text primary key,\n" + 
        "hp integer not null, \n" +
       " type1 text not null, \n" +
        "type2 text,\n" +
        "primary_attack text,\n" + 
        "evolution_level integer,\n" +
        "secondary_attack text,\n" +
        "foreign key(primary_attack) references attacks(name),\n" +
        "foreign key(secondary_attack) references attacks(name));")

    exec_string.append("create table location_reference(" + 
       'pokemon_name text not null, location_name text not null, foreign key (pokemon_name) references pokemon(name), foreign key (location_name) references locations(name));' )

    exec_string.append("create table evolutions (" +
            "id integer primary key, parent_poke text not null, child_poke text not null, evolved integer default 0, item_used integer default 0, item text default '', " +
            "traded integer default 0, bred integer default 0, notes text," +
            "foreign key (parent_poke) references pokemon(name), foreign key (child_poke) references pokemon(name));")


    con = low_level.open_db('pokedb.db')

    print(con)

    print("CREATING TABLES \n")
    for i in exec_string:
        print("\nexecuting: " + i)
        out = low_level.execute_sql(i,con)
        print("output: \n")
        if out != None:
            for o in out:
                print(o)
        print("next statement")
        
    out = low_level.execute_sql("select * from sqlite_master where type = 'table' order by name;",con)

    print("\n\nRESULTANT TABLES:")
    for o in out:
        print(o)

    con.commit()

    print("FINISHED CREATING TABLES.") 
    con.close()
    #executor = con.cursor()

    #executor.execute('select * from sqlite_master where type="table";')

def import_data():
    #import data from csv files
    #import attack datas
    con = low_level.open_db('pokedb.db')
    poke_csv = "poke_import.csv"
    attacks_csv = "attacks_import.csv"
    locations_csv = "location_import.csv"
    local_reference_csv = "location_reference.csv"
    evolutions_csv = "evolution_import.csv"
    pokereader = csv.reader(open(poke_csv))
    attackreader = csv.reader(open(attacks_csv))
    locationreader = csv.reader(open(locations_csv))
    locationrefreader = csv.reader(open(local_reference_csv))
    evolutionsreader = csv.reader(open(evolutions_csv))

    print("\n\n IMPORTING DATA")
    insert_locations(locationreader,con,'name,description')
    insert_attacks(attackreader,con,'name,damage,effect,targets,power_points,accuracy,location_name')
    insert_pokemon(pokereader,con,'name,type1,type2,hp,primary_attack,secondary_attack,evolution_level')
    insert_location_references(locationrefreader,con,'pokemon_name,location_name')
    insert_evolutions(evolutionsreader, con)

    con.close()



if __name__ == '__main__':
    create_tables()
    import_data()
