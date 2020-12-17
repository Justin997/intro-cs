# if statement
is_walking = False
is_running = False
is_crawling = False

if is_walking:
    print("This person is walking.")
    print("hello")
elif is_running:
    print("this person is running!")
elif is_crawling:
    print("This person is crawling.")
else:
    print("This person is lazy.")
    

# while loop
counter = 0
while counter != 20:
    if counter == 0:
        print('special message')
    print("The current value of counter is: " + str(counter))
    if counter == 11:
        print("counter is currently 11")
        break
    counter += 1


# for loop
for var in range(0, 21, 3):
    print("the current value of var is " + str(var))
    
