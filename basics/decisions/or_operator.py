print("What type of adventure should I have?")
answer = input()

if ((answer == "scary") or (answer == "short")):
  print("Entering the dark forest!")
elif ((answer == "safe") or (answer == "long")):
  print("Taking the safe route!")
else:
  print("Not sure which route to take.")
  