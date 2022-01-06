from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest/")
    data = response.json()
    canvas.itemconfig(quote_text, text=data["quote"])


window = Tk()
window.title("Emmanuel Quotes ...")
window.config(padx=50, pady=50)

canvas = Canvas(width=400, height=514, bg="blue")
bg_img = PhotoImage(file="images/background.png")
canvas.create_image(200, 257, image=bg_img)
quote_text = canvas.create_text(200, 257, text="Emmanuel Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0, columnspan=2)

kanye_img = PhotoImage(file="images/emmanuel.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

she_img = PhotoImage(file="images/shepherd.png")
she_button = Button(image=she_img, highlightthickness=0, command=get_quote)
she_button.grid(row=1, column=1)

window.mainloop()
