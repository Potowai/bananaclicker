import time
import pyautogui
import subprocess
import pygetwindow as gw

# Lancer l'application Unity en utilisant une chaîne brute ou des barres obliques doubles
subprocess.Popen([r'C:\Program Files (x86)\Steam\steamapps\common\Banana\banana.exe'])  # Utilisation de chaîne brute

# Ou vous pouvez utiliser des barres obliques doubles
# subprocess.Popen(['C:\\Program Files (x86)\\Steam\\steamapps\\common\\Banana\\banana.exe'])

# Attendre que l'application se charge
time.sleep(10)  # Ajustez ce délai selon le temps de chargement de votre application

# Focaliser sur la fenêtre de l'application
window = gw.getWindowsWithTitle('Banana')[0]  # Remplacez 'Banana' par le titre exact de la fenêtre de votre application
window.activate()

# Obtenir la résolution de l'écran
screen_width, screen_height = pyautogui.size()

# Calculer les coordonnées du centre de l'écran
center_x, center_y = screen_width / 2, screen_height / 2

# Nombre total de clics
total_clicks = 100

# Démarrer le chronomètre
start_time = time.time()

# Cliquer le nombre de fois spécifié au centre de l'écran
for _ in range(total_clicks):
    pyautogui.click(center_x, center_y)

# Arrêter le chronomètre
end_time = time.time()

# Calculer le temps total passé
time_spent = end_time - start_time

# Calculer les clics par seconde
clicks_per_second = total_clicks / time_spent

# Imprimer les résultats
print(f"Clicked {total_clicks} times in {time_spent:.2f} seconds!")
print(f"Clicks per second: {clicks_per_second:.2f}")
