

#task 1
#shaik Mosin
#1
print("pattern_1;\n")
for i in range(5,0,-1):
    for j in range(i):
        print(5,end=" ")
    print()
    
print()
print("pattern_2;\n")  
#2
for i in range(6,1,-1):
    for j in range(i):
        print(j,end=" ")
        
    print()
    
print()
print("pattern_3;\n") 
#3
k=1
for i in range(1,6):
    for j in range(i):
        print(k,end=" ")
    k+=2
    print()

print()

print("pattern_4;\n") 
#4
for i in range(5):
     k=i+1
     for j in range(i+1):
         print(k,end=" ")
         k-=1
     print()
     
     
print("pattern_5;\n")     
#5
print()
k=1
val=0
for i in range(5):
    val+=k+i 
    
    for j in range(i+1):
     print(val,end=" ")
     val-=1
    k+=1
    print()
print()
print("pattern_6;\n")     
#6
list1=[]
for i in range(7):
     temp=[]
     for j in range(i+1):
         if j==0 or j==i:
             temp.append(1)
         else:
             temp.append(list1[i-1][j-1]+list1[i-1][j])
     list1.append(temp)
for i in range(7):
             for j in range(i+1):
                 print(list1[i][j],end=" ")
             print()
             
print()


print("pattern_7;\n") 
#7
n=5
list1=[[0 for i in range(n)]for j in range(n)]
#print(list1)
low=0
high=n-1
val=n
for i in range(n):
    for j in range(low,high+1):
        list1[j][high]=val
        list1[high][j]=val
    
    

    high-=1
    val-=1
   
  
    
    
for i in range(n):
    for j in range(n):
       
        print(list1[i][j],end=" ")
    print()
    
print()   
    
   
   
print("pattern_8;\n")   
#8
n=8
for i in range(1,n+1):
    k=i 
    val=k 
    
    for j in range(i):
        print(val,end=" ")
        val+=k
    print()

print()
#9
print("pattern_9;\n") 
n=6
for i in range(n):
                                 for j in range(i):
                                     print(" ",end="")
                                 for j in range(n-i):
                                     print("*",end=" ")
                                 print()
                                 
                                 
print()                             
print("pattern_10;\n") 
#10
n=6
for i in range(n):
                                  for j in range(n-i):
                                      print(" ",end="")
                                  for j in range(i+1):
                                      print("*",end=" ")
                                  print()                         
print()                                  
#11
print("pattern_11;\n") 
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
print()
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()                            
                 
              
print()
print("pattern_12;\n") 
#12
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

for i in range(n):
    for j in range(n-i-1):
        print("*",end=" ")
    print()                        
print("pattern_13;\n")                     
#13
print ()
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    print()
           
         
print("pattern_14;\n") 
#14
n=5
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("*",end=" ")
    print()

for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()    
     
print("pattern_15;\n")  
#15
print()
n=7
for i in range(n):
    
    for j in range(n-i):
        print("*",end="")
    for j in range(2*i):
        print("_",end="")
    for j in range(n-i):
        print("*",end="")
    print()
           
 
     
    
    
 