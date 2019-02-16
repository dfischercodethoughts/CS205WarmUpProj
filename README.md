# CS205WarmUpProj
Team Neutral FTW

Updated Tasks to be completed:
    - Create functions Validate and Transform
        - Put Validate in main and Transform in low level
    - Create function to format the tables
    - Create two functions to display array of data
        - First function, one to remove Null data from output array
        - Second Function takes the processed Array and formats it and display to console
    - Decide what data user should be able to look at
    - Write the function that takes the user input and validates it
    - Function which executes the user input and converts it to SQL query

Hey guys, we should at the least have a decent run through of how our program works here.

the main body of our program should split user input into words, and run a quick check to make sure no invalid characters (else quit), and then run a switch statement on the words...

i.e. expect user input: 
pokemon *type*


DF 2-12:
All right, so tables are all set up. note that location_reference.csv is incomplete (I did the first 120 records or so though).
also, locations.csv contains a null record and an incomplete record, one of which indicates we haven't set up that pokemon's location reference, and one of which indicates that location slot is null

LOCATIONS:
PK name txt,
description txt,
FK (LOCATIONS.name) north_exit,
FK (LOCATIONS.name) east_exit,
FK (LOCATIONS.name) south_exit,
FK (LOCATIONS.name) west_exit

ATTACKS:
pk name txt,
damage int,
effect txt,
targets txt,
power_points int,
accuracy int,
FK (LOCATIONS.name) location_name

POKEMON:
pk name txt,
hp int (not null),
type1 txt (not null),
type2 txt,
FK (ATTACKS.name) primary_attack txt,
FK (ATTACKS.name) secondary_attack txt

LOCATION REFERENCE:
pk id int (autoinc),
FK (LOCATIONS.name) location_1 txt,
FK (LOCATIONS.name) location_2 txt,
FK (LOCATIONS.name) location_3 txt,
FK (LOCATIONS.name) location_4 txt,
FK (LOCATIONS.name) location_5 txt,
FK (LOCATIONS.name) location_6 txt,
FK (POKEMON.name) pokemon_name txt,
evolved int default 0,
bred int default 0,
item_used default 0,
FK (POKEMON.name) parent_pokemon txt,
evolution_level int
  
  Git with a Group Commands

To be used after you link your local repo to the project on GitLab.

    git pull origin master
    git checkout -b [YOUR_INITIALS]_[WORK_DESIGNATION]
    Do work. Check to see if it works.
    git add -A
    git commit -m "[COMMIT_MESSAGE]"
    git push origin [YOUR_INITIALS]_[WORK_DESIGNATION]
    On GitLab, send a merge request for your branch
    Wait for code approval.
    git checkout master
    git pull origin master

    //This is for deleting your branch...do this at the end, otherwise you
    //will have to create a new branch every time you do work
    git branch -D [YOUR_INITIALS]_[WORK_DESIGNATION]

How to add project to github repository

    git init
    git add .
    git commit -m "my commit"
    git remote add origin git@github.com:username/repo.git
    git push origin master
