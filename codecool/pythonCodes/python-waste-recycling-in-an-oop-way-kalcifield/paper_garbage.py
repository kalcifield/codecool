from garbage import Garbage


class PaperGarbage(Garbage):

    def __init__(self, name, state):
        Garbage.__init__(self, name)
        if state:
            self.squeeze()
        else:
            self.is_squeezed = False

    def squeeze(self):
        self.is_squeezed = True