import scrambleGenerator
from uuid import uuid1
from pathlib import Path
import json
if __name__ == "__main__":
    try:
        if Path("db").is_file():
            with open("db","r") as f:
                db = json.loads(f.read())
        else:
            with open("db","w") as f:
                f.write("{}")
        while True:
            scramble = scrambleGenerator.gen_scramble()
            uid = str(uuid1())
            print(uid)
            print(f"\n{scramble}\n")
            time = input("Time (**:**.***) ---> ")
            min = 60 * 1000 * int(time.split(":")[0])
            sec = 1000 * int(time.split(":")[1].split(".")[0])
            msec = int(time.split(":")[1].split(".")[1])
            print(min + sec + msec)
            with open("db","w") as f:
                db[uid] = {}
                db[uid]["scramble"] = scramble
                db[uid]["time"] = min + sec + msec
                f.write(json.dumps(db,indent=4))
    except KeyboardInterrupt:
        print("stop")