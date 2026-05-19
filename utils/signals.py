#utils/signals.py
from PySide6.QtCore import QObject, Signal


class MainSignals(QObject):  # Наследуемся от QObject
    """Сигналы главного окна"""
    signal_click_search_btn = Signal()  # Нажата кнопка обзор в главном окне
    signal_click_hot_key_btn = Signal() # Нажата кнопка горячие клавишы в главном окне
    signal_folder_selected = Signal(str) # Сигнал содержит путь к выбранной папке
    signal_load_folder = Signal(str) #Загружает путь по умолчанию при запуске программы 
    signal_save_hot_key = Signal(str) #Посылает сигнал с горячими клавишами

    def __init__(self)-> None: 
        super().__init__()