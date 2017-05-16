# 安装 Python3
## Mac
`brew install python3`

## Centos 上
在 Mac 上用ssh远程服务器

```
ssh -t root@ip -p 22（端口）
```

在 Windows 推荐用 Xshell。

## 下载解压
1. `wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz`
1. `yum install xz-libs`
1. `xz -d Python-3.6.1.tar.xz`

或

1. `wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz`
1. `tar xf Python-3.6.1.tgz`

## 设置
1. `cd Python-3.6.1`    
1. `./configure` : 修改安装路径： `./configure --prefix=/root` 默认是，`/usr/local`

## 编译
1. `yum -y update`
1. `yum groupinstall -y development`
1. `make`
1. `sudo make altinstall`

## 安装完成后
```
python3 --version
```

用 python 做为命令
```
alias python='/usr/local/bin/python3.6'
```

## 在别的地方也可以用
`export PATH="/usr/local/bin:$PATH"`


## 参考
* [How To Set Up Python 2.7.6 and 3.3.3 on CentOS 6.4](https://www.digitalocean.com/community/tutorials/how-to-set-up-python-2-7-6-and-3-3-3-on-centos-6-4)
* [How to install Python3 on CentOS](http://ask.xmodulo.com/install-python3-centos.html)