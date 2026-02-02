# Convert the time entered in hh, min and sec into seconds

hours = int(input("Enter time in hours: "))
mins = int(input("Enter time in minutes: "))
sec = int(input("Enter time in seconds: "))

timeInSeconds = (hours*60*60) + (mins*60) + sec

print(f"{hours} hour {mins} minutes {sec} seconds in total is {timeInSeconds} seconds")