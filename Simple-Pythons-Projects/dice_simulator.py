import random
import PySimpleGUI as sg


class DiceSimulator:
    # Init is the initial value.
    def __init__(self):
        self.minimum_value = 1
        self.maximum_value = 6
        self.message = 'Would you like to generate a new value for the dice?'

        self.layout = [
            [sg.Text("Throw the dice?")],
            [sg.Button("yes"), sg.Button("no")]
        ]

    def Start(self):

        self.window = sg.Window("Dice Simulator", layout=self.layout)
        self.events, self.values = self.window.Read()

        while True:
            try:
                if self.events == "yes" or self.events == "y":
                    self.GenerateValueOfDice()
                    break
                elif self.events == "no" or self.events == "n":
                    print("Thanks for your participation")
                    break
                else:
                    print('Please digit yes or no')
                    continue
            except Exception:
                print("Error: %s" % self.events)

    def GenerateValueOfDice(self):
        print(random.randint(self.minimum_value, self.maximum_value))


simulator = DiceSimulator()
simulator.Start()
