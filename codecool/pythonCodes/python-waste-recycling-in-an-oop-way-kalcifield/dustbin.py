from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin_content_error import DustbinContentError


class Dustbin:

    def __init__(self, color):
        self.color = color
        self.paper_content = []
        self.plastic_content = []
        self.house_waste_content = []

    def throw_out_garbage(self, garbage):
        if isinstance(garbage, Garbage):
            if isinstance(garbage, PaperGarbage):
                if garbage.is_squeezed == True:
                    self.paper_content.append(garbage.name)
                else:
                    raise DustbinContentError(garbage)
            elif isinstance(garbage, PlasticGarbage):
                if garbage.is_clean == True:
                    self.plastic_content.append(garbage.name)
                else:
                    raise DustbinContentError(garbage)
            else:
                self.house_waste_content.append(garbage.name)
        else:
            raise DustbinContentError

    def empty_contents(self):
        self.paper_content = []
        self.plastic_content = []
        self.house_waste_content = []