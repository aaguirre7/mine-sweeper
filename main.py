from tkinter import *
import settings
import utils

root = Tk()
# Window Setting Override 
root.configure(bg=settings.MAIN_COLOR)
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)

top_frame = Frame(
    root, 
    bg=settings.MAIN_COLOR,
    width=settings.WIDTH,
    height=utils.height_prct(25)
    )
top_frame.place(x = 0, y = 0)

left_frame= Frame(
    bg=settings.MAIN_COLOR,
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)

left_frame.place(x = 0, y =utils.height_prct(25))

center_frame =Frame(
    root,
    bg=settings.MAIN_COLOR,
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(
    x = utils.width_prct(25),
    y = utils.height_prct(25)
)


#Run Program
root.mainloop()