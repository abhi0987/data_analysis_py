import numpy as np
import matplotlib.pyplot as plt


#numpy example
d3_array = np.array([[[1,2,3],[4,5,6]],[[10,11,43],[23,34,21]]])
print "The 2nd list in first array : {}".format(d3_array[0,1])

array = np.array([[4,1,6],[3,2,4],[7,0,12]])

print 'first 2 rows : {}'.format(array[:2])
print 'first 2 rows and last 2 coloumns  : {}'.format(array[:2,1:])

personals = np.array(['Manu', 'Jeevan', 'Prakash', 'Prakash', 'Jeevan', 'Prakash'])
random_no = np.random.randn(6,4)
print random_no

print '\n'
print random_no[personals =='Manu']


#matplotlib example

x = range(100)
y = [val**3 for val in x]       # x vs x**2 graph

x = np.linspace(0,2*np.pi,100)
y = np.cos(x)

#plt.plot(x,y)

#bar graph with width

ghj =[5, 10 ,15, 20, 25]
it =[ 1, 2, 3, 4, 5]
#plt.bar(ghj, it, width =2)


#multiple bars in a isngle graph

new_llist = [[5,10,15,20],[4,12,18,19],[6,8,21,22]]
v = np.arange(4)

plt.bar(v+0.00,new_llist[0],color = 'r',width=0.25)
plt.bar(v+0.25,new_llist[1],color = 'g',width=0.25)
plt.bar(v+0.50,new_llist[2],color = 'b',width=0.25)

plt.show()
