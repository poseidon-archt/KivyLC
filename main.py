from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import os
import random
import string
from jnius import autoclass  # Importez autoclass de Pyjnius

Environment = autoclass('android.os.Environment')
File = autoclass('java.io.File')

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.current_dir_label = Label(
            text="Répertoire courant : Pas encore défini"
        )
        self.layout.add_widget(self.current_dir_label)

        self.create_file_button = Button(
            text="Créer un fichier",
            pos_hint={'center_x': 0.5},
            on_press=self.create_random_file
        )
        self.layout.add_widget(self.create_file_button)

        return self.layout

    def create_random_file(self, instance):
        # Obtenez le stockage externe puis ajoutez le dossier DCIM
        dcim_path = File(Environment.getExternalStorageDirectory(), "DCIMT").getAbsolutePath()

        # Générer un nom de fichier aléatoire
        random_filename = ''.join(random.choices(string.ascii_letters, k=8)) + ".txt"

        # Chemin complet du fichier dans le dossier DCIM
        file_path = os.path.join(dcim_path, random_filename)

        # Créer le fichier texte
        with open(file_path, 'w') as file:
            file.write("Contenu du fichier.")

        # Mettre à jour le label avec le chemin du dossier DCIM
        self.current_dir_label.text = f"Répertoire courant : {dcim_path}"

if __name__ == '__main__':
    MyApp().run()
