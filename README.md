# AutoTUnet
清华校园网自动连接

### 安装Python

安装时添加到PATH，然后安装requests、selenium等库。

### 安装Firefox及geckodriver

Firefox下载地址：<http://www.firefox.com.cn/>

Geckodriver是Firefox的驱动器，下载地址：<https://github.com/mozilla/geckodriver/releases/tag/v0.26.0>

下载后解压，并将地址添加到PATH。

### 使用Selenium登录校园网

实际使用中发现，有时即使校园网断了，再打开auth4.tsinghua.edu.cn，也不会出现连接选项。因此要先断再连。

```python
import requests
import os
from selenium import webdriver
import time
import subprocess
def connect():
    driver=webdriver.Firefox()
    new_url = 'http://auth4.tsinghua.edu.cn'
    driver.get(new_url)
    try:
        driver.find_element_by_id('username').send_keys('用户名')
        driver.find_element_by_id('password').send_keys('密码')
        time.sleep(2)
        driver.find_element_by_name('connect').click()
        time.sleep(2)
        driver.quit()
    except:
        try:
            time.sleep(2)
            driver.find_element_by_class_name('disconnect').click()
            time.sleep(2)
            driver.quit()
            driver=webdriver.Firefox()
            driver.get(new_url)
            driver.find_element_by_id('username').send_keys('用户名')
            driver.find_element_by_id('password').send_keys('密码')
            time.sleep(2)
            driver.find_element_by_name('connect').click()
            time.sleep(2)
            driver.quit()
        except:
            pass

if __name__ == '__main__':
    fnull = open(os.devnull, 'w')
    return1 = subprocess.call('ping baidu.com', shell = True, stdout = fnull, stderr = fnull)
    if return1:
        connect()


```



复制上面的脚本，输入用户名及密码，保存到一个txt文档中，改变文件名为如“AutoTUnet.py”。为了防止可能的编码的问题，最好用专用代码编辑器编辑，或者点击阅读原文下载代码包。**如果你的环境是Python2，保存路径最好不好有中文或其他中文符号。**



理论上通过这个脚本可以实现自动连网。但是不美妙的地方在于运行的总会有一个黑框闪过。可以考虑采用下面的解决方案：

1. 编写一个运行Python的bat脚本，保存为AutoTUnet.bat（如果Python没有添加到PATH，需要写下完整的Python所在路径。）

   ```
   dir
   python AutoTUnet.py
   exit
   ```

2. 编写一个不在黑框中运行bat脚本的VB脚本，保存为AutoTUnet.vbs

   ```
   createobject ("wscript.shell").run "AutoTUnet.bat",0
   ```

最后我们只需要运行VB脚本就行了。

### Windows定时运行VB脚本 

这个过程稍微复杂点。下面以Win10为例说明如何进行：

首先在Windows搜索框中搜索”任务计划程序“

![img](https://mmbiz.qpic.cn/mmbiz_png/ZEQm45uYocKJZtygCpDhgYMUibKOkwia0Yyn78ibkzYTDWGmsb1dOOOnj7QlEH5WZAz8kPbcVbcFFeVgSuhicoSNHA/640?wx_fmt=png)

![img](https://mmbiz.qpic.cn/mmbiz_png/ZEQm45uYocKJZtygCpDhgYMUibKOkwia0YILIcH9ZECT1mRjmibnib9icgIwyiaFcO2iafPRDpsWzKJCaNrTs3bIhmQsg/640?wx_fmt=png)

点击上图右侧的【创建任务】，弹出如下图所示界面，输入名称和描述。

![img](https://mmbiz.qpic.cn/mmbiz_png/ZEQm45uYocKJZtygCpDhgYMUibKOkwia0YU4hBrJeqqicb1jeP1FhMher9icqmBeW0NLz9rC9ibGCQrnv6wPPF119vQ/640?wx_fmt=png)

点击【触发器】，点击【新建】，在下图右侧框中输入你希望的运行时间间隔。下图设定1天内间隔1小时运行一次。设定完后点击确定。

![img](https://mmbiz.qpic.cn/mmbiz_png/ZEQm45uYocKJZtygCpDhgYMUibKOkwia0YO0EBmEV2L6icvAZic9hGIh7uewK8YvHCjOGfcwWPW2FEz7Pefia4dx6jw/640?wx_fmt=png)

点击“操作”，下面是最关键的一步。解释一下三个文本框内容的含义，【程序或脚本】文本框中填的是VB脚本的完整名称，【起始于】文本框中填的是VB脚本的目录

![img](https://mmbiz.qpic.cn/mmbiz_jpg/ZEQm45uYocKJZtygCpDhgYMUibKOkwia0YzxjTZFXrkQlg3bicoDZmCwwE7edU0LYM4415771cfH1oQvKn7Uav7LQ/640?wx_fmt=jpeg)

可以进一步对【条件】或【设置】进行进一步设置，一般按照默认配置即可，点击确定即可完成对定时任务的设置。完成后可以在【任务计划程序库】中看到”AutoTUnet“。

![img](https://mmbiz.qpic.cn/mmbiz_png/ZEQm45uYocKJZtygCpDhgYMUibKOkwia0YVB7YWogyzsyMuxGAIFM3KXEvD96ld4DyibaciaZqbPpjCkh793tMJbDA/640?wx_fmt=png)

完成以上设置后，基本可以做到神不知鬼不觉地连网。