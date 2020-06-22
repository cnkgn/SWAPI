from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"SWAPI"}

people = ["Luke Skywalker", "Chewbacca", "Yoda", "Jedi", "Storm Trooper"]

@app.get("/people/{person_id}")
def read_person(person_id : int):
    str = people[person_id - 1]
    return {"This is":str}
