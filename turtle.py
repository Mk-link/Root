#Start - Sinus Turtle
 
 
# sinus_turtle.py
import turtle
import math
import time
import itertools
import random
 
# -------- Konfiguration --------
WIDTH, HEIGHT = 800, 400         # Fenstergröße
AMPLITUDE = 120                 # Amplitude der Sinuskurve (Pixel)
FREQUENCY = 0.02                  # Frequenz (kleiner -> längere Wellen)
PHASE_SPEED = 0.3              # Wie schnell sich die Wellen verschieben
X_STEP = 0.5                     # Schrittweite in Pixel beim Zeichnen (kleiner = glatter)
FRAME_DELAY = 0.02              # Pause zwischen Frames (Sekunden)
COLORS = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]  # Farben-Rotation
# --------------------------------
 
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Animierte Sinuskurve — Turtle")
screen.bgcolor("black")
 
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(2)
 
# Performance: kein automatisches Zeichnen bis screen.update()
screen.tracer(0, 0)
 
center_x = 0
center_y = 0
 
def draw_sine(phase, color, amplitude=AMPLITUDE, frequency=FREQUENCY):
    pen.clear()
    pen.color(color)
    first = True
    x_start = -WIDTH // 2
    x_end = WIDTH // 2
    x = x_start
    while x <= x_end:
        # Die x-Koordinate nutzen wir direkt in Pixeln; die Sinus-Argumente sind beliebig skaliert
        y = amplitude * math.sin(frequency * x + phase)
        if first:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            first = False
        else:
            pen.goto(x, y)
        x += X_STEP
 
    # Optional: Mittelachse zeichnen
    pen.penup()
    pen.goto(x_start, 0)
    pen.pendown()
    pen.pensize(1)
    pen.color("white")
    pen.goto(x_end, 0)
    pen.pensize(2)
 
    screen.update()
 
def stop_program(x, y):
    """Wird aufgerufen, wenn auf das Fenster geklickt wird — beendet das Programm."""
    turtle.bye()
 
# Klick beendet das Programm sauber
screen.onclick(stop_program)
 
 
# Endlosschleife mit Farbwechsel
phase = 0.0
colors_cycle = itertools.cycle(COLORS)
try:
    while True:
        color = next(colors_cycle)
        draw_sine(phase, color)
        phase += PHASE_SPEED
        time.sleep(FRAME_DELAY)
except turtle.Terminator:
    # Turtle-Fenster wurde geschlossen, Ende
    pass
except KeyboardInterrupt:
    # Falls du das Skript mit STRG+C in Terminal stoppst
    pass
 
 
 
#End