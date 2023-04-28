# 人脸识别项目使用说明

使用的`linux`系统为`ubuntu`

## 1.安装anaconda

在当前目录下有以下文件夹：

```bash
.
├── data
│   └── face
├── models
└── xml

4 directories
```

点击下载链接https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/安装对应版本anaconda。

下载完成后，进入文件目录打开终端执行命令：

`linux_x86_64`系统：

```bash
sudo bash Anaconda3-2023.03-1-Linux-x86_64.sh
```

`jetson`机器：

```bash
sudo bash Anaconda3-2023.03-1-Linux-aarch64.sh
```

接下来的操作可以查看链接：https://blog.csdn.net/Jorbo_Li/article/details/124984936

## 2.`anaconda`更换镜像源

执行以下命令打开`.condarc`文件：

```bash
sudo gedit ~/.condarc
```

将以下内容覆盖该文件：

```
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch-lts: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
```

运行 `conda clean -i` 清除索引缓存，保证用的是镜像站提供的索引。

参考链接：https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/

## 3.创建虚拟环境

终端执行以下命令：

激活`conda`：

```bash
conda activate
```

创建虚拟环境`python3.9(opencv)`：

```bash
conda create --name opencv python=3.9
```

激活虚拟环境`opencv`:

```bash
conda activate opencv
```

在项目文件夹内打开终端，下载相关包：

```bash
pip install -r ./requirements_py39.txt
```

至此，运行环境已经完成。`（python3.9, 'opencv')`

## 4.运行文件

### 1.录入人脸

在项目文件夹内打开终端，启动虚拟环境，运行`./face_save.py`文件，即可进行人脸录入工作。

文件运行时会弹出窗口显示摄像头获取的画面，当画面内有人脸时，会用红色方框圈住。（最好在光线明亮的地方，这样识别准确率高）

当画面内只有一个方框时，点击窗口，按下q键即可退出程序；按下s键，即可进行照片保存。

按下s键后，会弹出两个窗口，face窗口展示截取到的人脸，original展示原图。

点击任意窗口，按下q键即可退出程序；按下s键，即可在终端输入该人物的姓名。（最好用英文，不然人脸识别时可能乱码）当终端出现"finished"字样时，保存照片成功，退出程序。

### 2.训练数据

在项目文件夹内打开终端，启动虚拟环境，运行`./face_train.py`文件，即可进行训练数据工作。

当终端出现"successfully to train."字样时，训练成功，退出程序。

### 3.人脸识别

在项目文件夹内打开终端，启动虚拟环境，运行`./face_recgnize.py`文件，即可进行人脸识别工作。(充足的光照可以提升识别准确率，指台灯对着脸照)

人脸会用红色方框标记，同时左上角显示识别结果。如果是已经录入的人脸，会显示名字；如果不是，则会显示"unkown"。当陌生人在摄像头面前停留时间过长时，程序会执行warning函数，在终端打印"warning"字样，用于后续操作。点击窗口按下q键即可关闭程序。
# face-detected-for-linux
