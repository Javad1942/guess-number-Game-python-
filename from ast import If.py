# from ast import If
# from this import s


# Name = input('enter your name :')
# if Name == 'javad' :
#     print('salam  jigar tala')
# elif Name == 'amin':
#     print('salam dayus')
# else :
#     print('salam {} oskol'.format(Name))
    
#     n=13
#     i=0
# while i <  n :
#     i = i+1
#     print(i)
#     if i == 10 :
#         break
#----------------------------
# sum = 0
# count = 0
# i = 0   
# while i != -1 :
#     i = int(input(' enter your number for average :')) 
#     sum = sum + i    
#     count +=1
    
# print('here is your anwser :',sum/count )    
#---------------------------------
# def hooghogh(hour, income_per_hour) :
#     if hour > 8 :
#         return 'mage asbi inghad kar mikoni'
#     return hour*income_per_hour

# print(hooghogh(7,24))
#-------------------------
import random
answer = random.randint(10,100)
guess = int(input('what is your guess number :'))

while guess != answer :
    
    if guess > answer:
        print('try lower guess')
        guess = int (input('try another guess :')) 
    if guess < answer :
        print('try bigger guess')
        guess = int (input('try another guess :')) 
        
print(' u made it bro ')