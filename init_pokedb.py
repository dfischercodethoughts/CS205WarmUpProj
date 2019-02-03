#code to read in .csv files and init sqlite3 db
import csv
import sqlite3
from sqlite3 import Error

try:
poke_file = open("/pokemon.csv")
attacks_file = open("/attacks.csv")
locations_file = open("/locations.csv")

con = sqlite3.connect("PokeDB.db")

executor = con.cursor()

exec_string[0] = "create table pokemon (id integer primary key, name text not null, type_1 text not null, type_2 text, health integer not null, location_id integer not null, form text, base_attack_id integer not null, special_attack_id integer);";

exec_string[1] = "create table attacks (id integer primary key, name text not null, damage integer not null, effect text)";

exec_string[2] = "create table locations (id integer primary key, name text not null, description text, north_exit integer, east_exit integer, south_exit integer, west_exit integer);"

for to_exec in exec_string:
    executor.execute(to_exec)
    

con.commit()


#for each row in the csv files, turn it into a record to insert and then fucking DO IT

