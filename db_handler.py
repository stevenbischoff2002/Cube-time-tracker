from urllib.request import DataHandler
import scrambleGenerator
from uuid import uuid1
from pathlib import Path
import json
class DB:
    def __init__(self,dbPath):
        self.dbPath = dbPath
        if Path(self.dbPath).is_file():
            self.loadDB()
        else:
            self.db = {}
            self.saveDB()

    def loadDB(self):
        with open(self.dbPath,"r") as f:
            data = json.loads(f.read())
            self.db = data

    def saveDB(self):
        with open(self.dbPath,"w") as f:
            f.write(json.dumps(self.db,indent=4))

    def addEntry(self,scramble,time):
        uid = str(uuid1())
        self.db[uid] = {}
        self.db[uid]["scramble"] = scramble
        self.db[uid]["time"] = time
        self.saveDB()

if(__name__ == "__main__"):
    db = DB("db.test")