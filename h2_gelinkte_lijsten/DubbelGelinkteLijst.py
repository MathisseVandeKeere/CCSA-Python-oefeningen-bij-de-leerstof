class DubbelGelinkteLijst:

    class Knoop:

        def __init__(self, data=None, volgende=None, vorige=None) -> None:
            self.data = data
            self.volgende = volgende
            self.vorige = vorige

    
    def __init__(self) -> None:
        self.eerste = DubbelGelinkteLijst.Knoop()
        self.laatste = DubbelGelinkteLijst.Knoop()
        self.eerste.volgende = self.laatste
        self.laatste.vorige = self.eerste

    def zoek(self, element):
        ref_vooruit = self.eerste.volgende
        ref_achteruit = self.laatste.vorige
        while ref_vooruit.data != element and ref_achteruit.data != element and ref_vooruit != ref_achteruit and ref_vooruit.vorige != ref_achteruit:
            ref_vooruit = ref_vooruit.volgende
            ref_achteruit = ref_achteruit.vorige
        return ref
    
    def voeg_toe_voor(self, ref, element):
        self.voeg_toe_na(ref.vorige, element)
    
    def voeg_toe_na(self, ref, element):
        nieuwe_knoop = DubbelGelinkteLijst.Knoop()
        nieuwe_knoop.volgende = ref.volgende
        nieuwe_knoop.vorige = ref
        ref.volgende.vorige = nieuwe_knoop
        ref.volgende = nieuwe_knoop
    
    def verwijder(self, ref):
        x = ref.data
        ref.vorige.volgende = ref.volgende
        ref.volgende.vorige = ref.vorige
        return x
    
    def size(self) -> int:
        aantal = 0
        ref = self.eerste.volgende
        while ref != self.laatste:
            ref = ref.volgende
            aantal += 1
        return aantal

    def invert(self):
        lijst_inv = DubbelGelinkteLijst()

        ref = self.eerste.volgende
        while ref is not None:
            lijst_inv.voeg_toe(lijst_inv.eerste, ref.data)
            ref = ref.volgende
        return lijst_inv
