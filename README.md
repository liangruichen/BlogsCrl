## BlogsCr —— 洛谷博客文章的自动保存

[洛谷更新日志](https://www.luogu.com.cn/discuss/223773) 中提到，

> 洛谷博客已不再大维护，之后将考虑停止运营

而有一部分人，并未将文章备份到其他位置，在洛谷的博客中存放着重要的信息。

这个脚本，可以**在 Windows 下**实现洛谷博客文章的自动下载。

请使用 Python3 编译 `BlogsCr.py`，确保有 `requests`，`time`，`os`，`re` 库。其中的后三个多半是有的，如果没有 `requests` 库，您可以在 `cmd` 中输入 `pip install requests` 来获得。

在代码中，这一段被醒目地标注出来，因为您需要更改这里的信息。

![](https://s4.ax1x.com/2022/01/27/7XdRTU.png)

先登录洛谷，按 F12 或右键打开检查，存储中 `__client_id` 的值即您的 cookie。

![](https://s4.ax1x.com/2022/01/27/7XwOuq.png)



**两项信息均需要打上引号。**

您的文章将被下载到与该 Python 文件同目录的 `Blogs` 文件夹中，文件名为 `您的文章的名称.md`。特别地，如果您的文章名称中含有 `?`、`、`、`╲`、`/`、`*`、`“`、`”`、`<`、`>`、`|`，均会被替换为 `&`，原因是 Windows 不允许文件名中出现上述字符。


前一部分使用 cookie 登录的代码，参考了洛谷日报的 [这篇](https://www.luogu.com.cn/blog/12cow/python)。
