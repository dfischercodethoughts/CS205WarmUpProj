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
    "id integer primary key, " +
    "route_1 integer default 0, "+ 
    "route_2 integer default 0, "+ 
    "route_3 integer default 0, "+ 
    "route_4 integer default 0, "+ 
    "route_5 integer default 0, "+ 
    "route_6 integer default 0, "+ 
    "route_7 integer default 0, "+ 
    "route_8 integer default 0, "+ 
    'route_9 integer default 0, '+ 
    "route_10 integer default 0, "+ 
    "route_11 integer default 0, "+ 
    "route_12 integer default 0, "+ 
    'route_13 integer default 0, '+ 
    'route_14 integer default 0, '+ 
    'route_15 integer default 0, '+ 
    'route_16 integer default 0, '+ 
    'route_17 integer default 0, '+ 
    'route_18 integer default 0, '+ 
    'route_19 integer default 0, '+ 
    'route_20 integer default 0, '+ 
    'route_21 integer default 0, '+ 
    'route_22 integer default 0, '+ 
    'route_23 integer default 0, '+ 
    'route_24 integer default 0, '+ 
    'lumiose integer default 0, '+ 
    'santalune_forest integer default 0, '+ 
    'friend_safari_bug integer default 0, '+ 
    'friend_safari_flying integer default 0, '+ 
    'evolved integer default 0, '+ 
    'parent_poke_lvl integer, '+ 
    'parent_poke_name text, '+ 
    'friend_safari_electric integer default 0, '+ 
    'bred integer default 0, '+ 
    'terminus_cave integer default 0, '+ 
    'friend_safari_fairy integer default 0, '+ 
    'item_used text, '+ 
    'pokemon_village integer default 0, '+ 
    'connecting_cave integer default 0, '+ 
    'friend_safari_grass integer default 0, '+ 
    'friend_safari_fighting integer default 0, '+ 
    'glittering_cave integer default 0, '+ 
    'friend_safari_fire integer default 0, '+ 
    'ambrette_town integer default 0, '+ 
    'azure_bay integer default 0, '+ 
    'cyllage_village integer default 0, '+ 
    'trade integer default 0, '+ 
    'friend_safari_ice integer default 0, '+ 
    'lost_hotel integer default 0, '+ 
    'friend_safari integer default 0, '+ 
    'frost_cavern integer default 0, '+ 
    'friend_safari_ground integer default 0, '+  
    'parfum_palace integer default 0, '+
    'reflection_cave integer default 0,'+
    'friend_safari_rock integer default 0, '+
    'friend_safari_dark integer deafult 0,'+
    'shalour_city integer default 0,'+
    'tower_of_mastery integer default 0);')


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

exec_string.append( """modify table pokemon(
    foreign key (primary_attack) references attacks(name),
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
