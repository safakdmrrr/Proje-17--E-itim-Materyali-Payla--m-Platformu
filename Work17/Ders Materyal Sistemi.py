import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, \
        QTextEdit, QListWidget, QListWidgetItem, QDialog, QFileDialog, QComboBox, QLineEdit


class MainWindow(QMainWindow):
        class Ders:
            def __init__(self, ders_adi, icerik, ogretmen):
                self.ders_adi = ders_adi
                self.icerik = icerik
                self.ogretmen = ogretmen
                self.materials = []

            def materyal_yukle(self, materyal):
                self.materials.append(materyal)

            def materyallere_eris(self):
                return self.materials

        class Materyal:
            def __init__(self, materyal_adi, materyal_turu, icerik):
                self.materyal_adi = materyal_adi
                self.materyal_turu = materyal_turu
                self.icerik = icerik

            def bilgileri_goster(self):
                return f"Adı: {self.materyal_adi}, Türü: {self.materyal_turu}, İçerik: {self.icerik}"

        class Ogretmen:
            def __init__(self, ogretmen_id, ogretmen_adi):
                self.ogretmen_id = ogretmen_id
                self.ogretmen_adi = ogretmen_adi

            def materyal_yukle(self, ders, materyal):
                ders.materyal_yukle(materyal)

            def materyallere_eris(self, ders):
                return ders.materyallere_eris()

        class Ogrenci:
            def __init__(self, ogrenci_id, ogrenci_adi, ders, ogretmen):
                self.ogrenci_id = ogrenci_id
                self.ogrenci_adi = ogrenci_adi
                self.ders = ders
                self.ogretmen = ogretmen

            def ders_sec(self, ders):
                self.ders = ders

            def ogretmen_sec(self, ogretmen):
                self.ogretmen = ogretmen

        def __init__(self):
            super().__init__()
            self.setWindowTitle("Eğitim Materyali Paylaşım Platformu")
            self.setGeometry(550, 100, 800, 600)

            self.ogretmen = self.Ogretmen(1, "Öğretmen")

            central_widget = QWidget()
            self.setCentralWidget(central_widget)

            main_layout = QHBoxLayout()
            central_widget.setLayout(main_layout)

            dersler_widget = QWidget()
            dersler_layout = QVBoxLayout()
            dersler_widget.setLayout(dersler_layout)

            self.ders_label = QLabel("Dersler")
            dersler_layout.addWidget(self.ders_label)

            self.ders_listesi = QListWidget()
            dersler_layout.addWidget(self.ders_listesi)

            main_layout.addWidget(dersler_widget)

            materyaller_widget = QWidget()
            materyaller_layout = QVBoxLayout()
            materyaller_widget.setLayout(materyaller_layout)

            self.materyal_label = QLabel("Materyaller")
            materyaller_layout.addWidget(self.materyal_label)

            self.materyal_goruntu = QTextEdit()
            materyaller_layout.addWidget(self.materyal_goruntu)

            main_layout.addWidget(materyaller_widget)

            self.ders_detay_button = QPushButton("Ders Detaylarını Göster")
            self.ders_detay_button.setStyleSheet("background-color: green; color: white; padding: 5px; padding: 14px 20px; font-size:17px; font-weight: bold; font-family: sans-serif;")
            self.ders_detay_button.clicked.connect(self.ders_detaylarini_goster)
            dersler_layout.addWidget(self.ders_detay_button)

            self.materyal_yukle_button = QPushButton("Materyal Yükle")
            self.materyal_yukle_button.setStyleSheet("background-color: purple; color: white; padding: 5px;padding: 14px 20px; font-size:17px; font-weight: bold; font-family: sans-serif;")
            self.materyal_yukle_button.clicked.connect(self.materyal_yukle)
            dersler_layout.addWidget(self.materyal_yukle_button)

            self.ogrenci_ekle_button = QPushButton("Öğrenci Ekle")
            self.ogrenci_ekle_button.setStyleSheet("background-color: black; color: white; padding: 5px;padding: 14px 20px; font-size:17px; font-weight: bold; font-family: sans-serif;")
            self.ogrenci_ekle_button.clicked.connect(self.ogrenci_ekle)
            dersler_layout.addWidget(self.ogrenci_ekle_button)

            self.ders_secim = QComboBox()
            dersler_layout.addWidget(self.ders_secim)

            self.ogretmen_secim = QComboBox()
            dersler_layout.addWidget(self.ogretmen_secim)

            self.soru_label = QLabel("Sorular ve Eklenen Öğrenciler:")
            dersler_layout.addWidget(self.soru_label)

            self.sorular_goruntu = QTextEdit()
            dersler_layout.addWidget(self.sorular_goruntu)

            self.ogretmenler = ["Hamza-Mat", "Ali-Fizik", "Ayşe-Kimya", "Veli-Biyoloji", "Selim-Türkçe", "İlknur-Din", "Fevzi-İnkılap", "Murat-Nesne TP."]
            self.ogretmen_secim.addItems(self.ogretmenler)

            self.ders1 = self.Ders("Matematik", "Ders 2 saattir. 16:00 - 18:00 | Perşembe", self.Ogretmen(1, "Hamza"))
            self.ders2 = self.Ders("Fizik", "Ders 1s 50 dakikadır saattir. 13:20 - 15:10 | Çarşamba",
                                self.Ogretmen(2, "Ali"))
            self.ders3 = self.Ders("Kimya", "Ders 1s 30 dakikadır. 14:00 - 15:30 | Salı", self.Ogretmen(3, "Ayşe"))
            self.ders4 = self.Ders("Biyoloji", "Ders 2 saattir. 16:00 - 18:00 | Salı", self.Ogretmen(4, "Veli"))
            self.ders5 = self.Ders("Türkçe", "Ders 1s 50 dakikadır. 12:00 - 13:50 | Pazartesi", self.Ogretmen(5, "Selim"))
            self.ders6 = self.Ders("Din", "Ders 1 saattir. 14:00 - 15:00 Perşembe|", self.Ogretmen(6, "İlknur"))
            self.ders7 = self.Ders("İnkılap", "Ders 2 saattir. 16:00 - 18:00 | Cuma", self.Ogretmen(7, "Fevzi"))
            self.ders8 = self.Ders("Nesne Tabanlı Programlama", "Ders 2 saattir. 16:00 - 18:00 | Pazartesi",
                                self.Ogretmen(8, "Murat"))

            self.materyal1 = self.Materyal("Matematik Ders Notları", "Not", "Matematik ders notları içeriği")
            self.materyal2 = self.Materyal("Fizik Sunumu", "Sunum", "Fizik sunumu içeriği")
            self.materyal3 = self.Materyal("Kimya Deneyleri", "Deney", "Kimya deneyleri içeriği")
            self.materyal4 = self.Materyal("Biyoloji Kitabı", "Kitap", "Biyoloji kitabı içeriği")
            self.materyal5 = self.Materyal("Türkçe Yazıları", "Yazı", "Türkçe yazıları içeriği")
            self.materyal6 = self.Materyal("Din Konuları", "Konu", "Din konuları içeriği")
            self.materyal7 = self.Materyal("İnkılap Sunumları", "Sunum", "İnkılap sunumları içeriği")
            self.materyal8 = self.Materyal("Python Kodları", "Kod", "Python kodları içeriği")

            materyaller_widget.setStyleSheet("background-color: #ADD8E6;")
            self.materyal_goruntu.setStyleSheet("font-size: 17px;")

            self.soru_label.setStyleSheet("background-color: #ADD8E6; color: black; font-size: 17px; padding: 5px;")
            self.sorular_goruntu.setStyleSheet("font-size: 17px;")

            self.ogretmen.materyal_yukle(self.ders1, self.materyal1)
            self.ogretmen.materyal_yukle(self.ders2, self.materyal2)
            self.ogretmen.materyal_yukle(self.ders3, self.materyal3)
            self.ogretmen.materyal_yukle(self.ders4, self.materyal4)
            self.ogretmen.materyal_yukle(self.ders5, self.materyal5)
            self.ogretmen.materyal_yukle(self.ders6, self.materyal6)
            self.ogretmen.materyal_yukle(self.ders7, self.materyal7)
            self.ogretmen.materyal_yukle(self.ders8, self.materyal8)

            self.ders_listesi.addItems([self.ders1.ders_adi, self.ders2.ders_adi, self.ders3.ders_adi,
                                        self.ders4.ders_adi, self.ders5.ders_adi, self.ders6.ders_adi,
                                        self.ders7.ders_adi, self.ders8.ders_adi])

            self.ders_secim.addItems([self.ders1.ders_adi, self.ders2.ders_adi, self.ders3.ders_adi,
                                    self.ders4.ders_adi, self.ders5.ders_adi, self.ders6.ders_adi,
                                    self.ders7.ders_adi, self.ders8.ders_adi])

        def ders_detaylarini_goster(self):
            secilen_ders = self.ders_listesi.currentItem().text()
            if secilen_ders == self.ders1.ders_adi:
                self.materyal_goruntu.setText(
                    f"Ders: {self.ders1.ders_adi}\nİçerik: {self.ders1.icerik}\nÖğretmen: {self.ders1.ogretmen.ogretmen_adi}")
            elif secilen_ders == self.ders2.ders_adi:
                self.materyal_goruntu.setText(
                    f"Ders: {self.ders2.ders_adi}\nİçerik: {self.ders2.icerik}\nÖğretmen: {self.ders2.ogretmen.ogretmen_adi}")
            elif secilen_ders == self.ders3.ders_adi:
                self.materyal_goruntu.setText(
                    f"Ders: {self.ders3.ders_adi}\nİçerik: {self.ders3.icerik}\nÖğretmen: {self.ders3.ogretmen.ogretmen_adi}")
            elif secilen_ders == self.ders4.ders_adi:
                self.materyal_goruntu.setText(
                    f"Ders: {self.ders4.ders_adi}\nİçerik: {self.ders4.icerik}\nÖğretmen: {self.ders4.ogretmen.ogretmen_adi}")
            elif secilen_ders == self.ders5.ders_adi:
                self.materyal_goruntu.setText(
                    f"Ders: {self.ders5.ders_adi}\nİçerik: {self.ders5.icerik}\nÖğretmen: {self.ders5.ogretmen.ogretmen_adi}")
            elif secilen_ders == self.ders6.ders_adi:
                self.materyal_goruntu.setText(
                    f"Ders: {self.ders6.ders_adi}\nİçerik: {self.ders6.icerik}\nÖğretmen: {self.ders6.ogretmen.ogretmen_adi}")
            elif secilen_ders == self.ders7.ders_adi:
                self.materyal_goruntu.setText(
                    f"Ders: {self.ders7.ders_adi}\nİçerik: {self.ders7.icerik}\nÖğretmen: {self.ders7.ogretmen.ogretmen_adi}")
            elif secilen_ders == self.ders8.ders_adi:
                self.materyal_goruntu.setText(
                    f"Ders: {self.ders8.ders_adi}\nİçerik: {self.ders8.icerik}\nÖğretmen: {self.ders8.ogretmen.ogretmen_adi}")

        def soru_sor(self):
            dialog = QDialog(self)
            dialog.setWindowTitle("Soru Sor")

            layout = QVBoxLayout()

            label = QLabel("Sorunuzu Buraya Yazın:")
            layout.addWidget(label)

            soru_metni = QTextEdit()
            layout.addWidget(soru_metni)

            gonder_button = QPushButton("Gönder")
            gonder_button.clicked.connect(lambda: self.soru_gonder(soru_metni.toPlainText()))
            layout.addWidget(gonder_button)

            dialog.setLayout(layout)

            dialog.exec_()

        def materyal_yukle(self):
            ders_adi = self.ders_secim.currentText()
            secilen_ders = None
            if ders_adi == self.ders1.ders_adi:
                secilen_ders = self.ders1
            elif ders_adi == self.ders2.ders_adi:
                secilen_ders = self.ders2
            elif ders_adi == self.ders3.ders_adi:
                secilen_ders = self.ders3
            elif ders_adi == self.ders4.ders_adi:
                secilen_ders = self.ders4
            elif ders_adi == self.ders5.ders_adi:
                secilen_ders = self.ders5
            elif ders_adi == self.ders6.ders_adi:
                secilen_ders = self.ders6
            elif ders_adi == self.ders7.ders_adi:
                secilen_ders = self.ders7
            elif ders_adi == self.ders8.ders_adi:
                secilen_ders = self.ders8

            dosya_secim_penceresi = QFileDialog()
            dosya_yolu = dosya_secim_penceresi.getOpenFileName()[0]

            materyal_adi = dosya_yolu.split("/")[-1]
            materyal_turu = "Dosya"
            icerik = "Dosya içeriği"
            yeni_materyal = self.Materyal(materyal_adi, materyal_turu, icerik)

            secilen_ders.materyal_yukle(yeni_materyal)

            self.materyal_goruntu.clear()
            for materyal in secilen_ders.materyallere_eris():
                self.materyal_goruntu.append(materyal.bilgileri_goster())

        def ogrenci_ekle(self):
            dialog = QDialog(self)
            dialog.setWindowTitle("Öğrenci Ekle")

            layout = QVBoxLayout()

            label_ders = QLabel("Ders Seçin:")
            layout.addWidget(label_ders)

            ders_secim = QComboBox()
            ders_secim.addItems([self.ders1.ders_adi, self.ders2.ders_adi, self.ders3.ders_adi,
                                self.ders4.ders_adi, self.ders5.ders_adi, self.ders6.ders_adi,
                                self.ders7.ders_adi, self.ders8.ders_adi])
            layout.addWidget(ders_secim)

            label_ogretmen = QLabel("Öğretmen Seçin:")
            layout.addWidget(label_ogretmen)

            ogretmen_secim = QComboBox()
            ogretmen_secim.addItems(self.ogretmenler)
            layout.addWidget(ogretmen_secim)

            ogrenci_adi = QLineEdit()
            ogrenci_adi.setPlaceholderText("Öğrenci Adı")
            layout.addWidget(ogrenci_adi)

            ekle_button = QPushButton("Öğrenciyi Ekle")
            ekle_button.clicked.connect(lambda: self.ogrenci_ekle_onayla(ogrenci_adi.text(), ders_secim.currentText(), ogretmen_secim.currentText()))
            layout.addWidget(ekle_button)

            dialog.setLayout(layout)

            dialog.exec_()

        def ogrenci_ekle_onayla(self, ogrenci_adi, ders_adi, ogretmen_adi):
            ogretmen = None
            for o in self.ogretmenler:
                if o == ogretmen_adi:
                    ogretmen = o
                    break

            secilen_ders = None
            if ders_adi == self.ders1.ders_adi:
                secilen_ders = self.ders1
            elif ders_adi == self.ders2.ders_adi:
                secilen_ders = self.ders2
            elif ders_adi == self.ders3.ders_adi:
                secilen_ders = self.ders3
            elif ders_adi == self.ders4.ders_adi:
                secilen_ders = self.ders4
            elif ders_adi == self.ders5.ders_adi:
                secilen_ders = self.ders5
            elif ders_adi == self.ders6.ders_adi:
                secilen_ders = self.ders6
            elif ders_adi == self.ders7.ders_adi:
                secilen_ders = self.ders7
            elif ders_adi == self.ders8.ders_adi:
                secilen_ders = self.ders8

            ogrenci = self.Ogrenci(1, ogrenci_adi, secilen_ders, ogretmen)
            secilen_ders.materyal_yukle(self.materyal8)

            self.sorular_goruntu.append(f"{ogrenci_adi} adlı öğrenci {ders_adi} dersine eklendi ve Nesne Tabanlı Programlama dersi için çözülmesi gereken sorular yüklendi.")


if  __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
