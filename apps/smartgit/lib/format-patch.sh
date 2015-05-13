#!/bin/bash
dir=$1
from=$2
to=$3
if ! [ -z "$to" ]; then
  git format-patch -o "$dir" $from..$to
else
  git format-patch -o "$dir" -1 $from
fi
