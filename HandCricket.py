import random
def even(coin,name):
    z=0
    if coin%2==0:
        print("Congratulations",name,"You have won the Toss")
        z+=1
        return z
    else:
        print(f"Hard luck {name}!,You have lost the toss" )
        z+=2
        return z
def odd(coin,name):
    z=0
    if coin%2==1:
        print(f"Congratulations {name},You have won the toss")
        z+=3
        return z
    else:
        print(f"Hard luck {name},You have lost the toss")
        z+=4
        return z


def bat1(name,overs):
    score=0
    z=0
    value=None
    print("Let's start the match",name)
    for i in range(0,overs):
        ub=int(input("Enter number:"))
        ab=value or int(random.randint(1,6))
        print("My guess is",ab)
        if ub!=ab:
            score=score+ub
            print("Your score is",score)
            continue
        return int(score) 
        if ub==ab:
            if score<=10:
                 print("Gone.. Go home",name,"You are out for very cheap score",score)
                 return int(score) 
            if score>=11:
                print("You are out",name,"for",score)
                return int(score) 
                
    return int(score)
    


def winner(name,target,scr2,abow):
    if scr2>=target:
        print("Well played",name, "You Lost..Better luck next time")
    if scr2==abow:
        print("So So close...Match is drawn",name)
        
    if scr2<target:
        print("Congratulations",name,"You deserved to be the winner")
def winuser(name,target,usersc,aiscore):
    if usersc>=target:
        print("Congratulations!.. ",name," You have won the match")
    if usersc==aiscore:
        print("so.. so..  close match is drawn",name)
    if usersc<aiscore:
        print("Well played!!.. ",name," Better luck next time")
        
def chase(overs,name,target):
    value=None
    scr2=0
    print("My target to beat you is",target)
    if scr2<target:
        for i in range(0,overs):
            uch=int(input("Enter your guess:"))
            ach=value or int(random.randint(1,6))
            print("My guess is",ach)
            if uch!=ach:
                scr2=scr2+ach
                print("score=",scr2)
                if scr2>=target:
                    return scr2
                    break
            if uch==ach:
                print("Oh my god!!.. am out for",scr2)
                return scr2
                break
    return scr2
            
def aibat(name,overs):
    print("Let's start the match",name)
    aiscore=0
    value=None
    for i in range(0,overs):
        u2bowl=int(input("Enter your guess:"))
        aibat=int(value or random.randint(1,6))
        print("Mychoice:",aibat)
        if u2bowl!=aibat:
             aiscore=aiscore+aibat
             print("My score is",aiscore)
             continue
             return aiscore
        if u2bowl==aibat:
            print("Arey yar.. I am out for",aiscore) 
            break
            return aiscore
    return int(aiscore)   
        
def uchase(name,overs,u2trgt):
    value=None
    uscore=0
    print("Your target to beat me is",u2trgt)
    if uscore<u2trgt:
        for i in range(0,overs):
            user=int(input("Enter your guess:"))
            art=int(value or random.randint(1,6)) 
            print("My choice:",art)
            if user!=art:
                uscore=uscore+user
                print("Your score is",uscore)
                if uscore>=u2trgt:
                    return uscore
                    break
            if user==art:
                print("Gone!.. You are out for",uscore)
                return uscore
                break
        return uscore
        
value=None
toss=["bat","bowl"]
name=input("Hey bro!!.. How can i call You?:")
print("Hello",name)
balls=6
overs=int(input("Enter the number of overs:"))
overs=balls*overs
uc=input("odd or even:")
uip=int(input(("Enter the number for Toss:"))) 
aip=value or int(random.randint(1,6))
print("My guess is",aip)
coin=uip+aip
if uc=="even":
    option=even(coin,name)
if uc=="odd":
   option=odd(coin,name)
if option==1 or option==3:
    print("Bowling or Fielding...lol!!,sorry",name)
    dec=input("Bat or Bowl:")
    if dec=="bat":
        f1=bat1(name,overs)
        target=f1+1
        user1sc=f1
        final=chase(overs,name,target)
        winner(name,target,final,
        user1sc)
    if dec=="bowl":
        u1=aibat(name,overs)
        u2trgt=u1+1
        a2score=u1
        usefin=uchase(name,overs,u2trgt)
        winuser(name,u2trgt,usefin,a2score)
if option==2 or option==4:
    choice=random.choice(toss)
    adec=print("I have decided to",choice,"first") 
    if choice=="bat":
        a1score=aibat(name,overs)
        atrgt=a1score+1
        print("You can't win.. But give a try",name,"Your target is",atrgt)
        dumm=uchase(name,overs,atrgt)
        winuser(name,atrgt,dumm,a1score)
    if choice=="bowl":
        abow=bat1(name,overs)
        abtrgt=abow+1
        abfina=chase(overs,name,abtrgt) 
        winner(name,abtrgt,abfina,abow)
