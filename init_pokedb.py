code to read in .csv files and init sqlite3 db
import csv
import sqlite3

poke_csv = "poke_import.csv"
attacks_csv = "attacks_import.csv"
locations_csv = "location_import.csv"
local_reference_csv = "location_reference.csv"

pokereader = csv.reader(open(poke_csv))
attackreader = csv.reader(open(attacks_csv))
locationreader = csv.reader(open(locations_csv))
locationrefreader = csv.reader(open(local_reference_csv))

con = sqlite3.connect('pokedb.db')

executor = con.cursor()

exec_string = []

exec_string.append( "create table location_records_no_fk (" +
    "id integer primary key, " +'location_name_1 text not null, location_name_2 text not null, location_name_3 text not null, location_4 text not null, location_5 text not null, location_6 text not null,' + 
    'pokemon_name text not null, ' + 'evolved int not null default 0, '+
    'evolved_from text, ' + 'evolution_level integer );')


exec_string.append("""create table pokemon_no_fk (name text primary key, 
    hp integer not null, 
    location_record_id integer, 
    type1 text not null, 
    type2 text);"""
)
exec_string.append("""create table locations (name text primary key, 
    description text, 
    north_exit text, 
    east_exit text, 
    south_exit text, 
    west_exit text, 
    foreign key(north_exit) references locations(name),
    foreign key(east_exit) references locations(name),
    foreign key(south_exit) references locations(name),
    foreign key(west_exit) references locations(name)
    );""")

exec_string.append( """create table attacks (name text primary key, 
    damage integer, 
    effect text, 
    targets text, 
    power_points integer,
    accuracy integer,
    location_name text not null,
    foreign key (location_name) references locations(name)
    );""")

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

exec_string.append('drop table location_records_no_fk;')
exec_string.append('drop table pokemon_no_fk;')



for i in exec_string:
    print(i)
    executor.execute(i)
    executor.execute("select * from sqlite_master")
    out = executor.fetchall()
    print("output:")
    for o in out:
        print(o)

con.commit()

#executor = con.cursor()

#executor.execute('select * from sqlite_master where type="table";')

table_name_verify = executor.fetchall()
for table_name in table_name_verify:
    print(table_name)

executor.close()
<<<<<<< HEAD
con.close()
=======
con.close()
>>>>>>> 7f042b38be5955b3cf8cdd86b32779b90560cf0f
