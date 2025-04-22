from utils.fichiers import lire_S_lec, ecrire_S_ecr

class EntiteTransport:
    def __init__(self):
        self.demandes = lire_S_lec()
        self.connexions = {}
        self.ER = None

    def set_ER(self, ER):
        self.ER = ER

    def envoyer_demandes_connexion(self):
        for id_demande, demande in enumerate(self.demandes):
            src, dest = map(int, demande.split(','))
            self.connexions[id_demande] = 'En attente'
            print(f"ET envoie N_CONNECT.req (id={id_demande}, src={src}, dest={dest})")
            self.ER.recevoir_demande_connexion(id_demande, src, dest)

    def recevoir_confirmation(self, id_demande, acceptee):
        if acceptee:
            self.connexions[id_demande] = 'Établie'
            resultat = f"Connexion {id_demande} établie avec succès."
            self.envoyer_donnees(id_demande, "Message de test pour la connexion établie.")
        else:
            resultat = f"Connexion {id_demande} refusée/libérée."

        print(f"ET reçoit confirmation : {resultat}")
        ecrire_S_ecr(resultat)

    def envoyer_donnees(self, id_demande, donnees):
        if self.connexions.get(id_demande) == 'Établie':
            print(f"ET envoie N_DATA.req (id={id_demande}, donnees={donnees[:30]}...)")
            self.ER.recevoir_donnees(id_demande, donnees)

    def liberer_connexion(self, id_demande):
        if self.connexions.get(id_demande) == 'Établie':
            print(f"ET envoie N_DISCONNECT.req (id={id_demande})")
            self.ER.recevoir_lib_request(id_demande)
            del self.connexions[id_demande]
            ecrire_S_ecr(f"Connexion {id_demande} libérée proprement.")
        else:
            print(f"Connexion {id_demande} non libérable.")
