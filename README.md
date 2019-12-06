### 软件截图
![软件截图](https://img-blog.csdnimg.cn/20191206164851850.png)

![](https://img-blog.csdnimg.cn/20191206165201125.png)

## 下面说一下主要的思想
### 界面方面
&emsp;&emsp;界面主要采用PyQt5的QtDesigner来制作，主要是因为QT的界面可以支持CSS样式，制作起来比较好看，当然为了简单，我自己也没有加任何特效。读者可以自行加载CSS样式。

&emsp;&emsp;这里没有直接采用tkinter也是想试一下QT，对于熟悉tkinter的同学，可以自己改进，也比较简单。

**注意：** 翻译这个按钮其实没有用，增加了实时翻译的效果，所以不太会用到翻译按钮，这里加上翻译按钮主要是为了更好的模仿一些翻译软件。

### 程序方面
&emsp;&emsp;使用的Python作为编程软件，一方面是爬取方便，另一方面也比较简单 (-_-)。
```Python
# 主要文件Translate.py
    def translateText(self): # 翻译文本
        text = self.translate_in.toPlainText()
        if text != '':
            self.data['i'] = text
            data = urllib.parse.urlencode(self.data).encode('utf-8')
            request = urllib.request.urlopen(self.url, data)
            html = request.read().decode('utf-8')
            target = json.loads(html)
            # print(target['translateResult'])
            result = []
            for i in range(len(target['translateResult'])):
                res = target['translateResult'][i][0]['tgt']
                result.append(res)
            self.translate_out.setPlainText('\n'.join(result))

    def copy_text(self):  # 复制文本
        clipboard = QApplication.clipboard()   # 剪切板
        clipboard.setText(self.translate_out.toPlainText()) 
```

整体来说还是比较简单的，如果大家需要tkinter的版本可以和我留言，我可以外加一篇。

![小猫咪](https://img-blog.csdnimg.cn/20191206170644586.jpg)
