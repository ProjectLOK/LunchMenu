import widgets
import tkinter as tk
import copy

class WidgetManager:
    def __init__(self, root):
        self.root = root
        self.__running = dict()

    def load(self, preset):
        for widget in self.__running:
            widget.destroy()
            del widget
        
        for widget in preset:
            widget["kwargs"]["anchor"] = getattr(tk, widget["kwargs"]["anchor"])
            widget["kwargs"]["bordermode"] = getattr(tk, widget["kwargs"]["bordermode"])
            orientations = dict(widget["kwargs"]["orientation"])
            for value in orientations:
                temp = int(widget["kwargs"]["orientation"][f"{value}"])
                widget["kwargs"][f"rel{value}"] = widget["kwargs"]["orientation"][f"{value}"] - temp
                widget["kwargs"][f"{value}"] = temp
            
            del widget["kwargs"]["orientation"]
            self.__running[widget["name"]] = getattr(widgets, widget["class"])(getattr(self, widget["master"]))
            self.__running[widget["name"]].place(**widget["kwargs"])