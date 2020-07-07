# Python学习环境
该环境使用了VSCode编辑器，MiniConda程序发布。

## 安装VSCode
下载并安装该编辑器：[下载地址](https://code.visualstudio.com/?utm_expid=101350005-25.TcgI322oRoCwQD7KJ5t8zQ.0)。

### 安装扩展包
点击VSCode侧边栏上的扩展图标，搜索关键词：Python。安装微软公司提供的Python扩展包。

## 安装MiniConda
MiniConda是Anaconda发布的一个最简版本。可以通过[清华国内镜像](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Windows-x86_64.exe)进行下载。

安装完成后可以看到开始菜单内出现了Anaconda Prompt图标，双击打开后可以利用conda命令进行管理，[使用方法](https://www.cnblogs.com/cqliu/p/11199771.html)参见链接。

### 配置国内镜像
conda的软件源，即软件源头在国外，下载较慢。可以参考[使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)配置.condarc文件使用清华的镜像服务安装软件包。

部分软件包不能在conda上找到，可以使用pip安装。同样可以使用[国内镜像](https://mirrors.tuna.tsinghua.edu.cn/help/pypi/)进行下载。

## 使用VSCode编辑Python源文件
选择菜单栏中文件->新建文件，并将该文件保存在某目录下，命名为xxx.py。
创建后点击左下角“Python x.x.x”处选择python解释器，可以选择miniconda安装目录下的python.exe文件。随后可以进行编程实验。

可选项：在VSCode中，若py文件中包含单独一行，其内容为#%%，则表示该标志后的代码到下一个同类标志为止均可以独立运行。初学者可以一次观察代码运行方式和相关的变量内容。具体操作参见[这里](https://www.jianshu.com/p/fa90e902c6ae)。该功能要求conda环境安装jupyter和notebook包，可以使用conda install jupyter notebook命令实现。

## 练习和学习资料

本仓库附带的《笨办法学Python》一书入门比较方便。

[从零开始学Python](https://doc.yonyoucloud.com/doc/wiki/project/start-learning-python/index.html)

[廖雪峰学习库Jupyter Notebook](https://github.com/Watermelon233/PythonXueFeng.Liao-notebook)

[Python练习册](https://github.com/Yixiaohan/show-me-the-code)

[项目导向的编程学习](https://github.com/tuvtran/project-based-learning)

## Python学习计划
[Python从入门到精通](https://www.jiqizhixin.com/articles/2019-10-08)

## git工具及相关资料
[GitExtension: ](https://gitextensions.github.io/)git图形工具

[Git for windows: ](https://gitforwindows.org/)git在Windows操作系统上的移植

[Meld: ](https://meldmerge.org/)比较合并工具,KDiff3也可选但已经不再继续开发了。两个都是不错的工具。

[Git学习资料: ](https://github.com/geeeeeeeeek/git-recipes)

[GitExtension入门: ](https://cloud.tencent.com/developer/article/1174366)入门指导，不过用的putty。


