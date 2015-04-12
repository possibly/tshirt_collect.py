class Order:
  def __init__(self,name,size,email):
    self.name = name
    self.size = size
    self.email = email

  def __str__(self):
    return '{0} <{1}>'.format(self.name,self.email)