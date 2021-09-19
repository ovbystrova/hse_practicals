#!/bin/bash

LETTERS=abcdefghijklmnopqrstuvwxyz
N=12

while [[ $message = "" ]]
do
  echo -n "What message do you want to process?"
  read message
done

output=""

for (( i=0; i<${#message}; i++ )); do
    letter=${message:$i:1}
    if [[ $LETTERS =~ $letter ]]; then
        shift=$(((N + `expr index "$LETTERS" $letter`) % 26))
        output+=${letter/$letter/${LETTERS:$shift:1}}
    fi
done

echo $output
exit 0
