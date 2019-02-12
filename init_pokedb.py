#code to read in .csv files and init sqlite3 db
import csv
import sqlite3

def open_db(db_name):
    try:
        con = sqlite3.connect(db_name)
        return con
    except Exception as e:
        print(e)

    return None

def execute_sql(sql_str, con):
    cur = con.cursor()
    try:
        cur.execute(sql_str)
        out = cur.fetchall()
        con.commit()
        return out
    except Exception as e:
        print(e)

    return None

con = open_db('pokedb.db')

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
    "location_record_id integer,\n" +
    "foreign key(primary_attack) references attacks(name),\n" +
    "foreign key(secondary_attack) references attacks(name),\n" +
    "foreign key(location_record_id) references locations(name));")

exec_string.append("create table location_records(" + 
    "id integer primary key, \n" +'location_1 text not null,\n location_2 text not null,\n location_3 text not null,\n location_4 text not null, \nlocation_5 text not null,\n location_6 text not null,\n' + 
    'pokemon_name text not null, \n' + 'evolved int not null default 0, \n'+
    'evolved_from text, \n' + 'evolution_level integer,\n' + 'foreign key(location_1) references locations(name),\n'  + 
    'foreign key(location_2) references locations(name),\n' + 'foreign key(location_3) references locations(name),\n'  + 
    'foreign key(location_4) references locations(name),\n'  + 'foreign key(location_5) references locations(name),\n'  + 
    'foreign key(location_6) references locations(name),\n' +
    'foreign key(pokemon_name) references pokemon(name));\n')

print("CREATING TABLES \n")
for i in exec_string:
    print("\nexecuting: " + i)
    out = execute_sql(i,con)
    print("output: \n")
    if out != None:
        for o in out:
            print(o)
    print("next statement")
    
out = execute_sql("select * from sqlite_master where type = 'table' order by name;",con)

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
for record in locationreader:
        if record[0] != "name":
            if record[1] != "":
                sqlstring = "insert into locations (name, description) values ('" + record[0] + "','" + record[1] + "');"
            else:
                sqlstring = "insert into locations (name) values ('" + record[0] + "');"

        print("executing " + sqlstring)
        outs = execute_sql(sqlstring,con)
        print("output: ")
        if outs != None:
            for o in outs:
                print(o)

con.close()


