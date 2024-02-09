from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import os
import random
import string

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        # Label pour afficher le répertoire courant
        self.current_dir_label = Label(
            text="Répertoire courant : Pas encore créé"
        )
        self.layout.add_widget(self.current_dir_label)
        
        # Bouton pour créer un fichier texte avec un nom aléatoire
        self.create_file_button = Button(
            text="Créer un fichier",
            pos_hint={'center_x': 0.5},
            on_press=self.create_random_file
        )
        self.layout.add_widget(self.create_file_button)
        
        return self.layout
    
    def create_random_file(self, instance):
        # Chemin vers le dossier DCIM sur Android
        dcim_path = '/storage/emulated/0/DCIMT'
        
        # Vérifiez si le dossier DCIM existe, sinon créez-le
        if not os.path.exists(dcim_path):
            os.makedirs(dcim_path)
        
        # Générer un nom de fichier aléatoire
        random_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + ".txt"
        
        # Chemin complet du fichier dans le dossier DCIM
        file_path = os.path.join(dcim_path, random_filename)
        
        # Créer le fichier texte
        with open(file_path, 'w') as file:
            file.write("Contenu du fichier.")
        
        # Mettre à jour le label avec le nouveau répertoire courant
        self.current_dir_label.text = f"Répertoire courant : {dcim_path}"

if __name__ == '__main__':
    MyApp().run()
