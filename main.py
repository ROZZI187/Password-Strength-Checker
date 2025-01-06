import sys
import os
import re
import random
import string
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                               QWidget, QTextEdit, QDialog, QMessageBox)
from PySide6.QtGui import QTextCursor, QTextCharFormat, QColor
from PySide6.QtCore import Qt

class PasswordStrengthChecker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprawdzanie Siły Hasła")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet("background-color: #f0f0f0; font-family: Arial; font-size: 14px;")

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.password_label = QLabel("Wprowadź swoje hasło:")
        layout.addWidget(self.password_label)

        password_layout = QHBoxLayout()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(self.password_input)

        self.show_password_button = QPushButton("👁")
        self.show_password_button.setFixedWidth(30)
        self.show_password_button.clicked.connect(self.toggle_password_visibility)
        self.show_password_button.setStyleSheet("background-color: #dcdcdc; border-radius: 5px;")
        password_layout.addWidget(self.show_password_button)
        layout.addLayout(password_layout)

        self.check_button = QPushButton("Sprawdź siłę hasła")
        self.check_button.clicked.connect(self.check_password_strength)
        self.check_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px; padding: 5px;")
        layout.addWidget(self.check_button)

        self.generate_button = QPushButton("Wygeneruj silne hasło")
        self.generate_button.clicked.connect(self.open_generated_password_dialog)
        self.generate_button.setStyleSheet("background-color: #2196F3; color: white; border-radius: 5px; padding: 5px;")
        layout.addWidget(self.generate_button)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setStyleSheet("background-color: #ffffff; border: 1px solid #ccc; border-radius: 5px; padding: 5px;")
        layout.addWidget(self.result_display)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def toggle_password_visibility(self):
        if self.password_input.echoMode() == QLineEdit.Password:
            self.password_input.setEchoMode(QLineEdit.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.Password)

    def check_password_strength(self):
        password = self.password_input.text()
        result, score = self.evaluate_password(password)

        self.result_display.clear()
        self.result_display.setTextColor(QColor("black"))
        self.result_display.append(f"Wynik siły hasła: {score}/100")
        self.result_display.append(f"Klasyfikacja: {self.classify_strength(score)}")
        self.result_display.append("\nSzczegóły:\n")
        self.display_colored_details(result)

    def open_generated_password_dialog(self):
        generated_password = self.generate_password()

        dialog = QDialog(self)
        dialog.setWindowTitle("Wygenerowane Hasło")
        dialog.setStyleSheet("background-color: #ffffff; font-family: Arial; font-size: 14px;")
        dialog.setFixedSize(400, 150)

        layout = QVBoxLayout()

        password_label = QLabel("Wygenerowane hasło:")
        password_label.setStyleSheet("font-size: 14px; font-weight: normal;")
        layout.addWidget(password_label)

        password_display = QLabel(generated_password)
        password_display.setStyleSheet("font-size: 18px; font-weight: bold; color: #4CAF50;")
        layout.addWidget(password_display)

        copy_button = QPushButton("Skopiuj hasło")
        copy_button.setStyleSheet("background-color: #2196F3; color: white; border-radius: 5px; padding: 5px;")
        copy_button.clicked.connect(lambda: self.copy_to_clipboard(generated_password))
        layout.addWidget(copy_button)

        dialog.setLayout(layout)
        dialog.exec()

    def copy_to_clipboard(self, text):
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        QMessageBox.information(self, "Skopiowano", "Hasło zostało skopiowane do schowka.")

    def generate_password(self):
        length = 12
        characters = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
        return ''.join(random.choice(characters) for _ in range(length))

    def evaluate_password(self, password):
        score = 0
        details = []

        # Check length
        if len(password) >= 8:
            score += 20
            details.append(("+ Dobra długość (>= 8 znaków)", True))
        else:
            details.append(("- Zbyt krótkie (< 8 znaków)", False))

        # Check for uppercase and lowercase
        if any(c.islower() for c in password) and any(c.isupper() for c in password):
            score += 20
            details.append(("+ Zawiera małe i wielkie litery", True))
        else:
            details.append(("- Brakuje małych lub wielkich liter", False))

        # Check for digits
        if any(c.isdigit() for c in password):
            score += 20
            details.append(("+ Zawiera cyfry", True))
        else:
            details.append(("- Brakuje cyfr", False))

        # Check for special characters
        if any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in password):
            score += 20
            details.append(("+ Zawiera znaki specjalne", True))
        else:
            details.append(("- Brakuje znaków specjalnych", False))

        # Check for common passwords from file
        try:
            base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
            file_path = os.path.join(base_path, "hasla.txt")
            with open(file_path, "r") as file:
                common_passwords = [line.strip() for line in file]
        except FileNotFoundError:
            common_passwords = []

        if password.lower() in common_passwords:
            details.append(("- Zawiera popularne lub łatwe do odgadnięcia wzorce", False))
        else:
            score += 20
            details.append(("+ Nie zawiera popularnych wzorców", True))

        return details, score

    def display_colored_details(self, details):
        cursor = self.result_display.textCursor()
        for detail, is_positive in details:
            format = QTextCharFormat()
            format.setForeground(QColor("green") if is_positive else QColor("red"))
            cursor.insertText(detail + "\n", format)

    def classify_strength(self, score):
        if score < 40:
            return "Słabe"
        elif score < 70:
            return "Średnie"
        elif score < 90:
            return "Mocne"
        else:
            return "Bardzo mocne"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordStrengthChecker()
    window.show()
    sys.exit(app.exec())
