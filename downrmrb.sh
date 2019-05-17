#!/bin/bash

# get page number
number=$(python3 ~/rmrb/get_rmrb_page_num.py $1)
echo ${number}

# date definition
def=$1
year=${def:0:4}
month=${def:4:2}
day=${def:6:2}

# clear download links file
echo "" > down.txt
# create download links and write them to file
for i in `seq -w -s ' ' 1 ${number}`
do
        echo "http://paper.people.com.cn/rmrb/page/${year}-${month}/${day}/$i/rmrb${year}${month}${day}$i.pdf" >> down.txt
done
# download files
wget -i down.txt -P ~/rmrb -a ~/rmrb/rmrb_down.log
echo "`date '+%Y-%m-%d %H:%M:%S'` download files completed."

# merge pdf files
pdftk ~/rmrb/*.pdf cat output ~/rmrb${year}${month}${day}.pdf
echo "`date '+%Y-%m-%d %H:%M:%S'` merge files completed."

# upload file
rclone copy ~/rmrb${year}${month}${day}.pdf wlyn:rmrb --log-file rclone_rmrb.log --log-level INFO
echo "`date '+%Y-%m-%d %H:%M:%S'` upload file completed."

# rm files
rm ~/rmrb/*.pdf
echo "`date '+%Y-%m-%d %H:%M:%S'` delete files completed."
