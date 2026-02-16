# 6. Create a log file and write error messages
try:
    x = 1 / 0
except Exception as e:
    with open("error.log", "a") as log:
        log.write(str(e) + "\n")
    print("Error logged to error.log")
