import sys
import mysql.connector
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, QFormLayout, QDialog, QDialogButtonBox, QSpinBox, QHBoxLayout
import mysql.connector
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QWidget, QTableWidgetItem, QTableWidget
)
from datetime import datetime


class testClassViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"Таблица пробных занятий")
        self.setGeometry(500, 450, 1050, 600)
        self.init_ui()

    def init_ui(self):
        # Таблица для отображения данных
        self.table_widget = QTableWidget(self)

        # Поле ввода для поиска по ФИО хореографа
        self.fio_input = QLineEdit(self)
        self.fio_input.setPlaceholderText("Введите ФИО хореографа")

        # Кнопка поиска
        self.search_button = QPushButton("Поиск", self)
        self.search_button.clicked.connect(self.search_by_fio)

        # Размещение виджетов
        layout = QVBoxLayout()
        layout.addWidget(self.fio_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.table_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Загрузка данных из таблицы при запуске
        self.load_table_data()

    def connect_to_database(self):
        """Подключение к базе данных."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Замените на свой логин
                database="db"  # Замените на имя базы данных
            )
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных:\n{err}")
            return None

    def load_table_data(self, fio=None):
        """Загрузка данных из указанной таблицы с фильтрацией по ФИО хореографа (если предоставлено)."""
        connection = self.connect_to_database()
        if not connection:
            return

        try:
            cursor = connection.cursor()

            # Если введено ФИО, фильтруем данные по ФИО хореографа
            if fio:
                query = f"""
                    SELECT testClass.NumberOfClass AS 'Номер группы', 
                           testClass.IdChoreographer AS 'Номер хореографа', 
                           Choreographer.Fio AS 'ФИО хореографа', 
                           testClass.DateOfClass AS 'Дата занятия', 
                           testClass.TimeOfClass AS 'Время занятия'
                    FROM testClass
                    JOIN Choreographer ON testClass.IdChoreographer = Choreographer.IdChoreographer
                    WHERE Choreographer.Fio LIKE %s
                """
                cursor.execute(query, ('%' + fio + '%',))  # Используем LIKE для поиска по части ФИО
            else:
                query = f"""
                    SELECT testClass.NumberOfClass AS 'Номер группы', 
                           testClass.IdChoreographer AS 'Номер хореографа', 
                           Choreographer.Fio AS 'ФИО хореографа', 
                           testClass.DateOfClass AS 'Дата занятия', 
                           testClass.TimeOfClass AS 'Время занятия'
                    FROM testClass
                    JOIN Choreographer ON testClass.IdChoreographer = Choreographer.IdChoreographer
                """
                cursor.execute(query)

            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(columns))
            self.table_widget.setHorizontalHeaderLabels(columns)

            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы testClass:\n{err}")
        finally:
            cursor.close()
            connection.close()

    def search_by_fio(self):
        """Поиск по ФИО хореографа."""
        fio = self.fio_input.text().strip()

        if not fio:
            QMessageBox.warning(self, "Ошибка ввода", "Пожалуйста, введите ФИО хореографа для поиска!")
            return

        self.load_table_data(fio)  # Загрузка данных по введенному ФИО


class GrouppaViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"Таблица пробных занятий")
        self.setGeometry(500, 450, 1050, 600)
        self.init_ui()

    def init_ui(self):
        # Таблица для отображения данных
        self.table_widget = QTableWidget(self)

        # Поле ввода для ID хореографа и кнопка поиска
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Введите ID хореографа")
        self.search_button = QPushButton("Поиск", self)
        self.search_button.clicked.connect(self.search_by_choreographer)

        layout = QVBoxLayout()
        layout.addWidget(self.search_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.table_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Загрузка всех данных при первом запуске
        self.load_table_data()

    def connect_to_database(self):
        """Подключение к базе данных."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Замените на свой логин
                database="db"  # Замените на имя базы данных
            )
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных:\n{err}")
            return None

    def load_table_data(self, choreographer_id=None):
        """Загрузка данных из таблицы с возможностью фильтрации по ID хореографа."""
        connection = self.connect_to_database()
        if not connection:
            return

        try:
            cursor = connection.cursor()

            # Если ID хореографа предоставлен, фильтруем по нему
            if choreographer_id:
                query = f"SELECT * FROM Grouppa WHERE IdChoreographer = %s"
                cursor.execute(query, (choreographer_id,))
            else:
                # Без фильтрации
                query = "SELECT * FROM Grouppa"
                cursor.execute(query)

            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(columns))
            self.table_widget.setHorizontalHeaderLabels(columns)

            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы Grouppa:\n{err}")
        finally:
            cursor.close()
            connection.close()

    def search_by_choreographer(self):
        """Поиск по ID хореографа."""
        choreographer_id = self.search_input.text()

        if not choreographer_id.isdigit():
            QMessageBox.warning(self, "Ошибка ввода", "Пожалуйста, введите корректный ID хореографа!")
            return

        self.load_table_data(choreographer_id)

class ScheduleViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"Таблица расписания")
        self.setGeometry(800, 400, 600, 400)
        self.init_ui()

    def init_ui(self):
        # Таблица для отображения данных
        self.table_widget = QTableWidget(self)

        # Поле ввода для номера группы и кнопка поиска
        self.group_input = QLineEdit(self)
        self.group_input.setPlaceholderText("Введите номер группы")
        self.search_button = QPushButton("Поиск", self)
        self.search_button.clicked.connect(self.search_by_group)

        layout = QVBoxLayout()
        layout.addWidget(self.group_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.table_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Загрузка всех данных при первом запуске
        self.load_table_data()

    def connect_to_database(self):
        """Подключение к базе данных."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Замените на свой логин
                database="db"  # Замените на имя базы данных
            )
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных:\n{err}")
            return None

    def load_table_data(self, group=None):
        """Загрузка данных из таблицы с возможностью фильтрации по номеру группы."""
        connection = self.connect_to_database()
        if not connection:
            return

        try:
            cursor = connection.cursor()

            # Если номер группы предоставлен, фильтруем по нему
            if group:
                query = f"SELECT * FROM Schedule WHERE NumberOfGroup = %s"
                cursor.execute(query, (group,))
            else:
                # Без фильтрации
                query = "SELECT * FROM Schedule"
                cursor.execute(query)

            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(columns))
            self.table_widget.setHorizontalHeaderLabels(columns)

            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы Schedule:\n{err}")
        finally:
            cursor.close()
            connection.close()

    def search_by_group(self):
        """Поиск по номеру группы."""
        group = self.group_input.text()

        if not group.isdigit():
            QMessageBox.warning(self, "Ошибка ввода", "Пожалуйста, введите корректный номер группы!")
            return

        self.load_table_data(group)  # Загрузка данных по номеру группы

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно")
        self.setGeometry(800, 400, 300, 200)
        self.init_ui()

    def init_ui(self):
        # Создание кнопок
        self.button1 = QPushButton("Смотреть расписание", self)
        self.button2 = QPushButton("Смотреть пробные занятия", self)
        self.button3 = QPushButton("Смотреть списки групп", self)

        # Привязка сигналов (обработчиков событий)
        self.button1.clicked.connect(self.button1_action)
        self.button2.clicked.connect(self.button2_action)
        self.button3.clicked.connect(self.button3_action)

        # Макет
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        # Виджет контейнера
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def button1_action(self):
        self.DBW = ScheduleViewer()
        self.DBW.show()

    def button2_action(self):
        self.TCW = testClassViewer()
        self.TCW.show()

    def button3_action(self):
        self.GW = GrouppaViewer()
        self.GW.show()
class AdminView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно входа")
        self.setGeometry(800, 400, 300, 200)
        self.init_ui()

    def init_ui(self):
        # Создание кнопок
       self.button1 = QPushButton("абонементы", self)
       self.button2 = QPushButton("группы", self)
       self.button3 = QPushButton("список клиентов", self)
       self.button4 = QPushButton("записи на пробные занятия", self)
       self.button5 = QPushButton("пробные занятия", self)
       self.button6 = QPushButton("продажи", self)
       self.button7 = QPushButton("расписание", self)
       self.button8 = QPushButton("товары", self)
       self.button9 = QPushButton("списки хореографов", self)
       self.button10 = QPushButton("списки участников групп", self)
       # Привязка сигналов (обработчиков событий)
       self.button1.clicked.connect(self.open_subscription_window)
       self.button2.clicked.connect(self.open_groups_window)
       self.button3.clicked.connect(self.open_clients_window)
       self.button4.clicked.connect(self.open_records_window)
       self.button5.clicked.connect(self.open_trials_window)
       self.button6.clicked.connect(self.open_sales_window)
       self.button7.clicked.connect(self.open_schedule_window)
       self.button8.clicked.connect(self.open_products_window)
       self.button9.clicked.connect(self.open_choreographers_window)
       self.button10.clicked.connect(self.open_participants_window)
       # Макет
       layout = QVBoxLayout()
       layout.addWidget(self.button1)
       layout.addWidget(self.button2)
       layout.addWidget(self.button3)
       layout.addWidget(self.button4)
       layout.addWidget(self.button5)
       layout.addWidget(self.button6)
       layout.addWidget(self.button7)
       layout.addWidget(self.button8)
       layout.addWidget(self.button9)
       layout.addWidget(self.button10)

       # Виджет контейнера
       container = QWidget()
       container.setLayout(layout)
       self.setCentralWidget(container)

    def open_subscription_window(self):
        self.subscription_window = SubscriptionWindow()
        self.subscription_window.show()
    def open_groups_window(self):
        self.groups_window = GroupsWindow()
        self.groups_window.show()
    def open_clients_window(self):
        self.clients_window = ClientsWindow()
        self.clients_window.show()
    def open_records_window(self):
        self.records_window = RecordsWindow()
        self.records_window.show()
    def open_trials_window(self):
        self.trials_window = TrialsWindow()
        self.trials_window.show()
    def open_sales_window(self):
        self.sales_window = SalesWindow()
        self.sales_window.show()
    def open_schedule_window(self):
        self.schedule_window = ScheduleWindow()
        self.schedule_window.show()
    def open_products_window(self):
        self.products_window = ProductsWindow()
        self.products_window.show()
    def open_choreographers_window(self):
        self.choreographers_window = ChoreographersWindow()
        self.choreographers_window.show()
    def open_participants_window(self):
        self.participants_window = ParticipantsWindow()
        self.participants_window.show()


# Классы для окон
class SubscriptionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Абонементы")
        self.setGeometry(500, 450, 1050, 600)
        label = QLabel("Окно с информацией об абонементах", self)
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.load_table_data()

        self.table_widget.cellChanged.connect(self.on_cell_changed)

    def connect_to_database(self):
        """Подключение к базе данных."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Замените на свой логин
                database="db"  # Замените на имя базы данных
            )
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных:\n{err}")
            return None

    def load_table_data(self):
        """Загрузка данных из указанной таблицы."""
        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()
            query = f"SELECT * FROM Subscription "
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(columns))
            self.table_widget.setHorizontalHeaderLabels(columns)
            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы:\n{err}")
        finally:
            cursor.close()
            connection.close()

    def on_cell_changed(self, row, column):
        """Обработчик изменения данных в ячейке таблицы."""
        new_value = self.table_widget.item(row, column).text()
        column_name = self.table_widget.horizontalHeaderItem(column).text()
        row_id = self.table_widget.item(row, 0).text()  # Предполагаем, что первый столбец - это ID записи

        # Обновляем значение в базе данных
        self.update_database(row_id, column_name, new_value)

    def update_database(self, row_id, column_name, new_value):
        """Обновление данных в базе данных."""
        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()
            query = f"UPDATE Subscription SET {column_name} = %s WHERE id_Sub = %s"
            cursor.execute(query, (new_value, row_id))
            connection.commit()
            QMessageBox.information(self, "Успех", "Данные обновлены успешно!")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось обновить данные в базе:\n{err}")
        finally:
            cursor.close()
            connection.close()


class GroupsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Группы")
        self.setGeometry(500, 450, 1050, 600)

        # Лейбл
        label = QLabel("Окно с информацией о группах", self)
        self.table_widget = QTableWidget(self)

        # Поля для добавления группы
        self.input_number = QLineEdit(self)
        self.input_number.setPlaceholderText("Номер группы")

        self.input_choreographer = QLineEdit(self)
        self.input_choreographer.setPlaceholderText("ID хореографа")

        self.input_dance_style = QLineEdit(self)
        self.input_dance_style.setPlaceholderText("Танцевальный стиль")

        self.add_button = QPushButton("Добавить группу")
        self.add_button.clicked.connect(self.add_group)

        # Макет для отображения таблицы и ввода данных
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
        layout.addWidget(QLabel("Добавить новую группу:"))
        layout.addWidget(self.input_number)
        layout.addWidget(self.input_choreographer)
        layout.addWidget(self.input_dance_style)
        layout.addWidget(self.add_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Загрузка данных из таблицы
        self.load_table_data()

    def connect_to_database(self):
        """Подключение к базе данных."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Замените на свой логин
                database="db"  # Замените на имя базы данных
            )
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных:\n{err}")
            return None

    def load_table_data(self):
        """Загрузка данных из таблицы Grouppa."""
        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()
            query = 'SELECT Grouppa.NumberOfGroup AS "Номер группы", Choreographer.Fio AS "ФИО Хореографа", Grouppa.IdChoreographer AS "Номер хореографа", Grouppa.DanceStyle as "Стиль танца"FROM Grouppa JOIN Choreographer ON Grouppa.IdChoreographer = Choreographer.IdChoreographer;'
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(columns))
            self.table_widget.setHorizontalHeaderLabels(columns)
            '''custom_columns = ["Номер группы", "Номер хореографа", "Стиль танца"]
            self.table_widget.setHorizontalHeaderLabels(custom_columns)'''
            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы Grouppa:\n{err}")
        finally:
            cursor.close()
            connection.close()

    def add_group(self):
        """Добавление новой группы в таблицу Grouppa."""
        number_of_group = self.input_number.text()
        id_choreographer = self.input_choreographer.text()
        dance_style = self.input_dance_style.text()

        if not number_of_group or not id_choreographer or not dance_style:
            QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены!")
            return

        connection = self.connect_to_database()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = "INSERT INTO Grouppa (NumberOfGroup, IdChoreographer, DanceStyle) VALUES (%s, %s, %s)"
            cursor.execute(query, (number_of_group, id_choreographer, dance_style))
            connection.commit()

            QMessageBox.information(self, "Успех", "Группа успешно добавлена!")
            self.load_table_data()  # Обновить данные в таблице
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить группу:\n{err}")
        finally:
            cursor.close()
            connection.close()


class ClientsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Клиенты")
        self.setGeometry(500, 450, 1050, 600)
        self.init_ui()
        self.load_table_data()

    def init_ui(self):
        """Инициализация пользовательского интерфейса."""
        # Таблица для отображения данных
        self.table_widget = QTableWidget(self)

        # Поля ввода
        self.input_id = QLineEdit(self)
        self.input_id.setPlaceholderText("ID клиента")
        self.input_fio = QLineEdit(self)
        self.input_fio.setPlaceholderText("ФИО")
        self.input_birthday = QLineEdit(self)
        self.input_birthday.setPlaceholderText("Дата рождения (YYYY-MM-DD)")
        self.input_gender = QLineEdit(self)
        self.input_gender.setPlaceholderText("Пол (M/Ж)")
        self.input_phone = QLineEdit(self)
        self.input_phone.setPlaceholderText("Телефон")

        # Кнопка добавления
        self.button_add = QPushButton("Добавить клиента", self)
        self.button_add.clicked.connect(self.add_client)

        # Макет
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Окно с информацией о клиентах", self))
        layout.addWidget(self.table_widget)
        layout.addWidget(QLabel("Добавить клиента:"))
        layout.addWidget(self.input_id)
        layout.addWidget(self.input_fio)
        layout.addWidget(self.input_birthday)
        layout.addWidget(self.input_gender)
        layout.addWidget(self.input_phone)
        layout.addWidget(self.button_add)

        # Главный контейнер
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Подключаем обработчик изменения данных в таблице
        self.table_widget.cellChanged.connect(self.on_cell_changed)

    def connect_to_database(self):
        """Подключение к базе данных."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Замените на свой логин
                database="db"  # Замените на имя базы данных
            )
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных:\n{err}")
            return None

    def load_table_data(self):
        """Загрузка данных из таблицы Client."""
        # Отключаем обработчик на время загрузки данных
        self.table_widget.cellChanged.disconnect(self.on_cell_changed)

        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM Client"
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            custom_columns = ["Номер пользователя", "Фио", "Дата рождения", "Пол", "Номер телефона"]
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(columns))
            self.table_widget.setHorizontalHeaderLabels(columns)

            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы Client:\n{err}")
        finally:
            cursor.close()
            connection.close()

        # Включаем обработчик обратно после загрузки данных
        self.table_widget.cellChanged.connect(self.on_cell_changed)

    def add_client(self):
        """Добавление клиента в таблицу Client."""
        client_id = self.input_id.text()
        fio = self.input_fio.text()
        birthday = self.input_birthday.text()
        gender = self.input_gender.text()
        phone = self.input_phone.text()

        if not client_id or not fio or not birthday or not gender or not phone:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля!")
            return
        if gender != "М" and gender != "Ж":  # UPDATE
            QMessageBox.warning(self, "Ошибка", "Указывайте Ж или М в строке пола")
            return

        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()

            # Проверка, существует ли уже клиент с таким ID
            query_check = "SELECT ClientId FROM Client WHERE ClientId = %s"
            cursor.execute(query_check, (client_id,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Ошибка", "Клиент с таким ID уже существует!")
                return

            # Добавление нового клиента
            query_insert = """
                INSERT INTO Client (ClientId, FIO, birtday, Gender, Phone)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query_insert, (client_id, fio, birthday, gender, phone))
            connection.commit()

            QMessageBox.information(self, "Успех", "Клиент успешно добавлен!")
            self.load_table_data()  # Обновить таблицу после добавления
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить клиента:\n{err}")
        finally:
            cursor.close()
            connection.close()
            # Очистка полей ввода
            self.input_id.clear()
            self.input_fio.clear()
            self.input_birthday.clear()
            self.input_gender.clear()
            self.input_phone.clear()

    def on_cell_changed(self, row, column):
        """Обработчик изменения данных в ячейке таблицы."""
        new_value = self.table_widget.item(row, column).text()
        column_name = self.table_widget.horizontalHeaderItem(column).text()
        client_id = self.table_widget.item(row, 0).text()  # Предполагаем, что первый столбец - это ID клиента

        # Обновляем значение в базе данных
        self.update_database(client_id, column_name, new_value)

    def update_database(self, client_id, column_name, new_value):
        """Обновление данных в базе данных."""
        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()
            query = f"UPDATE Client SET {column_name} = %s WHERE ClientId = %s"
            cursor.execute(query, (new_value, client_id))
            connection.commit()
            QMessageBox.information(self, "Успех", "Данные обновлены успешно!")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось обновить данные в базе:\n{err}")
        finally:
            cursor.close()
            connection.close()


class RecordsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Записи")
        self.setGeometry(500, 450, 1050, 600)

        # Лейбл
        label = QLabel("Окно с информацией о записях", self)
        self.table_widget = QTableWidget(self)

        # Поля для записи на пробное занятие
        self.input_number = QLineEdit(self)
        self.input_number.setPlaceholderText("Номер занятия")

        self.input_client_id = QLineEdit(self)
        self.input_client_id.setPlaceholderText("ID клиента")

        # Кнопка для записи на пробное занятие
        self.add_button = QPushButton("Записать на пробное занятие")
        self.add_button.clicked.connect(self.add_record)

        # Поле для поиска
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Поиск по номеру занятия или ФИО клиента")
        self.search_input.textChanged.connect(self.search_records)

        # Макет для отображения таблицы и ввода данных
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.search_input)  # Добавляем поле поиска
        layout.addWidget(self.table_widget)
        layout.addWidget(QLabel("Записать клиента на пробное занятие:"))
        layout.addWidget(self.input_number)
        layout.addWidget(self.input_client_id)
        layout.addWidget(self.add_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Загрузка данных из представления
        self.load_table_data()

    def connect_to_database(self):
        """Подключение к базе данных."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Замените на свой логин
                database="db"  # Замените на имя базы данных
            )
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных:\n{err}")
            return None

    def load_table_data(self, search_query=""):
        """Загрузка данных из представления cl_rec с возможностью фильтрации по запросу."""
        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()

            # Если поисковый запрос не пустой, фильтруем по номеру занятия или ФИО клиента
            if search_query:
                query = """
                    SELECT FIO as "ФИО пользователя", NumberOfClass AS "Номер группы" 
                    FROM cl_rec
                    WHERE cl_rec.FIO LIKE %s
                """
                search_query = f"%{search_query}%"  # Форматируем запрос для LIKE
                cursor.execute(query, (search_query,))  # Параметризованный запрос, передаем search_query как кортеж
            else:
                # Без фильтрации
                query = """
                    SELECT FIO as "ФИО пользователя", NumberOfClass AS "Номер группы" 
                    FROM cl_rec
                """
                cursor.execute(query)

            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(columns))
            self.table_widget.setHorizontalHeaderLabels(columns)

            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из представления cl_rec:\n{err}")
        finally:
            cursor.close()
            connection.close()

    def add_record(self):
        """Добавление записи клиента на пробное занятие в таблицу ClientRecord."""
        number_of_class = self.input_number.text()
        client_id = self.input_client_id.text()

        if not number_of_class or not client_id:
            QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены!")
            return

        connection = self.connect_to_database()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = "INSERT INTO ClientRecord (NumberOfClass, ClientId) VALUES (%s, %s)"
            cursor.execute(query, (number_of_class, client_id))
            connection.commit()

            QMessageBox.information(self, "Успех", "Клиент успешно записан на пробное занятие!")
            self.load_table_data()  # Обновить данные в представлении
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось записать клиента в таблицу ClientRecord:\n{err}")
        finally:
            cursor.close()
            connection.close()

    def search_records(self):
        """Функция для фильтрации данных по введенному запросу в поисковое поле."""
        search_query = self.search_input.text()
        self.load_table_data(search_query)


class TrialsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пробные")
        self.setGeometry(500, 450, 1050, 600)

        # Лейбл
        label = QLabel("Окно с информацией о пробных занятиях", self)
        self.table_widget = QTableWidget(self)

        # Поля для добавления тестового занятия
        self.input_number = QLineEdit(self)
        self.input_number.setPlaceholderText("Номер занятия")

        self.input_choreographer = QLineEdit(self)
        self.input_choreographer.setPlaceholderText("ID хореографа")

        self.input_date = QLineEdit(self)
        self.input_date.setPlaceholderText("Дата занятия (ГГГГ-ММ-ДД)")

        self.input_time = QLineEdit(self)
        self.input_time.setPlaceholderText("Время занятия (ЧЧ:ММ)")

        # Кнопка для добавления пробного занятия
        self.add_button = QPushButton("Добавить пробное занятие")
        self.add_button.clicked.connect(self.add_trial_class)

        # Поле для поиска
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Поиск по ФИО хореографа")
        self.search_input.textChanged.connect(self.search_trial_classes)

        # Макет для отображения таблицы и ввода данных
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.search_input)  # Добавим поле для поиска
        layout.addWidget(self.table_widget)
        layout.addWidget(QLabel("Добавить новое пробное занятие:"))
        layout.addWidget(self.input_number)
        layout.addWidget(self.input_choreographer)
        layout.addWidget(self.input_date)
        layout.addWidget(self.input_time)
        layout.addWidget(self.add_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Загрузка данных из таблицы
        self.load_table_data()

    def connect_to_database(self):
        """Подключение к базе данных."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Замените на свой логин
                database="db"  # Замените на имя базы данных
            )
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных:\n{err}")
            return None

    def load_table_data(self, search_query=""):
        """Загрузка данных из таблицы testClass с возможностью фильтрации по запросу."""
        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()

            # Если поисковый запрос не пустой, фильтруем по номеру занятия или ФИО хореографа
            if search_query:
                query = f"""
                    SELECT testClass.NumberOfClass AS 'Номер группы', testClass.IdChoreographer AS 'Номер хореографа', 
                           Choreographer.Fio AS 'ФИО хореографа', testClass.DateOfClass AS 'Дата занятия', 
                           testClass.TimeOfClass AS 'Время занятия' 
                    FROM testClass 
                    JOIN Choreographer ON testClass.IdChoreographer = Choreographer.IdChoreographer
                    WHERE testClass.NumberOfClass LIKE %s OR Choreographer.Fio LIKE %s
                """
                search_query = f"%{search_query}%"  # Форматируем запрос для LIKE
                cursor.execute(query, (search_query, search_query))
            else:
                # Без фильтрации
                query = f"""
                    SELECT testClass.NumberOfClass AS 'Номер группы', testClass.IdChoreographer AS 'Номер хореографа', 
                           Choreographer.Fio AS 'ФИО хореографа', testClass.DateOfClass AS 'Дата занятия', 
                           testClass.TimeOfClass AS 'Время занятия' 
                    FROM testClass 
                    JOIN Choreographer ON testClass.IdChoreographer = Choreographer.IdChoreographer
                """
                cursor.execute(query)

            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(columns))
            self.table_widget.setHorizontalHeaderLabels(columns)

            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы testClass:\n{err}")
        finally:
            cursor.close()
            connection.close()

    def add_trial_class(self):
        """Добавление нового пробного занятия в таблицу testClass."""
        number_of_class = self.input_number.text()
        id_choreographer = self.input_choreographer.text()
        date_of_class = self.input_date.text()
        time_of_class = self.input_time.text()

        if not number_of_class or not id_choreographer or not date_of_class or not time_of_class:
            QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены!")
            return

        connection = self.connect_to_database()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = "INSERT INTO testClass (NumberOfClass, IdChoreographer, DateOfClass, TimeOfClass) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (number_of_class, id_choreographer, date_of_class, time_of_class))
            connection.commit()

            QMessageBox.information(self, "Успех", "Пробное занятие успешно добавлено!")
            self.load_table_data()  # Обновить данные в таблице
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить пробное занятие:\n{err}")
        finally:
            cursor.close()
            connection.close()

    def search_trial_classes(self):
        """Функция для фильтрации данных по введенному запросу в поисковое поле."""
        search_query = self.search_input.text()
        self.load_table_data(search_query)



class SalesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Продажи")
        self.setGeometry(500, 450, 1050, 600)

        # Создаем виджеты
        label = QLabel("Окно с информацией о продажах", self)
        self.table_widget = QTableWidget(self)
        self.add_sale_button = QPushButton("Продажа товара", self)

        # Создаем layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
        layout.addWidget(self.add_sale_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Привязываем обработчик события для кнопки
        self.add_sale_button.clicked.connect(self.add_sale)

        # Загрузка данных из таблицы продаж
        self.load_table_data()



class SalesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Продажи")
        self.setGeometry(500, 450, 1050, 600)
        # Создаем виджеты
        label = QLabel("Окно с информацией о продажах", self)
        self.table_widget = QTableWidget(self)
        self.add_sale_button = QPushButton("Продажа товара", self)
        # Создаем layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
        layout.addWidget(self.add_sale_button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        # Привязываем обработчик события для кнопки
        self.add_sale_button.clicked.connect(self.add_sale)
        # Загрузка данных из таблицы продаж
        self.load_table_data()
    def connect_to_database(self):
        """Подключение к базе данных."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Замените на свой логин
                database="db"  # Замените на имя базы данных
            )
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных:\n{err}")
            return None
    def load_table_data(self):
        """Загрузка данных из указанной таблицы продаж."""
        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()
            query = 'select sale.NumberOfDeal AS "Номер сделки", sale.Id_product AS "Номер продукта", Item.Item_name AS "Название товара", sale.ClientId AS "Номер клиента", Client.FIO AS "ФИО клиента", Sale.SaledCount AS "Кол-во продаж", sale.DateOfDeal AS "Кол-во продаж"FROM sale JOIN item ON sale.Id_product = Item.Product_ID JOIN Client ON sale.ClientId = Client.ClientId;'
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(columns))
            self.table_widget.setHorizontalHeaderLabels(columns)
            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы sale:\n{err}")
        finally:
            cursor.close()
            connection.close()
    def add_sale(self):
        """Открытие диалогового окна для добавления продажи."""
        dialog = AddSaleDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            id_product = dialog.id_product.text()
            client_id = dialog.client_id.text()
            saled_count = dialog.saled_count.value()
            self.insert_sale_to_db(id_product, client_id, saled_count)
            self.load_table_data()  # Обновить таблицу после добавления продажи

    def insert_sale_to_db(self, id_product, client_id, saled_count):
        """Вставка данных о продаже в таблицу sale и уменьшение количества оставшихся товаров в таблице Item."""
        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()

            # Получаем следующий номер сделки (если он автоинкрементный, этот шаг не нужен)
            cursor.execute("SELECT MAX(NumberOfDeal) FROM sale")
            max_number_of_deal = cursor.fetchone()[0]
            next_number_of_deal = max_number_of_deal + 1 if max_number_of_deal is not None else 1

            # Вставка данных о продаже в таблицу sale
            query_sale = """INSERT INTO sale (NumberOfDeal, Id_product, ClientId, SaledCount, DateOfDeal)
                            VALUES (%s, %s, %s, %s, CURDATE())"""
            cursor.execute(query_sale, (next_number_of_deal, id_product, client_id, saled_count))

            # Уменьшение количества оставшихся товаров в таблице Item
            query_item_update = """UPDATE Item SET NumberOfRemaining = NumberOfRemaining - %s WHERE Product_ID = %s"""
            cursor.execute(query_item_update, (saled_count, id_product))

            # Подтверждение изменений в базе данных
            connection.commit()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка добавления продажи", f"Не удалось добавить запись о продаже:\n{err}")
        finally:
            cursor.close()
            connection.close()


class AddSaleDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить продажу")
        # Создаем виджеты для ввода данных
        self.id_product = QLineEdit(self)
        self.id_product.setPlaceholderText("Введите ID товара")
        self.client_id = QLineEdit(self)
        self.client_id.setPlaceholderText("Введите ID клиента")
        self.saled_count = QSpinBox(self)
        self.saled_count.setRange(1, 1000)
        self.saled_count.setPrefix("Количество: ")
        # Layout для формы
        layout = QFormLayout()
        layout.addRow("ID товара:", self.id_product)
        layout.addRow("ID клиента:", self.client_id)
        layout.addRow("Количество:", self.saled_count)
        # Кнопки для подтверждения или отмены
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        self.setLayout(layout)


class AddSaleDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить продажу")

        # Создаем виджеты для ввода данных
        self.id_product = QLineEdit(self)
        self.id_product.setPlaceholderText("Введите ID товара")

        self.client_id = QLineEdit(self)
        self.client_id.setPlaceholderText("Введите ID клиента")

        self.saled_count = QSpinBox(self)
        self.saled_count.setRange(1, 1000)
        self.saled_count.setPrefix("Количество: ")

        # Layout для формы
        layout = QFormLayout()
        layout.addRow("ID товара:", self.id_product)
        layout.addRow("ID клиента:", self.client_id)
        layout.addRow("Количество:", self.saled_count)

        # Кнопки для подтверждения или отмены
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)
        self.setLayout(layout)


class ScheduleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Расписание")
        self.setGeometry(500, 450, 1050, 600)

        # Метка и таблица для отображения расписания
        label = QLabel("Окно с информацией о расписании", self)
        self.table_widget = QTableWidget(self)

        # Ввод данных для нового расписания
        self.group_input = QLineEdit(self)
        self.date_input = QLineEdit(self)
        self.time_input = QLineEdit(self)
        self.add_button = QPushButton("Добавить", self)
        self.delete_button = QPushButton("Удалить", self)

        # Поле для фильтрации по номеру группы
        self.filter_group_input = QLineEdit(self)
        self.filter_group_input.setPlaceholderText("Фильтр по номеру группы")
        self.filter_button = QPushButton("Применить фильтр", self)
        self.filter_button.clicked.connect(self.load_table_data)

        # Подключаем действия к кнопкам
        self.add_button.clicked.connect(self.add_schedule)
        self.delete_button.clicked.connect(self.delete_schedule)

        # Расположение виджетов
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)

        # Создание горизонтального макета для ввода нового расписания
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Номер группы:", self))
        input_layout.addWidget(self.group_input)
        input_layout.addWidget(QLabel("Дата занятия:", self))
        input_layout.addWidget(self.date_input)
        input_layout.addWidget(QLabel("Время занятия:", self))
        input_layout.addWidget(self.time_input)
        input_layout.addWidget(self.add_button)
        input_layout.addWidget(self.delete_button)

        # Добавление поля для фильтрации
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Фильтр по номеру группы:", self))
        filter_layout.addWidget(self.filter_group_input)
        filter_layout.addWidget(self.filter_button)

        layout.addLayout(input_layout)
        layout.addLayout(filter_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Загрузка данных в таблицу
        self.load_table_data()

    def connect_to_database(self):
        """Подключение к базе данных."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Замените на свой логин
                database="db"  # Замените на имя базы данных
            )
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных:\n{err}")
            return None

    def load_table_data(self):
        """Загрузка данных из указанной таблицы с фильтрацией по номеру группы."""
        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()

            # Получаем значение для фильтрации
            group_filter = self.filter_group_input.text()

            # Если фильтр не пустой, добавляем условие WHERE
            if group_filter:
                query = """
                    SELECT Schedule.Id_Schedule AS "Номер расписания", Schedule.NumberOfGroup AS "Номер группы", 
                           Schedule.DateOfClass AS "Дата занятия", Schedule.TimeOfClass AS "Время занятия" 
                    FROM Schedule
                    WHERE Schedule.NumberOfGroup = %s
                """
                cursor.execute(query, (group_filter,))
            else:
                # Без фильтрации
                query = """
                    SELECT Schedule.Id_Schedule AS "Номер расписания", Schedule.NumberOfGroup AS "Номер группы", 
                           Schedule.DateOfClass AS "Дата занятия", Schedule.TimeOfClass AS "Время занятия" 
                    FROM Schedule
                """
                cursor.execute(query)

            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(columns))
            self.table_widget.setHorizontalHeaderLabels(columns)
            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы:\n{err}")
        finally:
            cursor.close()
            connection.close()

    def add_schedule(self):
        """Добавление нового расписания в базу данных."""
        group = self.group_input.text()
        date = self.date_input.text()
        time = self.time_input.text()

        if not group or not date or not time:
            QMessageBox.warning(self, "Ошибка ввода", "Пожалуйста, заполните все поля!")
            return

        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()
            query = "INSERT INTO Schedule (NumberOfGroup, DateOfClass, TimeOfClass) VALUES (%s, %s, %s)"
            cursor.execute(query, (group, date, time))
            connection.commit()
            QMessageBox.information(self, "Успех", "Расписание успешно добавлено!")
            self.load_table_data()  # Обновить данные в таблице
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить расписание:\n{err}")
        finally:
            cursor.close()
            connection.close()

    def delete_schedule(self):
        """Удаление выбранного расписания из базы данных."""
        selected_row = self.table_widget.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите строку для удаления!")
            return

        schedule_id = self.table_widget.item(selected_row, 0).text()  # ID расписания в первом столбце

        confirmation = QMessageBox.question(self, "Подтверждение", f"Вы уверены, что хотите удалить расписание с номером {schedule_id}?", QMessageBox.Yes | QMessageBox.No)
        if confirmation == QMessageBox.No:
            return

        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()
            query = "DELETE FROM Schedule WHERE Id_Schedule = %s"
            cursor.execute(query, (schedule_id,))
            connection.commit()
            QMessageBox.information(self, "Удаление", f"Расписание с номером {schedule_id} успешно удалено!")
            self.load_table_data()  # Обновить данные в таблице
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось удалить расписание:\n{err}")
        finally:
            cursor.close()
            connection.close()





class ProductsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Товары")
        self.setGeometry(500, 450, 1050, 600)

        # Создаем виджеты
        label = QLabel("Окно с информацией о товарах", self)
        self.table_widget = QTableWidget(self)
        self.add_button = QPushButton("Добавить товар", self)

        # Создаем layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
        layout.addWidget(self.add_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Привязываем обработчик события для кнопки
        self.add_button.clicked.connect(self.add_product)

        # Загрузка данных из таблицы
        self.load_table_data()

    def connect_to_database(self):
        """Подключение к базе данных."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Замените на свой логин
                database="db"  # Замените на имя базы данных
            )
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных:\n{err}")
            return None

    def load_table_data(self):
        """Загрузка данных из указанной таблицы."""
        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()
            query = f'SELECT Item.Product_ID AS "Номер товара", Item.Item_name AS "Назвние" ,Item.Price AS "Цена", Item.NumberOfRemaining AS "Сколько осталось"FROM Item;'
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(columns))
            self.table_widget.setHorizontalHeaderLabels(columns)
            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы Item:\n{err}")
        finally:
            cursor.close()
            connection.close()

    def add_product(self):
        """Открытие диалогового окна для добавления товара."""
        dialog = AddProductDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            product_id = dialog.product_id.text()
            price = dialog.price.value()
            availability = dialog.availability.text()
            remaining = dialog.remaining.value()
            self.insert_product_to_db(product_id, price, availability, remaining)
            self.load_table_data()  # Обновить таблицу после добавления товара

    def insert_product_to_db(self, product_id, price, availability, remaining):
        """Вставка нового товара в базу данных."""
        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()
            query = """INSERT INTO Item (Product_ID, Price, ProductAvailability, NumberOfRemaining)
                       VALUES (%s, %s, %s, %s)"""
            cursor.execute(query, (product_id, price, availability, remaining))
            connection.commit()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка добавления", f"Не удалось добавить товар:\n{err}")
        finally:
            cursor.close()
            connection.close()


class AddProductDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить товар")

        # Создаем виджеты для ввода данных
        self.product_id = QLineEdit(self)
        self.product_id.setPlaceholderText("Введите ID товара")

        self.price = QSpinBox(self)
        self.price.setRange(1, 10000)
        self.price.setPrefix("Цена: ")

        self.availability = QLineEdit(self)
        self.availability.setPlaceholderText("Введите доступность товара")

        self.remaining = QSpinBox(self)
        self.remaining.setRange(0, 1000)
        self.remaining.setPrefix("Осталось: ")

        # Layout для формы
        layout = QFormLayout()
        layout.addRow("ID товара:", self.product_id)
        layout.addRow("Цена:", self.price)
        layout.addRow("Доступность:", self.availability)
        layout.addRow("Осталось:", self.remaining)

        # Кнопки для подтверждения или отмены
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        layout.addWidget(buttons)
        self.setLayout(layout)

class ChoreographersWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Хореографы")
        self.setGeometry(500, 450, 1050, 600)
        self.init_ui()
        self.load_table_data()

    def init_ui(self):
        """Инициализация пользовательского интерфейса."""
        # Таблица для отображения данных
        self.table_widget = QTableWidget(self)

        # Поля ввода
        self.input_id = QLineEdit(self)
        self.input_id.setPlaceholderText("ID хореографа")
        self.input_fio = QLineEdit(self)
        self.input_fio.setPlaceholderText("ФИО")
        self.input_birthday = QLineEdit(self)
        self.input_birthday.setPlaceholderText("Дата рождения (YYYY-MM-DD)")
        self.input_gender = QLineEdit(self)
        self.input_gender.setPlaceholderText("Пол (M/F)")
        self.input_phone = QLineEdit(self)
        self.input_phone.setPlaceholderText("Телефон")
        self.input_experience = QLineEdit(self)
        self.input_experience.setPlaceholderText("Стаж (в годах)")
        self.input_dance_style = QLineEdit(self)
        self.input_dance_style.setPlaceholderText("Стиль танца")
        self.input_password = QLineEdit(self)
        self.input_password.setPlaceholderText("Пароль")

        # Поле ввода для поиска
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Поиск хореографов...")
        self.search_input.textChanged.connect(self.search_choreographers)

        # Кнопка добавления
        self.button_add = QPushButton("Добавить хореографа", self)
        self.button_add.clicked.connect(self.add_choreographer)

        # Макет
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Окно с информацией о хореографах", self))
        layout.addWidget(self.search_input)  # Добавим поле для поиска
        layout.addWidget(self.table_widget)
        layout.addWidget(QLabel("Добавить хореографа:"))
        layout.addWidget(self.input_id)
        layout.addWidget(self.input_fio)
        layout.addWidget(self.input_birthday)
        layout.addWidget(self.input_gender)
        layout.addWidget(self.input_phone)
        layout.addWidget(self.input_experience)
        layout.addWidget(self.input_dance_style)
        layout.addWidget(self.input_password)
        layout.addWidget(self.button_add)

        # Главный контейнер
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def connect_to_database(self):
        """Подключение к базе данных."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Замените на свой логин
                database="db"  # Замените на имя базы данных
            )
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных:\n{err}")
            return None

    def search_choreographers(self):
        """Функция для фильтрации данных по введенному запросу в поисковое поле."""
        search_query = self.search_input.text().strip()  # Убираем лишние пробелы
        self.load_table_data(search_query)

    def load_table_data(self, search_query=""):
        """Загрузка данных из таблицы Choreographer."""
        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()

            if not search_query:  # Если поисковый запрос пустой, загружаем все данные
                query = '''
                    SELECT Choreographer.IdChoreographer AS "Номер хореографа", Choreographer.Fio AS "ФИО", 
                           Choreographer.birthday AS "Дата рождения", Choreographer.Gender AS "Пол", 
                           Choreographer.Phone AS "Номер телефона", Choreographer.Experience AS "Стаж", 
                           Choreographer.DanceStyle AS "Танцевальный стиль", Choreographer.password AS "Пароль" 
                    FROM Choreographer
                '''
            else:  # Если есть поисковый запрос, добавляем фильтрацию
                query = '''
                    SELECT Choreographer.IdChoreographer AS "Номер хореографа", Choreographer.Fio AS "ФИО", 
                           Choreographer.birthday AS "Дата рождения", Choreographer.Gender AS "Пол", 
                           Choreographer.Phone AS "Номер телефона", Choreographer.Experience AS "Стаж", 
                           Choreographer.DanceStyle AS "Танцевальный стиль", Choreographer.password AS "Пароль" 
                    FROM Choreographer 
                    WHERE Choreographer.Fio LIKE %s
                '''
                search_query = f"%{search_query}%"  # Форматируем запрос для LIKE

            cursor.execute(query, (search_query,) if search_query else ())
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]

            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(columns))
            self.table_widget.setHorizontalHeaderLabels(columns)

            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы Choreographer:\n{err}")
        finally:
            cursor.close()
            connection.close()

    def add_choreographer(self):
        """Добавление хореографа в таблицу Choreographer."""
        choreographer_id = self.input_id.text()
        fio = self.input_fio.text()
        birthday = self.input_birthday.text()
        gender = self.input_gender.text()
        phone = self.input_phone.text()
        experience = self.input_experience.text()
        dance_style = self.input_dance_style.text()
        password = self.input_password.text()

        # Проверка на заполненность полей
        if not all([choreographer_id, fio, birthday, gender, phone, experience, dance_style, password]):
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля!")
            return

        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()

            # Проверка, существует ли уже хореограф с таким ID
            query_check = "SELECT IdChoreographer FROM Choreographer WHERE IdChoreographer = %s"
            cursor.execute(query_check, (choreographer_id,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Ошибка", "Хореограф с таким ID уже существует!")
                return

            # Добавление нового хореографа
            query_insert = """
                INSERT INTO Choreographer (IdChoreographer, Fio, Birthday, Gender, Phone, Experience, DanceStyle, Password)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query_insert, (choreographer_id, fio, birthday, gender, phone, experience, dance_style, password))
            connection.commit()

            QMessageBox.information(self, "Успех", "Хореограф успешно добавлен!")
            self.load_table_data()  # Обновить таблицу после добавления
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить хореографа:\n{err}")
        finally:
            cursor.close()
            connection.close()

            # Очистка полей ввода
            self.input_id.clear()
            self.input_fio.clear()
            self.input_birthday.clear()
            self.input_gender.clear()
            self.input_phone.clear()
            self.input_experience.clear()
            self.input_dance_style.clear()
            self.input_password.clear()


class AddParticipantDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавить участника")
        self.setGeometry(600, 400, 300, 200)

        self.layout = QFormLayout()

        self.group_input = QLineEdit()
        self.client_id_input = QLineEdit()

        self.layout.addRow("Номер группы:", self.group_input)
        self.layout.addRow("ID клиента:", self.client_id_input)

        self.add_button = QPushButton("Добавить")
        self.add_button.clicked.connect(self.add_participant)
        self.layout.addWidget(self.add_button)

        self.setLayout(self.layout)
        self.result = None

    def add_participant(self):
        """Сохраняет введенные данные и закрывает диалог."""
        group = self.group_input.text().strip()
        client_id = self.client_id_input.text().strip()

        if not group or not client_id:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля!")
            return

        self.result = (group, client_id)
        self.accept()


class ParticipantsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Участники групп")
        self.setGeometry(500, 450, 1050, 600)

        label = QLabel("Окно с информацией об участниках групп", self)

        self.table_widget = QTableWidget(self)
        self.add_button = QPushButton("Добавить участника")
        self.add_button.clicked.connect(self.open_add_dialog)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
        layout.addWidget(self.add_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.load_table_data()

    def connect_to_database(self):
        """Подключение к базе данных."""
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Замените на свой логин
                database="db"  # Замените на имя базы данных
            )
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных:\n{err}")
            return None

    def load_table_data(self):
        """Загрузка данных из указанной таблицы."""
        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()
            query = "SELECT DanceStyle AS 'Танцевальный стиль', FIO AS 'ФИО' from group_fio"
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(columns))
            self.table_widget.setHorizontalHeaderLabels(columns)
            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные:\n{err}")
        finally:
            cursor.close()
            connection.close()

    def open_add_dialog(self):
        """Открывает окно для добавления нового участника."""
        dialog = AddParticipantDialog(self)
        if dialog.exec_() == QDialog.Accepted and dialog.result:
            self.add_participant_to_database(dialog.result)

    def add_participant_to_database(self, participant_data):
        """Добавляет нового участника в базу данных."""
        connection = self.connect_to_database()
        if not connection:
            return
        try:
            cursor = connection.cursor()
            query = "INSERT INTO BandMember (NumberOfGroup, ClientId) VALUES (%s, %s)"
            cursor.execute(query, participant_data)
            connection.commit()
            QMessageBox.information(self, "Успех", "Участник успешно добавлен!")
            self.load_table_data()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить участника:\n{err}")
        finally:
            cursor.close()
            connection.close()
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно входа")
        self.setGeometry(800, 400, 300, 200)
        self.init_ui()
        self.db_connection = self.connect_to_database()

    def init_ui(self):
        # Лейблы и поля ввода
        self.label_login = QLabel("Логин:")
        self.input_login = QLineEdit(self)
        self.label_password = QLabel("Пароль:")
        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.Password)

        # Кнопка
        self.button_login = QPushButton("Войти")
        self.button_login.clicked.connect(self.check_login)

        # Макет
        layout = QVBoxLayout()
        layout.addWidget(self.label_login)
        layout.addWidget(self.input_login)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.button_login)

        # Главный виджет
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def connect_to_database(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",  # Замените на свой логин
                database="db"  # Замените на имя базы данных
            )
            return connection
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка подключения", f"Не удалось подключиться к базе данных:\n{err}")
            sys.exit(1)

    def check_login(self):
        login = self.input_login.text()
        password = self.input_password.text()

        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните оба поля.")
            return

        try:
            cursor = self.db_connection.cursor()
            query = "SELECT * FROM Choreographer WHERE Phone = %s AND password = %s"
            cursor.execute(query, (login, password))
            result = cursor.fetchone()

            if result:
                QMessageBox.information(self, "Успех", "Вы успешно вошли в систему!")
                self.close()  # Закрыть окно логина

                if login == "admin":
                    self.admin_view = AdminView()
                    self.admin_view.show()
                else:
                    self.main_app = MainApp()
                    self.main_app.show()

            else:
                QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль.")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Ошибка базы данных", f"Произошла ошибка:\n{err}")
        finally:
            cursor.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
