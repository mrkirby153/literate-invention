class Room(object):
  def __init__(self, title, actions):
    self.title = title
    self.actions = actions
  def onEnter(self):
    pass
  def onLeave(self):
    pass
  def printActions(self):
    for i, action in enumerate(self.actions):
      print(" - "+str(i+1)+": "+action.description)
  def getAction(self, index):
    return self.actions[index - 1]

class Action(object):
  def __init__(self, description):
    self.description = description
  def perform(self):
    pass