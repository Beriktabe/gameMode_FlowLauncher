import subprocess
import sys,os
from flowlauncher import FlowLauncher

class gameMode(FlowLauncher):

    def query(self, query):
        return [
            {
                "title": "Hello World, this is where title goes. {}".format(('Your query is: ' + query , query)[query == '']),
                "subTitle": "This is where your subtitle goes, press enter to open Flow's url",
                "icoPath": "Images/app.png",
                "jsonRPCAction": {
                    "method": "executeCommand",
                    "parameters": ["echo [Entire Text] > [File-Name].txt"]
                },
                "score": 0
            }
        ]

    def context_menu(self, data):
        return [
            {
                "title": "Hello World Python's Context menu",
                "subTitle": "Press enter to open Flow the plugin's repo in GitHub",
                "icoPath": "Images/app.png", # related path to the image
                "jsonRPCAction": {
                    "method": "executeCommand",
                    "parameters": ["echo [Entire Text 2] > [File-Name].txt"]
                },
                "score": 0
            }
        ]

    def executeCommand(self, command):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.run(command, startupinfo=startupinfo, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
