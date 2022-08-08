#!/usr/bin/env bash
echo "Time to set your range"
echo "Starting number"
read startn
echo "Ending numeber"
read endn
while [ true ] 
do
    clear
    echo "Are you ready?"
    read
    #Generating Random Numbers
    rand=$(($startn + $RANDOM % $endn))
    rand_2=$(($startn + $RANDOM % $endn))
    echo "What is ${rand}+${rand_2}"

    
    start=$(date +'%s')
    read z
    end=$(date +'%s')
    total=$((rand+rand_2))

    if [ $z == $total ]; then
        echo "COrect"
    else
        echo "Nope"
    fi
    #Calculating duration it took to give input on line 19
    duration=$(($end-$start))
    echo "It took you ${duration} seconds to answer the question"
    read
done