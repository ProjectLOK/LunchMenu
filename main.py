import tkinter as tk
import asyncio
import widget_manager
import json

async def main():
    root = tk.Tk()
    root.title('Lunch Menu') 
    root.geometry('1872x1404')
    root.attributes('-transparent', False)
    root.configure(background='white')
    #root.resizable(False, False)
    #root.attributes('-fullscreen', True)
    with open('presets/main.json', 'r') as data:
        preset_main = json.loads(data.read())["composition"]
        data.close()

    manager = widget_manager.WidgetManager(root)
    manager.load(preset_main)

    while True:
        root.update()
        await asyncio.sleep(0.01)

if __name__ == "__main__":
    asyncio.run(main())
    exit(0)
