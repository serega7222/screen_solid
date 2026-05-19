#controllers/main_screen_control.py
from PySide6.QtWidgets import QFileDialog
from utils.signals import MainSignals
from utils.log import logger
import keyboard
from PySide6.QtCore import  QThread

class SearchBtn(QFileDialog):
    """Отвечает за кнопку обзор в начальном экране"""
    def __init__(self,signals:MainSignals) -> None:
        super().__init__()
        self.signal = signals
        self._connect_signals()

    def _connect_signals(self)-> None:
        self.signal.signal_click_search_btn.connect(self._show_dialog)
    
    def _show_dialog(self)-> None:   
        """Открывает диалог выбора папки""" 
        folder = QFileDialog.getExistingDirectory(None,"Выбери папку для сохранения скриншотов",)
        if folder:
            self.signal.signal_folder_selected.emit(folder)
            logger.info(f"Выбранна папка {folder}")

class HotKetBtn(QThread):
    """Отслеживание и установка горячих клавиш"""
    def __init__(self,signals:MainSignals)-> None:
        super().__init__()
        self.signals = signals
        self.keys = set()
        self._connect_signals()

    def _connect_signals(self)-> None:
        self.signals.signal_click_hot_key_btn.connect(self._start_tracking)


    def add_pressed_keys(self,event:keyboard.KeyboardEvent)-> None:
        """Добавляет горячие клавишы в множество"""
        self.keys.add(event.name)
        if len(self.keys) == 2 :
            self._stop_tracking()
            self.keys.clear()
            

    def _start_tracking(self) -> None:
        keyboard.unhook_all()
        """Устанавливает горячие клавишы"""
        keyboard.on_press(self.add_pressed_keys)
        logger.info("Отслеживаем нажатие клавиш")

    def _stop_tracking(self)-> None:
        """Останавливает отслеживание горячих клавиш"""
        keyboard.unhook_all() 
        logger.info("Горячие клавиши установлены , отслеживание прекращено")