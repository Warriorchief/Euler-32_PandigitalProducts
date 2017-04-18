#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 16:23:40 2017

@author: christophergreen

Euler Project

Pandigital products
Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and 
product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 
9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""


import itertools;

elems=['1','2','3','4','5','6','7','8','9'];

def change_to_int(listofstrings):
    i=0;
    holder="";
    while i<len(listofstrings):
        holder+=listofstrings[i];
        i+=1;
    #print(str(holder));
    #print(int(holder));
    return int(holder);

def is_pandigital(num):
    i=0;
    while i<9:
        if elems[i] in str(num):
            i+=1;
        else:
            return False;
    return True;

ones=(list(itertools.permutations(elems,1)))
twos=(list(itertools.permutations(elems,2)));
threes=(list(itertools.permutations(elems,3)));
fours=list(itertools.permutations(elems,4));
#print(len(twos),len(threes),len(fours));  #--> 72 504 3024

c=0;
while c<72:
    twos[c]=change_to_int(twos[c]);
    c+=1;
d=0;
while d<504:
    threes[d]=change_to_int(threes[d]);
    d+=1;
e=0;
while e<3024:
    fours[e]=change_to_int(fours[e]);
    e+=1;
m=0
while m<9:
    ones[m]=change_to_int(ones[m])
    m+=1
n=0

    
    
    
prods=[];
i=0;
while i<72:
    j=0;
    while j<504:
        triple=[twos[i],threes[j],twos[i]*threes[j]];
        prods.append(triple);
        j+=1;
    i+=1
#print("length of prods is",len(prods));  #--> 38288
#print("each element in prods has length",len(prods[7777]),". For example prods[7777] is", prods[7777]);
#print("this means:",prods[7777][0],"*",prods[7777][1],"=",prods[7777][2]);

goods=[];
f=0;
while f<36288:
    if len(str(prods[f][2]))==4:
        goods.append(prods[f]);
    f+=1;    
#print("products of (two-dig)*(three-dig) that are (four-dig):",len(goods),"before removing dupes");   #-->5697 
#print("for example,goods[3333] is",goods[3333]); #--> [26, 312, 8112]
   
nines=[];  
g=0;
while g<len(goods):
    twostr=str(goods[g][0])[0]+str(goods[g][0])[1];
    threestr=str(goods[g][1])[0]+str(goods[g][1])[1]+str(goods[g][1])[2];
    fourstr=str(goods[g][2])[0]+str(goods[g][2])[1]+str(goods[g][2])[2]+str(goods[g][2])[3];
    nines.append([twostr+threestr+fourstr,goods[g]]);
    g+=1;
#print("the length of nines is",len(nines),". For example nines[222] is",nines[222]); #--> 5697 -->124975964
#print("each element in nines has length",len(nines[555])); #-->9


                                              
                                              
                                              
                                              


#########SPECIAL LATE REALIZATION THAT YOU CAN ACTUALLY GET A ONE-NINE PANDIG BY MULT A ONE-DIG BY FOUR-DIG########
one_by_fours=[]
h=0
while h<9:
    k=0
    while k<3024:
        thing=[ones[h],fours[k],ones[h]*fours[k]]
        one_by_fours.append(thing)
        k+=1
    h+=1
#print("the length of one_by_fours is",len(one_by_fours))  #--> 27216
    
specgoods=[]
for p in one_by_fours:
    if len(str(p[2]))==4:
        specgoods.append(p)
#print("products of (one-dig) and (four-dig) that are (four-dig):",len(specgoods)) #--> 6215

newnines=[]
q=0
while q<len(specgoods):
    newonestr=str(specgoods[q][0])[0]
    newfourstr=str(specgoods[q][1])[0]+str(specgoods[q][1])[1]+str(specgoods[q][1])[2]+str(specgoods[q][1])[3]
    otherfourstr=str(specgoods[q][2])[0]+str(specgoods[q][2])[1]+str(specgoods[q][2])[2]+str(specgoods[q][2])[3]
    newnines.append(newonestr+newfourstr+otherfourstr)
    q+=1
#print("the length of newnines is",len(newnines),".For example newnines[555] is",newnines[555]) #--> 6215 --> 12736
#print("each element in newnines has length",len(newnines[555])) #--> 5



answers=[];                                         
for q in nines:
    if is_pandigital(q[0]):
        answers.append(q)      
for r in newnines:
    if is_pandigital(r[0]):
        answers.append(r)
print(answers)


"""
z=0
while z<len(answers):
    answers[z][0]=int(answers[z][0])
    z+=1
#print(answers) #--> the actual "products" are the last element in each substring of this
finals = [y[1][2] for y in answers]
#print(finals) #--> [5796, 5346, 5346, 4396, 7254, 5796, 7632] #then remove duplicates!!!
ultimate=(list(set(finals)))
print (sorted(ultimate)) #--> [4396, 5346, 5796, 7254, 7632]
print("the solution to this euler question is the sum of these above, which is",sum(ultimate)) 30424 INCORRECT
"""

