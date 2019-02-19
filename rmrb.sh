#! /bin/bash
# date definition
year=$(date "+%Y")
month=$(date "+%m")
day=$(date "+%d")
# clear download links file
echo "" > down.txt
# create download links and write them to file
for i in `seq -w -s ' ' 1 $1`
do
        echo "http://paper.people.com.cn/rmrb/page/${year}-${month}/${day}/$i/rmrb${year}${month}${day}$i.pdf" >> down.txt
done
# download files
wget -i down.txt -P ~/rmrb
