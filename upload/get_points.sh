#!/bin/bash

img="../band4_norm.jpg"

for i in inp.*
do
	suffix=`expr substr $i 5 4`
	echo "python get_points.py $img pts.$suffix"
done
