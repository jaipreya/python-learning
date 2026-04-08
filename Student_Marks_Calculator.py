def calculate_total(marks):
    return sum(marks)
    
def calculate_average(total, count):
    return total/count

def find_grade(avg):
    if (avg>=90):
        return "A"
    elif (avg>=75):
        return "B"
    elif (avg>=50):
        return "C"
    else:
        return "fail"


marks=[]
i=0
while i<5:
    n=int(input(f"Enter marks {i+1}:"))
    if n<0 or n>100:
        print("Invalid number entered please enter correct mark between 1-100")
        continue
    marks.append(n)
    i+=1 
        
total=calculate_total(marks)
avg=calculate_average(total,len(marks))
grade=find_grade(avg)

print("Total:",total)
print("Average:",round(avg,2))
print("Grade:",grade)





