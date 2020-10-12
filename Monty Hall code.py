#!/usr/bin/env python
# coding: utf-8

# In[2]:


def Monty_Hall():
    import random
    c=True
    item=['car','goat','goat']
    list=[]
    flag=0
    while(c):  #loop for randomising door number
        r=random.randint(1,3)  #selecting a random number in range 1 to 3
        if r not in list: 
            list.append(r)  #storing that random number in the list
        if len(list)==3:
            c=False
    list2=[]
    c=True
    while(c):  #loop for randomising items
        r=random.randint(0,2)  #selecting a random number in range 0 to 2
        if r not in list2: 
            list2.append(r)  #storing that random number in the list2
        if len(list2)==3:
            c=False
    dic={list[0]:item[list2[0]],list[1]:item[list2[1]],list[2]:item[list2[2]]}
    #assigning the randomly selected item to the randomly selected door(double randomisation)
    #at this point even the coder doesnt know which door is assigned to which item
    print('DOOR 1\nDOOR 2\nDOOR 3')
    print('Choose a door')
    door_chosen=int(input())
    if(door_chosen>3 or door_chosen<1):
        print('wrong option')
        flag=1
    if flag==0:
        print('You chose door No.',door_chosen)
        for i in range(1,4):
            if(dic[i]=='goat' and i!=door_chosen):
                door_open=i
                break
        print('Door No.',door_open,'is opened and it has a',dic[door_open])
        print('Make your choice\n1.Stick to my choice\n2.Switch my choice')
        final_choice=int(input())
        if(final_choice==1):
            print('Door No.',door_chosen,'is opened and it has',dic[door_chosen])
            if(dic[door_chosen]=='car'):
                print('CONGRATULATIONS YOU WON')
            else:
                print('YOU LOST')
        elif(final_choice==2):
            for i in list:
                if(i!=door_chosen and i!=door_open):
                    switch_door=i
                    break
            print('Door No.',switch_door,'is opened and it has',dic[switch_door])
            if(dic[switch_door]=='car'):
                print('CONGRATULATIONS YOU WON')
            else:
                print('YOU LOST')
        else:
            print('Wrong choice')
            print()
        print('Answer Key\n',dic) 

Monty_Hall()

