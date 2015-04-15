from OrderCollection import OrderCollection

    
myord = OrderCollection([
                {'name':'tyler', 'otherprop':1},
                {'size':'m','name':'sarah'}
              ])

filteredOrders = myord.getPeopleWhoOrdered({
                                            'name':'sarah',
                                          })

print filteredOrders
'''
Returns: 
>>> [{'name': 'sarah', 'size': 'm'}]
'''

filteredOrders = myord.getPeopleWhoOrdered({
                                            'name':'tyler',
                                          },strict=True)

print filteredOrders
'''
Returns:
>>> Sorry, no orders were found that match your criteria.
'''

filteredOrders = myord.getPeopleWhoOrdered({
                                            'size':'m',
                                            'name':'sarah'
                                          },strict=True)

print filteredOrders
'''
Returns:
>>> [{'name': 'sarah', 'size': 'm'}]
'''