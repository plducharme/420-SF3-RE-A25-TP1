###########################
# nom1 (utilisateur github)
# nom2 (utilisateur github)
# nom3 (utilisateur github)
##########################
from PySide6.QtWidgets import QApplication, QMainWindow
import numpy as np
from scipy.io import wavfile

from filtres import AbstractFiltre, ReverberationFiltre, PasseBasFiltre, PasseHautFiltre
import sounddevice as sd



class LecteurAudio(QMainWindow):

    def __init__(self):
        super().__init__()



        # Données fichier audio
        self.frequence_echantillonnage_source = None
        self.signal_source = None
        self.signal_filtre = None


    def appliquer_filtres(self, filtres: list[AbstractFiltre]):

        signal_modifie = self.signal_source.astype(np.float32)

        for filtre in filtres:
            signal_modifie = np.array(filtre.filtrer(signal_modifie.tolist(), self.frequence_echantillonnage_source))


        # Normalisation du signal modifié (éviter la saturation)
        max_val = np.max(np.abs(signal_modifie))
        if max_val > 0:
            signal_modifie = signal_modifie / max_val

        return signal_modifie