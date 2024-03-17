

class PATTERN:
    def pattern(self):
        
        print('KITE')
        n=5
        for i in range(0,n):
            for j in range(0,n-i):
                print(" ",end='')
            for k in range(0,(2*i)-1):
                print("*",end='')
            print()
        for i in range(0,n-2):
            for j in range(3,n+i):
                print(" ",end='')
            for k in range(0,n-(i*2)):
                print("*",end='')
            print()

        print('PYRAMID')
        n=5
        for i in range(0,n):
            for j in range(0,n-i):
                print(" ",end='')
            for k in range(0,(2*i)-1):
                print("*",end='')
            print()

        print('REV PYRAMID')
        n=7
        for i in range(0,n):
            for j in range(n,n+i):
                print(" ",end='')
            for k in range(0,n-(i*2)):
                print("*",end='')
            print()

        print('HALF PYRAMID')
        n=5
        for i in range(0,n):
            for j in range(0,i+1):
                print('*',end='')
            print()

        print('REV HALF PYRAMID')
        n=5
        for i in range(0,n):
            for j in range(0,n-i):
                print('*',end='')
            print()

        print('HALF PYRAMID MIRROR REFLECTION')
        n=4
        a=1
        for i in range(n,-1,-1):
            s=' '*i+"*"*a
            a+=1
            print(s)
            

        print('PARALELLOGRAM')
        n=7
        for i in range(0,4):
            for j in range(4,n+i):
                print(" ",end='')
            for k in range(0,n):
                print('*',end='')
            print()
            

        print('2D  DIAMOND')
        n=10
        for i in range(0,1):
            for j in range(0,1):
                print(' ',end='')
            for k in range(0,n-2):
                print('*',end='')
            print()
        for i in range(0,n):
            for j in range(n,n+i):
                print(" ",end='')
            for k in range(0,n-(i*2)):
                print("*",end='')
            print()

        print(' ZED  -  Z')
        n=5
        for i in range(0,n+1):
            print('*',end='')
        print()
        for k in range(0,n):
            for j in range(0,n-k):
                print(' ',end='')
            for l in range(0,1):
                print('*',end='')
            print()
        for i in range(0,n+1):
            print('*',end='')
        print()

        print('DOOR MAT')
        n=21
        m=n*3
        a=n//2
        b=(m-3)//2
        for i in range(1,a+1):
            s='-'*(b)+'.|.'*(i*2-1)+'-'*(b)
            b-=3
            print(s)
        c=(m-7)//2
        print('-'*c+'WELCOME'+'-'*c)
        d=3
        for j in range(a,0,-1):
            s='-'*(d)+'.|.'*(j*2-1)+'-'*(d)
            d+=3
            print(s)

        print('hexagon')
        n=3
        a=1
        for i in range(n,0,-1):
            s=' '*i+"*"*a
            a+=2
            print(s)
        for j in range(n):
            s='*'*(n*2+1)
            print(s)
        for k in range(0,n+1):
            s=' '*k+'*'*a
            a-=2
            print(s)
        print()


        print('BRIDGE')
        n=10
        a=0
        for i in range(n,0,-1):
            s="*"*i+' '*a+'*'*i
            a+=2
            print(s)
        print()

        print('V VEE')
        n=5
        a=(n*2)-1
        for i in range(0,n):
            s=' '*i+'X'+' '*a+'X'
            a-=2
            print(s)
        print(' '*n+'X')
        print()

        print('X -EX')
        n=3
        a=(n*2)-1
        for i in range(0,n):
            s=' '*i+'O'+' '*a+'O'
            a-=2
            print(s)
        print(' '*n+'O')
        b=1
        for i in range(n-1,-1,-1):
            s=' '*i+'O'+' '*b+'O'
            b+=2
            print(s)
        print()

        print('HOLOW - TRIANGLE')
        for i in range(0,5):
            for j in range(0,5-i):
                print(' ',end='')
            for k in range(1,2):
                print('*',end='')
            for l in range(i*2):
                print(' ',end='')
            for m in range(1,2):
                print('*',end='')
            print()
        for j in range(0,5*2+2):
            print('*',end='')

        print()
        print('FLUTTER BY')
        n=7

        for i in range(n,0,-1):
            for j in range(i,n):
                print("o",end='')
            for k in range(i*2-2,0,-1):
                print(" ",end='')
            for l in range(i,n):
                print("o",end='')
            print()

        for i in range(1,n-1):
            for j in range(n-1,i,-1):
                print("o",end='')
            for k in range(i*2):
                print(" ",end='')
            for l in range(n-1,i,-1):
                print("o",end='')
            print()


import math
class binary_decimal:
    
    def dec_bin(self):
        n=int(input('enter number\n'))
        b=''
        while(n!=0):
            a=n%2
            b=str(a)+b
            n=n//2
            
        print(b)
        
    def bin_dec(self):
        n=int(input('enter the bin number\n'))
        s=str(n)
        a=0
        dec=0
        for i in range(len(s)-1,-1,-1):
            dec=dec+int(s[a])*(math.pow(2,i))
            a+=1
        print(f'Bin {s} : Dec ',int(dec))

    def bin_addition(self):
        print('ADDITION')
        a=input('enter the 1st bin number\n')
        b=input('enter the 2nd bin number\n')
        max_length=max(len(a),len(b))
        a=a.zfill(max_length)
        b=b.zfill(max_length)
        c=len(a)-1
        carry=0
        s=''
        for i in range(max_length):
            d=carry+int(a[c])+int(b[c])
            c-=1
            if d==1:
                carry=0
                s='1'+s
            elif d==2:
                carry=1
                s='0'+s
            elif d==3:
                carry=1
                s='1'+s
            else:
                carry=0
                s='0'+s
        if carry==1:
            s='1'+s
        print(' '+a+'\n'+'+'+b+'\n'+'---------'+'\n'+s)
        print()
        
    def bin_substraction(self):
        print('SUBSTRACTION')
        print('IF LENGTH IS SAME TRY PUTTING BIGGER BIN NUMBER FIRST')
        a=input('enter the 1st bin number\n')
        b=input('enter the 2nd bin number\n')
        max_length=max(len(a),len(b))
        a=a.zfill(max_length)
        b=b.zfill(max_length)
        c=len(a)-1
        s=''
        carry=0
        for i in range(max_length):
            if a[c]=='0' and b[c]=='1':
                if carry==0:
                    carry=1
                    s='1'+s
                else:
                    carry=1
                    s='0'+s
            elif a[c]=='1' and b[c]=='0':
                if carry==0:
                    carry=0
                    s='1'+s
                else:
                    carry=0
                    s='0'+s
            elif a[c]=='0' and b[c]=='0':
                if carry==0:
                    carry=0
                    s='0'+s
                else:
                    carry=1
                    s='1'+s
            elif a[c]=='1' and b[c]=='1':
                if carry==0:
                    carry=0
                    s='0'+s
                else:
                    carry==1
                    s='1'+s
            c-=1
        print(' '+a+'\n'+'-'+b+'\n'+'---------'+'\n'+' '+s)
        print()

class dec_oct_hex_bin:
    def print(self,number):
        def decimal(n):
            return str(n)
    
        def octal(n):
            d=''
            while(n>0):
                a=n%8
                d=str(a)+d
                n=n//8
            return d
    
        def hexdec(n):
            table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
            h=''
            while(n>0):
                a=n%16
                h=table[a]+h
                n=n//16
            return h
    
        def binary(n):
            d=''
            while(n>0):
                a=n%2
                d=str(a)+d
                n=n//2
            return d
        pad = number.bit_length()         
        for i in range(1,number+1):
            print(decimal(i).rjust(pad),octal(i).rjust(pad),hexdec(i).rjust(pad),binary(i).rjust(pad))

class String:
    def split(self):
        s=input('enter the string\n')
        s=s+' '
        a=''
        b=[]
        c=0
        for i in range(len(s)):
            if s[i]==' ':
                b.append(a)
                a=''
            else:
                a=a+s[i]
        for i in b:
            print(i)
    def name_short(self):
        s=input('enter your long name\n')
        s=(s+' ').upper()
        a=''
        b=[]
        name=''
        for i in range(len(s)):
            if s[i]==' ':
                b.append(a)
                a=''
            else:
                a=a+s[i]
        for i in range(len(b)-1):
            name+=b[i][0]+"."
        print(name+b[len(b)-1])
        



    #ob=String()
    #ob.split()

class stack:
    def __init__(self,a):
        self.a=[]
    def push(self,i):
        self.a.append(i)
    def pop(self):
        l=len(self.a)-1
        if len(self.a)<1:
            print('cannot be popped, Empty stack')
        else:
            print('LIFO popped -->',self.a[l])
            del(self.a[l])
    def trav(self):
        if len(self.a)<1:
            print('Empty stack, nothing exist')
        else: 
            s=''
            for i in self.a:
                s=i+s
            for j in s:
                print(" ",j)
    def peek(self):
        if len(self.a)<1:
            print('cannot be seen, Empty stack')
        else:
            l=len(self.a)-1
            print('First elemnt in stack -->',self.a[l])
   
    #ob=stack([])
    #ob.push("R")
    #ob.push("I")
    #ob.push("K")
    #ob.push("U")
    #ob.trav()
    #ob.pop()
    #ob.peek()
    #ob.trav()



def hackerrank_1(sen):
    S=sen.lower()
    s=''
    s1=""
    for i in range(len(sen)-1):
        if(S[i+1]<S[i]):
            s=S[i+1].lower()
        elif(S[i+1]==S[i]):
            s=S[i+1].upper()
        else:
            s=S[i+1].upper()
        s1=s1+s
    print(S[0]+s1) 
# create object and call function to print output

def alpa_to_num():
    s='SHASWATA'
    alp='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num=[]
    cyper=''

    for i in range(len(s)):
        for j in range(len(alp)):
            if(s[i]==alp[j]):
                num.append(j+1)
    for i in num:
        cyper+=str(i)
    print(cyper)


def check_circular_prime():
    num=19
    #num=131
    #num=13
    #num=171
    def check_prime(n):
        c=0
        for i in range(1,num+1):
            if(num%i==0):
                c+=1
        if(c==2):
            return 1
        else:
            return 0
    length=len(str(num))
    positive=0
    while(length>0):
        a=int(num%10)
        b=int(num/10)
        num=int(str(a)+str(b))
        length-=1

        if(check_prime(num)==1):
            positive+=1
            print(num,"prime")
        else:
            positive+=0
            print(num,"not prime")

    if(positive==len(str(num))):
        print("circular prime")
    else:
        print("not a circular prime")



def validate_password():
    s=str(input('ENTER YOUR PASSWORD HERE\nShould be in between 15-25 char long\nShould contain atleast\n1 upper case character\n1 lower case character\n1 special character !@#$%&*\n1 digit     -->\n'))
    def check(S,check):
        holder=[]
        for i in S:
            if i in check:
                c=1
            else:
                c=0
            holder.append(c)
        if 1 in holder:
            return 1
        else:
            return 0


    upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower='abcdefghijklmnopqrstuvwxyz'
    num='0123456789'
    spl='!@#$%&*'
    print(check(s,upper),check(s,lower),check(s,num),check(s,spl))
    if(len(s)<=15):
        print('INVALID\nless than 15 char long')
    elif(len(s)>=25):
        print('INVALID\ngreater than 25 char long')
    elif(check(s,upper) == 0):
        print('no UPPER CASE character provided')
    elif(check(s,lower) == 0):
        print('no LOWER CASE character provided')
    elif(check(s,num) == 0):
        print('no DIGIT provided')
    elif(check(s,spl) == 0):
        print('no SPECIAL character provided')
    else:
        print('VALID  PASSWORD O--,')
    
    

def matrix_add():
    # you can change the matrix
    m_1=[[1,2,3],[4,5,6],[7,8,9]]
    m_2=[[9,8,7],[6,5,4],[3,2,1]]


    print('''
    THIS  IS
    MATRIX
    ADDITION
    ''')


    for i in range(0,3):
        for j in range(0,3):
            print(str(m_1[i][j]+m_2[i][j])+' ',end='')
        print()
    print('1st Matrix\n')

    for i in range(0,3):
        for j in range(0,3):
            print(m_1[i][j],end='')
        print()

    print('2nd Matrix\n')
    for i in range(0,3):
        for j in range(0,3):
            print(m_2[i][j],end='')
        print()


def roman_to_digit():
    m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
    ans = 0
        
    for i in range(len(s)):
        if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
            ans -= m[s[i]]
        else:
            ans += m[s[i]]
        
    return ans


def add_rev_list(l1, l2):
        """
        [1,2,3] = 123
        [4,5,6] = 456
        123+456 = 579
        [9,7,5]
        """
        rev_s1=''
        rev_s2=''
        for i in l1:
            rev_s1=str(i)+rev_s1
        for j in l2:
            rev_s2=str(j)+rev_s2
        print(rev_s1,rev_s2)
        S=str(int(rev_s1)+int(rev_s2))
        L=[]
        for k in range(len(S)-1,-1,-1):
            L.append(int(S[k]))
        return L
        

def prime_series(n):
    a=[]
    for i in range(2,n+1):
        t=[]
        for j in range(2,i-1):
            if(i%j==0):
                t.append(1)
        if(t==[]):
            a.append(i)    
    print(a)


def Array_Median(arr1,arr2):
    arr=arr1+arr2
    arr.sort()

    m=0.0
    if(len(arr)%2!=0):
        n=int(len(arr)/2)
        m+=arr[n]
    else:
        n=int(len(arr)/2)
        a=arr[n]
        b=arr[n-1]
        m+=(a+b)/2
    print(m,n,n-1)


def HCF(a,b):
    if(a>b):
        m=b
    else:
        m=a
    for i in range(2,m+1):
        if(a%i==0 and b%i==0):
            gcd=i
    print(gcd)

def XL_pattern():
    s=''
    for i in range(5):
        for j in range(5):
            if(i==j or i+j==5-1):
                s+='*'
            else:
                s+=' '
        s+='\n'

    s1=''
    for i in range(5):
        for j in range(5):
            if(i==5-1 or j==0):
                s1+='*'
            else:
                s1+=' '
        s1+='\n'
    print(s,s1)

def phno_conversion_IBM():
    s=input()
    new=s.split()

    dic={'zero':'0',
         'one':'1',
         'two':'2',
         'three':'3',
         'four':'4',
         'five':'5',
         'six':'6',
         'seven':'7',
         'eight':'8',
         'nine':'9'}

    a=''

    for i in range(len(new)):    
        if 'double' in new[i]:
            a=a+(dic[new[i+1]])
        elif 'triple' in new[i]:
            a=a+(dic[new[i+1]])+(dic[new[i+1]])
        else:
            a=a+(dic[new[i]])
    print(a)


def book_allingment():
    #//\\//\\
    #remember \\ means \ user input carefully
    # see the pattern if / allingment exist more then arrange => ////
    # see the pattern if \ allingment exist more then arrange => \\\\
    # if / and \ allingment exists at same rate then arrange => ||||
    s='//\\'
    c1=0
    c2=0
    d={}
    for i in s:
        if(i=='/'):
            c1+=1
        else:
            c2+=1

    b=''
    if(c1>c2):
        b+='/'
    elif(c2>c1):
        b+='\\'
    else:
        b+='|'

    new_s=''
    for j in range(len(s)):
        new_s+=b
    print(new_s,"\nYour Books are Arranged Properly")
    print(f"alignment pattern = {b}\n / = {c1}  \\ = {c2}")

def keypad_mobile_typing():
   #          1     2     3
   #         wait  abc   def
   #          4     5     6
   #         ghi   jkl   mnp
   #          7     8     9
   #         pqrs  tuv  wxyz
   #                0
   #              space


   #     manupulate s  2222 means CA 22222 means CB  222222 means CC 
    
    s=''
    dic = {
        '0':'  ',
        '1':'wait',
        '2':['A','B','C'],
        '3':['D','E','F'],
        '4':['G','H','I'],
        '5':['J','K','L'],
        '6':['M','N','O'],
        '7':['P','Q','R','S'],
        '8':['T','U','V'],
        '9':['W','X','Y','Z']
    }

    if s=='':
        s=' '

       
    S=s[1:]+' '
    b=f"{s[0]}"
    new=[]
    for i in S:
        if i in b:
            b=b+i
        else:
            new.append(b)
            b=i
    print(new)      # seperated string

    hold1=['2','3','4','5','6','8']
    hold2=['7','9']

    # time complexity    O(MARATTOK LEVEL)
    sep=[]
    for i in new:
        if i[0] in hold1:
            if len(i)>3:
                split=[i[j:j+3] for j in range(0,len(i),3)]
                for k in split:
                    sep.append(k)
            else:
                sep.append(i)
        elif i[0] in hold2:
            if len(i)>4:
                split = [i[j:j + 4] for j in range(0, len(i), 4)]
                for k in split:
                    sep.append(k)
            else:
                sep.append(i)
        elif i[0] == '0':
            sep.append(i)
        else:
            pass
    print(sep)   # seperated string
    final_s=''
    for val in sep:
        final_s+=(dic[val[0]][len(val)-1])

    print(final_s)



def merry_christmas_turtle():

    #  paste it in pycharm idle
    #from turtle import *

    tim = Turtle()
    tim.shape('arrow')
    tim.color('green')
    tim.shapesize(2,2)
    tim.color()
    tim.pensize(3)
    tim.penup()
    tim.speed(10)
    tim.setposition(0,250)


    for i in range(1,5):

        tim.right(140)
        tim.pendown()
        tim.forward(40*i)
        tim.left(150)
        tim.forward(20)


    for i in range(3):

        tim.right(90)
        tim.forward(20)

        tim.right(270)
        tim.forward(20)
    tim.right(90)
    tim.forward(20)
    tim.right(40)
    tim.forward(100)
    tim.right(70)
    tim.forward(40)
    tim.right(200)
    tim.forward(100)
    tim.left(160)
    tim.forward(40)
    tim.right(70)
    tim.forward(100)
    tim.right(45)

    for i in range(4):

        tim.forward(20)
        tim.right(90)
        tim.forward(20)
        tim.left(90)

    tim.penup()
    tim.setposition(0,250)
    tim.left(45)
    tim.pendown()
    tim.right(130)
    tim.forward(40)
    tim.left(210)
    tim.forward(20)

    for i in range(2,5):
        tim.right(130+45*2)
        tim.forward(40*i)
        tim.left(210)
        tim.forward(20)

    tim.left(90)
    tim.forward(30)

    tim.penup()
    tim.setposition(0,250)
    tim.color('yellow')
    tim.pencolor('black')
    tim.speed(25)

    hideturtle()
    write("Merry Christmas",align="center",font=("Cooper Black", 45, "italic", ),)


    while(True):
        tim.right(45)

    turtle.exitonclick()


def occurence_of_string_in_another_string():
    a='badamsadambadam'
    b='sadam'

    i=0
    j=0
    k=0
    c=0
    index=0
    t=True
    while(t):    
        if(b[j]==a[k]):
            j=j+1
            k=k+1
            c=c+1
        else:
            j=0
            k=k+1
            c=0
            index=i+1
        print(j,k)
        i=i+1
        if(j==len(b)):
            t=False
        
    print(c)
    if(c==len(b)):
        print('exist',index)
    else:
        print('donot')

def howmanytimes_the_substr_occurs_in_str():
    s=str(input('Main string :'))

    s1=str(input('substring : '))
    j=0
    c=0
    n=0
    for i in range(0,len(s)):
        if s1[j]==s[i]:
            c+=1
            j+=1
        else:
            c=0
            j=0
        if c==len(s1):
            n+=1
            j=0
            c=0
    print(n)
    if n>=1:
        print('present',n,'times')
    else:
        print('not present')

def trimorphic_number():
    # 49^3 = trimorphic  =117649
    n=int(input())
    n1=n
    cub=n*n*n
    c=0
    while(n!=0):
        c+=1
        n=n//10
    i=0
    d=0
    while(i<c):
        rem = cub%10
        d=d*10+rem
        cub=cub//10
        i+=1
    rev=0
    while(d!=0):
        rem=d%10
        rev=rev*10+rem
        d=d//10
    if(rev==n1):
        print("trimorphic",rev,n1)
    else:
        print("not trimorphic",rev,n1)

def diff_occurence():
    a=[1,1,1,2,2,2,3]
    d={}
    # [3,3,1]
    # NO
    #[1,1,1,2,2,3]
    #[3,2,1]
    #YES
    for i in a:
        if i in d:
            d[i]+=1     
        else:
            d[i]=1

    new1=[]
    for j in d:
        new1.append(d[j])

    print(new1)
    new=[]
    for j in new1:
        if j not in new:
            new.append(j)
    if(len(new1)==len(new)):
        print('diff occurence-- OK')
    else:
        print('have same ocuurence-- NO')

def On2_iterator_in_On():
    n=int(input())
    f=n*n

    c=0
    j=0
    i=0
    for k in range(0,f):
        print(i,j)
        if(j==n-1):
            j=0
            i+=1
        else:
            j+=1

def chess_board_making():
    a=[]
    main=['♜','♝','♞','♚','♛','♞','♝','♜']
    oth=['♟']

    for i in range(8):
        b=[]
        for j in range(8):
            if(i==1 or i==6):
                b.append(oth[0]+' ')
            elif(i==0 or i==7):
                b.append(main[j]+' ')
            else:
                b.append('☐'+' ')
        a.append(b)

    for i in range(8):
        for j in range(8):
            print(a[i][j],end='')
        print()

def array_target_sum(arr,target):
    i=0
    j=i+1
    n=len(arr)
    new=[]
    for k in range(n*n):
        s=arr[i]+arr[j]
        if(s!=target):
            if(j<2):
               j+=1
            else:
                i+=1
                j=i+1
        else:
            new.append(i)
            new.append(j)
            break
    print(new)

def staircase_leetcode():
    #eg - there are 2 stairs
    #     can take only 1 steps and 2 steps
    # ways to climb = (1,1) (2) = 2 ways

    #eg - there are 4 stairs
    # (1111) (112) (121)  (211) (22) = 5 ways
    n=int(input())
    a=1
    b=2
    for i in range(2,n):
        s=a+b
        t=s
        a=b
        b=t
    print(s)
        
def sorting_list_oN(arr):
    k=0
    i=0
    m=arr[k]
    mindex=0
    while(k!=len(arr)-1):
        if(m>arr[i]):
            m=arr[i]
            mindex=i
        if(i==len(arr)-1):
            tmp=arr[k]
            arr[k]=m
            arr[mindex]=tmp
            k+=1
            i=k
            m=arr[k]
            mindex=k
        else:
            i+=1
    print(arr)
    
    

