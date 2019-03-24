import random
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QLabel, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

#Creaing list of tv shows
def choose(): 
    words = ['gotham', 'riverdale', 'supernatural', 'lucifer', 'shameless', 'arrow', 'westworld', 'blindspot', 'vikings', 'fargo',
             'sherlock', 'columbo', 'mash', 'startrek', 'lost', 'seinfeld', 'fraiser', 'madmen', 'sopranos', 'deadwood',
             'cracker', 'blackadder', 'friends', 'simpsons', 'scandal', 'flash', 'daredevil', 'supergirl', 'teentitans', 'suits'] 
    pick = random.choice(words)
    return pick

#Jumbling the random work picked in choose function
def jumble(word): 
    random_word = random.sample(word, len(word)) 
    jumbled = ''.join(random_word) 
    return jumbled

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Jumble Game'
        self.left = 10
        self.top = 10
        self.width = 450
        self.height = 220
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.play()
        
        self.show()
        
    #playing the game
    def play(self):
        player_score = 0
        turn = 0
        while turn < 10:
            picked_word = choose()
            question = jumble(picked_word)

            #printing jumbled word
            QMessageBox.question(self, 'Jumbled Word', "The jumbled word is: " + question, QMessageBox.Ok, QMessageBox.Ok)

            answer, okPressed = QInputDialog.getText(self, "Get text","Your answer:", QLineEdit.Normal, "")
            
            #validating answer
            if answer == picked_word:
                QMessageBox.question(self, 'Result', "Corect!", QMessageBox.Ok, QMessageBox.Ok)
                #increasing player score
                player_score += 1
            else:
                #dsiplaying the correct answer
                QMessageBox.question(self, 'Result', "Wrong! The answer is: " + picked_word, QMessageBox.Ok, QMessageBox.Ok)           
        
            #going to next turn
            turn += 1

        #displaying the final score
        QMessageBox.question(self, 'Total Score', "Total Score: " + str(player_score), QMessageBox.Ok, QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 

