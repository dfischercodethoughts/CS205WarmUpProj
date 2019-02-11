#code to read in .csv files and init sqlite3 db
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

exec_string.append( "create table location_records (" +
    "id integer primary key, " +'location_name_1 text not null, location_name_2 text not null, location_name_3 text not null, location_4 text not null, location_5 text not null, location_6 text not null,' + 
    'pokemon_name text not null, ' + 'evolved int not null default 0, '+
    'evolved_from text, ' + 'evolution_level integer );')


exec_string.append("""create table pokemon (name text primary key, 
    hp integer not null, 
    location_record_id integer, 
    type1 text not null, 
    type2 text, 
    primary_attack text not null, 
    secondary_attack text);"""
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

exec_string.append( """alter table pokemon add primary_attack foreign key (primary_attack) references attacks(name),
    foreign key (secondary_attack) references attacks(name),
    foreign key (location_record_id) references location_records(id)
    );""")


for i in exec_string:
    print(i)
    executor.execute(i)

con.commit()

#executor = con.cursor()

#executor.execute('select * from sqlite_master where type="table";')

table_name_verify = executor.fetch_all()
for table_name in table_name_verify:
    print(table_name)

executor.close()
con.close()
