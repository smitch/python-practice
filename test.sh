#!/bin/bash

cd `dirname $0`

function assert(){
  if [ "$1" = "$2" ]; then
    echo success
  else
    echo fail
    echo "expected: $1, answer: $2"
  fi
}


# test fizbuzz
ret=`python fizzbuzz.py 20`
ans="1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz"
assert "$ans" "$ret"
