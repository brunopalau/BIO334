#!/bin/bash
for filename in *.fa
do 
	echo $filename
	cat $filename | grep ">" | wc -l
done
	
