from OrderCollection import OrderCollection
from Order import Order

myorders = OrderCollection([
           Order('Tyler','m','tylerbrothers1@gmail.com'),
           Order('person2','xl','theiremail@whatevs.com'),
          ])

myorders.getPeopleWhoOrderedSize()
'''
Outputs: 
1 people ordered the m size: ['Tyler <tylerbrothers1@gmail.com>']
1 people ordered the l size: ['person2 <theiremail@whatevs.com>']
'''
myorders.getPeopleWhoOrderedSize('m')
'''
Outputs: 
1 people ordered the m size: ['Tyler <tylerbrothers1@gmail.com>']
'''