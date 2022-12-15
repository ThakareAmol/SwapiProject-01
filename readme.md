LI application to pull data from SWAPI API and perform operations on it.
Project Structure
|--- swapi_mini
   |---models
       |--- __init__.py
       |--- basemodel.py
       |--- datamodels
          |--- __init__.py
          |--- characters.py
          |--- films.py
          |--- planets.py
          |--- species.py
          |--- starships.py
          |--- vehicles.py
   |--- resources
       |--- __init__.py
       |--- base.py
       |--- characters.py
       |--- films.py
       |--- planets.py
       |--- species.py
       |--- starships.py
       |--- vehicles.py
   |--- utils
       |--- __init__.py
       |--- fetch_data.py
       |--- logger.py
       |--- randgen.py
       |--- timeit.py
   |--- database_.sql
   |--- main.py
   |--- output.txt
   |--- readme.md
   |--- requirements.txt
   |--- task_one.py
   |--- task_three.py
   |--- task_two.py
    
CLI command to run the project
example: python main.py task_one/task_two/task_three

task_one:
Prints detail of 15 random characters
task_two:
Prints name of below resources in film 1
Character
Planet
Vehicle
task_three:
resources - ["Films", "People","Planet","Species","Starships","Vehicles"]
get count of each resource
get "singular" resource urls of each resource
pull data from random 3 "singular" resource URLs
