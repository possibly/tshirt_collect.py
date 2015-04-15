class OrderCollection:
  def __init__(self, orders):
    self.orders = orders

  # make work for arrays (get all objects which have, as keys, the properties in array)
  # make work for arrays (get all objects which have, as values, the properties in array)
  def getPeopleWhoOrdered(self, requestedProperties, strict=False):
    # Strict means dict's were used and all properties in requestedProperties must be in an order.
    if strict is True:
      filteredList = filter(lambda order: order == requestedProperties, self.orders)
      if not filteredList:
        return 'Sorry, no orders were found that match your criteria.'
      else:
        return filteredList
    else:
      '''
      Unholy lambda functions with list comprehensions

      Explanation:
      return any object in orders that meets this condition:
         return any object in requestedProperties that meets this condition:
           the key in RequestedProperties that is in order and order's key is the same as RequestedProperties key
        [object in requestedProperties]
      bool([object in requestedProperties]) is True, bool(None) is False
      '''
      return filter(lambda order:
                      filter(lambda (key,value): 
                        key in order and order.get(key) is value,
                      requestedProperties.iteritems()),
                    self.orders)

      # Functional approach with list comprehensions
      # self.requestedProperties = requestedProperties
      # return filter(self.matchProperties,self.orders)

      #Imperative approach with List Comprehensions
      # filterOrders = []
      # for order in self.orders:
      #   hasAllProperties = True
      #   for reqProperty,reqValue in requestedProperties.iteritems(): 
      #       try:
      #         if (reqProperty in order and order.get(reqProperty) is not reqValue): 
      #           hasAllProperties = False
      #           break
      #       except Exception, e:
      #         hasAllProperties = False
      #         break
      #   if (hasAllProperties):
      #     filterOrders.append(order)
      # return filterOrders

  def matchProperties(self,order):
    for reqProperty,reqValue in self.requestedProperties.iteritems():
      try:
        if (reqProperty in order and order.get(reqProperty) is not reqValue): return False 
      except Exception, e:
        return False
    return True