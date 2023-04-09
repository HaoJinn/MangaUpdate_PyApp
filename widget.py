from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy, QMessageBox, QLineEdit, QInputDialog
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QSize, QSettings, QUrl
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
import requests

data = QSettings("MyApp")

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manga Manager")
        self.setFixedSize(800, 800)



        button1 = QPushButton()
        button1.setIcon(QIcon(r"C:\Users\nymph\Desktop\Application Qt\src\reload-2398777_1280.jpg"))
        button1.setText("Check All")
        button1.setIconSize(QSize(16, 16))
        #button1.setFixedSize(QSize(150, 30))
        button1.clicked.connect(self.check_all)

        button2 = QPushButton("Add")
        button2.setFixedWidth(50)
        button2.clicked.connect(self.add_manga)

        button3 = QPushButton("Remove")
        button3.setFixedWidth(50)
        button3.clicked.connect(self.remove_manga)

        h_layout = QHBoxLayout()
        h_layout.addStretch()
        h_layout.setSpacing(0)
        h_layout.addWidget(button3, alignment=Qt.AlignRight)
        h_layout.addWidget(button2, alignment=Qt.AlignRight)
        h_layout.addWidget(button1, alignment=Qt.AlignRight)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)

        #data = QSettings("App")

        #img_download = QNetworkAccessManager()

        for key in data.allKeys():

            temp_hb = QHBoxLayout()
            temp_value = data.value(key)
            #print(temp_value[2])
            #temp_req = QNetworkRequest(QUrl(temp_value[2]))
            #reply = img_download.get(temp_req)
            #pixmap = QPixmap()
            #pixmap.loadFromData(reply.readAll())
            #icon = QIcon(pixmap)

            response = requests.get(temp_value[2])
            image_data = response.content

            pixmap = QPixmap()
            pixmap.loadFromData(image_data)

            temp_label = QLabel()
            temp_label.setScaledContents(True)
            temp_label.setMaximumSize(55, 80)
            temp_label.setPixmap(pixmap)

            temp_label1 = QLabel()
            temp_label1.setText("<a href = '" + temp_value[0] + "'>" + key)
            temp_label1.setOpenExternalLinks(True)
            temp_label1.setAlignment(Qt.AlignTop)

            temp_hb.addWidget(temp_label, alignment=Qt.AlignLeft)
            temp_hb.addWidget(temp_label1, alignment= Qt.AlignLeft)
            temp_hb.addStretch()


            v_layout.addLayout(temp_hb)
            v_layout.addStretch()




        self.setLayout(v_layout)


    def check_all(self):
        #check for new chapters
        print("")

    def add_manga(self):
        #pop up window asking for new manga url
        link, ok = QInputDialog.getText(None, "Add a new manga", "Enter the URL(from manganato):")
        response = requests.get(link)
        html_content = response.text

        #get manga name
        start = html_content.find("<title>")
        start += 7
        end = html_content.find("Manga Online", start) - 1
        key = html_content[start:end]

        #get newest chapter link
        cstart = html_content.find("href=",html_content.find("li class")) + 6
        cend = html_content.find("\"", cstart + 1)
        chapter = html_content[cstart:cend]

        #get image url
        istart = html_content.find("twitter:image") + 24
        iend = html_content.find("jpg", istart) + 3
        image = html_content[istart:iend]

        value = [link, chapter, image]

        #data = QSettings("MyApp")
        data.setValue(key, value)

        '''
        for key in data.allKeys():
            print(data.value(key)) 
        '''



    def remove_manga(self):
        #click on the manga to remove
        print("")
