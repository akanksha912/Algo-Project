import math,sys,time

count=0         #initializing count

def build_max_heapify(unsort_arr, heap_size, idx):
    
    left = 2 * idx + 1
    right = 2 * idx + 2
    parent = idx
    
    if left < heap_size and comparison_func(unsort_arr[left],unsort_arr[parent])>0:
        parent = left
    else:
        parent=idx
       
    if right < heap_size and comparison_func(unsort_arr[right],unsort_arr[parent])>0:
        parent = right
    
    if parent != idx:
        swap(unsort_arr,parent,idx)
        build_max_heapify(unsort_arr, heap_size, parent)
 

def build_heap(A,n):
   
    for i in range (int(n/2)-1,-1,-1):
        build_max_heapify(A,n, i)
        
def comparison_func(x,y): # Function for comparing two elements(x,y) and return a negative value if x < y, zero if x == y and strictly positive value if x > y.
    global count          
    count+=1              # Increaments the counter when a comparison is made
    return x-y  

# Function used for swapping 2 elements in an Array    
def swap(A,a,b):
    tmp= A[a] 
    A[a]= A[b] 
    A[b]=tmp  

def heapsort(arr):
   
    heap_size = len(arr)
    build_heap(arr,heap_size)
    
    for i in range(heap_size-1,0,-1):
        swap(arr,0,i)
        build_max_heapify(arr, i, 0)
    return arr
       
if __name__ == '__main__':
    user_input = raw_input().strip()   # Takes the user input and strips it(as the value of n is not needed to determine the size of the array in python)
    arr = []
    while True:                        # This loop takes user input and appends it in the array till enter key is pressed twice continuosly
        try:
            line= raw_input()
        except EOFError:
            break
        if line:
            arr.append(line)
            
        else:
            break
    arr = [int(item) for item in arr]   # Creating the Array arr

    start_time = float(time.time()*1000)
    heapsort(arr)
    time = float(time.time()*1000 - start_time) # Runtime is calculated using the time taken before and after the command calling heapsort function

    sys.stdout.write("\n".join(map(str,arr))+"\n")
    sys.stderr.write("runtime,"+ str(time)+"\n")
    sys.stderr.write("comparisons,"+ str(count)+"\n")
