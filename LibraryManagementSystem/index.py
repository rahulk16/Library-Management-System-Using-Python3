import string
import random
import getpass
import sys
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def welcome():
    print('                        __      __          _ _        _            _ _         _ _                             _ _    ')
    print('                       / /      \ \        / _ \      / /          / _ \       / _ \         /\      /\        / _ \   ')
    print('                      / /        \ \      / / \ \    / /          / / \ \     / / \ \       /  \    /  \      / / \ \  ')
    print('                     / /          \ \    / /        / /          / /   \ \   / /   \ \     / /\ \  / /\ \    / /       ')
    print('                    / /     /\     \ \  / /_ _ _   / /          / /         / /     \ \   / /  \ \/ /  \ \  / /_ _ _   ')
    print('                   / /     /  \     \ \ | |_ _ _| / /          / /         / /       \ \ / /    \  /    \ \ | |_ _ _|  ')
    print('                   \ \    / /\ \    / / | |_ _ _| \ \          \ \         \ \       / / \ \     \/     / / | |_ _ _|  ')
    print('                    \ \  / /  \ \  / /  \ \        \ \          \ \         \ \     / /   \ \          / /   \ \       ')
    print('                     \ \/ /    \ \/ /    \ \   / /  \ \          \ \   / /   \ \   / /     \ \        / /     \ \   / /')
    print('                      \  /      \  /      \ \_/ /    \ \_ _ _ _   \ \_/ /     \ \_/ /       \ \      / /       \ \_/ / ')
    print('                       \/        \/        \_ _/      \ _ _ _ _|   \_ _/       \_ _/         \ \    / /         \_ _/  ')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def enterEmailID():
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print("Please enter your email-id")
    global emailID
    emailID=input().strip()
    while emailID.rfind('.')==-1 or emailID.rfind('@')==-1 or emailID.rfind('.')<emailID.rfind('@') or emailID.rfind('.')==len(emailID)-1:
        print("You have entered an incorrect email-id")
        print("Please enter a valid email-id")
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        emailID=""
        emailID=input().strip()
    return emailID
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def extractEmailID(ch):
    s=""
    s=ch[ch.rfind(' ')+1:]
    return s
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def checkIfExists(emailID):
    check=0
    fp=open("user.txt","r+")
    ch=fp.readline()
    while ch!="":
        s=extractEmailID(ch).strip()
        if s==emailID:
                check=1
                break
        s=""
        ch=fp.readline()
    fp.close()
    return check
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def check():
    print("Are you a member of our library:y/N")
    response=input().strip()
    check=0
    if set(response.lower()).issubset("yes")==True:
        s=""
        emailID=enterEmailID()
        check=checkIfExists(emailID)
    if check==0 or set(response.lower()).issubset("no")==True:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("                                                           YOU ARE NOT A REGISTERED MEMBER OF OUR LIBRARY")
        print("                                      IF YOU WANT TO ENJOY THE SERVICES OF OUR LIBRARY THEN PLEASE FILL THE REGISTRATION FORM")
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    elif check==1:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("                                                            YOU MAY PROCEED")
    return check
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def registeration():
    na=""
    ro=""
    em=""
    cre=""
    flag=0
    print("Please enter your name")
    name=input().strip()
    na+=name
    while set(na.lower()).issubset(string.ascii_letters+' ')==False:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("                                                   YOU HAVE ENTERED AN INVALID USERNAME")
        print("                                                           ENTER A VALID USERNAME")
        na=""
        name=input().strip()
        na+=name
    na+=" "
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print("Please enter your roll number:")
    roll=input().strip()
    ro+=roll
    while set(ro).issubset(string.ascii_letters)==True or ro.count(' ')>0:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("                                                 YOU HAVE ENTERED AN INVALID ROLL NUMBER")
        print("                                                          ENTER A VALID ROLL NUMBER")
        ro=""
        roll=input().strip()
        ro+=roll
    ro+=" "
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    print("Please enter your email-id")
    global emailID
    emailID=input().strip()
    em+=emailID
    while em.rfind('.')==-1 or em.rfind('@')==-1 or em.rfind('.')<em.rfind('@') or em.rfind('.')==len(em)-1:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("                                                YOU HAVE ENTERED AN INCORRECT EMAIL-ID")
        print("                                                     PLEASE ENTER A VALID EMAIL-ID")
        em=""
        emailID=input().strip()
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        em+=emailID
    em+='\n'
    cre=na+ro+em
    fp=open("user.txt","r")
    ch=fp.readline()
    flag=1
    while ch!="":
        if cre==ch:
            flag=0
            break
        ch=fp.readline()
    fp.close()
    if flag==1:
        fp=open("user.txt","a")
        fp.write(cre)
        fp.close()
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("                                               CONGRATULATIONS! YOUR REGISTRATION WAS SUCESSFULL")
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("                                               NOW YOU CAN ENJOY THE SERVICES OF OUR LIBRARY")
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("                                               DO YOU WANT TO LEAVE THIS SESSION: y/N")
        response=input().strip()
        if set(response.lower()).issubset("yes")==True:
            sys.exit()
    elif flag==0:
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++') 
        print("                                               YOU ARE ALREADY A MEMBER OF OUR LIBRARY")
        print("                                               DO YOU WANT TO LEAVE THIS SESSION: y/N")
        response=input().strip()
        if set(response.lower()).issubset("yes")==True:
            sys.exit()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def userAccount(emailID):
    fp=open("userBooks.txt")
    ch=fp.readline()
    s=""
    while ch!="":
        ch=ch.split()
        if ch!=[]:
            if ch[0]==emailID:
                s+=(' ').join(ch[1:len(ch)-1])
                s+=';'
        ch=fp.readline()
    fp.close()
    return s

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def displayBooks():
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    fp=open("booksList.txt","r")
    ch=fp.readline()
    print('                                     THIS IS THE COMPLETE LIST OF THE BOOKS THAT ARE AVAILABLE IN OUR LIBRARY')
    while ch!="":
        ch=fp.readline()
        print(ch)
    fp.close()
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    return
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def listBooks():
    fp=open("booksList.txt","r")
    s=[]
    ch=fp.readline()
    while ch!="":
        s.append(ch.split())
        ch=fp.readline()
    fp.close()
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    return s   #------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def checkBook(nameBook):
    fp=open("booksList.txt","r")
    ch=fp.readline()
    flag=0
    while ch!="":
        if ch[:ch.rfind(' ')]==nameBook:
            flag=1
            break
        ch=fp.readline()
    return flag
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def changeUserBooks(emailID,nameBook):
    fp=open("userBooks.txt","r")
    ch=fp.readline()
    userDet=[]
    flag=0
    s=""
    e=""
    while ch!="":
        ch=ch.split()
        userDet.append(ch)
        ch=fp.readline()
    for i in range(0,len(userDet)):
        s=(' ').join(userDet[i])
        if s[s.find(' ')+1:s.rfind(' ')]==nameBook:
            userDet[i][-1]=str(int(userDet[i][-1])+1)
            flag=1
            break

    if flag==1:
        fp=open("userBooks.txt","r+")
        s=""
        for i in range(0,len(userDet)):
            s+=(' ').join(userDet[i])
            if i<len(s)-1:
                s+='\n'
            fp.write(s)
            s=""
        fp.close()
    else:
        fp=open("userBooks.txt","a")
        s=""
        s=emailID+' '+nameBook+' '+'1'+'\n'
        fp.write(s)
        fp.close()
    return
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def changeUserBooks(emailID,nameBook,operation):
    fp=open("userBooks.txt","r")
    ch=fp.readline()
    userDet=[]
    flag=0
    s=""
    e=""
    while ch!="":
        ch=ch.split()
        userDet.append(ch)
        ch=fp.readline()
    for i in range(0,len(userDet)):
        s=(' ').join(userDet[i])
        if s[s.find(' ')+1:s.rfind(' ')]==nameBook:
            if operation=="borrow":
                userDet[i][-1]=str(int(userDet[i][-1])+1)
            elif operation=="return":
                userDet[i][-1]=str(int(userDet[i][-1])-1)
                if userDet[i][-1]=='0':
                    userDet.remove(userDet[i])
            flag=1
            break

    if flag==1:
        fp=open("userBooks.txt","r+")
        s=""
        for i in range(0,len(userDet)):
            s+=(' ').join(userDet[i])
            if i<len(s)-1:
                s+='\n'
            fp.write(s)
            s=""
        fp.close()
    else:
        fp=open("userBooks.txt","a")
        s=""
        s=emailID+' '+nameBook+' '+'1'+'\n'
        fp.write(s)
        fp.close()
    return
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def bookOperation(emailID,nameBook,operation):
    fp=open("booksList.txt","r")
    ch=fp.readline()
    books=[]
    flag=0
    s=""
    while ch!="":
        ch=ch.split()
        books.append(ch)
        ch=fp.readline()
    for i in range(0,len(books)):
        s=(' ').join(books[i])
        if s[:s.rfind(' ')]==nameBook:
            if operation=="borrow":
                if int(books[i][-1])!=0:
                        books[i][-1]=str(int(books[i][-1])-1)
            elif operation=="return":
                books[i][-1]=str(int(books[i][-1])+1)
            changeUserBooks(emailID,nameBook,operation)
            flag=1
            break
    fp.close()
    if flag==1:
        s=""
        fp=open("booksList.txt","r+")
        for i in range(0,len(books)):
            s+=(' ').join(books[i])
            if i<len(s)-1:
                s+='\n'
            fp.write(s)
            s=""
        fp.close()
    if flag==0 and operation=="borrow":
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("                                   THE BOOK '%s' IS NO LONGER AVAILABLE IN OUR LIBRARY"%nameBook)
        s=""
    if flag==0 and operation=="return":
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("                                   YOU HAVE NOT TAKEN ANY SUCH BOOK FROM OUR LIBRARY")
    return
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def addUserBooks(nameBook,emailID,no):
    fp=open("booksList.txt","a")
    s=""
    s='\n'+nameBook+' '+'1'
    fp.write(s)
    fp.close()
    s=""
    fp=open("userBooks.txt","a")
    s='\n'+emailID+' '+nameBook+' '+'1'
    fp.write(s)
    fp.close()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def serve():
    print('How can we serve you:')
    print('Do you wish to:')
    print('1. Borrow')
    print('2. Return')
    response=input().strip()
    if set(response.lower()).issubset("borrow")==True:
        displayBooks()
        flag=0
        print("Type the name of the book which you want to borrow")
        nameBook=""
        nameBook+=input().strip()
        nameBook+=" "
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("Type the name of the author")
        nameBook+=input().strip()
        flag=checkBook(nameBook.upper())
        if flag==0:
            check=0
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print("The given book is not present in our library")
            print("What do u want us to do")
            print("1.Order")
            print("2.Leave")
            userResponse=input().strip()
            if userResponse.lower()=="order" or userResponse=='1':
                print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                print("Do you want to add %s to your cart"%nameBook)
                inputResponse=input().strip()
                if set(inputResponse.lower()).issubset("yes")==True:
                    addUserBooks(nameBook.upper(),emailID,1)
                    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                    print("The book: %s has been added to your cart"%nameBook)
                    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            else:
                print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                print('                                                     We hope to see us again')
                print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
                sys.exit()
        elif flag==1:
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print("                                 We can give you only 1 book at a time and that too for a maximum period of 2 weeks")
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print('                                                     It was a pleasure serving you')
            addUserBooks(nameBook.upper(),emailID,1)
            bookOperation(emailID,nameBook.upper(),response.lower())
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print('                                                    We look forward to serve you again')
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    elif response.lower()=="return":
        print("Type the name of the book which you want to return")
        nameBook=""
        nameBook+=input().strip()
        nameBook+=" "
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print("Type the name of the author")
        nameBook+=input().strip()
        bookOperation(emailID,nameBook.upper(),"return")
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('                                                     It was a pleasure serving you')
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
welcome()
chck=check()
userAfterReg=0
if chck==0:
    userAfterReg=registeration()
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print("                                                         YOU ARE INSIDE OUR LIBRARY")
record=userAccount(emailID)
print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
if record=="":
    print("                                            YOU HAVE NOT TAKEN ANY BOOK FROM OUR LIBRARY")
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
else:
    print("As per our record you have taken '%s' from our library."%(record))
    print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
serve()
#--------------------------------------------------------------------------END---------------------------------------------------------------------------------------
