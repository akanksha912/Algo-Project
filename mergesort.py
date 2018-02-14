from __future__ import print_function
import time,sys,math
count=0

# Function comparing 2 sorted arrays and merging them to get one sorted array
def merge(B,p,q,r):
    global count
    n1 = q-p+1          #n1 and n2 are the sizes of Left and Right array. 
    n2 = r-q
    L = [0]*(n1)
    R = [0]*(n2)
    L.append(float("inf"))  #Infinity is appended at the end of both the arrays to avoids checking whether either array is empty in each step
    R.append(float("inf"))
    for i in range(0,n1):   # Elements of Array B that are to be compared are copied into L and R array
        L[i]=B[p+i]
    for j in range(0,n2):
        R[j]=B[q+j+1]
    i=0;
    j=0;
    for k in range(p,r+1):                      # Varing the pointer used to point to the elements in B[] from p to r+1
        if (comparison_func(L[i],R[j])<=0):     # Comparing the L[] and R[] array and putting the element with lesser value in array B[]
            B[k]=L[i]
            i=i+1
            if(R[j]== float("inf")):            # In this program, the last element is compared with infinity, which is an extra comparison, and needs to be decremented from the counter
                count=count-1
        else:
            B[k]=R[j]
            j=j+1
            if(L[i]== float("inf")):
                count=count-1

def comparison_func(x,y): # Function for comparing two elements(x,y) and return a negative value if x < y, zero if x == y and strictly positive value if x > y.
    global count          
    count+=1              # Increaments the counter when a comparison is made
    return x-y    

# Function for sorting the array using merge sort algorithm
def mergesort(B,p,n):
    
    if p<n:                 # To check if there's more than one element in the array
        q = int((p+n-1)/2)  # Finding the mid-point of the array for dividing
        mergesort(B,p,q)
        mergesort(B,q+1,n)
        merge(B,p,q,n)
        

if __name__ == '__main__':

    user_input = raw_input().strip()        # Takes the user input and strips it(as the value of n is not needed to determine the size of the array in python)
    
    arr = []
    while True:                             # This loop takes user input and appends it in the array till enter key is pressed twice continuosly
        try:
            line= raw_input()
        except EOFError:
            break
        if line:
            arr.append(line)
            
        else:
            break
    
    B = [int(item) for item in arr]         # Creating the Array B

 
    r=len(B)                            
   
    start_time = float(time.time()*1000)
    mergesort(B,0,r-1)
    time = float(time.time()*1000 - start_time) # Runtime is calculated using the time taken before and after the command calling mergesort function
   

    sys.stdout.write("\n".join(map(str,B))+"\n")

    sys.stderr.write("runtime, "+ str(time)+"\n")

    sys.stderr.write("comparisons, "+ str(count)+"\n")
    
