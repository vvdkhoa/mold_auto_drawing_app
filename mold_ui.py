from PySide2 import QtWidgets, QtCore
from ui import main
from database.database import clear_all, update_dimention, update_setting, sql_get_dict
from database.database import create_table_dimentions, create_table_settings

import os
import subprocess

####################  UI CLASS ############################## 
class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        # self.setIcon(QIcon("/images/main.png"))
        # self.setWindowIcon(QIcon(":/icons/main"))
        # self.showMaximized() # Show all desktop
        # self.setWindowTitle("Mold Drawing") # Windowns name
        # self.populate_tree_widget()
        # self.populate_list_widget()
        self.fill_form_from_dabatase()
        self.clearDimentionsButton.clicked.connect(self.clear_dimentions)
        self.saveDimentionsButton.clicked.connect(self.save_dimentions)
        self.selectPathButton.clicked.connect(self.select_path)
        self.selectPathSaveButton.clicked.connect(self.save_path)
        self.exportButton.clicked.connect(self.export_mold)

    # Read database and fill values
    def fill_form_from_dabatase(self):
        # Read database
        dimentions_dict = sql_get_dict(table_name='dimentions')
        settings_dict = sql_get_dict(table_name='settings')
        database_dict = dimentions_dict
        database_dict.update(settings_dict)
        for key in database_dict:
            try:
                value_int = int(database_dict[key])
                database_dict[key] = value_int
            except:
                pass
        print(database_dict)
        # Fill form
        for widget in qApp.allWidgets(): # Dimention and save path
            if isinstance(widget, QtWidgets.QLineEdit):
                try:
                    value = database_dict[widget.objectName()]
                    widget.setText(str(value)) # setText can use with str only
                except:
                    print('No data in database: %s' % widget.objectName())

            if isinstance(widget, QtWidgets.QComboBox): # File Type
                try:
                    value = database_dict[widget.objectName()]
                    index = widget.findText(value, QtCore.Qt.MatchFixedString)
                    if index >= 0:
                        widget.setCurrentIndex(index)
                except:
                    print('No data in database: %s' % widget.objectName())

    # Clear all dimentions in database
    def clear_dimentions(self):
        # Clear value in database
        clear_all(table_name='dimentions')
        # Clear form
        for widget in qApp.allWidgets():
            if isinstance(widget, QtWidgets.QLineEdit):
                if widget.objectName() == 'selectPath':
                    continue
                widget.clear()
        QtWidgets.QMessageBox.about(self, '寸法削除', '入力の寸法を全て削除しました。　　　　　')

    def save_dimentions(self): # Get dimentions and save to database
        for widget in qApp.allWidgets():
            if isinstance(widget, QtWidgets.QLineEdit):
                update_dimention(dimention=widget.objectName(), value=widget.text())
        QtWidgets.QMessageBox.about(self, '寸法保存', '入力の寸法を保存しました。　　　　　')

    def select_path(self): # Get save path and auto save to database
        save_path = QtWidgets.QFileDialog.getExistingDirectory(self) # Get path from button
        if save_path: # Show selected path and save to data base
            self.selectPath.setText(save_path)
            update_setting(setting='save_path', value=save_path)
            QtWidgets.QMessageBox.about(self, '保存', '保存先、拡張子を保存しました。　　　　　')
        else:
            QtWidgets.QMessageBox.about(self, '注意', '保存先を選択してください。　　　　　')

    def save_path(self): # Save enter path
        save_path = self.selectPath.text()
        if save_path:
            update_setting(setting='save_path', value=save_path)
            QtWidgets.QMessageBox.about(self, '保存', '保存先、拡張子を保存しました。　　　　　')
        else:
            QtWidgets.QMessageBox.about(self, '注意', '保存先を選択してください。　　　　　')
        file_type = self.file_type.currentText()
        # file_type.setCurrentIndex(
        update_setting(setting='file_type', value=file_type) # Save to setting table
        # update_dimention(dimention='file_type', value=file_type) # Save to dimention table use for film form

    def export_mold(self):
        # Check save path
        settings_dict = sql_get_dict(table_name='settings')
        try:
            if settings_dict['save_path'] == '':
                QtWidgets.QMessageBox.about(self, '注意', '保存先を選択してください。　　　　　')
        except:
            QtWidgets.QMessageBox.about(self, '注意', '保存先を選択してください。　　　　　')
        # Save dimentions
        self.save_dimentions()
        # Call mold drawing exe
        ui_dirpath = os.getcwd()
        mold_dirpath = ui_dirpath.replace('mold_ui', 'mold_draw') + '/mold_draw.exe'
        subprocess.Popen([r"{}".format(mold_dirpath)])

        
#################################################################
if __name__ == '__main__':

    # Create Table #
    create_table_dimentions()
    create_table_settings()

    # Run UI #
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()



