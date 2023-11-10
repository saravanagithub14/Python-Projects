#!/usr/bin/env python
# coding: utf-8

# # Hand Cricket in python 
# By Saravana Perumal R

# In[1]:


#  Random library was imported for the purpose of computer gameplay.
import random
#  A function was defined for thr purpose of collecting player name.
def player_name():
    global player
    player = input ("enter your name  ")

            


# In[9]:


#  Function defined to take player input in game play and its error handling.
def player_input ():
    global p_input 
    p_input = int(input ('insert number between 1 to 6 '))
while p_input not in range(1,6):
    print ("invalid input, insert only numbers in range of 1 and 6")
    p_input = int(input ('insert number between 1 to 6 '))


# In[10]:


#  Defining a Function to enable the computer to randomly insert an input.
def computer_input():
    global c_input
    c_input = random.randint(1,6)


# In[11]:


#  Defining a toss function to have an unbiased batting choice.
def toss():
    global odd_or_even
    global p_toss
    global batting_team
    global c_toss
    p_toss = str(input('odd or even   '))

    while p_toss.lower() not in ['odd','even']:
        print ('invalid response, please enter odd or even')
        p_toss = input('odd or even')
    
    if p_toss == "odd":
        c_toss = "even"
    else:
        c_toss = "odd"
        
    player_input()
    computer_input()
    
    toss_sum = p_input + c_input
    print (f'Player input is {p_input} and computer input {c_input} and sum is {toss_sum}')
    if toss_sum % 2 == 0 and p_toss == 'even':
        p_bat_or_ball = str(input ('batting or bowling'))
        if p_bat_or_ball == "bowling":
            batting_team = 'computer'
        else:
            batting_team = player
    elif toss_sum % 2 != 0 and p_toss == 'odd':
        p_bat_or_ball = str(input ('batting or bowling'))
        if p_bat_or_ball == "bowling":
            batting_team = 'computer'
        else:
            batting_team = player
    else :
        c_bat_or_bowl = random.choice(['batting','bowling'])
        if c_bat_or_bowl == "batting":
            batting_team = 'computer'
        else:
            batting_team = player
            
    print(f"Batting team is {batting_team}")
            
          
        


# In[12]:


#  Defining a function for declaring the batting for both player and computer.
def batting_function():
    global c_runs
    global p_runs
    global batting_team
    if batting_team == 'computer':
        c_runs += c_input
        print (f'computer input is {c_input}')
        print (f'player input is {p_input}')
        print (f'computer scored {c_runs}runs')
    
    else:
        batting_team = player
        p_runs += p_input
        print (f'computer input is {c_input}')
        print (f'player input is {p_input}')
        print (f'{player} scored {p_runs} runs')
    


# In[13]:


#  Defining a function for declaring the bowling for both player and computer.
  
def bowling():
    global change
    global turn
    global batting_team 
    global game
    change = "no"
    if p_input == c_input:
        if turn == 1:
            print (f'*******************************{batting_team} is out ******************************************************** ')
            print (f'computer input is {c_input}')
            print (f'player input is {p_input}')
            if batting_team == 'computer':
                batting_team = player
            else:
                batting_team = 'computer'
            print (f'{batting_team} in now batting')
            turn = 2
            change = "yes"
        else:
            print (f'*******************************{batting_team} is out***********************************************************')
            print (f'computer input is {c_input}')
            print (f'player input is {p_input}')
            game = False


# In[14]:


# Defining a function for declaring the winner.
def winner():
    
    if p_runs > c_runs:
        print (f'congratulations {player} won the match against the system')
        
    if p_runs < c_runs:
        print ('You got beaten by the System, Pathetic')
        
    if p_runs == c_runs:
        print ('match draw No one won')
        


# In[15]:


# Defining a function to recall the functions defined into a game format.
def match():
    print('Welcome to the game, try to beat the system')
    global game
    global change
    global turn
    global c_runs 
    global p_runs
    player_name()
    toss()
    turn = 1
    p_runs = 0
    c_runs = 0
    game = True
    while game == True:
        player_input()
        computer_input()
        bowling()
        if change == 'yes':
            continue
            change = "no"
        batting_function ()
    winner()
    print ("-----------------------------------Match Summary----------------------------------------------") 
    print (f'{player} runs is {p_runs}')
    print (f'computer runs is {c_runs}')
     
    
    


# In[16]:


#  Recalling the match 
match()


# ## 

# In[ ]:




