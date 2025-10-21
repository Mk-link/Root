studenten= ["Jörg","Patrick","Holger","Christopher"]
print(studenten)

print(", ".join(studenten))
studenten = ["Jörg","Patrick","Holger","Christopher"]

s = ", ".join(studenten)
print(s)                          # "Jörg, Patrick, Holger, Christopher" — kein Separator am Anfang oder Ende

# Wenn du etwas davor oder danach willst:
print("Teilnehmer: " + s)        # Prefix vor der ganzen Liste
print(s + ".")                   # Suffix nach der ganzen Liste

# Separator auch am Ende erzwingen:
sep = ", "
print(sep.join(studenten) + sep) # "Jörg, Patrick, Holger, Christopher, "

# Prefix vor jedem Namen:
print(", ".join("Herr " + n for n in studenten))

# Mit Zeilenumbruch trennen:
print("\n".join(studenten))
studenten = ["Jörg","Patrick","Holger","Christopher"]

s = ", ".join(studenten)
print(s)                          # "Jörg, Patrick, Holger, Christopher" — kein Separator am Anfang oder Ende

# Wenn du etwas davor oder danach willst:
print("Teilnehmer: " + s)        # Prefix vor der ganzen Liste
print(s + ".")                   # Suffix nach der ganzen Liste

# Separator auch am Ende erzwingen:
sep = ", "
print(sep.join(studenten) + sep) # "Jörg, Patrick, Holger, Christopher, "

# Prefix vor jedem Namen:
print(", ".join("Herr " + n for n in studenten))

# Mit Zeilenumbruch trennen:
print("\n".join(studenten))