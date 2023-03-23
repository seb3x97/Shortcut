
            
# On récupére l'identifiant du thread
def get_id(self):
    # returns id of the respective thread
    if hasattr(self, '_thread_id'):
        return self._thread_id
    for id, thread in threading._active.items():
        if thread is self:
            return id