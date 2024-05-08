from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QWidget, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
import requests

class ForeCast(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("ForeCast")
        self.setGeometry(200,200,500,200)
        self.setWindowIcon(QIcon('weather.avif'))
        self.AUI()

    def AUI(self):
        self.layout = QVBoxLayout()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter any City name")
        self.input.setStyleSheet("background-color:#E5E7E9;color:#0000;border:1px solid black;font-size: 20px;width:400px;")
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_weather)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_input)

        self.layout.addWidget(self.input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.search_button)
        button_layout.addWidget(self.clear_button)

        self.layout.addLayout(button_layout)

        self.temperature_label = QLabel()
        self.pressure_label = QLabel()
        self.humidity_label = QLabel()
        self.description_label = QLabel()

        self.layout.addWidget(self.temperature_label)
        self.layout.addWidget(self.pressure_label)
        self.layout.addWidget(self.humidity_label)
        self.layout.addWidget(self.description_label)
        self.search_button.setStyleSheet("""QPushButton {
            background-color: #55F918; 
            height:27px;
            width:100px;
            border-radius:5px;
            
        }
        QPushButton:hover {
            background-color: #18F6F9;
            color:white;
        }
    """)
        self.clear_button.setStyleSheet("""QPushButton {
            background-color: red; 
            height:27px;
            width:100px;
            border-radius:5px;
            color:cyan;
        }
        QPushButton:hover {
            background-color: black;
            color:white;
            width:100px;
            height:35px;
        }
    """)

        self.setLayout(self.layout)

    def search_weather(self):
        city = self.input.text()
        if city:
            api_key = "a07f5a47c9198a51e2e3c908470cfadf"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = city
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            response = requests.get(complete_url)
            if response.status_code == 200:
                data = response.json()
                if data["cod"] != "404":
                    main_data = data["main"]
                    current_temperature = main_data["temp"]
                    current_pressure = main_data["pressure"]
                    current_humidity = main_data["humidity"]
                    weather_data = data["weather"]
                    weather_description = weather_data[0]["description"]
                    self.temperature_label.setStyleSheet("color:red;font-size:30px;")
                    self.temperature_label.setText(f"Temperature: {current_temperature}°C")
                    self.pressure_label.setStyleSheet("color:purple;font-size:30px;")
                    self.pressure_label.setText(f"Atmospheric Pressure: {current_pressure} hPa")
                    self.humidity_label.setStyleSheet("color:green;font-size:30px;")
                    self.humidity_label.setText(f"Humidity: {current_humidity}%")
                    self.description_label.setStyleSheet("color:blue;font-size:30px;")
                    self.description_label.setText(f"Description: {weather_description}")
                else:
                    QMessageBox.warning(self, "City Not Found", "City not found, please enter a valid city name.")
            else:
                QMessageBox.warning(self, "Error", "Failed to fetch weather data.")
        else:
            QMessageBox.warning(self, "Enter City", "Please enter a city name.")

    def clear_input(self):
        self.input.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = ForeCast()
    win.show()
    app.exec_()
