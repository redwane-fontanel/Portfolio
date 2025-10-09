# Prayer App
import sys

import requests

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt, QDateTime
from PyQt5.QtGui import QPixmap, QWindow


class PrayerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter the name of the city", self)
        self.city_input = QLineEdit(self)
        self.get_prayer_time = QPushButton("Get prayer time", self)
        self.prayer_label = QLabel(self)
        self.fajr = QLabel(self)
        self.sunrise = QLabel(self)
        self.dhur = QLabel(self)
        self.asr = QLabel(self)
        self.maghrib = QLabel(self)
        self.isha = QLabel(self)
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.latitude = ""
        self.longitude = ""
        self.time_offset_hours = 0
        self.time_offset_minutes = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Prayer time")
        self.setGeometry(0, 0, 800, 500)

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_prayer_time)
        vbox.addWidget(self.prayer_label)

        hbox = QHBoxLayout()

        hbox.addWidget(self.fajr)
        hbox.addWidget(self.sunrise)
        hbox.addWidget(self.dhur)
        hbox.addWidget(self.asr)
        hbox.addWidget(self.maghrib)
        hbox.addWidget(self.isha)

        vbox.addLayout(hbox)

        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.prayer_label.setAlignment(Qt.AlignCenter)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_prayer_time.setObjectName("get_prayer_time")
        self.prayer_label.setObjectName("prayer_label")
        self.fajr.setObjectName("fajr")
        self.sunrise.setObjectName("sunrise")
        self.dhur.setObjectName("dhur")
        self.asr.setObjectName("asr")
        self.maghrib.setObjectName("maghrib")
        self.isha.setObjectName("isha")

        self.setStyleSheet("""

            QLabel{
                font-size: 30px;
            }

            QLabel#city_label{
                font-size: 30px;
                font-family: italic;
            }
            QLineEdit#city_input{
                font-size: 40px
            }
            QPushButton#get_prayer_time{
                font-size: 30px;
                font-weight: bold
            }

        """)
        self.time_label.setStyleSheet("font-size: 120px;"
                                      "font-family: Arial;"
                                      "color: black")
        self.setStyleSheet("background-color: black")

        self.get_prayer_time.clicked.connect(self.get_prayer)

    def get_prayer(self):
        api_key = "cc9fca75e29d2c95463d0d8efa574bbd"
        city = self.city_input.text()
        url = f"https://muslimsalat.com/{city}.json?key={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["status_code"] == 1:
                self.display_prayer(data)



            else:
                self.display_error("City not found. Please try again.")

        except requests.exceptions.RequestException as e:
            self.display_error("Error fetching prayer times. Please try again later.")

    def display_error(self, message):
        self.prayer_label.setStyleSheet("font-size: 30px;")
        self.prayer_label.setText(message)

    def display_prayer(self, data):
        fajr_praytime = data["items"][0]["fajr"]
        sunrise = data["items"][0]["shurooq"]
        dhur_praytime = data["items"][0]["dhuhr"]
        asr_praytime = data["items"][0]["asr"]
        maghrib_praytime = data["items"][0]["maghrib"]
        isha_praytime = data["items"][0]["isha"]

        self.prayer_label.setText("")
        self.fajr.setText(f"Fajr\n{fajr_praytime} ")
        self.sunrise.setText(f"Sunrise\n{sunrise} ")
        self.dhur.setText(f"Dhur\n{dhur_praytime} ")
        self.asr.setText(f"Asr\n{asr_praytime} ")
        self.maghrib.setText(f"Maghrib\n{maghrib_praytime} ")
        self.isha.setText(f"Isha\n{isha_praytime} ")

        self.get_time(data)

    def get_time(self, data):
        api_key2 = "pk.8dadcebfa1a9de8ae81e922528bc9fce"
        latitude = data["latitude"]
        longitude = data["longitude"]
        url2 = f"https://us1.locationiq.com/v1/timezone?key={api_key2}&lat={latitude}&lon={longitude}&format=json"


        try:
            response = requests.get(url2)
            response.raise_for_status()
            data2 = response.json()

            time_offset = data2["timezone"]["offset_sec"]

            self.time_offset_hours = time_offset // 3600
            self.time_offset_minutes = (time_offset % 3600) // 60

            self.timer.timeout.connect(self.update_time)
            self.timer.start(1000)

            self.update_time()

        except requests.exceptions.RequestException as e:
            print("Error fetching time offset:", e)
            self.display_error("Error fetching time. Please try again later.")

    def update_time(self):
        current_time = QDateTime.currentDateTimeUtc().time()

        updated_time = current_time.addSecs(self.time_offset_hours * 3600 + self.time_offset_minutes * 60)

        formatted_time = updated_time.toString("hh:mm:ss ap")

        self.time_label.setText(formatted_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    prayer_app = PrayerApp()
    prayer_app.show()
    sys.exit(app.exec_())
