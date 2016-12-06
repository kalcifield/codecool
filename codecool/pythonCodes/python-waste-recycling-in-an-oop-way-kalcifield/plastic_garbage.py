from garbage import Garbage


class PlasticGarbage(Garbage):

    def __init__(self, name, state):
        Garbage.__init__(self, name)
        if state:
            self.clean()
        else:
            self.is_clean = False

    def clean(self):
        self.is_clean = True