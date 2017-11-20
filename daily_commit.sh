#!/bin/bash

if [ $# -eq 0 ]; then
        COMMENT='daily commit at `date`'
elif [ $# -eq 1 ]; then
        COMMENT=$1
else
        echo "usage: commit [comment]"
fi
git add .
git commit -am "$COMMENT"
git push
