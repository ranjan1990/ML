#!/bin/bash

#get the points and write them to a file for input

img="./band4_norm.jpg"
iodir="io"
suffixlen=4

for i in $iodir/inp.*
do
	len=`expr length $i`
	idx=`expr $len - $suffixlen + 1`
	suffix=`expr substr $i $idx $suffixlen`
	python get_points.py $img $iodir/pts.$suffix < $i
done
