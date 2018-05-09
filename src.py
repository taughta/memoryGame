from tkinter import Tk,Button, Frame, Entry, END, PhotoImage
import random

class mainWindow(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent=parent
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        self.winfo_toplevel().title("Memory Game by Taught")

    def revealCard(self):
        clickCounter=0
        # while not(clickCounter == 2):


# Initializing Tkinter and starting the main window
root=Tk()
# Setting window size
root.geometry('{}x{}'.format(650, 435))

# Defining card back image
cardback=PhotoImage(file= 'cardBack/back1.png')

# Defining the main window
mainWindow=mainWindow(root)
mainWindow.grid(in_=root, row=8, column=6, columnspan=3)
root.columnconfigure(8, weight=1)
root.rowconfigure(6, weight=1)

# Defining the card pairs

# Here define all unpaired cards that yet to be paired with each other
unpairedCards = ['card1', 'card2', 'card3', 'card4', 'card5', 'card6', 'card7', 'card8', 'card9', 'card10', 'card11', 'card12', 'card13', 'card14', 'card15', 'card16', 'card17', 'card18', 'card19', 'card20', 'card21', 'card22', 'card23', 'card24']

# This is the dictionairy where the card pairs will be filled
pairedCards = {}

# This 'while' cycle will make sure to find a pair for each cards randomly. When a pair is found then those cards are removed from the base pool ('unpairedCards') so paired cards will not be used again. Also if somehow the random sequencer would select the same two cards then that iteration will be dropped.
while len(unpairedCards) > 0:
    pair1 = unpairedCards[random.randint(0,len(unpairedCards)-1)]
    pair2 = unpairedCards[random.randint(0,len(unpairedCards)-1)]
    if not(pair1 == pair2):
        pairedCards[pair1] = pair2
        unpairedCards.remove(pair1)
        unpairedCards.remove(pair2)
    else:
        pass

# Assigning images to card pairs
sourceImages=['AirAmbulance_Red.png','Airplane_Grey.png', 'Ambulance_Red.png', 'Cabriolet_Red.png', 'Car_Grey.png', 'CargoShip_Black.png', 'CarTrailer_Red.png', 'ContainerLoader_Grey.png', 'DieselLocomotive_Boxcar_Blue.png', 'Excavator_Yellow.png', 'ExecutiveCar_Black.png', 'FireTruck_Red.png', 'ForkliftTruck_Loaded_Black.png', 'Lorry_Green.png', 'MixerTruck_Yellow.png', 'PoliceCar_Blue.png', 'QuadBike_Blue.png', 'RecoveryTruck_Blue.png', 'SubwayTrain_Green.png', 'TouringMotorcycle_Green.png', 'TowTruck_Yellow.png', 'TractorUnit_Black.png', 'Truck_Yellow.png', 'TruckMountedCrane__Yellow.png']

# Defining the cards
card1 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card2 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card3 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card4 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card5 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card6 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card7 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card8 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card9 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card10 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card11 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card12 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card13 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card14 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card15 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card16 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card17 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card18 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card19 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card20 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card21 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card22 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card23 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)
card24 = Button(root, image=cardback, width=100, height=100, relief='ridge', bd=3, command=mainWindow.revealCard)

# Defining card positions
card1.grid(row=0, column=1)
card2.grid(row=0, column=2)
card3.grid(row=0, column=3)
card4.grid(row=0, column=4)
card5.grid(row=0, column=5)
card6.grid(row=0, column=6)
card7.grid(row=1, column=1)
card8.grid(row=1, column=2)
card9.grid(row=1, column=3)
card10.grid(row=1, column=4)
card11.grid(row=1, column=5)
card12.grid(row=1, column=6)
card13.grid(row=2, column=1)
card14.grid(row=2, column=2)
card15.grid(row=2, column=3)
card16.grid(row=2, column=4)
card17.grid(row=2, column=5)
card18.grid(row=2, column=6)
card19.grid(row=3, column=1)
card20.grid(row=3, column=2)
card21.grid(row=3, column=3)
card22.grid(row=3, column=4)
card23.grid(row=3, column=5)
card24.grid(row=3, column=6)


root.mainloop()
