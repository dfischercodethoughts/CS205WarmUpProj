#code to read in .csv files and init sqlite3 db
import csv
import sqlite3
import low_level

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
            
            for i in record:
                if i!="" and i != "FALSE" and i != "yes" and i != "no" and i != "use" and i != "bred" and i != "trade" and i != "NA":
                    sqlstring += "'" + i.replace("'","").replace('"',"") + "',"
                elif i == "no":
                    sqlstring += "0,"
                elif i == "yes":
                    sqlstring += "1,"
                else:
                    sqlstring += "null,"

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
                    sqlstring += "'" + i.replace("'","").replace('"',"") + "',"
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
    "secondary_attack text,\n" +
    "foreign key(primary_attack) references attacks(name),\n" +
    "foreign key(secondary_attack) references attacks(name)\n" +
    ");")

exec_string.append("create table location_reference(" + 
    "id integer primary key, \n" +"location_1 text not null,\n location_2 text not null,\n " +
    'location_3 text not null,\n location_4 text not null, \nlocation_5 text not null,\n location_6 text not null,\n' + 
    'pokemon_name text not null, \n' + 'evolved int not null default 0, \n'+'bred integer not null default 0, \n' + 'item_used integer not null default 0, \n'+
    'parent_pokemon text, \n' + 'evolution_level integer,\n' + 'foreign key(location_1) references locations(name),\n'  + 
    'foreign key(location_2) references locations(name),\n' + 'foreign key(location_3) references locations(name),\n'  + 
    'foreign key(location_4) references locations(name),\n'  + 'foreign key(location_5) references locations(name),\n'  + 
    'foreign key(location_6) references locations(name),\n' +
    'foreign key(pokemon_name) references pokemon(name),\n' +
    'foreign key(parent_pokemon) references pokemon(name));' )


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

#executor = con.cursor()

#executor.execute('select * from sqlite_master where type="table";')


#import data from csv files
#import attack datas

poke_csv = "poke_import.csv"
attacks_csv = "attacks_import.csv"
locations_csv = "location_import.csv"
local_reference_csv = "location_reference.csv"
pokereader = csv.reader(open(poke_csv))
attackreader = csv.reader(open(attacks_csv))
locationreader = csv.reader(open(locations_csv))
locationrefreader = csv.reader(open(local_reference_csv))


print("\n\n IMPORTING DATA")
insert_locations(locationreader,con,'name,description')
insert_attacks(attackreader,con,'name,damage,effect,targets,power_points,accuracy,location_name')
insert_pokemon(pokereader,con,'name,type1,type2,hp,primary_attack,secondary_attack')
insert_location_references(locationrefreader,con,'pokemon_name,location_1,location_2,location_3,location_4,location_5,location_6,bred,item_used,parent_pokemon,evolution_level,evolved')

con.close()


