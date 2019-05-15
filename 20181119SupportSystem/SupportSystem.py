from InputReader import InputReader
from Responder import Responder

class SupportSystem:
    def __init__(self):
        self.reader = InputReader()
        self.responder = Responder()

    def start(self):
        finished = False
        self.printWelcome()
        while not finished:
            user_input = self.reader.getInput()

            if user_input.startswith('bye'):
                finished = True
            else:
                response = self.responder.generateResponse()
                print(response)

        self.printGoodbye()
    
    def printWelcome(self):
        print("Welkom bij het Immalle helpsysteem, vertel ons uw probleem!")
        print("Typ bye om te stoppen.")

    def printGoodbye(self):
        print("Tot ziens!")