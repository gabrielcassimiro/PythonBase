# Python Base
My study on the Python language


# The Project

This project contains several examples of what I am studying about the Python language.

## OOP

This file includes various examples of OOP (Object-Oriented Programming) that I put into practice. It covers:

* Classes
* Public and private variables
* Functions that modify variables
* Data input from the prompt
* Use of Try-Catch
* Creation of Custom Exceptions for Try-Catch
* Declaration of static functions

## LIST

In this section, there are multiple examples showing how lists and dictionaries work, ranging from basic to more advanced declarations. It includes:

* Creation of Lists and Dictionaries
* Different ways to create lists and dictionaries

## UTILS

Here you will find several other functionalities that are easier to implement here rather than dedicating a full script as in the other sections above. It includes:

* Creation of Decorators
* Iterators
* Yield

___

# Biblioteas Populares

Aqui deixarei para referências as bibliotecas populares que são muito utilizadas no Python

> Lembrando que para instalar uma biblioteca, basta digitar o comando:
>> pip install <nome_da_biblioteca>

- math
```py
import math

print(math.sqrt(16))   # square root → 4.0
print(math.factorial(5))  # 120
print(math.pi)         # 3.14159...
```
- random
```py
import random

print(random.randint(1, 6))   # number between 1 e 6
print(random.choice(["Head", "Tail"]))  # random choice
```
- datetime
```py
import datetime

hoje = datetime.date.today()
print("Hoje:", hoje)

agora = datetime.datetime.now()
print("Agora:", agora.strftime("%d/%m/%Y %H:%M"))
```
- requests - HTTP Requests
```py
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())

```
- pandas - Data Analysis
```py
import pandas as pd

data = {"Name": ["Ana", "Carlos"], "Age": [25, 30]}
df = pd.DataFrame(data)

print(df)
```
- flask - Web Framework
```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world from web with Flask!"

if __name__ == "__main__":
    app.run()
```
- pygame - Game Framework

```py
import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("My Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
```
- BeautifulSoup - Web Scraping
```bash
pip install beautifulsoup4 requests

```
```py
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

print(soup.title.text)
```
- TKinter - GUI Framework

```py
import tkinter as tk

screen = tk.Tk()
screen.title("My screen")
screen.geometry("300x200")

label = tk.Label(screen, text="Hello, Tkinter!")
label.pack(pady=10)

button = tk.Button(screen, text="Close", command=screen.quit)
button.pack(pady=10)

screen.mainloop()
```
- customtkinter

```py
import customtkinter as ctk

ctk.set_appearance_mode("dark")  # opções: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # pode ser "blue", "green", "dark-blue"

screen = ctk.CTk()
screen.title("My Modern Screen")
screen.geometry("300x200")

label = ctk.CTkLabel(screen, text="Hello, CustomTkinter!", font=("Arial", 16))
label.pack(pady=10)

button = ctk.CTkButton(screen, text="Close", command=screen.quit)
button.pack(pady=10)

screen.mainloop()
```