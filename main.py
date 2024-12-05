import sys
import mysql.connector
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QWidget, QTableWidgetItem, QTableWidget
)

class ScheduleViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        super().__init__()

        self.setWindowTitle(f"Таблица расписания")
        self.setGeometry(800, 400, 600, 400)
        self.init_ui()

    def init_ui(self):
        # Таблица для отображения данных
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

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
        """Загрузка данных из указанной таблицы."""
        connection = self.connect_to_database()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = f"SELECT * FROM Schedule"
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
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы {self.table_name}:\n{err}")
        finally:
            cursor.close()
            connection.close()

class testClassViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        super().__init__()

        self.setWindowTitle(f"Таблица пробных занятий")
        self.setGeometry(800, 400, 600, 400)
        self.init_ui()

    def init_ui(self):
        # Таблица для отображения данных
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

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
        """Загрузка данных из указанной таблицы."""
        connection = self.connect_to_database()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = f"SELECT * FROM testClass"
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
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы {self.table_name}:\n{err}")
        finally:
            cursor.close()
            connection.close()

class GrouppaViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        super().__init__()

        self.setWindowTitle(f"Таблица пробных занятий")
        self.setGeometry(800, 400, 600, 400)
        self.init_ui()

    def init_ui(self):
        # Таблица для отображения данных
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

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
        """Загрузка данных из указанной таблицы."""
        connection = self.connect_to_database()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = f"SELECT * FROM Grouppa"
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
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы {self.table_name}:\n{err}")
        finally:
            cursor.close()
            connection.close()
class ScheduleViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"Таблица расписания")
        self.setGeometry(800, 400, 600, 400)
        self.init_ui()

    def init_ui(self):
        # Таблица для отображения данных
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

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
        """Загрузка данных из указанной таблицы."""
        connection = self.connect_to_database()
        if not connection:
            return

        try:
            cursor = connection.cursor()
            query = f"SELECT * FROM Schedule"
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
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить данные из таблицы {self.table_name}:\n{err}")
        finally:
            cursor.close()
            connection.close()
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
       self.button4 = QPushButton("записи", self)
       self.button5 = QPushButton("пробные", self)
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
        self.setGeometry(850, 450, 300, 200)
        label = QLabel("Окно с информацией об абонементах", self)
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
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
            QMessageBox.critical(self, "Ошибка",
                                 f"Не удалось загрузить данные из таблицы {self.table_name}:\n{err}")
        finally:
            cursor.close()
            connection.close()


class GroupsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Группы")
        self.setGeometry(850, 450, 300, 200)
        label = QLabel("Окно с информацией о группах", self)
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
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
            query = f"SELECT * FROM Grouppa"
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
            QMessageBox.critical(self, "Ошибка",
                                 f"Не удалось загрузить данные из таблицы {self.table_name}:\n{err}")
        finally:
            cursor.close()
            connection.close()

class ClientsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Клиенты")
        self.setGeometry(850, 450, 300, 200)
        label = QLabel("Окно с информацией о клиентах", self)
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
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
            query = f"SELECT * FROM Client"
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
            QMessageBox.critical(self, "Ошибка",
                                 f"Не удалось загрузить данные из таблицы {self.table_name}:\n{err}")
        finally:
            cursor.close()
            connection.close()

class RecordsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Записи")
        self.setGeometry(850, 450, 300, 200)
        label = QLabel("Окно с информацией о записях", self)
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
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
            query = f"SELECT * FROM cl_rec"
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
            QMessageBox.critical(self, "Ошибка",
                                 f"Не удалось загрузить данные из таблицы {self.table_name}:\n{err}")
        finally:
            cursor.close()
            connection.close()

class TrialsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пробные")
        self.setGeometry(850, 450, 300, 200)
        label = QLabel("Окно с информацией о пробных занятиях", self)
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
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
            query = f"SELECT * FROM testClass"
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
            QMessageBox.critical(self, "Ошибка",
                                 f"Не удалось загрузить данные из таблицы {self.table_name}:\n{err}")
        finally:
            cursor.close()
            connection.close()

class SalesWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Продажи")
        self.setGeometry(850, 450, 300, 200)
        label = QLabel("Окно с информацией о продажах", self)
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
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
            query = f"SELECT * FROM sale"
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
            QMessageBox.critical(self, "Ошибка",
                                 f"Не удалось загрузить данные из таблицы {self.table_name}:\n{err}")
        finally:
            cursor.close()
            connection.close()

class ScheduleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Расписание")
        self.setGeometry(850, 450, 300, 200)
        label = QLabel("Окно с информацией о расписании", self)
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
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
            query = f"SELECT * FROM Schedule"
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
            QMessageBox.critical(self, "Ошибка",
                                 f"Не удалось загрузить данные из таблицы {self.table_name}:\n{err}")
        finally:
            cursor.close()
            connection.close()

class ProductsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Товары")
        self.setGeometry(850, 450, 300, 200)
        label = QLabel("Окно с информацией о товарах", self)
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
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
            query = f"SELECT * FROM Item"
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
            QMessageBox.critical(self, "Ошибка",
                                 f"Не удалось загрузить данные из таблицы {self.table_name}:\n{err}")
        finally:
            cursor.close()
            connection.close()

class ChoreographersWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Хореографы")
        self.setGeometry(850, 450, 300, 200)
        label = QLabel("Окно с информацией о хореографах", self)
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
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
            query = f"SELECT * FROM Choreographer"
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
            QMessageBox.critical(self, "Ошибка",
                                 f"Не удалось загрузить данные из таблицы {self.table_name}:\n{err}")
        finally:
            cursor.close()
            connection.close()

class ParticipantsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Участники групп")
        self.setGeometry(850, 450, 300, 200)
        label = QLabel("Окно с информацией об участниках групп", self)
        self.table_widget = QTableWidget(self)
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.table_widget)
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
            query = f"SELECT * FROM group_fio"
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
            QMessageBox.critical(self, "Ошибка",
                                 f"Не удалось загрузить данные из таблицы {self.table_name}:\n{err}")
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
