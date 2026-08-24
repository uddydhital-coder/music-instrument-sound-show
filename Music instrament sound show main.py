from abc import ABC, abstractmethod



class Instrument(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass



class Guitar(Instrument):

    def __init__(self, name, strings):
        super().__init__(name)
        self.strings = strings

    def make_sound(self):
        print(f"The {self.name} ({self.strings}-string) goes: Strum strum! 🎸")



class Piano(Instrument):

    def __init__(self, name, keys):
        super().__init__(name)
        self.keys = keys

    def make_sound(self):
        print(f"The {self.name} ({self.keys}-key) goes: Plink plonk! 🎹")



class Drum(Instrument):

    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print(f"The {self.name} goes: Boom boom tap! 🥁")



instruments = [
    Guitar("Acoustic Guitar", 6),
    Piano("Grand Piano", 88),
    Drum("Bass Drum"),
]

print("--- 🎶 Music Instrument Sound Show 🎶 ---")
for instrument in instruments:
    instrument.make_sound()
