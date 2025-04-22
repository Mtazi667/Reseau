from utils.fichiers import ecrire_L_ecr
from utils.fichiers import ecrire_L_ecr, ecrire_L_lec
import random

class EntiteReseau:
    def __init__(self, ET):
        self.ET = ET
        self.connexions_actives = {}

    def recevoir_demande_connexion(self, id_demande, src, dest):
        if src % 27 == 0:
            self.envoyer_paquet_liberation(id_demande, src, dest, "00000010")
            self.ET.recevoir_confirmation(id_demande, False)
        else:
            num_connexion = random.randint(1, 254)
            self.connexions_actives[id_demande] = num_connexion
            self.envoyer_paquet_appel(num_connexion, src, dest)

            if src % 19 == 0 or src % 13 == 0:
                raison = "00000001"
                self.envoyer_paquet_liberation(id_demande, src, dest, raison)
                self.ET.recevoir_confirmation(id_demande, False)
            else:
                self.envoyer_paquet_confirmation(num_connexion, src, dest)
                self.ET.recevoir_confirmation(id_demande, True)

    def envoyer_paquet_appel(self, num_connexion, src, dest):
        paquet = f"{num_connexion},00001011,{src},{dest}"
        ecrire_L_ecr(paquet)

    def envoyer_paquet_confirmation(self, num_connexion, src, dest):
        paquet = f"{num_connexion},00001111,{src},{dest}"
        ecrire_L_ecr(paquet)

    def envoyer_paquet_liberation(self, id_demande, src, dest, raison_code):
        paquet = f"{id_demande},00010011,{src},{dest},{raison_code}"
        ecrire_L_ecr(paquet)
        ecrire_L_lec(f"LIB:{paquet}")

    def recevoir_donnees(self, id_demande, donnees):
        num_connexion = self.connexions_actives.get(id_demande)
        if not num_connexion:
            return

        segments = [donnees[i:i+128] for i in range(0, len(donnees), 128)]
        for idx, segment in enumerate(segments):
            bit_M = 1 if idx < len(segments) - 1 else 0
            paquet_donnees = f"{num_connexion},DATA,p(s)={idx % 8},M={bit_M},{segment}"
            ecrire_L_lec(f"DATA:{paquet_donnees}")

            if not self.simuler_acquittement(id_demande, idx):
                ecrire_L_lec(f"REEMIS:{paquet_donnees}")


    def simuler_acquittement(self, id_demande, num_paquet):
        src = int(self.connexions_actives[id_demande])
        if src % 15 == 0 or num_paquet == random.randint(0,7):
            return False
        return True
    
    def recevoir_lib_request(self, id_demande):
        num_connexion = self.connexions_actives.get(id_demande)
        if num_connexion:
            paquet = f"{num_connexion},00010011,FIN"
            ecrire_L_ecr(paquet)
            del self.connexions_actives[id_demande]

def envoyer_paquet_confirmation(self, num_connexion, src, dest):
    paquet = f"{num_connexion},00001111,{src},{dest}"
    ecrire_L_ecr(paquet)
    ecrire_L_lec(f"CONFIRM:{paquet}")
