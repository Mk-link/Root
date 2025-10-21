print("Bitte trage deinen Benutzernamen ein:")
username = input() #Benutzereingabe

print("Bitte gib jetzt dein Passwort ein:")
password = input() #Benutzereingabe vom Passwort

print("Registrierung erfolgreich!")
print("---------------------")

#Login
print("Gib jetzt deinen Benutzernamen ein:")
eingabe_username = input()

#if Bedingung
if eingabe_username == username:
    print("Gib jetzt dein Passwort ein:")
    eingabe_password = input()

    if eingabe_password == password:
        print("Login erfolgreich! Willkommen", username)
    else:
        print("Falsches Passwort!")
else:
    print("Benutzername nicht gefunden!")
