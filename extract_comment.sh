#!/bin/sh

qType=$(date +'%d_%m_%Y')
#qType=$(date +'%d_%m_%Y_%H_%M')

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

getAllFilesQtype(){
  for u in "${users[@]}"
  do
    grep -rl "$u" --include=\*.py . > $fileName
    qType="$u"
    outputFile="allFilesComments_$qType.txt"
    echo "" > $outputFile
    extract
  done
}

getAllFilesCategory(){
  categoryFileList="category_file_list.txt"
  grep -oe "[0-9A-Za-z\_\/]*.py" all_questions_category.txt > $categoryFileList
  fileName=$categoryFileList
  outputFile="allFilesComments_category.txt"
  echo "" > $outputFile
  extract
  rm -f $categoryFileList
}

getAllFilesQtype
getAllFilesCategory