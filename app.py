import classes
import objects as Object

loadedObjects = []


def findObject(name):
  for obj in loadedObjects:
    if obj.name == name:
      return obj
  return None

while True:
  read = input("> ").lower()
  
  # Allow the user to quit the app gracefully
  if read == "exit":
    break
  
  split = read.split()
  action = split[0]
  obj = None
  
  if len(split) >= 2:
    obj = split[1]
  
  # Find the object in the room
  if obj != None:
    obj = findObject(obj)
    
  # Perform the action on the object
  try:
    getattr(obj, action)()
  except AttributeError:
    print("Cannot perform that action on that object")
    continue