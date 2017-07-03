import sys
from PyQt5 import QtGui, QtCore, QtWidgets

icon_url = r'C:\Users\Rudy\Desktop/icon.png'

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        # Only put stuff that will always be there in init
        
        super(Window, self).__init__()
        
        self.setGeometry(50, 50, 500, 300)        
        self.setWindowTitle("PyQT Tutorials")
        self.setWindowIcon(QtGui.QIcon(icon_url))
        
        # Add main menu here
        
        extract_action = QtWidgets.QAction("&Get to the Chopper", self)
        extract_action.setShortcut("Ctrl+Q")
        extract_action.setStatusTip("Leave the App")
        extract_action.triggered.connect(self.close_application)
        
        
        # Editor
        
        open_editor = QtWidgets.QAction("&Editor", self)
        open_editor.setShortcut("Ctrl+E")
        open_editor.setStatusTip("Open Editor")
        open_editor.triggered.connect(self.editor)
        
        open_file = QtWidgets.QAction("&Open File", self)
        open_file.setShortcut("Ctrl+O")
        open_file.setStatusTip("Open File")
        open_file.triggered.connect(self.file_open)
        
        save_file = QtWidgets.QAction("&Save File", self)
        save_file.setShortcut("Ctrl+S")
        save_file.setStatusTip("Save File")
        save_file.triggered.connect(self.file_save)
        
        
        self.statusBar()
        
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("&File")
        
        file_menu.addAction(extract_action)
        
        file_menu.addAction(open_file)
        file_menu.addAction(save_file)
        
        editor_menu = main_menu.addMenu("&Editor")
        editor_menu.addAction(open_editor)
        
        self.home()
        
        
    def home(self):
        btn = QtWidgets.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(100,100)
        btn.move(50,100)
        
        # Adding toolbar
        
        extract_action = QtWidgets.QAction(QtGui.QIcon(icon_url), 'Flee the Scene', self)
        extract_action.triggered.connect(self.close_application)
        
        self.tool_bar = self.addToolBar("Extraction")
        self.tool_bar.addAction(extract_action)
        
        # Font picker
        
        font_choice = QtWidgets.QAction("Font", self)
        font_choice.triggered.connect(self.font_choice)
        
        
        # Color picker
        
        color = QtGui.QColor(0,0,0)
        font_color = QtWidgets.QAction("Font bg Color", self)
        font_color.triggered.connect(self.color_picker)
        
        self.tool_bar.addAction(font_color)
        
        # self.tool_bar = self.addToolBar("Font")
        self.tool_bar.addAction(font_choice)
        
        
        # Checkbox
        
        check_box = QtWidgets.QCheckBox("Enlarge Window", self)
        check_box.move(200,100)
        check_box.stateChanged.connect(self.enlarge_window)
        
        # Progressbar
        
        self.progress = QtWidgets.QProgressBar(self)
        
        self.progress.setGeometry(200, 80, 250, 20)
        self.progress.move(200, 200)
        
        self.btn = QtWidgets.QPushButton("Download", self)
        self.btn.move(250,250)
        
        # Dropdown menu
        
        self.style_choice = QtWidgets.QLabel("Windows", self)
        
        combo_box = QtWidgets.QComboBox(self)
        combo_box.addItem("motif")
        combo_box.addItem("Windows")
        combo_box.addItem("cde")
        combo_box.addItem("Plastique")
        combo_box.addItem("Cleanlooks")
        combo_box.addItem("windowsvista")
        
        combo_box.move(50,200)
        self.style_choice.move(50,220)
        
        combo_box.activated[str].connect(self.set_style_choice)
        
        cal = QtWidgets.QCalendarWidget(self)
        cal.move(500,200)
        cal.resize(200,200)
        
        self.btn.clicked.connect(self.download)
        
        
        self.show()
    
    
    def editor(self):
        self.text_edit = QtWidgets.QTextEdit()
        self.setCentralWidget(self.text_edit)
    
    
    def file_save(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self, "Save File")
        
        print(name)
        
        
        f = open(name, "w")
        
        text = self.text_edit.toPlainText()
        
        f.write(text)
        f.close()
        
        
    def file_open(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")
        f = open(name, 'r')
        
        self.editor()
        
        with f:
            text = f.read()
            self.text_edit.setText(text)
        
        
    def font_choice(self):
        font, valid = QtWidgets.QFontDialog.getFont()
        
        if valid:
            self.style_choice.setFont(font)
            
    def color_picker(self):
        color = QtWidgets.QColorDialog.getColor()
        
        self.style_choice.setStyleSheet("QWidget { background-color: %s}" % color.name())
            
            
    def set_style_choice(self, text):
        self.style_choice.setText(text)
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create(text))
        
    
    def download(self):
        self.completed = 0
        
        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
            
            
    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50,50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)
            
            
    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, "Quit Program", "Are you sure you want to quit?",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        
        if choice == QtWidgets.QMessageBox.Yes:    
            sys.exit()
        else:
            pass
        
        
def run():    
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()

    sys.exit(app.exec_())
    
run()