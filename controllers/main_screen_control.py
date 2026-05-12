#controllers/main_screen_control.py
from PySide6.QtWidgets import QFileDialog
from utils.signals import MainSignals
from utils.log import logger

class OpenDialog(QFileDialog):
    """Отвечает за кнопку обзор в начальном экране"""
    def __init__(self,signal:MainSignals) -> None:
        super().__init__()
        self.signal = signal
        self._connect_signals()

    def _connect_signals(self)-> None:
        self.signal.signal_click_search_btn.connect(self._show_dialog)
    
    def _show_dialog(self)-> None:   
        """Открывает диалог выбора папки""" 
        folder = QFileDialog.getExistingDirectory(None,"Выбери папку для сохранения скриншотов",)
        if folder:
            self.signal.signal_folder_selected.emit(folder)
            logger.info(f"Выбранна папка {folder}")

        