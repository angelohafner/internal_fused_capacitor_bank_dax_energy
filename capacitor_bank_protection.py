class CapacitorBank_InternalFused:
    def __init__(self, S=4, Pt=11, Pa=6, P=3, G=0, N=14, Su=3, f=0):
        """
        Parâmetros:
        - S: Número de grupos em série linha-neutro (padrão: 4)
        - Pt: Número de unidades paralelas por fase (padrão: 11)
        - Pa: Número de unidades paralelas por fase na configuração wye à esquerda (padrão: 6)
        - P: Número de unidades paralelas na string afetada (padrão: 3)
        - G: Estado de aterramento (0 = aterrado, 1 = não aterrado, padrão: 0)
        - N: Número de elementos paralelos em um grupo (padrão: 14)
        - Su: Número de grupos em série em uma unidade de capacitor (padrão: 3)
        """
        self.S = S
        self.Pt = Pt
        self.Pa = Pa
        self.P = P
        self.G = G
        self.N = N
        self.Su = Su
        self.f = f

        # Cálculos de capacitância
        self.Ci = self.calculate_Ci()
        self.Cu = self.calculate_Cu()
        self.Cg = self.calculate_Cg()
        self.Cs = self.calculate_Cs()
        self.Cp = self.calculate_Cp()

        # Cálculos de tensão (ajustada a ordem)
        self.Vng = self.calculate_Vng()
        self.Vln = self.calculate_Vln()
        self.Vcu = self.calculate_Vcu()
        self.Vg = self.calculate_Vg()
        self.Ve = self.calculate_Ve()

        # Cálculos de corrente
        self.Iu = self.calculate_Iu()
        self.Ist = self.calculate_Ist()
        self.Iph = self.calculate_Iph()
        self.Ig = self.calculate_Ig()
        self.In = self.calculate_In()
        self.Id = self.calculate_Id()

    def calculate_Ci(self):
        Ci = (self.N - self.f) / self.N
        return Ci

    def calculate_Cu(self):
        num = self.Su * self.Ci
        den = self.Ci * (self.Su - 1) + 1
        Cu = num / den
        return Cu

    def calculate_Cg(self):
        num = self.P - 1 + self.Cu
        Cg = num / self.P
        return Cg

    def calculate_Cs(self):
        num = self.S * self.Cg
        den = self.Cg * (self.S - 1) + 1
        Cs = num / den
        return Cs

    def calculate_Cp(self):
        num = (self.Cs * self.P) + self.Pt - self.P
        Cp = num / self.Pt
        return Cp

    def calculate_Vng(self):
        Vng = self.G * (3 / (2 + self.Cp) - 1)
        return Vng

    def calculate_Vln(self):
        Vln = 1 + self.Vng
        return Vln

    def calculate_Vcu(self):
        num = self.Vln * self.Cs
        Vcu = num / self.Cg
        return Vcu

    def calculate_Vg(self):
        num = self.Su * self.N
        den = (self.Su-1)*(self.N-self.f) + self.N
        Vg = num / den
        return Vg

    def calculate_Ve(self):
        Ve = self.Vcu * self.Vg
        return Ve

    def calculate_Iu(self):
        Iu = self.Vcu * self.Cu
        return Iu

    def calculate_Ist(self):
        Ist = self.Vln * self.Cs
        return Ist

    def calculate_Iph(self):
        Iph = self.Vln * self.Cp
        return Iph

    def calculate_Ig(self):
        Ig = (1 - self.G) * (1 - self.Iph)
        return Ig

    def calculate_In(self):
        In = 3 * self.Vng * self.G * (self.Pt - self.Pa) / self.Pt
        return In

    def calculate_Id(self):
        Id = self.Vln * (1 - self.Cp)
        return Id


