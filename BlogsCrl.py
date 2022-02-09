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
    while ct[l] != "\"":
        lag += ct[l]
        l += 1
    ct = chg(ct, x + lag + '\"' + '>', "```" + lag + '\n')
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
        while ct[sl] != '<' or ct[sl + 1] != '/':
            mes += ct[sl]
            sl += 1
        ans += mes + ' | '
        cnt += 1

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
    tf = ""    
    if ct.find("<td style=\"text-align: right;\">", l) != -1 and ct.find("<td style=\"text-align: right;\">", l) < r:
        tf = "<td style=\"text-align: right;\">"
    elif ct.find("<td style=\"text-align: left;\">", l) != -1 and ct.find("<td style=\"text-align: left;\">", l) < r:
        tf = "<td style=\"text-align: left;\">"
    else:
        tf = "<td style=\"text-align: center;\">"

    w = l
    ans = "| "
    while ct.find(tf, w + 1) != -1 and ct.find(tf, w + 1) < r:
        w = ct.find(tf, w + 1)
        mes = ""
        sl = w + len(tf)
        while ct[sl] != '<' or ct[sl + 1] != '/':
            mes += ct[sl]
            sl += 1
        ans += mes + ' | '
    rpt = ""
    for i in range(l):
        rpt += ct[i]
    rpt += ans
    for i in range(r + 5, len(ct)):
        rpt += ct[i]
    return rpt
    

syst = os.name
if syst == "nt":
    syst = "Windows"
else:
    syst = "Others"
spc = ""

if syst == "Windows":
    spc = "\\/:*?\"<>|"
else:
    spc = ":/"
    
def fname(st1):
    for i in range(len(st1)):
        x = st1[i]
        if spc.find(x) != -1:
            t = ""
            for j in range(i):
                t += st1[j]
            t += '&'
            for j in range(i + 1, len(st1)):
                t += st1[j]
            st1 = t
    return st1

def wist(ct, bg):
    fst = "<blockquote>"
    l = bg
    bg += len(fst)
    cnt, q = 1, 0
    now = ""
    rta = ""
    while cnt > 0:
        cot = ""
        q = ct.find("</blockquote>", bg)
        w = ct.find("<blockquote>", bg)
        while ct[bg] != '\n':
            cot += ct[bg]
            bg += 1
        bg += 1
        if cot != "":
            for i in range(cnt):
                now += '>'
            now += ' ' + cot + '\n'
        if bg == q:
            cnt -= 1
            bg += len(fst) + 1
        elif bg == w:
            cnt += 1
            bg += len(fst)
    
    for i in range(l):
        rta += ct[i]
    rta += now
    for i in range(q + 13, len(ct)):
        rta += ct[i]
    return rta


def wist2(ct):
    li = ct.find("<ul>")
    la = ct.find("<ol>")
    l = 0
    opt = []
    lop = 0
    if li == -1:
        l = la
        opt.append("1. ")
    elif la == -1:
        l = li
        opt.append("- ")
    else:
        if li > la:
            l = la
            opt.append("1. ")
        else:
            l = li
            opt.append("- ")
    bg = l + 4
    cnt, q = 1, 0
    now = ""
    rta = ""
    while cnt > 0:
        cot = ""
        cg1 = ct.find("</ul>", bg)
        cg2 = ct.find("<ul>", bg)
        cg3 = ct.find("</ol>", bg)
        cg4 = ct.find("<ol>", bg)
        if cg1 == -1:
            cg1 = len(ct) + 114514
        if cg3 == -1:
            cg3 = len(ct) + 114514

        # print(ct[bg], end = '??\n')

        pic = ct.find("![", bg)
        lnk = ct.find("[", bg)
        cod = ct.find("```", bg)

        if pic != -1 and bg == pic:
            pr = ct.find(")", pic)
            for i in range(cnt - 1):
                now += '\t'
            for i in range(pic, pr + 2):
                now += ct[i]
            bg = pr + 1
            continue
        if lnk != -1 and bg == lnk:
            pr = ct.find(")", lnk)
            for i in range(cnt - 1):
                now += '\t'
            for i in range(lnk, pr + 2):
                now += ct[i]
            bg = pr + 1
            continue
        if cod != -1 and bg == cod:
            pr = ct.find("```", cod + 4)
            for i in range(cnt - 1):
                now += '\t'
            for i in range(cod, pr + 4):
                now += ct[i]
            bg = pr + 3
            continue
        if bg >= len(ct):
            break

        while ct[bg] != '\n':
            cot += ct[bg]
            bg += 1
        while ct[bg] == '\n':
            bg += 1
        if cot != "":
            for i in range(cnt - 1):
                now += '\t'
            now += opt[lop] + cot + '\n'
        if bg == cg1 or bg == cg3:
            cnt -= 1
            del(opt[lop])
            lop -= 1
            bg += 5
            if cg1 > cg3:
                q = cg3
            else:
                q = cg1
        elif bg == cg2:
            cnt += 1
            opt.append("- ")
            lop += 1
            bg += 4
        elif bg == cg4:
            cnt += 1
            opt.append("1. ")
            lop += 1
            bg += 4
    
    for i in range(l):
        rta += ct[i]
    rta += now
    for i in range(q + 5, len(ct)):
        rta += ct[i]
    return rta
            
##############################################
uid = "xxxxxx"
client = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
##############################################
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
response.encoding = 'utf-8'
s = response.text


p = re.search(r"<h2 style='margin-bottom: 0'>(.*?)</h2>",s)
if p:
    s=p.group()
    p = re.search(r"target=\"_blank\">(.*?)</a>",s)
    print("成功登录 " + p.group(1))
else:
    p = re.search(r"<h2>欢迎回来，(.*?)</h2>",s)
    if p:
        p = re.search(r"target=\"_blank\">(.*?)</a>",s)
        print("成功登录 " + p.group(1), end = "\n\n")
    else:
        ref = "https://www.luogu.com.cn/api/user/search?keyword="+uid
        response = requests.get(ref,headers=headers)
        response.encoding = 'utf-8'
        id = response.json()
        id = id['users'][0]["name"]
        print("登录失败","uid:",uid,"id:",id)

esc = '\\`*_{}[]()#+-.!'

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

tim = 1
while True:
    url = "https://www.luogu.com.cn/blogAdmin/article/list?status=%5B1%2C2%5D&solution=%5B%5D&page=" + str(tim) + "&pageType=list&name=&status-check=1&status-check=2&order=0"
    response = requests.get(url, headers = headers)
    response.encoding = 'utf-8'
    T = response.text

    ft = 0
    fd = "/blogAdmin/article/edit/"
    if T.find(fd, ft) == -1:
        break
    while T.find(fd, ft) != -1:
        ft = T.find(fd, ft) + len(fd)
        bid = 0
        for i in range(ft, ft + 6):
            bid = bid * 10 + int(T[i])

        fd = "https://www.luogu.com.cn" + fd + str(bid)
        response = requests.get(fd, headers = headers)
        response.encoding = 'utf-8'
        t = response.text

        sat = "type=\"text\" placeholder=\"文章分类\""
        gsat = t.find(sat) + len(sat)
        gsat = t.find("value=", gsat) + 7
        gty = ""
        while t[gsat] != '\"' or t[gsat + 1] != '/' or t[gsat + 2] != '>':
            gty += t[gsat]
            gsat += 1

        w = t.find("可根据标题自动生成")
        w = t.find("value", w + 1) + 7
        ul = ""
        while t[w] != '\"':
            ul += t[w]
            w += 1
            
        url = urob + ul
        response = requests.get(url, headers = headers)
        response.encoding = 'utf-8'
        t = response.text

        nameall = ""
        l = t.find("<title>") + 7
        r = t.find(" - " + blogname, l + 1)
        for i in range(l, r):
            nameall += t[i]

        n = "id=\"article-content\">"
        l = t.find(n) + len(n)
        r = t.find("</div>", l + 1)

        ans = ""
        for i in range(l, r):
            ans += t[i]

        # print(ans)
        ans = ans.replace("$$", "$$  ")

        lt = rt = img = href = cod = my = my2 = 0
        while ans.find("<p>", rt + 1) != -1:
            lt = ans.find("<p>", rt + 1)
            rt = ans.find("</p>", lt + 1)
            cod = ans.find("<code>", lt)
            img = ans.find("<img src=", lt)
            href = ans.find("<a href=", lt)
            my = ans.find("$", lt)
            my2 = ans.find("$$", lt)
            while my + 1 < len(ans) and ans[my + 1] == '$':
                my = ans.find("$", my + 2)
            i = lt + 3
            while i < rt:
                if i == img:
                    i = ans.find("/>", img) + 2
                    img = ans.find("<img src=", img + 1)
                if i == cod:
                    i = ans.find("</code>", cod) + 7
                    cod = ans.find("<code>", i)
                if i == href:
                    i = ans.find("</a>", href) + 4
                    href = ans.find("<a href=", href + 1)
                if i == my2:
                    i = ans.find("$$", my2 + 2) + 2
                    my2 = ans.find("$$", i)
                if i == my:
                    i = ans.find("$", my + 1) + 1
                    my = ans.find("$", i + 1)
                    while my + 1 < len(ans) and ans[my + 1] == '$':
                        my = ans.find("$", my + 2)
                # print(str(img) + ": " + ans[img] + '   ' + str(i) + ': ' + ans[i], end = "!!!\n")
                if ans[i] == '\n':
                    q = ""
                    for j in range(i):
                        q += ans[j]
                    for j in range(i + 1, len(ans)):
                        q += ans[j]
                    ans = q
                    i -= 1
                    rt -= 1
                    img -= 1
                    href -= 1
                    cod -= 1
                    my -= 1
                    my2 -= 1
                if esc.find(ans[i]) != -1:
                    q = ""
                    for j in range(i):
                        q += ans[j]
                    q += "\\" + ans[i]
                    for j in range(i + 1, len(ans)):
                        q += ans[j]
                    ans = q
                    i += 1
                    rt += 1
                    img += 1
                    href += 1
                    cod += 1
                    my += 1
                    my2 += 1
                i += 1
        # print(ans)
        ans = chg(ans, "<p>", "\n")
        ans = chg(ans, "&lt;", "<")
        ans = chg(ans, "&gt;", ">")
        ans = chg(ans, "&amp;", "&")
        ans = chg(ans, "</p>", "")
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
        ans = chg(ans, "<br />", "\n")
        ans = chg(ans, "<pre><code>", "```\n")
        ans = chg(ans, "</code></pre>", "\n```")
        ans = chg(ans, "<code>", "`")
        ans = chg(ans, "</code>", "`")
        ans = chg(ans, "</tbody>", "")
        ans = chg(ans, "</table>", "")
        ans = chg(ans, "<table>", "")
        ans = chg(ans, "<em>", "*")
        ans = chg(ans, "</em>", "*")
        ans = chg(ans, "$$", "\n$$\n")
        ans = ans.replace("\u200b", " ")
        while ans.find("<pre><code class=\"language-") != -1:
            ans = chg2(ans)
        while ans.find("<thead>") != -1:
            ans = ctr2(ans, "<thead>")
        while ans.find("<tr>") != -1:
            ans = ctr3(ans)
        ans = chg(ans, "&quot;", "\"")
        ans = chg(ans, "</li>", "")
        ans = chg(ans, "<li>", "")
        w = "<a href=\""
        while ans.find(w) != -1:
            l = ans.find(w) + len(w)
            r = ans.find("\"", l)
            un = ""
            for i in range(l, r):
                un += ans[i]
            r2 = ans.find("</a>", r + 1)
            name = ""
            for i in range(r + 2, r2):
                name += ans[i]
            q = ""
            for i in range(l - len(w), r2 + 4):
                q += ans[i]
            if name == un and un.find("http") != -1:
                ans = chg(ans, q, "<" + un + ">")
            else:
                ans = chg(ans, q, "[" + name + "](" + un + ")")
        w = "<img src=\""
        while ans.find(w) != -1:
            l = ans.find(w) + len(w)
            r = ans.find("\"", l)
            un = ""
            for i in range(l, r):
                un += ans[i]
            state = ""
            k = r + 7
            while ans[k] != '\"':
                state += ans[k]
                k += 1
            q = ""
            for i in range(l - len(w), k + 4):
                q += ans[i]
            ans = chg(ans, q, "![" + state + "](" + un + ")")

        while ans.find("<blockquote>") != -1:
            ans = wist(ans, ans.find("<blockquote>"))

        # print(ans)

        while ans.find("<ol>") != -1 or ans.find("<ul>") != -1:
            ans = wist2(ans)

        # print(ans)
        
        ans = chg(ans, "\n", "  \n")

        q = ans.find("<>&# ## ### #### ##### ###### ~~~~****  ")

        ot = ""
        for i in range(q):
            ot += ans[i]
        # print(ot)
        # syst = "Others"
        if syst == "Others":
            if nameall[0] == '+':
                p = "A "
                for i in range(1, len(nameall)):
                    p += nameall[i]
                nameall = p
            elif nameall[0] == '-':
                p = "M "
                for i in range(1, len(nameall)):
                    p += nameall[i]
                nameall = p
            elif nameall[0] == '.':
                p = "P "
                for i in range(1, len(nameall)):
                    p += nameall[i]
                nameall = p
        ##############################################
        nameall = '【' + gty + '】' + nameall
        ##############################################
        
        print("Downloading: " + nameall + '\n')
        
        ##############################################
        ot += "\n-----\n分类：" + gty
        ##############################################
        
        nameall = fname(nameall)
        with open("Blogs\\" + nameall + ".md", 'w+') as f:
            f.write(ot)
        fd = "/blogAdmin/article/edit/"
        time.sleep(7)
    tim += 1
