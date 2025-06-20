#!/bin/zsh

if [[ $# -ne 2 ]]; then
    echo "Usage: $0 <Site List> <Word List>"
    exit 1
fi

siteList=$1
wordList=$2

# Check if both files exist
if [[ ! -f "$siteList" ]]; then
    echo "Error: File '$siteList' not found."
    exit 1
fi

if [[ ! -f "$wordList" ]]; then
    echo "Error: File '$wordList' not found."
    exit 1
fi

# Read File1 into an array (line by line)
lines1=()
while IFS= read -r line; do
  if [[ -z $line ]]; then
    continue
  fi
    lines1+=("$line")
done < "$siteList"

# Read File2 into an array (line by line)
lines2=()
while IFS= read -r line; do
    if [[ -z $line ]]; then
      continue
    fi
    lines2+=("$line")
done < "$wordList"

for line1 in "${lines1[@]}"; do
    for line2 in "${lines2[@]}"; do
        # Correct way to assign a string with variables and quotes
        output="\"${line2}\" site:${line1}"

        # Remove spaces around the '='
        outputFile="${line1}-${line2}.txt"

        echo "Now passing ${output} -> Output: ${outputFile}"

        # Quote variables to avoid issues with spaces
        python3 dorkScraper.py -d "${output}" 1000 -s "${outputFile}"
    done
done
