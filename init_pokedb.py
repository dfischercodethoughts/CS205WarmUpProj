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

exec_string.append("create table locations (name text primary key, " +
    "description text, "+
    "north_exit text, "+
    "east_exit text, "+
    "south_exit text, "+
    "west_exit text, "+
    "foreign key(north_exit) references locations(name),"+
    "foreign key(east_exit) references locations(name),"+
    "foreign key(south_exit) references locations(name),"+
    "foreign key(west_exit) references locations(name)"+
    ");")

exec_string.append( "create table attacks (name text primary key, " +
    "damage integer, " +
    "effect text, " +
    "targets text, " +
    "power_points integer, "+
    "accuracy integer, "+
    "location_name text not null, "+
    "foreign key (location_name) references locations(name)" +
    ");")

exec_string.append("create table pokemon (" +
        "name text primary key," + 
    "hp integer not null, " +
   " type1 text not null, " +
    "type2 text," +
    "primary_attack text," + 
    "secondary_attack text," +
    "location_record_id integer," +
    "foreign key(primary_attack) references attacks(name)," +
    "foreign key(secondary_attack) references attacks(name)," +
    "foreign key(location_record_id) references locations(name));")

exec_string.append("create table location_records(" + 
    "id integer primary key, " +'location_1 text not null, location_2 text not null, location_3 text not null, location_4 text not null, location_5 text not null, location_6 text not null,' + 
    'pokemon_name text not null, ' + 'evolved int not null default 0, '+
    'evolved_from text, ' + 'evolution_level integer,' + 'foreign key(location_1) references locations(name),'  + 
    'foreign key(location_2) references locations(name),' + 'foreign key(location_3) references locations(name),'  + 
    'foreign key(location_4) references locations(name),'  + 'foreign key(location_5) references locations(name),'  + 
    'foreign key(location_6) references locations(name),' +
    'foreign key(pokemon_name) references pokemon(name));')

print("CREATING TABLES \n")
for i in exec_string:
    execute_sql(i,con)
    
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
        sqlstring = "insert into locations (name, description) values (" + record[0] + "," + record[1] + ");"
    print("executing " + sqlstring)
    executor.execute(sqlstring)
    print("output: ")
    outs = executor.fetchall()
    for o in outs:
        print(o)


executor.close()

con.close()


