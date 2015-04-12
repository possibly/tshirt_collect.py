import Order

class OrderCollection:
  def __init__(self,arrayOfOrders):
    self.orders = arrayOfOrders
    self.orderSizes = self._orderSizes()

  # returns a dictionary where key = shirt size and value is
  # an array of orders that match that shirt size.
  def _orderSizes(self):
    knownSizes = {} # [size,[order1, order2]
    for order in self.orders:
      try:
        knownSizes[order.size].append(order)
      except:
        knownSizes[order.size] = [order]
    return knownSizes

  # prints the orders of the people who ordered a given size.
  # If no size is given, prints the complete set of orders for
  # all the sizes.
  def getPeopleWhoOrderedSize(self,size=None):
    if(size != None):
      print '{0} people ordered the {1} size: {2}'.format(len(self.orderSizes[size]), size, list(str(order) for order in self.orderSizes[size]))
    else:
      for k,v in self.orderSizes.iteritems():
        print '{0} people ordered the {1} size: {2}'.format(len(v), k, list(str(order) for order in v))
        print ''

  # prints the names of the people who have ordered.
  def getNames(self):
    names = [] # [name1,name2]
    for order in self.orders:
      names.append(order.name)
    print 'The following people have orders:'
    for name in sorted(names):
      print name

  # print the emails of the people who have ordered.
  def getEmails(self):
    emails = [] # [email1,email2]
    for order in self.orders:
      emails.append(order.email)
    print 'The emails of the people who have ordered are:'
    for email in emails:
      print email
