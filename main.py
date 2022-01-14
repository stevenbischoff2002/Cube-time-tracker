
if __name__ == "__main__":
    try:
        #while True:
            # time = input("---> ")
        time = "0:56.334"
        min = 60 * 1000 * int(time.split(":")[0])
        sec = 1000 * int(time.split(":")[1].split(".")[0])
        msec = int(time.split(":")[1].split(".")[1])
        print(min + sec + msec)
    except KeyboardInterrupt:
        print("stop")