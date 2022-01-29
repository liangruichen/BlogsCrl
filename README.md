## BlogsCrl —— 洛谷博客文章的自动保存

**声明：通过查询 `robots.txt` 可知，下列爬虫内容是合法的。**  

[洛谷更新日志](https://www.luogu.com.cn/discuss/223773) 中提到，

> 洛谷博客已不再大维护，之后将考虑停止运营

而有一部分人，并未将文章备份到其他位置，在洛谷的博客中存放着重要的信息。

这个脚本，可以实现洛谷博客文章的自动下载。

请使用 Python3 编译 `BlogsCrl.py`，确保有 `requests`，`time`，`os`，`re` 库。其中的后三个多半是有的，如果没有 `requests` 库，您可以在 `cmd` 中输入 `pip install requests` 来获得。

在代码中，这几段被醒目地标注出来，因为您需要更改这里的信息。

**第一处：**

![](https://s4.ax1x.com/2022/01/27/7XdRTU.png)

Firefox：先登录洛谷，按 F12 或右键打开检查，存储中 `__client_id` 的值即您的 cookie。

![](https://s4.ax1x.com/2022/01/27/7XwOuq.png)

Chrome（这里是 Microsoft Edge）：先登录洛谷，按 F12 或右键打开检查，Application 中的 Cookies 内，找到  `__client_id` 的 Value 即您的 cookie。

![](https://s4.ax1x.com/2022/01/29/HSOS8P.png)

**两项信息均需要打上引号。**

-----

**第二处：**

![](https://s4.ax1x.com/2022/01/27/7XIZ60.png)

把 headers 的 `User-Agent` 后面的那个字符串改成 A 串。A 串获得方法如下：

同样登录洛谷，按 F12 或右键**打开检查后再刷新一次**，在 网络（Network） 中点击一条名为 `www.luogu.com.cn` 的信息，找到 `User-Agent`，复制后面的内容作为 A 串。

Firefox:  
![](https://s4.ax1x.com/2022/01/27/7X2RJ0.png)

Microsoft Edge:  
![](https://s4.ax1x.com/2022/01/29/HSjwAH.png)

~~似乎这个不改也没什么问题。~~

------

您的文章将被下载到与该 Python 文件同目录的 `Blogs` 文件夹中，文件名为 `您的文章的名称.md`。特别地，如果您的文章名称中含有 `?`、`、`、`╲`、`/`、`*`、`“`、`”`、`<`、`>`、`|`，均会被替换为 `&`，原因是 Windows 不允许文件名中出现上述字符。


前一部分使用 cookie 登录的代码，参考了洛谷日报的 [这篇](https://www.luogu.com.cn/blog/12cow/python)。

### 可能的错误

由于洛谷对每个 IP 每秒访问次数的限制，代码的倒数第二行为 `time.sleep(7)`。如果您发现下载下来的文件为空文件，可以考虑是否是访问过快所致。您可以通过增大停止的时间来降低访问速度。

如果您追求效率，可以考虑 IP 代理。详细方法还是可以参考洛谷日报的 [这篇](https://www.luogu.com.cn/blog/12cow/python)。

------

如有 Bug 或配置问题，可以洛谷私信联系 @[liangruichen](https://www.luogu.com.cn/user/409236)。

### 已知问题（这些问题将在之后逐渐修复）

1. ~~引用（即 `>`） 的 md 会出现问题。~~ fixed on 2022/1/28
2. ~~自动链接（即`<https://xxxxx>`）的 md 会出现问题。~~ fixed on 2022/1/28
3. ~~爬取带有说明的图片（即 `![xxx](https://xxxxx)`）时会死。~~ fixed on 2022/1/28
4. ~~特殊 markdown 字符不会被转义。~~ fixed on 2022/1/29
5. Windows 外的操作系统（如 Linux，Mac）在保存文件时，若博客名称含有特殊字符，会出现问题。
