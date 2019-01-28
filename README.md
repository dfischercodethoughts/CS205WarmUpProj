# CS205WarmUpProj
Team Neutral FTW


Hey guys, we should at the least have a decent run through of how our program works here.

the main body of our program should split user input into words, and run a quick check to make sure no invalid characters (else quit), and then run a switch statement on the words...

i.e. expect user input: 
pokemon *type*


So, from what I can tell of our conversation last week, we want our tables to be:
POKEMON
  name
  trainer
  foreignKey attacks (one to many)
  foreignKey regions (one to one)
  type
  health
  
ATTACKS
  name
  type
  damage
  
REGIONS
  etcetc
  
TYPE
  fire
  water
  earth
  lightning
  poison
  psy
  air
  ??mud?
