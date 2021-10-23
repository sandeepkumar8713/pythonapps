#!/bin/sh

total=0

printTypeCount(){
  type=$1
  typeCount=$(grep -r "Question Type : $type" --include=\*.py . | wc -l)
  echo "$type = $typeCount"
  total=$((total+typeCount))
}

#askedCount=$(printInput "Generic")
#echo "askedCount = $askedCount"

echo ""
echo "Counts :"
printTypeCount "Asked"
printTypeCount "Generic"
printTypeCount "ShouldSee"
printTypeCount "OddOne"
printTypeCount "Easy"
printTypeCount "SimilarAdded"

echo ""
echo "Total : $total"
