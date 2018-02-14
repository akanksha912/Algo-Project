import random
import sys

def usage(program_name):
    print("Usage", program_name, "N SEED")
    print(" prints N random integers using the SEED, integers range from 1 to 2^31 - 1")
    
def main():
    if len(sys.argv) != 3:
        usage(sys.argv[0])
        sys.exit()
    N = int(sys.argv[1])
    SEED = int(sys.argv[2])
    random.seed(SEED)
    largest_int = (1 << ) -1
    #print("n", N)
    for i in range(N):
        elements = random.randint(1,largest_int)
        print(elements)
   
    
    

main()
