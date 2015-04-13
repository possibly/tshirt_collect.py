class Order:
  def __init__(self,name,size,email,canPay=False):
    self.name = name
    self.size = size
    self.email = email
    self.canPay = canPay

  def __str__(self):
    return '{0} <{1}>'.format(self.name,self.email)