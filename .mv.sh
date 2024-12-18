mv ~/Downloads/*.zip .
# 遍历每个 .zip 文件并解压
for zipfile in ./*.zip; do
    unzip "$zipfile" -d "${zipfile%.*}"  # 解压到以文件名命名的目录
done
rm ./*.zip

