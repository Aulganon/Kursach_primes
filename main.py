from functions import *
import time
import os
import random



def write_to_file(numbers):
    
    if os.path.exists('result.txt'):
        os.remove('result.txt')
            
    with open('result.txt', 'w') as f:
        for num in numbers:
            counter = 0
            if counter ==50: 
                f.write(num + "\n")
                counter = 0
            f.write(num+ " ")



def luke():
    classic_array_limiter = 50000 
    luke = Luke()
    for i in range(classic_array_limiter):
        print(luke.LucasMethod(i))


def maurer_check(cal):
    maurer = Maurer()
    for i in range(cal):
        print(maurer.execute(math.pow(10,12), math.pow(10,13))) # maurer check
    end = time.time()

def main():

    #start = time.time()
    # here is our main code of program
    # -------------------------------------------------------    
    #luke()
    #end = time.time()
    #print(f" Resulting time was = {end - start} sec.")
    
    start = time.time()
    luke_t = Luke()
    maurer = Maurer()
    check = maurer.execute(math.pow(10,7), math.pow(10,8))
    print(luke_t.LucasMethod(check))
    print(check)
    end = time.time()
    # -------------------------------------------------------
    # here main code ends
    end = time.time()
    print(f" Resulting time was = {end - start} sec.")
    
if __name__ == "__main__":
    main()
