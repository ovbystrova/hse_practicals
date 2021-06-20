#!/bin/bash

while [[ $name = "" ]]
do
  echo -n "What's your name?"
  read name
done

echo "Hello, $name"
exit 0
