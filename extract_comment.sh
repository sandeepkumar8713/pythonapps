#!/bin/sh

currentDate=$(date +'%d_%m_%Y')
#currentDate=$(date +'%d_%m_%Y_%H_%M')

fileName='fileList.txt'
#find . -name '32_zero_matrix.py' > $fileName

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

extract(){
  count=1
  while IFS='' read -r line || [[ -n "$line" ]]; do
    printInput $line $count
    count=$((count+1))
  done < $fileName

  rm -f $fileName
}

rm allFilesComments_*.txt

users=(Asked Generic ShouldSee Easy SimilarAdded OddOne)
for u in "${users[@]}"
do
    grep -rl "$u" --include=\*.py . > $fileName
    currentDate="$u"
    outputFile="allFilesComments_$currentDate.txt"
    echo "" > $outputFile
    extract
done
