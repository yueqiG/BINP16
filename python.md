## python 解压 tgz文件

import trafile

tar = tarfile.open('source path')

tar.extractall('target path')
