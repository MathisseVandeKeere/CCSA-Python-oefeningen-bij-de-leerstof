class GelinkteLijst:

    class Knoop:

        def __init__(self, data=None, volgende=None) -> None:
            self.data = data
            self.volgende = volgende

    
    def __init__(self) -> None:
        self.eerste = GelinkteLijst.Knoop()

    def zoek(self, element):
        ref = self.eerste.volgende
        while ref is not None and ref.data != element:
            ref = ref.volgende
        return ref
    
    def voeg_toe(self, ref, element):
        nieuwe_knoop = GelinkteLijst.Knoop(element, ref.volgende)
        ref.volgende = nieuwe_knoop
    
    def verwijder(self, ref): #ref = knoop vóór te verwijderen knoop
        x = ref.volgende.data
        ref.volgende = ref.volgende.volgende
        return x
    
    def size(self) -> int:
        aantal = 0
        ref = self.eerste.volgende
        while ref is not None:
            ref = ref.volgende
            aantal += 1
        return aantal

    def invert(self):
        lijst_inv = GelinkteLijst()

        ref = self.eerste.volgende
        while ref is not None:
            lijst_inv.voeg_toe(lijst_inv.eerste, ref.data)
            ref = ref.volgende
        return lijst_inv
