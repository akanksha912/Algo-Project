import time, sys

count=0 # Initializing count

def comparison_func(x,y): # Function for comparing two elements(x,y) and return a negative value if x < y, zero if x == y and strictly positive value if x > y.
    global count          
    count+=1              # Increaments the counter when a comparison is made
    return x-y  
    

if __name__ == '__main__':

    user_input = raw_input().strip()  # Takes the user input and strips it(as the value of n is not needed to determine the size of the array in python)
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

    
    arr = [int(item) for item in arr]   # Creating the Array arr
   

    start_time = float(time.time()*1000)
    
    sys.stdout.write("\n".join(map(str,sorted(arr, cmp=comparison_func)))+"\n") # python's sorted function is called and output is printed
    time = float(time.time()*1000 - start_time)   # Runtime is calculated using the time taken before and after the command calling python sort utility function

    
    sys.stderr.write("runtime,"+ str(time)+"\n")
    sys.stderr.write("comparisons,"+ str(count)+"\n")
