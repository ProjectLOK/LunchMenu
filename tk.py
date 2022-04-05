import asyncio
from tkinter import *


root = Tk()
root.geometry('800x600')
l1 = Label(root, text='Label 1', font=('arial', 32))
l1.pack()


async def main():
    gui_task = asyncio.create_task(gui()) # gui() coroutine을 task로 실행 (비동기적으로 처리됨)
    asyncio.create_task(update()) # update() coroutine을 task로 실행 (비동기적으로 처리됨)
    await gui_task # 무한루프가 꺼지지 않도록 유지, main 맨 뒷줄에 위치하면 됨


async def gui():
    while True:
        root.update()
        await asyncio.sleep(0.001)  # 없으면 코드 막힘


async def update():
    await asyncio.sleep(3)
    l1.configure(text='Label updated!')


if __name__ == '__main__':
    asyncio.run(main())