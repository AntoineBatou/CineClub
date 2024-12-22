from PySide6 import QtWidgets, QtCore
import movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self) # type: ignore
        self.qline_taper = QtWidgets.QLineEdit()
        self.qlist_liste = QtWidgets.QListWidget()
        self.btn_ajouter = QtWidgets.QPushButton("Ajouter un film !")
        self.btn_supr = QtWidgets.QPushButton("Suprimmer un film !")

        self.layout.addWidget(self.qline_taper)
        self.layout.addWidget(self.btn_ajouter)
        self.layout.addWidget(self.qlist_liste)
        self.layout.addWidget(self.btn_supr)

    def populate_movies(self):
        movies = movie.get_movies()
        for i in movies:
            qlist_item = QtWidgets.QListWidgetItem(i.title)
            qlist_item.setData(QtCore.Qt.UserRole, i)
            self.qlist_liste.addItem(qlist_item)

    def setup_connections(self):
        self.btn_ajouter.clicked.connect(self.add_movie)
        self.btn_supr.clicked.connect(self.remove_movie)
        self.qline_taper.returnPressed.connect(self.add_movie)

    def add_movie(self):
        print("On ajoute un film")
        ajout = self.qline_taper.text()
        if not ajout:
            return False
        else:
            test = movie.Movie(ajout)
            resultat = test.add_to_movies()
            if resultat == True:
                self.qlist_liste.addItem(test.title)


    def remove_movie(self):
        print("On retire un film")
        #for selected_movies in self.qlist_liste.selectedItems():
        #    movie = selected_movies.data(QtCore.Qt.UserRole)
        #    movie.remove_from_movie()
        #    self.qlist_liste.takeItem(self.qlist_liste.row(selected_item))

        supr = self.qlist_liste.selectedItems()
        
        if supr:
            test = supr[0].text()
            act_del = movie.Movie(test)
            act_del.remove_from_movies()
            index = self.qlist_liste.row(supr[0])
            self.qlist_liste.takeItem(index) # type: ignore
        else:
            print('Veuillez selectionner un film !')


a = QtWidgets.QApplication([])
win = App()
win.show()
a.exec_()

