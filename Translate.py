import urllib.request
import urllib.parse
import json
from tkinter import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI_Designer.translate import Ui_MainWindow
from PyQt5.QtGui import QIcon


class App(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setWindowIcon(QIcon('translateIcon.ico'))
        self.master = 0
        self.setupUi(self)
        self.data = {}
        self.url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        self.data['from'] = 'AUTO'
        self.data['to'] = 'AUTO'
        self.data['smartresult'] = 'dict'
        self.data['client'] = 'fanyideskweb'
        self.data['salt'] = '15688142575922'
        self.data['sign'] = '10d39d8e6dcf6bb449a8f5bbf0065efd'
        self.data['ts'] = '1568814257592'
        self.data['bv'] = '894207082b60436e559a7260e4bfb1fc'
        self.data['doctype'] = 'json'
        self.data['version'] = '2.1'
        self.data['keyfrom'] = 'fanyi.web'
        self.data['action'] = 'FY_BY_CLICKBUTTION'

    def translateText(self):
        text = self.translate_in.toPlainText()
        # print(text + "==")
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

    def copy_text(self):
        clipboard = QApplication.clipboard()
        print('Hello')
        self.translate('Heelo')
        clipboard.setText(self.translate_out.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = App()
    MainWindow.show()
    sys.exit(app.exec())
