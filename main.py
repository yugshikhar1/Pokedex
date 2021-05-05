import pypokedex as pyp
import PIL.Image, PIL.ImageTk
from tkinter import *
import urllib3
from io import BytesIO

pokedex = Tk()
pokedex.geometry("600x530")
pokedex.title("Pokedex")
pokedex.config(padx=10, pady=10)
pokedex.resizable(False, False)

title = Label(pokedex, text="Pokedex")
title.config(font="Arial 32 bold")
title.pack(padx=10, pady=10)

pokemonImage = Label(pokedex)
pokemonImage.pack(padx=10, pady=10)

info = Label(pokedex)
info.config(font="Arial 20")
info.pack(padx=10, pady=10)

types = Label(pokedex)
types.config(font="Arial 20")
types.pack(padx=10, pady=10)

def load():
    pokemon = pyp.get(name=text.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemonImage.config(image=img)
    pokemonImage.image = img

    info.config(text=f"{pokemon.dex} - {pokemon.name}")
    types.config(text=f"{pokemon.types}")

id_name = Label(pokedex, text="Enter id or name".lower())
id_name.config(font="Arial 20")
id_name.pack(padx=10, pady=10)

text = Text(pokedex, height=1)
text.config(font="Arial 20")
text.pack(padx=10, pady=10)

btn = Button(pokedex, text="Load pokemon", command=load)
btn.config(font="Arial 20")
btn.pack(padx=10, pady=10)

pokedex.mainloop()
