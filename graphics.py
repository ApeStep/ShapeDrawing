from abc import ABC, abstractmethod


# INTERFACE FOR IMPLEMENTATION


class Graphics(ABC):

    # ABSTRACT METHOD TO DEFINE THE TYPE OF GRAPHICS THAT IS NEEDED

    @abstractmethod
    def create_graphics(self):
        pass
