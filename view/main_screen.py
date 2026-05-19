#view/main_screen.py
from PySide6.QtWidgets import (QMainWindow, QPushButton, QLabel, 
                                QLineEdit, QGridLayout, QWidget)
                          
from model.model import config
from utils.signals import MainSignals
from PySide6.QtCore import  Slot

class MainScreen(QMainWindow):
    """Создает основное окно программы .Появляется при старте программы"""
    def __init__(self,signals : MainSignals) -> None:
        super().__init__()
        self.signals = signals
        self._load_win_setting()
        self._load_ui()
        self._connect_signals()

    def _connect_signals(self)-> None:

        self.signals.signal_folder_selected.connect(self._change_folder)
        self.signals.signal_load_folder.connect(self._change_folder)
        
    def _load_win_setting(self)-> None:
        """Настройки главного окна (размер, название)"""
        self.setMinimumHeight(config.app_min_height)
        self.setMinimumWidth(config.app_min_width)
        self.setWindowTitle(config.app_name)  

    def _load_ui(self)-> None:
        """Загрузка кнопок и элементов интерфейса"""
        _central_widget = QWidget()
        self.setCentralWidget(_central_widget)
        _layout = QGridLayout(_central_widget)  
        
        #Кнопки и элементы интерфейса первой строки
        self._label_save = QLabel("Куда сохранить")
        self._path = QLineEdit()

        self._search_button = QPushButton("Обзор")
        self._search_button.clicked.connect(self._click_search)

        #Кнопки и элементы интерфейса второй строки
        self._label_hot_key = QLabel("Сделать скриншот")
        self._hot_key_button = QPushButton("ctrl+shift")
        self._hot_key_button.clicked.connect(self._click_hot_key_btn)
        self._status_label = QLabel("")

        #Первая строка
        _layout.addWidget(self._label_save, 0, 0)
        _layout.addWidget(self._path, 0, 1)
        _layout.addWidget(self._search_button, 0, 2)

        #Вторая строка 
        _layout.addWidget(self._label_hot_key, 1, 0)
        _layout.addWidget(self._hot_key_button, 1, 1)
        _layout.addWidget(self._status_label, 1, 2)


        #Располагает виджеты вверху
        _layout.setRowStretch(0, 0)    
        _layout.setRowStretch(1, 0)   
        _layout.setRowStretch(2, 1)    

        self.show_main_window()

    #сигналы
    def _click_search(self)-> None:
        self.signals.signal_click_search_btn.emit()
    
    def _click_hot_key_btn(self)-> None:
        self.signals.signal_click_hot_key_btn.emit()
    
    #слоты
    @Slot(str)
    def _change_folder(self,folder:str)-> None:
        """изменяет путь сохранения"""
        self._path.setText(folder)

    
    # публичные методы
    def show_main_window(self)-> None:
        """Показывает главное окно"""
        self.show()    

    def hide_main_window(self) -> None:
        """Скрывает главное окно"""
        self.hide()


