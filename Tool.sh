#!bin/sh
############################################################
#
#		Some useful tools based on shell bash
#		Copyright(c) KazukiAmakawa, all right reserved.
#		Tool.sh
#
############################################################
#It is time for me to study shell bash

#Here are some basic function
for file in ./*
do
	if test -f $file
	then
		echo $file	
	cat $file | grep ZLM
		echo "\n"
	fi
done