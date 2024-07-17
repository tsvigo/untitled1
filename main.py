from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

# Создание приложения
app = QApplication([])

# Создание главного виджета
main_widget = QWidget()
main_widget.setWindowTitle('Hello, World App')

# Создание метки с текстом
label = QLabel('Hello, World!')

# Создание компоновки и добавление метки в компоновку
layout = QVBoxLayout()
layout.addWidget(label)

# Установка компоновки для главного виджета
main_widget.setLayout(layout)

# Отображение главного виджета
main_widget.show()

# Запуск приложения
app.exec()
