"""
https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/
https://realpython.com/python-pyqt-layout/
"""

from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar, QLabel, QVBoxLayout, QFrame, QComboBox
from PyQt6.QtGui import QAction
import sys

from models.envs import envs, EnvsState, PoguesEnv

class SettingEnvsFrame(QFrame):
    def __init__(self, envs_state: EnvsState) -> None:
        super(QFrame, self).__init__()

        self.envs_state = envs_state

        label = QLabel("Setting envs (QFrame)")
        self.source_env_label = QLabel()
        if self.envs_state.source_env is not None:
            self.source_env_label.setText(self.envs_state.source_env)
        else:
            self.source_env_label.setText("Aucun environnemnent source choisi.")
        envs_dropdown = QComboBox()
        envs_dropdown.addItems(envs.keys())
        envs_dropdown.currentTextChanged.connect(self.on_envs_dropdown_select)
        

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.source_env_label)
        layout.addWidget(envs_dropdown)

        self.setLayout(layout)

    def on_envs_dropdown_select(self, text):
        self.envs_state.source_env = text
        self.source_env_label.setText(f"L'environnement source est : {text}")


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        # --- General conf
        self.setWindowTitle("Pogzops")
        self.setMinimumSize(400,400)

        # --- State
        self.envs_state = EnvsState(None, None)

        toolbar = QToolBar("Toolbar")
        self.addToolBar(toolbar)

        # --- Actions
        button_copy = QAction("Copy", self)
        button_copy.setStatusTip("Copier des questionnaires")
        button_copy.triggered.connect(self.on_copy_click)
        button_copy.setCheckable(True)

        set_envs = QAction("Set envs", self)
        set_envs.triggered.connect(self.on_set_envs_click)

        menu = self.menuBar()
        settings_menu = menu.addMenu("&Settings")
        copy_menu = menu.addMenu("&Copy")

        settings_menu.addAction(set_envs)
        copy_menu.addAction(button_copy)

    def on_copy_click(self, message: str):
        print("Copy opz")
        self.setCentralWidget(QLabel("Copy!"))


    def on_set_envs_click(self, status):
        print("Setting envs")        
        self.setCentralWidget(SettingEnvsFrame(self.envs_state))

app = QApplication(sys.argv)
mw = MainWindow()
mw.show() 

app.exec()
