#!/bin/bash
declare -A arr
row=4
col=5

for ((i=1;i<=row;i++)) do
    for ((j=1;j<=col;j++)) do
        arr[$i,$j]=$(($i*$col+$j))
    done
done

f1="%$((${#row}+1))s"
f2=" %9s"

printf "$f1" ''
for ((i=1;i<=row;i++)) do
    printf "$f2" $i
done
echo

for ((i=1;i<=row;i++)) do
    printf "$f1" $j
    for ((j=1;j<=col;j++)) do
        printf ${arr[$i,$j]}" "
    done
    echo
done