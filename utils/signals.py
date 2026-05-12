#utils/signals.py
from PySide6.QtCore import QObject, Signal


class MainSignals(QObject):  # Наследуемся от QObject
    """Сигналы главного окна"""
    signal_click_search_btn = Signal()  # Нажата кнопка обзор в главном окне
    signal_click_hot_key_btn = Signal() # Нажата кнопка горячие клавишы в главном окне
    signal_folder_selected = Signal(str) # Папка выбрана 
    signal_load_folder = Signal(str) #Загружает путь по умолчанию при запуске программы 
    def __init__(self):
        super().__init__()