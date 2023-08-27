#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 19:05:40 2023

@author: adi
"""

########################################################################
#Write a function to covert an integer number to binary using base.
#Write a function to covert binary to an integer number using base.
#Write a function to coverts a binary number to another binary number
#when base changes.
#Write a function that embeddes a given message into an image using LSB
#Write a fuction to decode the pervious function.
#Apply the funtions and make loops to print out desire result in 
#main function.
########################################################################

MENU = '''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             E. Encode an image with a text.
             D. Decode an image.
             M. Display the menu of options.
             X. Exit from the program.'''
    
def numtobase( N, B ):
    res=''
    #Initialize quotient as N for code to run in loop
    quotient=N 

    while True:
        # Used to calculate binary number
        if quotient!=0:
            remainder=quotient%B
            quotient=quotient//B
            remainder=str(remainder)
            res+=remainder

            
        else:

            break
    # reverse the result and add the additional zeros
    res=res[::-1]
    length=len(res)%8
    extra_zeros=8-length
    total=extra_zeros*"0"+res
    if total=="00000000":
        total=""
    return total



#function to covert binary to an integer number using base.
def basetonum( S, B ):
    total=0
    index=0
    S=S[::-1]
    for i in S:
        total+=(int(i))*(B**index)
        index+=1
    return total


                   
#function to coverts a binary number to another binary numberwhen base changes.
def basetobase(B1,B2,s_in_B1):
    s_in_B1=str(s_in_B1)
    B2=int(B2)
    B1=int(B1)
    x=(basetonum(s_in_B1, B1))
    y=(numtobase(x,B2))
    return y


#function that embeddes a given message into an image using LSB
def encode_image(image,text,N):
    res=''
    index = 0
    message = image
    for i in text:
        x=ord(i)
        conversion=numtobase(x, 2)
        res+=conversion
    if len(message)/3<len(res):
        return ''
    else:
        index = int(N)-1
        for ch in res:
            message = message[:index] + ch +image[index+1:]
            index += N
            
        return message

#fuction to decode the pervious function (reverse of perivous function).  
def decode_image(sego,N):
    encoded = ''
    for i in range(N-1, len(sego),N):
        encoded += sego[i]
    character = ''
    result = ''
    if sego=='':
        return ''
    else:
        for i in range(0,(len(encoded)//8)*8,8):
            character = encoded[i:i+8]
            conversion = chr(int(basetonum(character,2)))
            result += conversion
        return result

#Take user's input in order to perform desired function
def main():
    BANNER = '''
               A long time ago in a galaxy far, far away...   
              A terrible civil war burns throughout the galaxy.      
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~
    '''

    print(BANNER)
    print(MENU)
    #Write a while loop to output desired function
    while True:
        options=('A','B','C','E','D','M','X')
        answer=input("\n\tEnter option: ")
        answer=answer.upper()
        # if x is inputed a statement is printed and program ends.
        if answer=="X":
            print('\nMay the force be with you.')
            break
        if answer in options:
            if answer=="A":
                N=input("\n\tEnter N: ")
                #Error check and prompts user to input valid integer.
                while N.isdigit() == False:
                    print("\n\tError: {} was not a valid non-negative \
integer.".format(N))
                    N=input("\n\tEnter N: ")
                
                Base=int(input("\n\tEnter Base: "))
                #base check to prompr user to input valid base
                while Base < 2 or Base >10:
                    print("\n\tError: {} was not a valid integer between 2 \
and 10 inclusive.".format(Base))
                    Base=int(input("\n\tEnter Base: "))
                    #Uses numtobase function
                print("\n\t {} in base \
{}: {}".format(N,Base,numtobase(int(N),int(Base))))
                continue
            
            elif answer == "B":
                S=str(input("\n\tEnter string number S: "))
                Base=int(input("\n\tEnter Base: "))
                #base check to prompr user to input valid base
                while Base < 2 or Base >10:
                    print("\n\tError: {} was not a valid integer between 2 \
and 10 inclusive.".format(Base))
                    Base=int(input("\n\tEnter Base: "))
                    #uses basetonum function
                print("\n\t {} in base \
{}: {}".format(S,Base,basetonum(S,Base)))
                continue

            elif answer == "C":
                B1=int(input("\n\tEnter base B1: "))
                #base check to prompr user to input valid base
                while B1 < 2 or B1 >10:
                    print("\n\tError: {} was not a valid integer between 2 \
and 10 inclusive.".format(B1))
                    B1=int(input("\n\tEnter base B1: "))
                B2=int(input("\n\tEnter base B2: "))
                while B2 < 2 or B2 >10:
                    print("\n\tError: {} was not a valid integer between 2 \
and 10 inclusive.".format(B2))
                    B2=int(input("\n\tEnter base B2: "))
                s_in_B1=str(input("\n\tEnter string number: "))
                print("\n\t {} in base {} is {} in base \
{}...".format(s_in_B1,B1,basetobase(B1,B2,s_in_B1),B2))
                continue

            elif answer =="E":
                code=''
                image=str(input("\n\tEnter a binary string of an image: "))
                N= (input("\n\tEnter number of bits used for pixels: "))
                text=str(input("\n\tEnter a text to hide in the image: "))
                for ch in text:
                    code += numtobase(ord(ch),2)
                while N.isdigit() == False:
                    print("\n\tError: {} was not a valid non-negative \
integer.".format(N))
                    N=input("\n\tEnter N: ")
                if len(code) > len(image):
                    print("\n\tImage not big enough to hold all the text \
to steganography")
                else:
                    print("\n\t Original image: {}\n\n\t Encoded image: \
{}".format(image,encode_image(image,text,int(N))))
                continue

            elif answer =="D":
                sego=input("\n\tEnter an encoded string of an image: ")
                N=input("\n\tEnter number of bits used for pixels: ")
                print("\n\t Original \
text: {}".format(decode_image(sego,int(N))))
                continue

            # if M is inputed the menu is reprinted
            elif answer =="M":
                print(MENU)
                continue
        
# if a character out of domain is inputed display error and print menu again.    
        else:
            print("\nError:  unrecognized option [{}]".format(answer))
            print(MENU)
            continue



        

# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == '__main__': 
    main()
