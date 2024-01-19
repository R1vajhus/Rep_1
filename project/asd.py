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
            if not self.provider.text():
                msg.warning(self, "Ошибка", "Указанные вами значения не могут быть добавлены!")
            if not self.address.text():
                msg.warning(self, "Ошибка", "Указанные вами значения не могут быть добавлены!")