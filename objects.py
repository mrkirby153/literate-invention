class Object(object):
  def __init__(self, name):
    self.name = name

class HoldableObject(Object):
    def __init__(self, name):
        self.holding = False
        super(HoldableObject, self).__init__(name)
        
def canPickUp(item):
    return isinstance(item, HoldableObject)