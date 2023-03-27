import threading
import ctypes

# Class AbortableThread
class AbortableThread(threading.Thread):
    # Constructeur Renseigné
    def __init__(self, *args, **keywords):
        # Parent
        super().__init__(*args, **keywords)

        # Default
        self.event_kill = threading.Event()
        self.remain_to_kill = False
        
    def get_id(self) -> int:
        """
        On récupére l'identifiant du thread.
        Retourne un entier (int).
        """

        # Check si le thread est démarré
        if not self.is_alive(): return None

        # On retourne l'identifiant (python) du thread
        return self.ident
    
    def wait(self, timeout: float) -> bool:
        """
        On mets en pause le thread jusqu'à un timeout (en secondes).
        Attention: La fonction "wait" sera avortée si la fonction "stop" ou "kill" est exécutée.
        """

        # On mets en pause le thread et après
        self.event_kill.wait(timeout=timeout)

        # Si l'event kill a été trigger et qu'on veut fermer le thread, on ferme le thread
        if self.remain_to_kill: self.kill()

        # On reset le trigger
        self.event_kill.clear()

        # Succès
        return True

    def safe_zone(self) -> bool:
        """
        On reseigne au thread qu'on est dans une "zone de sécurité"
        et que si on kill le thread il n'y aura pas de conflit. Ex: fichier qui ne se ferme pas, etc...
        """
    
        # Si on ne veut pas fermer le thread
        if not self.remain_to_kill: return False

        # On essaye de kill le thread
        if not self.kill(): return False

        # Succès
        return True

    def stop(self) -> bool:
        """On dit au thread que dès qu'il entre en "safe zone" il doit s'auto kill."""

        # On renseigne au thread qu'on veut le fermer
        self.remain_to_kill = True

        # On trigger l'event kill
        self.event_kill.set()

        # Succès
        return True

    def kill(self) -> bool:
        """On force le thread à s'arrêter en injectant une exception."""
    
        # On essaye de récupérer l'identifiant du thread
        thread_id = self.get_id()
        if thread_id is None: return False

        # On demande de ne pas kill le thread pour éviter une boucle
        self.remain_to_kill = False

        # On trigger si besoin l'event et on le reset
        if not self.event_kill.is_set(): self.event_kill.set()
        self.event_kill.clear()

        # On essaye d'injecter une exception dans le thread pour le kill
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), ctypes.py_object(SystemExit))

        # Si il renvoie un nombre supérieur à '1' c'est qu'il y a un problème.
        # On doit donc l'appeler à nouveau avec exc=NULL pour annuler l'effet
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), None)
            return False

        # Succès
        return True