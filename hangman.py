# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:06:36 2022

@author: Pranay
"""
'''print("|"+"--"+"--| ");
print("|"+"  "+"  o ");
print("|"+"  "+" /|\ ");
print("|"+"  "+"  | ");
print("|"+"  "+" / \ ");
print("="+"  "+" ")'''
def choices(word):
    global opt
    opt=list(word)
    while(len(opt)<len(word)+10):
        a=chr(random.randrange(97, 123))
        if (opt.count(a)>0):
            pass
        else:
            opt.append(a)
            
    random.shuffle(opt)
    #return opt

def memory():
    global a,b,c,d,e,f,g
    a=("|"+"--"+"--| ");
    b=("|"+"  "+"   ");
    c=("|"+"  "+"  ");
    d=("|"+"  "+"   ");
    e=("|"+"  "+"  ");
    f=("="+"  "+" ")
    
#def correct(guess,word):
    
    
    
            
        
        
    
import random
print("welcome to hangman")
word="hello"
arr1=list(word)
guess=""
for j in range(0,len(arr1)):
    guess+="_ "
print("your choices are:")
options=(choices(word))
lives=5
print("you have",lives,"lives left!")
print("|"+"--"+"--| ");
print("|"+"  "+"   ");
print("|"+"  "+"  ");
print("|"+"  "+"   ");
print("|"+"  "+"  ");
print("="+"  "+" ")
memory()
correct=0
list2=guess.split(" ")
while(correct!=len(word) and lives>0):
    print("--------------------------------------------------------")
    print(opt)
    
    ans=str(input("enter a letter:"))


    if arr1.count(ans)>0:
        indx=[]
        for j in range(len(arr1)):
            if word[j]==ans:
                indx.append(j)
        for i in indx:
            list2[i]=ans

        #correct(guess,word)

        val=len(opt)
        print((list2[0:len(word)]))
        print("great you guessed right!")
        for i in range(opt.count(ans)):
            correct+=1
            opt.remove(ans)
        
        
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print()
    else:
        print("oops you guessed wrong!")
        lives-=1
        print("you have",lives,"lives left!")
        print((list2[0:len(word)]))
        if lives==4:
            
            b="|"+"  "+"  o "
            print(a)
            print("|"+"  "+"  o ");
            print(c)
            print(d)
            print(e)
            print(f)
            print()
        elif lives==3:
            c="|"+"  "+" /|\ "
            print(a)
            print("|"+"  "+"  o ");
            print("|"+"  "+" /|\ ")
            print(d)
            print(e)
            print(f)
            print()
        elif lives==2:
            d="|"+"  "+"  | "
            print(a)
            print("|"+"  "+"  o ");
            print("|"+"  "+" /|\ ")
            print("|"+"  "+"  | ")
            print(e)
            print(f)
            print()
        elif lives==1:
            e="|"+"  "+" / \ "
            print(a)
            print("|"+"  "+"  o ");
            print("|"+"  "+" /|\ ")
            print("|"+"  "+"  | ")
            print("|"+"  "+" / \ ")
            print(f)
            print()            
        elif lives==0:
            #a="|"+"  "+"  x "
            print("game over")
            print(a)
            print("|"+"  "+"  x ");
            print("|"+"  "+" /|\ ")
            print("|"+"  "+"  | ")
            print("|"+"  "+" / \ ")
            print(f)
            print()
            
        
if correct==len(word):
    print("you win")

                
    
