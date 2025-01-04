#Practise area

#Bubble Sort
def main():
    l = [12,23,45,56,76,12]
    print("Orignal list : ",l)
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    print("List after sorting is:",l)

#Insertion Sort
def sorty():
    l = [89,12,23,87,56,67]
    print("Orignal List : ",l)
    for i in l:
        j = l.index(i)
        while j>0:
            if l[j-1] > l[j]:
                l[j-1], l[j]=l[j], l[j-1]
            else:
                break
            j-=1
    print("List after sorting is:",l)
    
#Built in functions
def everything():    
    l=[12,23,89,56,67,45]
    print(max(l),min(l),sum(l))

#Finding the digits in a no.
def digits():    
    k = 103
    print(k)
    print(k//100)
    print((k//10) % 10)
    print(k % 10)
    
    
    l = 9382
    print(l)
    print(l // 1000)
    print((l//100) % 10)
    print((l//10) % 10)
    print(l % 10)
  
def randomy():
    import random
    print(random.randrange(1, 4))
    print(random.random())
    print(random.randint(1, 4))
    print(random.uniform(1,4))
    print(random.choice(['hello','random','cat','lives','in','a','street']))
    
    cards = ['Ace','Diamond','Black','Red']
    random.shuffle(cards)
    print(cards)    
    
def myfun(*arg):
    print("u",arg)
    
def heloo(jk,k,m,om=3):
    print(om, jk)
    


    
    
    
    
    
