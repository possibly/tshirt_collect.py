from OrderCollection import OrderCollection
from Order import Order

myorders = OrderCollection([
           Order('Tyler','m','tylerbrothers1@gmail.com'),
           Order('person2','xl','theiremail@whatevs.com',True),
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
myorders.getNames()
'''
Outputs:
The following people have orders:
Tyler
person2
'''
myorders.getEmails()
'''
Outputs:
The emails of the people who have ordered are:
tylerbrothers1@gmail.com
theiremail@whatevs.com
'''
myorders.displayPayInfo()
'''
Outputs:
1 people can pay: ['person2 <theiremail@whatevs.com>']
1 people who cannot pay: ['Tyler <tylerbrothers1@gmail.com>']
'''