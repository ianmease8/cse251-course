"""
Course: CSE 251 
Lesson Week: 03
File: assignment.py 
Author: Brother Comeau

Purpose: Retrieve Star Wars details from a server

Instructions:

- Each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used
  in this assignment.
- Run the server.py program from a terminal/console program.  Simply type
  "python server.py"
- The only "fixed" or hard coded URL that you can use is TOP_API_URL.  Use this
  URL to retrieve other URLs that you can use to retrieve information from the
  server.
- You need to match the output outlined in the decription of the assignment.
  Note that the names are sorted.
- You are requied to use a threaded class (inherited from threading.Thread) for
  this assignment.  This object will make the API calls to the server. You can
  define your class within this Python file (ie., no need to have a seperate
  file for the class)
- Do not add any global variables except for the ones included in this program.

The call to TOP_API_URL will return the following Dictionary(JSON).  Do NOT have
this dictionary hard coded - use the API call to get this.  Then you can use
this dictionary to make other API calls for data.

{
   "people": "http://127.0.0.1:8790/people/", 
   "planets": "http://127.0.0.1:8790/planets/", 
   "films": "http://127.0.0.1:8790/films/",
   "species": "http://127.0.0.1:8790/species/", 
   "vehicles": "http://127.0.0.1:8790/vehicles/", 
   "starships": "http://127.0.0.1:8790/starships/"
}
"""

from datetime import datetime, timedelta
import requests
import json
import threading

# Include cse 251 common Python files
from cse251 import *

# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
call_count = 0


# TODO Add your threaded class definition here
class Request_thread(threading.Thread):

    def __init__(self, url):
        # Call the Thread class's init function
        threading.Thread.__init__(self)
        self.url = url
        self.response = {}

    def run(self):
        response = requests.get(self.url)
        # Check the status code to see if the request succeeded.
        if response.status_code == 200:
            self.response = response.json()
        else:
            print('RESPONSE = ', response.status_code)


# TODO Add any functions you need here

def persons(movie6):
  global call_count
  steve = movie6.response['characters']
  index = 0
  players = []
  threadpersons = []
  for x in range(len(steve)):
    x = Request_thread(steve[index])
    threadpersons.append(x)
    index += 1
    call_count +=1
  for x in threadpersons:
    x.start()
  for x in threadpersons: 
    x.join()
    players.append(x.response['name'])
  players.sort()
  print(f"characters: {len(players)}")
  return players
  
def world(movie6):
  global call_count
  job = movie6.response['planets']
  index = 0
  galaxies = []
  threadgalaxies= []
  for x in range(len(job)):
    x = Request_thread(job[index])
    threadgalaxies.append(x)
    index+=1
    call_count +=1
  for x in threadgalaxies:
    x.start()
  for x in threadgalaxies:
    x.join()
    galaxies.append(x.response['name'])
  galaxies.sort()
  print(f"planets: {len(galaxies)}")
  return galaxies 

def ship(movie6):
  global call_count
  plane = movie6.response['starships']
  index = 0
  starflight = []
  threadship= []
  for x in range(len(plane)):
    x = Request_thread(plane[index])
    index+=1
    threadship.append(x)
    call_count +=1
  for x in threadship:
    x.start()
  for x in threadship:  
    x.join()
    starflight.append(x.response['name'])
  starflight.sort()
  print(f"starships: {len(starflight)}")
  return starflight

def vehicles(movie6):
  global call_count
  car = movie6.response['vehicles']
  index = 0
  bus = []
  threadvehicles = []
  for x in range(len(car)):
    x = Request_thread(car[index])
    index+=1
    threadvehicles.append(x)
    call_count +=1
  for x in threadvehicles:
    x.start()
  for x in threadvehicles:
    x.join()
    bus.append(x.response['name'])
  bus.sort()
  print(f"vehicles: {len(bus)}")
  return bus

def species(movie6):
  global call_count
  type = movie6.response['species']
  index = 0
  alien = []
  threadspecies = []
  for x in range(len(type)):
    x = Request_thread(type[index])
    index+=1
    threadspecies.append(x)
    call_count +=1
  for x in threadspecies:
    x.start()
  for x in threadspecies:
    x.join()
    alien.append(x.response['name'])
  alien.sort()
  print(f"species: {len(alien)}")
  return alien

def main():
    global call_count
    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')

    # TODO Retrieve Top API urls
    response = requests.get(TOP_API_URL)
    data = response.json()
    call_count +=1

    # TODO Retireve Details on film 6
    movie6 = Request_thread(rf"{TOP_API_URL}/films/6")
    movie6.start()
    movie6.join()
    call_count +=1

    # TODO Display results
    print(f"Title: {movie6.response ['title']}")
    print(f"Director: {movie6.response ['director']}")
    print(f"Producer: {movie6.response ['producer']}")
    print(f"Released: {movie6.response ['release_date']}")
    print(', '.join(persons(movie6)))
    print(', '.join(world(movie6)))
    print(', '.join(ship(movie6)))
    print(', '.join(vehicles(movie6)))
    print(', '.join(species(movie6)))

    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')
    

if __name__ == "__main__":
    main()
