import requests
import time
import re
import os

def chg(ct, st1, st2):
    w = ct.split(st1)
    ans = ""
    for x in w:
        ans += x + st2
    return ans

def chg2(ct):
    x = "<pre><code class=\"language-"
    l = ct.find(x) + len(x)
    lag = ""
    # print(ct[l])
    while ct[l] != "\"":
        lag += ct[l]
        l += 1
    # print(x + lag + '\"' + '>')
    ct = chg(ct, x + lag + '\"' + '>', "```" + lag + '\n')
    # print(ct)
    return ct

def ctr(ct, st1, st2):
    if st1 == "<ol>":
        st = "</ol>"
    if st1 == "<ul>":
        st = "</ul>"
    l = ct.find(st1)
    r = ct.find(st, l + 1)
    w = l
    while ct.find("<li>", w) != -1 and ct.find("<li>", w) < r:
        w = ct.find("<li>", w)
        q = ""
        for i in range(w):
            q += ct[i]
        q += st2
        for i in range(w + 4, len(ct)):
            q += ct[i]
        ct = q

        # print(q)

    q = ""
    l = ct.find(st1)
    r = ct.find(st, l + 1)
    for i in range(l):
        q += ct[i]
    for i in range(l + 4, r):
        q += ct[i]
    for i in range(r + 5, len(ct)):
        q += ct[i]
    return q

def ctr2(ct, st):
    st1 = "</thead>"
    l = ct.find(st)
    r = ct.find(st1, l + 1)
    ntf = "</th>"
    tf = ""    
    if ct.find("<th style=\"text-align: right;\">", l) != -1 and ct.find("<th style=\"text-align: right;\">", l) < r:
        tf = "<th style=\"text-align: right;\">"
    elif ct.find("<th style=\"text-align: left;\">", l) != -1 and ct.find("<th style=\"text-align: left;\">", l) < r:
        tf = "<th style=\"text-align: left;\">"
    else:
        tf = "<th style=\"text-align: center;\">"

    w = l
    ans = "| "
    cnt = 0
    while ct.find(tf, w + 1) != -1 and ct.find(tf, w + 1) < r:
        w = ct.find(tf, w + 1)
        mes = ""
        sl = w + len(tf)
        # print(w, end = "?????\n")
        while ct[sl] != '<' or ct[sl + 1] != '/':
            mes += ct[sl]
            sl += 1
        ans += mes + ' | '
        cnt += 1
        # print(ans)

    r = ct.find("<tbody>", l)
    rpt = ""
    for i in range(l):
        rpt += ct[i]
    rpt += ans + '\n'
    esp = '----------'
    if tf.find("right") != -1:
        esp += ':'
    elif tf.find("left") != -1:
        esp = ':' + esp
    else:
        esp = ':' + esp + ':'
    for i in range(cnt):
        rpt += '| ' + esp + ' '
    rpt += '|'
    for i in range(r + 7, len(ct)):
        rpt += ct[i]
    return rpt

def ctr3(ct):
    st1 = "</tr>"
    l = ct.find("<tr>")
    r = ct.find(st1, l + 1)
    # ntf = "</td>"
    tf = ""    
    if ct.find("<td style=\"text-align: right;\">", l) != -1 and ct.find("<td style=\"text-align: right;\">", l) < r:
        tf = "<td style=\"text-align: right;\">"
    elif ct.find("<td style=\"text-align: left;\">", l) != -1 and ct.find("<td style=\"text-align: left;\">", l) < r:
        tf = "<td style=\"text-align: left;\">"
    else:
        tf = "<td style=\"text-align: center;\">"

    w = l
    ans = "| "
    # print(tf, end = "!!!!123123\n")
    # print(ct.find(tf, w + 1))
    while ct.find(tf, w + 1) != -1 and ct.find(tf, w + 1) < r:
        w = ct.find(tf, w + 1)
        # print(w, end = "?????\n")
        mes = ""
        sl = w + len(tf)
        while ct[sl] != '<' or ct[sl + 1] != '/':
            mes += ct[sl]
            sl += 1
        ans += mes + ' | '
        # print(ans)
    rpt = ""
    for i in range(l):
        rpt += ct[i]
    rpt += ans
    for i in range(r + 5, len(ct)):
        rpt += ct[i]
    return rpt
    

def fname(st1):
    for i in range(len(st1)):
        x = st1[i]
        if x == '?' or x == '/' or x == '\\' or x == ':' or x == '>' or x == '\"' or x == '*' or x == '<' or x == '|':
            t = ""
            for j in range(i):
                t += st1[j]
            t += '&'
            for j in range(i + 1, len(st1)):
                t += st1[j]
            st1 = t
    return st1
            

uid = "409236"
client = "0aa86f61fe7f368dc0b1f7d4cbf9a97c47201c92"
string = "_uid="+uid+";__client_id="+client

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
    "cookie":string
}

v = os.getcwd() + "\\Blogs" 
k = os.path.exists(v)
if k == False:
    os.makedirs(v)

response = requests.get("https://www.luogu.com.cn",headers=headers)
response.encoding = 'utf-8' # 解码
s = response.text # 获取网页源代码

# 以下程序为正则表达式，在后文会提到，作用为抓取登录洛谷后打卡页面的id
p = re.search(r"<h2 style='margin-bottom: 0'>(.*?)</h2>",s)
if p:
    s=p.group()
    p = re.search(r"target=\"_blank\">(.*?)</a>",s)
    print("成功登录 " + p.group(1))
else:
    p = re.search(r"<h2>欢迎回来，(.*?)</h2>",s)
    if p:
        p = re.search(r"target=\"_blank\">(.*?)</a>",s)
        print("成功登录 " + p.group(1))
    else:
        ref = "https://www.luogu.com.cn/api/user/search?keyword="+uid
        response = requests.get(ref,headers=headers)
        response.encoding = 'utf-8'
        id = response.json()
        id = id['users'][0]["name"]
        print("登录失败","uid:",uid,"id:",id)



url = "https://www.luogu.com.cn/blogAdmin/article/list?pageType=list"
response = requests.get(url, headers = headers)
response.encoding = 'utf-8'
T = response.text
        
urob = ""
w = T.find("<div class=\"mdui-toolbar-spacer\"></div>")
w = T.find("<a href=\"", w) + 9
while T[w] != '\"':
    urob += T[w]
    w += 1

response = requests.get(urob, headers = headers)
response.encoding = 'utf-8'
T = response.text

bnx = "<meta name=\"blog-name\" content=\""
w = T.find(bnx) + len(bnx)
blogname = ""
while T[w] != "\"":
    blogname += T[w]
    w += 1
    
# print(blogname)

tim = 1
while True:
    url = "https://www.luogu.com.cn/blogAdmin/article/list?status=%5B1%2C2%5D&solution=%5B%5D&page=" + str(tim) + "&pageType=list&name=&status-check=1&status-check=2&order=0"
    response = requests.get(url, headers = headers)
    response.encoding = 'utf-8'
    T = response.text
    # print(urob)
    # print(T)

    ft = 0
    fd = "/blogAdmin/article/edit/"
    if T.find(fd, ft) == -1:
        break
    while T.find(fd, ft) != -1:
        ft = T.find(fd, ft) + len(fd)
        # print(ft)
        bid = 0
        for i in range(ft, ft + 6):
            bid = bid * 10 + int(T[i])

        fd = "https://www.luogu.com.cn" + fd + str(bid)
        # print(fd)

        response = requests.get(fd, headers = headers)
        response.encoding = 'utf-8'
        t = response.text

        w = t.find("可根据标题自动生成")
        w = t.find("value", w + 1) + 7
        ul = ""
        while t[w] != '\"':
            ul += t[w]
            w += 1
            
        # print(ul)
        url = urob + ul
        response = requests.get(url, headers = headers)
        response.encoding = 'utf-8'
        t = response.text
        # print(t)

        nameall = ""
        l = t.find("<title>") + 7
        r = t.find(" - " + blogname, l + 1)
        for i in range(l, r):
            nameall += t[i]
        nameall = fname(nameall)
        # print(nameall)

        # print(r)

        n = "<div id=\"article-content\">"
        l = t.find(n) + len(n)
        r = t.find("</div>", l + 1)

        ans = ""
        for i in range(l, r):
            ans += t[i]
        # print(ans)

        ans = chg(ans, "<p>", "")
        ans = chg(ans, "&lt;", "<")
        ans = chg(ans, "&gt;", ">")
        ans = chg(ans, "&amp;", "&")
        ans = chg(ans, "</p>", "")
        # ans = chg(ans, "<ul>", "")
        # ans = chg(ans, "</ul>", "")
        # ans = chg(ans, "<li>", "\- ")
        ans = chg(ans, "<h1>", "# ")
        ans = chg(ans, "<h2>", "## ")
        ans = chg(ans, "<h3>", "### ")
        ans = chg(ans, "<h4>", "#### ")
        ans = chg(ans, "<h5>", "##### ")
        ans = chg(ans, "<h6>", "###### ")
        ans = chg(ans, "</h1>", "")
        ans = chg(ans, "</h2>", "")
        ans = chg(ans, "</h3>", "")
        ans = chg(ans, "</h4>", "")
        ans = chg(ans, "</h5>", "")
        ans = chg(ans, "</h6>", "")
        ans = chg(ans, "<del>", "~~")
        ans = chg(ans, "</del>", "~~")
        ans = chg(ans, "<strong>", "**")
        ans = chg(ans, "</strong>", "**")
        ans = chg(ans, "<hr />", "\n----\n")
        ans = chg(ans, "<br />", "\n\n")
        ans = chg(ans, "<pre><code>", "```\n")
        ans = chg(ans, "</code></pre>", "\n```")
        ans = chg(ans, "<code>", "`")
        ans = chg(ans, "</code>", "`")
        ans = chg(ans, "</tbody>", "")
        ans = chg(ans, "</table>", "")
        ans = chg(ans, "<table>", "")
        ans = chg(ans, "$$", "\n$$")
        ans = ans.replace("\u200b", " ")
        while ans.find("<pre><code class=\"language-") != -1:
            ans = chg2(ans)
        while ans.find("<ol>") != -1:
            ans = ctr(ans, "<ol>", "1. ")
        while ans.find("<ul>") != -1:
            ans = ctr(ans, "<ul>", "- ")
        while ans.find("<thead>") != -1:
            ans = ctr2(ans, "<thead>")
        while ans.find("<tr>") != -1:
            ans = ctr3(ans)
        ans = chg(ans, "&quot;", "\"")
        ans = chg(ans, "</li>", "")
        w = "<a href=\""
        while ans.find(w) != -1:
            l = ans.find(w) + len(w)
            r = ans.find(">", l)
            un = ""
            for i in range(l, r):
                un += ans[i]
            r2 = ans.find("</a>", r + 1)
            name = ""
            for i in range(r + 1, r2):
                name += ans[i]
            q = ""
            for i in range(l - len(w), r2 + 4):
                q += ans[i]
            ans = chg(ans, q, "[" + name + "](" + un + ")")
        w = "<img src=\""
        while ans.find(w) != -1:
            l = ans.find(w) + len(w)
            r = ans.find("\"", l)
            un = ""
            for i in range(l, r):
                un += ans[i]
            # print(un, end = "!!\n")
            r2 = ans.find("alt=\"\"", r)
            q = ""
            for i in range(l - len(w), r2 + 9):
                q += ans[i]
            # print(q, end = "??\n")
            ans = chg(ans, q, "![](" + un + ")")
        ans = chg(ans, "\n", "  \n")

        q = ans.find("<>&# ## ### #### ##### ###### ~~~~****  ")

        ot = ""
        for i in range(q):
            ot += ans[i]
        # print(ot)
        print("Downloading: " + nameall + '\n')
        with open("Blogs\\" + nameall + ".md", 'w+') as f:
            f.write(ot)
        # print(ft)
        fd = "/blogAdmin/article/edit/"
        time.sleep(7)
    tim += 1
