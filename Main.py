print("Hello word")
import panda3d as pd
import kivy as k
import time as t
import requests
import webbrowser
SET = 'S.E.T.A.I'

class Start():
    print('Available Commands: "url"  "game" ')
    def game(self):
        t.sleep(0.5)
        print("Starting Panda3d..  " + pd.__version__)
        t.sleep(0.5)
        print("Starting Kivy.. " + k.__version__)
        t.sleep(0.5)
        print("Application Starting...")

        from direct.showbase.ShowBase import ShowBase
        class MyApp(ShowBase):
            def __init__(self):
                ShowBase.__init__(self)
                # Load the environment model.
                self.scene = self.loader.loadModel("models/environment")
                # Reparent the model to render.
                self.scene.reparentTo(self.render)
                # Apply scale and position transforms on the model.
                self.scene.setScale(0.25, 0.25, 0.25)
                self.scene.setPos(-8, 42, 0)
        app = MyApp()
        app.run()

    def fstart(self):
        Choice = input(SET + ": What Do You need me for User? ")
        Answer = Choice.lower()
        if Answer == 'game':
            print(SET + ": Understod Starting a Game...")
            return Start.game(self)
        elif Answer == 'url':
            URL = input(SET + ": Please Specify the URL ")
            WBS = URL
            if WBS[0:4] == 'http' or WBS[0:5] == 'https':
                 print(SET + ": Redirecting To: " + WBS)
                 t.sleep(0.5)
                 webbrowser.open(url=WBS, autoraise=True)
                 return Start.fstart(self)
            else:
                  t.sleep(0.5)
                  print(SET + ": Invalid URL. Restarting...")
                  return  Start.fstart(self)
        else:
            t.sleep(0.5)
            print(SET + ": Unkown Command...Restarting")
            return Start.fstart(self)

Start.fstart(Start.fstart)



