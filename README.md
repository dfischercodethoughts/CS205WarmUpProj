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
    git remote set-url origin git@github.com:username/repo.git
    git push origin master
