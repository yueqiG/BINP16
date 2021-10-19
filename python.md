import tarfile

# python 解压 tgz文件

tar = tarfile.open('source path')

tar.extractall('target path')
