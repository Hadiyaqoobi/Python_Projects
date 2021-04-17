# While loop

number = 1

while number <5:
    print(number)
    number+=1
    
print("While loop has ended")


# Foor loop


cars = ['Audi', 'VW', 'Toyota', 'BMW', 'GMC', 'Hyundai', 'Ferrari']
for car_brands in cars:
    print(car_brands)
    

numbers = [1,2,3,4,90,5,6]

for number in numbers:
    print(number)
    
    if number == 90:
        break
    print("Inside the foor loop")
    
else:
    print("Outside the foor loop")
    
    
# loop control Statements

counter = [1,2,3,4,90,5,6]

for count in counter:
    if count ==90:
        print("Number needs to be skipped")
        continue
    print(count)

odd = [1,2,3,4,5,6,7,8,9,10]

for number in odd:
    if number %2:
        pass
    else:
        print(number) 

# Nested Loop

number = [1,2,3]
letters = ['a','b','c']

for number in numbers:    
    for letter in letters:
        print(number, letter)
        
        
#Functions in python
        
def print_name(name, surename, age):
    print("My name is :" +name+ " " + surename+ " " +age)
    
print_name("hadi", "Yaqoobi", "25")