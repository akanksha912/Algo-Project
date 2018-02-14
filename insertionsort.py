from __future__ import print_function
import time,sys

count=0  #initializing count

# Function to sort an array using insertion sort algorithm
def insertion(B):
    
    for j in range(1,len(B)): # for j ranging from 1 to n(n being the number of elements in Array B), we select a key at jth position and i is one less than j
        key=B[j];    
        i=j-1;
        
        while i>=0 and comparison_func(B[i],key)>0: # In this loop, we compare the key element(B[j]) with all the elements are appear before it the array and swap them if that element is greater than key 
            B[i+1]=B[i]
            i=i-1
        B[i+1]=key
        
def comparison_func(x,y): # Function for comparing two elements(x,y) and return a negative value if x < y, zero if x == y and strictly positive value if x > y.
    global count          
    count+=1              # Increaments the counter when a comparison is made
    return x-y  


if __name__ == '__main__':

    user_input = raw_input().strip() # Takes the user input and strips it(as the value of n is not needed to determine the size of the array in python)
    #next(sys.stdin)
    arr = []
    while True:                      # This loop takes user input and appends it in the array till enter key is pressed twice continuosly
        try:
            line=raw_input()
        except EOFError:
            break
        if line:
            arr.append(line)
            
        else:
            break
   
    B = [int(item) for item in arr]     # Creating the Array B 
    

    start_time = float(time.time()*1000)        
    insertion(B)
    time = float(time.time()*1000 - start_time) # Runtime is calculated using the time taken before and after the command calling insertion function
   
    
    sys.stdout.write("\n".join(map(str,B))+"\n") 
    
    sys.stderr.write("runtime, "+ str(time)+"\n")  
    sys.stderr.write("comparisons, "+ str(count)+"\n")
  
