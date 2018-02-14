#! /bin/bash
# or whatever you want to name your output file
# you could also create separate output files for each size or each algorithm
# modifying the right hand sides of the >>'s
outfile=my_runs.out
# customize the line below for your choice of problem sizes
for n in 10000 20000 40000 80000 160000 320000 640000 1280000; do
    for seed in 1 2 3 4 5; do
        instance=/tmp/rand_${n}_${seed}
        ./random_integers.py $n $seed > $instance
        for implementation in ./run_merge_sort.sh ./run_heapsort.sh ./run_sort_utility.sh; do
            # customize the output lines for your convenience
            echo "size,$n" >> $outfile
            echo "seed,$seed" >> $outfile
            echo "implementation,$implementation" >> $outfile
            # the > /dev/null makes the sorted output go away
            # the 2>> captures the stderr output
            cat $instance | $implementation > /dev/null 2>> $outfile
            echo "---------------------" >> $outfile
        done
    done
done
