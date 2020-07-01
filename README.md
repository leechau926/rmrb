# ARCHIEVED
2020-7-1 rmrb改版，已创建新的repo


## rmrb
用于下载rmrb，格式为pdf。

下载当天的
```shell
bash rmrb.sh 20
```
20为当天rmrb的版面数量，工作日为20，节假日为08（不能是8）

下载指定日期的
```shell
bash rmrbd.sh 08 20190217
```
第一个参数为指定日期rmrb版面数量，第二个参数为八位数字组成的日期

下载指定日期并且上传
```shell
root@bwg:~/rmrb# bash downrmrb.sh 20190511
08
2019-05-17 18:55:33 download files completed.
2019-05-17 18:55:34 merge files completed.
2019-05-17 18:55:37 upload file completed.
2019-05-17 18:55:37 delete files completed.
```
Requirement:
1.设置好rclone
2.安装好 pdftk

