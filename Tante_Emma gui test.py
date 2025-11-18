import sys
import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime


DEFAULT_PIN = "2206"
DEFAULT_QTY = 2

inventory = [
    {"name": "Schokolade", "price": 3.20, "qty": DEFAULT_QTY},
    {"name": "Chips", "price": 2.50, "qty": DEFAULT_QTY},
    {"name": "Kaugummi", "price": 0.80, "qty": DEFAULT_QTY},
    {"name": "Wasser", "price": 1.20, "qty": DEFAULT_QTY},
    {"name": "Bier", "price": 1.40, "qty": DEFAULT_QTY},
    {"name": "Kaffeebohnen", "price": 13.90, "qty": DEFAULT_QTY},
    {"name": "Tee", "price": 1.90, "qty": DEFAULT_QTY},
    {"name": "Kekse", "price": 3.90, "qty": DEFAULT_QTY},
    {"name": "Nüsse", "price": 4.70, "qty": DEFAULT_QTY},
    {"name": "Zigaretten", "price": 4.30, "qty": DEFAULT_QTY},
]

cart = {}  # name -> {'price': float, 'qty': int}
logged_in = False

def format_euro(value: float) -> str:
    s = f"{value:,.2f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{s} €"

def check_pin(pin: str) -> bool:
    return pin == DEFAULT_PIN

def update_buttons():
    for i, btn in enumerate(item_buttons):
        item = inventory[i]
        text = f"{item['name']}\n{format_euro(item['price'])}\nAnzahl: {item['qty']}"
        if item['qty'] <= 0:
            btn.config(text=text, state="disabled")
        else:
            btn.config(text=text, state="normal")

def purchase(index: int):
    # purchase assumes the GUI is unlocked (login done)
    item = inventory[index]
    if item['qty'] <= 0:
        messagebox.showinfo("Nicht verfügbar", f"{item['name']} ist nicht verfügbar.")
        update_buttons()
        return
    # decrement stock
    item['qty'] -= 1
    # add to cart
    name = item['name']
    if name in cart:
        cart[name]['qty'] += 1
    else:
        cart[name] = {'price': item['price'], 'qty': 1}
    status_var.set(f"{name} gekauft. Aktueller Warenkorb-Positionen: {len(cart)}")
    update_buttons()

def refill_all():
    pin = pin_var.get().strip()
    if not check_pin(pin):
        messagebox.showwarning("PIN falsch", "Ungültiger Jugendschutzcode. Auffüllen verweigert.")
        return
    for item in inventory:
        item['qty'] = DEFAULT_QTY
    update_buttons()
    status_var.set("Alle Artikel aufgefüllt.")

def show_invoice():
    if not cart:
        messagebox.showinfo("Warenkorb leer", "Keine gekauften Artikel.")
        return

    # Terminal-Ausgabe im gleichen Format wie vorher
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n======= Rechnung =======")
    print(f"Datum: {now}\n")
    total = 0.0
    print(f"{'Pos.':<4} {'Artikel':<20} {'Stck.':>5} {'Einzelpreis':>14}")
    print("-" * 60)
    for i, (name, info) in enumerate(cart.items(), start=1):
        qty = info['qty']
        unit = info['price']
        line_total = qty * unit
        total += line_total
        print(f"{i:<4} {name:<20} {qty:>5} {format_euro(unit):>14}")
    print("-" * 60)
    print(f"{'Gesamt:':>31} {format_euro(total):>14}")
    print("================\n")

    # Optionale kurze GUI-Rückmeldung und Aufräumen
    messagebox.showinfo("Rechnung", "Ihre Rechnung wird im Terminal ausgegeben.")
    cart.clear()
    status_var.set("Rechnung erstellt. Warenkorb geleert.")
    update_buttons()

def on_close():
    # Beim Schließen: falls Warenkorb Items enthält, zuerst Rechnung im Terminal ausgeben
    if cart:
        show_invoice()
    root.destroy()

def do_login(event=None):
    global logged_in
    pin = pin_var.get().strip()
    if check_pin(pin):
        logged_in = True
        status_var.set("PIN korrekt. Artikel freigeschaltet.")
        # disable pin entry and login button
        pin_entry.config(state="disabled")
        btn_login.config(state="disabled")
        # show the product grid
        grid_frame.pack(padx=8, pady=6)
        update_buttons()
    else:
        messagebox.showwarning("PIN falsch", "Ungültiger Jugendschutzcode.")
        status_var.set("PIN falsch. Bitte erneut eingeben.")
        pin_var.set("")
        pin_entry.focus()

# build GUI
root = tk.Tk()
root.title("Tante Emma - Mobile")

top_frame = tk.Frame(root)
top_frame.pack(padx=8, pady=6, fill="x")

tk.Label(top_frame, text="Jugendschutz-PIN:").pack(side="left")
pin_var = tk.StringVar()
pin_entry = tk.Entry(top_frame, textvariable=pin_var, show="*")
pin_entry.pack(side="left", padx=(6, 6))
pin_entry.focus()
pin_entry.bind("<Return>", do_login)  # Enter to login

btn_login = tk.Button(top_frame, text="Login", command=do_login)
btn_login.pack(side="left", padx=(0,8))

btn_refill = tk.Button(top_frame, text="Refill (admin)", command=refill_all)
btn_refill.pack(side="left")

status_var = tk.StringVar(value="Willkommen. Bitte PIN eingeben und mit Login die Artikel freischalten.")
status_label = tk.Label(root, textvariable=status_var, anchor="w")
status_label.pack(fill="x", padx=8)

grid_frame = tk.Frame(root)
# NOTE: do NOT pack grid_frame here — it will be packed after successful login

item_buttons = []
for idx, item in enumerate(inventory):
    btn = tk.Button(grid_frame, text="", width=20, height=4, command=lambda i=idx: purchase(i))
    row = idx // 2
    col = idx % 2
    btn.grid(row=row, column=col, padx=6, pady=6)
    item_buttons.append(btn)

# update_buttons will be called after login to set texts/states

bottom_frame = tk.Frame(root)
bottom_frame.pack(padx=8, pady=6, fill="x")

btn_invoice = tk.Button(bottom_frame, text="Rechnung anzeigen", command=show_invoice)
btn_invoice.pack(side="left")

btn_quit = tk.Button(bottom_frame, text="Beenden", command=on_close)
btn_quit.pack(side="right")

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()