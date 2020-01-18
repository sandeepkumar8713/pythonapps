#!/bin/sh

currentDate=$(date +'%d_%m_%Y')
#currentDate=$(date +'%d_%m_%Y_%H_%M')

outputFile="allFilesComments_$currentDate.txt"
#outputFile="allFilesCodes_$currentDate.txt"

fileName='fileList.txt'
#find . -name '32_zero_matrix.py' > $fileName

echo "" > $outputFile

printInput(){
  title="$2. FileName: $1"
  echo $title
  echo ""
  #cat $1
  grep -h '^#' $1 | sed 's/#//g' | sed 's/^ //g'
  echo ""
  echo "****************************************************************"
  echo ""
} >> $outputFile

# printInput './firstFolder/21_max_steal_house.py' 1
# printInput './firstFolder/22_array_wave_form.py' 2

count=1
while IFS='' read -r line || [[ -n "$line" ]]; do
    printInput $line $count
    count=$((count+1))
done < $fileName

#rm -f $fileName
