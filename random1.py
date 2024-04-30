import random as x
print(x.random())
print(x.randint(0,9))
my_list = [1, 2, 3, 4, 5]
print(x.choice(my_list))

x.shuffle(my_list)
print(my_list)

#choice,random,randint,shuffle are all in the same module 