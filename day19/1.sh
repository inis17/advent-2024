#!/bin/sh
grep "^\\($(head -n1 input.txt | sed -e 's/, /\\|/g')\\)\\+$" input.txt | nl
