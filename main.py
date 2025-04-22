from utils.fichiers import vider_fichiers, vider_L_lec
from src.entite_transport import EntiteTransport
from src.entite_reseau import EntiteReseau

def main():
    vider_fichiers()
    vider_L_lec()
    ET = EntiteTransport()
    ER = EntiteReseau(ET)
    ET.set_ER(ER)

    ET.envoyer_demandes_connexion()

    # On libère manuellement la connexion 0 si elle est établie
    ET.liberer_connexion(0)

if __name__ == "__main__":
    main()
