#! /bin/bash
# date definition
def=$2
year=${def:0:4}
month=${def:4:2}
day=${def:6:2}
# clear download links file
echo "" > down.txt
# create download links and write them to file
for i in `seq -w -s ' ' 1 $1`
do
        echo "http://paper.people.com.cn/rmrb/page/${year}-${month}/${day}/$i/rmrb${year}${month}${day}$i.pdf" >> down.txt
done
# download files
wget -i down.txt -P ~/rmrb
