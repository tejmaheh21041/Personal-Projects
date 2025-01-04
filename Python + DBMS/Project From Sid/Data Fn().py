
import csv 
def add():
      
    fields=['first','thanos','third']
    with open(r'numbers2.csv', 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(fields)
        
def remove():
    lines = list()

    members= input("Please enter a member's name to be deleted: ")
    
    with open('numbers2.csv', 'r') as readFile:
    
        reader = csv.reader(readFile)
    
        for row in reader:
    
            lines.append(row)
            print(row[1])
            print(members)
        if row[1]==members:
            lines.remove(row)
                
        print(lines)
    
    with open('numbers2.csv', 'w' ,newline="") as writeFile:
    
        writer = csv.writer(writeFile)
        print(lines)
        writer.writerows(lines)

remove()