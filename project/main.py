from MainWindow import Ui_MainWindow
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel, QSqlQuery
from PyQt5.QtGui import QIntValidator

class mainWindow(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = QSqlDatabase.addDatabase('QPSQL')
        self.db.setHostName('localhost')
        self.db.setPort(5432)
        self.db.setDatabaseName('shop2')
        self.db.setUserName('postgres')
        self.db.setPassword('student')
        self.db.open()
        
        self.table_1()
        self.table_2()
        self.table_3()
        self.table_4()
        
        self.number.setValidator(QIntValidator())
        self.number_change.setValidator(QIntValidator())
        self.name.setValidator(QIntValidator())
        self.name_change.setValidator(QIntValidator())
        self.price.setValidator(QIntValidator())
        self.price_change.setValidator(QIntValidator())
        
        self.tableView.setEditTriggers(QTableView.NoEditTriggers)
        self.tableView_2.setEditTriggers(QTableView.NoEditTriggers)
        self.tableView_3.setEditTriggers(QTableView.NoEditTriggers)
        self.tableView_4.setEditTriggers(QTableView.NoEditTriggers)
        
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableView_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        self.pushButton.setCheckable(True)
        self.calendarWidget.hide()
        
        self.pushButton.clicked.connect(self.calendar)
        self.date.setReadOnly(True)
        
        self.calendarWidget_change.hide()
        self.pushButton_2.setCheckable(True)
        
        self.pushButton_2.clicked.connect(self.calendar_2)
        self.date_change.setReadOnly(True)
        
        self.other.clicked.connect(self.btn_other)
        self.other_2.clicked.connect(self.btn_other_2)
        
        self.add.clicked.connect(self.btn_show_1)
        self.add.setCheckable(True)
        self.add_2.clicked.connect(self.btn_show_2)
        self.add_2.setCheckable(True)
        self.add_3.clicked.connect(self.btn_show_3)
        self.add_3.setCheckable(True)
        self.add_4.clicked.connect(self.btn_show_4)
        self.add_4.setCheckable(True)
        self.add_5.clicked.connect(self.btn_show_5)
        self.add_5.setCheckable(True)
        
        self.change_btn.clicked.connect(self.change_show)
        self.change_btn.setCheckable(True)
        self.change_btn_2.clicked.connect(self.change_show_2)
        self.change_btn_2.setCheckable(True)
        self.change_btn_3.clicked.connect(self.change_show_3)
        self.change_btn_3.setCheckable(True)
        self.change_btn_4.clicked.connect(self.change_show_4)
        self.change_btn_4.setCheckable(True)
        self.change_btn_5.clicked.connect(self.change_show_5)
        self.change_btn_5.setCheckable(True)
        
        self.cancel.clicked.connect(self.btn_cancel_1)
        self.cancel_2.clicked.connect(self.btn_cancel_2)
        self.cancel_3.clicked.connect(self.btn_cancel_3)
        
        self.cancel_change.clicked.connect(self.btn_cancel_change_1)
        self.cancel_change_2.clicked.connect(self.btn_cancel_change_2)
        self.cancel_change_3.clicked.connect(self.btn_cancel_change_3)
        
        self.dele.clicked.connect(self.delete_db_1)
        self.del_2.clicked.connect(self.delete_db_2)
        self.del_3.clicked.connect(self.delete_db_3)
        self.dele_2.clicked.connect(self.delete_db_4)
        
        self.ok.clicked.connect(self.add_tb_1)
        self.ok_2.clicked.connect(self.add_tb_2)
        self.ok_3.clicked.connect(self.add_tb_3)
        self.ok_4.clicked.connect(self.add_tb_4)
        
        self.ok_change.clicked.connect(self.change_1)
        self.ok_change_2.clicked.connect(self.change_2)
        self.ok_change_3.clicked.connect(self.change_3)
        
        self.group_postav.hide()
        self.group_postav_2.hide()
        self.group_postav_3.hide()
        self.group_postav_4.hide()
        self.group_postav_6.hide()
        
        self.group_postav_change.hide()
        self.group_postav_change_2.hide()
        self.group_postav_change_3.hide()
        self.group_postav_change_4.hide()
        self.group_postav_change_5.hide()
        
        self.cal()
        self.cal_2()
        
    def btn_other(self):
        self.stackedWidget.setCurrentIndex(1)
        
    def btn_other_2(self):
        self.stackedWidget.setCurrentIndex(0)
        
        
    def btn_show_1(self):
        if self.add.isChecked():
            self.group_postav.show()
            self.group_postav_change.hide()
            self.change_btn.setChecked(False)
        else:
            self.group_postav.hide()
    
    def btn_show_2(self):
        if self.add_2.isChecked():
            self.group_postav_2.show()
            self.group_postav_change_2.hide()
            self.calendarWidget_change.hide()
            self.change_btn_2.setChecked(False)
        else:
            self.group_postav_2.hide()
            self.calendarWidget.hide()
            self.pushButton.setChecked(False)
        
    def btn_show_3(self):
        if self.add_3.isChecked():
            self.group_postav_3.show()
            self.group_postav_change_3.hide()
            self.change_btn_3.setChecked(False)
        else:
            self.group_postav_3.hide()
            
    def btn_show_4(self):
        if self.add_4.isChecked():
            self.group_postav_4.show()
            self.group_postav_change_4.hide()
            self.change_btn_4.setChecked(False)
        else:
            self.group_postav_4.hide()
            
    def btn_show_5(self):
        if self.add_5.isChecked():
            self.group_postav_6.show()
            self.group_postav_change_5.hide()
            self.change_btn_5.setChecked(False)
        else:
            self.group_postav_6.hide()
            
    def change_show(self):
        if self.change_btn.isChecked():
            self.group_postav_change.show()
            self.group_postav.hide()
            self.add.setChecked(False)
        else:
            self.group_postav_change.hide()
            
    def change_show_2(self):
        if self.change_btn_2.isChecked():
            self.group_postav_change_2.show()
            self.group_postav_2.hide()
            self.calendarWidget.hide()
            self.add_2.setChecked(False)
        else:
            self.group_postav_change_2.hide()
            
    def change_show_3(self):
        if self.change_btn_3.isChecked():
            self.group_postav_change_3.show()
            self.group_postav_3.hide()
            self.add_3.setChecked(False)
        else:
            self.group_postav_change_3.hide()
            
    def change_show_4(self):
        if self.change_btn_4.isChecked():
            self.group_postav_change_4.show()
            self.group_postav_4.hide()
            self.add_4.setChecked(False)
        else:
            self.group_postav_change_4.hide()
            
    def change_show_5(self):
        if self.change_btn_5.isChecked():
            self.group_postav_change_5.show()
            self.group_postav_6.hide()
            self.add_5.setChecked(False)
        else:
            self.group_postav_change_5.hide()
        
    def btn_cancel_1(self):
        self.group_postav.hide()
        self.add.setChecked(False)
        
    def btn_cancel_2(self):
        self.group_postav_2.hide()
        self.add_2.setChecked(False)
        self.calendarWidget.hide()
        self.pushButton.setChecked(False)
        
    def btn_cancel_3(self):
        self.group_postav_3.hide()
        self.add_3.setChecked(False)
        
    def btn_cancel_change_1(self):
        self.group_postav_change.hide()
        self.change_btn.setChecked(False)
        
    def btn_cancel_change_2(self):
        self.group_postav_change_2.hide()
        self.change_btn_2.setChecked(False)
        self.calendarWidget_change.hide()
        
    def btn_cancel_change_3(self):
        self.group_postav_change_3.hide()
        self.change_btn_3.setChecked(False)
        
    def calendar(self):
        if self.pushButton.isChecked():
            self.calendarWidget.show()
        else:
            self.calendarWidget.hide()
    
    def calendar_2(self):
        if self.pushButton_2.isChecked():
            self.calendarWidget_change.show()
        else:
            self.calendarWidget_change.hide()
        
    def cal(self):
        def update_line_edit_date():
            selected_date = self.calendarWidget.selectedDate().toString('yyyy-MM-dd')
            self.date.setText(selected_date)
        self.calendarWidget.clicked.connect(update_line_edit_date)
        
    def cal_2(self):
        def update_line_edit_date():
            selected_date = self.calendarWidget_change.selectedDate().toString('yyyy-MM-dd')
            self.date_change.setText(selected_date)
        self.calendarWidget_change.clicked.connect(update_line_edit_date)
        
    def table_1(self):
        stm = QSqlTableModel(parent=self.tableView)
        stm.setTable('providers')
        stm.select()
        self.tableView.setModel(stm)
        stm.setHeaderData(0, QtCore.Qt.Horizontal, "Поставщик")
        stm.setHeaderData(1, QtCore.Qt.Horizontal, "Адрес")
        
        
    def table_2(self):
        stm = QSqlTableModel(parent=self.tableView_2)
        stm.setTable('soppliers')
        stm.select()
        self.tableView_2.setModel(stm)
        stm.setHeaderData(0, QtCore.Qt.Horizontal, "Номер")
        stm.setHeaderData(1, QtCore.Qt.Horizontal, "Дата")
    
    def table_3(self):
        stm = QSqlTableModel(parent=self.tableView_3)
        stm.setTable('productofinvoice')
        stm.select()
        self.tableView_3.setModel(stm)
        stm.setHeaderData(0, QtCore.Qt.Horizontal, "Товар")
        stm.setHeaderData(1, QtCore.Qt.Horizontal, "Цена")
        stm.setHeaderData(2, QtCore.Qt.Horizontal, "Количество")
        stm.setHeaderData(3, QtCore.Qt.Horizontal, "Стоимость")
        
    def table_4(self):
        stm = QSqlTableModel(parent=self.tableView_4)
        stm.setTable('product')
        stm.select()
        self.tableView_4.setModel(stm)
        stm.setHeaderData(0, QtCore.Qt.Horizontal, "Товар")
        stm.setHeaderData(1, QtCore.Qt.Horizontal, "Цена")
        
    def delete_db_1(self):
        model = QSqlTableModel()
        model.setTable('providers')
        model.select()
        selectedIndex = self.tableView.selectedIndexes()
        if selectedIndex:
            row = selectedIndex[0].row()
            model.removeRow(row)
            model.submitAll()
        self.tableView.setModel(model)
        model.setHeaderData(0, QtCore.Qt.Horizontal, "Поставщик")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Адрес")
        
    def delete_db_2(self):
        model = QSqlTableModel()
        model.setTable('soppliers')
        model.select()
        selectedIndex = self.tableView_2.selectedIndexes()
        if selectedIndex:
            row = selectedIndex[0].row()
            model.removeRow(row)
            if model.removeRow(row):
                model.submitAll()
                self.tableView_2.setModel(model)
            else:
                print("Failed to remove row")
        self.tableView_2.setModel(model)
        model.setHeaderData(0, QtCore.Qt.Horizontal, "Номер")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Дата")
        
    def delete_db_3(self):
        model = QSqlTableModel()
        model.setTable('productofinvoice')
        model.select()
        selectedIndex = self.tableView_3.selectedIndexes()
        if selectedIndex:
            row = selectedIndex[0].row()
            model.removeRow(row)
            model.submitAll()
        self.tableView_3.setModel(model)
        model.setHeaderData(0, QtCore.Qt.Horizontal, "Товар")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Цена")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Количество")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Стоимость")
        
    def delete_db_4(self):
        model = QSqlTableModel()
        model.setTable('product')
        model.select()
        selectedIndex = self.tableView_4.selectedIndexes()
        if selectedIndex:
            row = selectedIndex[0].row()
            model.removeRow(row)
            model.submitAll()
        self.tableView_4.setModel(model)
        model.setHeaderData(0, QtCore.Qt.Horizontal, "Товар")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Цена")
        
    def add_tb_1(self):
        msg = QMessageBox()
        if self.provider.text() and self.address.text():
            query = QSqlQuery()
            query.exec(f"INSERT INTO public.providers(providere, address) VALUES ('{self.provider.text()}','{self.address.text()}');")
            print(query.isActive())
            if query.isActive() == True:
                model = QSqlTableModel()
                model.setTable('providers')
                model.select()
                self.tableView.setModel(model)
                model.setHeaderData(0, QtCore.Qt.Horizontal, "Поставщик")
                model.setHeaderData(1, QtCore.Qt.Horizontal, "Адрес")
            elif query.isActive() == False:
                msg.warning(self, "Ошибка", "Указанные вами значения не могут быть добавлены!")
        else:
            msg.warning(self, "Ошибка", "Указанные вами значения не могут быть добавлены!")
        
    def add_tb_2(self):
        msg = QMessageBox()
        if self.number.text() and self.date.text():
            query = QSqlQuery()
            query.exec(f"INSERT INTO public.soppliers(numbers, date) VALUES ('{self.number.text()}', '{self.date.text()}');")
            print(query.isActive())
            if query.isActive() == True:
                model = QSqlTableModel()
                model.setTable('soppliers')
                model.select()
                self.tableView_2.setModel(model)
                model.setHeaderData(0, QtCore.Qt.Horizontal, "Номер")
                model.setHeaderData(1, QtCore.Qt.Horizontal, "Дата")
            elif query.isActive() == False:
                msg = QMessageBox()
                msg.warning(self, "Ошибка", "Указанные вами значения не могут быть добавлены!")
        else:
            msg.warning(self, "Ошибка", "Указанные вами значения не могут быть добавлены!")
        
    def add_tb_3(self):
        msg = QMessageBox()
        try:
            if self.number.text() and self.date.text():
                query = QSqlQuery()
                a = int(self.name.text()) * 12
                b = int(self.name.text()) * 10
                c = int(self.name.text()) * 90
                d = int(self.name.text()) * 15
                e = int(self.name.text()) * 30
                if self.comboBox.currentText() == "Кефир":
                    query.exec(f"INSERT INTO public.productofinvoice(tovar, price, quantity, stoimost) VALUES ('{self.comboBox.currentText()}', '12', '{self.name.text()}', '{a}');")
                    print(query.isActive())
                elif self.comboBox.currentText() == "Молоко":
                    query.exec(f"INSERT INTO public.productofinvoice(tovar, price, quantity, stoimost) VALUES ('{self.comboBox.currentText()}', '10', '{self.name.text()}', '{b}');")
                    print(query.isActive())
                elif self.comboBox.currentText() == "Свинина":
                    query.exec(f"INSERT INTO public.productofinvoice(tovar, price, quantity, stoimost) VALUES ('{self.comboBox.currentText()}', '90', '{self.name.text()}', '{c}');")
                    print(query.isActive())
                elif self.comboBox.currentText() == "Сметана":
                    query.exec(f"INSERT INTO public.productofinvoice(tovar, price, quantity, stoimost) VALUES ('{self.comboBox.currentText()}', '15', '{self.name.text()}', '{d}');")
                    print(query.isActive())
                elif self.comboBox.currentText() == "Тушёнка":
                    query.exec(f"INSERT INTO public.productofinvoice(tovar, price, quantity, stoimost) VALUES ('{self.comboBox.currentText()}', '30', '{self.name.text()}', '{e}');")
                    print(query.isActive())
                if query.isActive() == True:
                    model = QSqlTableModel()
                    model.setTable('productofinvoice')
                    model.select()
                    self.tableView_3.setModel(model)
                    model.setHeaderData(0, QtCore.Qt.Horizontal, "Товар")
                    model.setHeaderData(1, QtCore.Qt.Horizontal, "Цена")
                    model.setHeaderData(2, QtCore.Qt.Horizontal, "Количество")
                    model.setHeaderData(3, QtCore.Qt.Horizontal, "Стоимость")
                elif query.isActive() == False:
                    msg = QMessageBox()
                    msg.warning(self, "Ошибка", "Указанные вами значения не могут быть добавлены!")
            else:
                msg.warning(self, "Ошибка", "Указанные вами значения не могут быть добавлены!")
        except:
            print("error")
            
    def add_tb_4(self):
        msg = QMessageBox()
        if self.product.text() and self.price.text():
            query = QSqlQuery()
            query.exec(f"INSERT INTO public.product(products, price) VALUES ('{self.product.text()}','{self.price.text()}');")
            print(query.isActive())
            if query.isActive() == True:
                model = QSqlTableModel()
                model.setTable('product')
                model.select()
                self.tableView_4.setModel(model)
                model.setHeaderData(0, QtCore.Qt.Horizontal, "Продукт")
                model.setHeaderData(1, QtCore.Qt.Horizontal, "Цена")
            elif query.isActive() == False:
                msg.warning(self, "Ошибка", "Указанные вами значения не могут быть добавлены!")
        else:
            msg.warning(self, "Ошибка", "Указанные вами значения не могут быть добавлены!")
            
    def change_1(self):
        msg = QMessageBox()
        try:
            if self.provider_change.text() and self.address_change.text():
                model = QSqlTableModel()
                model.setTable('providers')
                model.select()
                selected_indexes = self.tableView.selectionModel().selectedIndexes()
                row_index = selected_indexes[0].row()
                record = model.record(row_index)
                record.setValue(0, f"{self.provider_change.text()}")
                record.setValue(1, f"{self.address_change.text()}")
                model.setRecord(row_index, record)
                model.submitAll()
                self.tableView.setModel(model)
                model.setHeaderData(0, QtCore.Qt.Horizontal, "Поставщик")
                model.setHeaderData(1, QtCore.Qt.Horizontal, "Адрес")
            else:
                msg.warning(self, "Ошибка", "Указанные вами значения не могут быть добавлены!")
        except:
            print("error")
                    
    def change_2(self):
        msg = QMessageBox()
        try:
            if self.number_change.text() and self.date_change.text():
                model = QSqlTableModel()
                model.setTable('soppliers')
                model.select()
                selected_indexes = self.tableView_2.selectionModel().selectedIndexes()
                row_index = selected_indexes[0].row()
                record = model.record(row_index)
                record.setValue(0, f"{self.number_change.text()}")
                record.setValue(1, f"{self.date_change.text()}")
                model.setRecord(row_index, record)
                model.submitAll()
                self.tableView_2.setModel(model)
                model.setHeaderData(0, QtCore.Qt.Horizontal, "Номер")
                model.setHeaderData(1, QtCore.Qt.Horizontal, "Дата")
            else:
                msg.warning(self, "Ошибка", "Указанные вами значения не могут быть добавлены!")
        except:
            print("error")
    
    def change_3(self):
        msg = QMessageBox()
        model = QSqlTableModel()
        model.setTable('productofinvoice')
        model.select()
        try:
            if self.comboBox_change.currentText() and self.name_change.text():
                selected_indexes = self.tableView_3.selectionModel().selectedIndexes()
                row_index = selected_indexes[0].row()
                record = model.record(row_index)
                if self.comboBox_change.currentText() == "Кефир":
                    a = int(self.name_change.text()) * 12
                    record.setValue(0, f"{self.comboBox_change.currentText()}")
                    record.setValue(1, f"{12}")
                    record.setValue(2, f"{self.name_change.text()}")
                    record.setValue(3, f"{a}")
                elif self.comboBox_change.currentText() == "Молоко":
                    b = int(self.name_change.text()) * 10
                    record.setValue(0, f"{self.comboBox_change.currentText()}")
                    record.setValue(1, f"{10}")
                    record.setValue(2, f"{self.name_change.text()}")
                    record.setValue(3, f"{b}")
                elif self.comboBox_change.currentText() == "Свинина":
                    c = int(self.name_change.text()) * 90
                    record.setValue(0, f"{self.comboBox_change.currentText()}")
                    record.setValue(1, f"{90}")
                    record.setValue(2, f"{self.name_change.text()}")
                    record.setValue(3, f"{c}")
                elif self.comboBox_change.currentText() == "Сметана":
                    d = int(self.name_change.text()) * 15
                    record.setValue(0, f"{self.comboBox_change.currentText()}")
                    record.setValue(1, f"{15}")
                    record.setValue(2, f"{self.name_change.text()}")
                    record.setValue(3, f"{d}")
                elif self.comboBox_change.currentText() == "Тушёнка":
                    e = int(self.name_change.text()) * 30
                    record.setValue(0, f"{self.comboBox_change.currentText()}")
                    record.setValue(1, f"{30}")
                    record.setValue(2, f"{self.name_change.text()}")
                    record.setValue(3, f"{e}")
                model.setRecord(row_index, record)
                model.submitAll()
            else:
                msg.warning(self, "Ошибка", "Указанные вами значения не могут быть добавлены!")
        except:
            print("error")
        self.tableView_3.setModel(model)
        model.setHeaderData(0, QtCore.Qt.Horizontal, "Товар")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Цена")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Количество")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Стоимость") 
        
app = QApplication(sys.argv)
window = mainWindow()
window.show()
app.exec_()