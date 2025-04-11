import numpy as np
import capacitor_bank_protection as cbp


def various_burned_fused(base_voltage, base_current, voltage_bank_work,
                         S=4, Pt=11, Pa=6, P=3, G=1, N=14, Su=3):
    casas_decimais = 4
    fear_factor = base_voltage / voltage_bank_work
    data_ieeec3799 = []
    f_values = np.arange(0, N, 1)

    for f in f_values:
        bank = cbp.CapacitorBank_InternalFused(S=S, Pt=Pt, Pa=Pa, P=P, G=G, N=N, Su=Su, f=f)
        row = {
            'f': f,
            'Ci [pu]': round(bank.Ci, casas_decimais),
            'Cu [pu]': round(bank.Cu, casas_decimais),
            'Cg [pu]': round(bank.Cg, casas_decimais),
            'Cs [pu]': round(bank.Cs, casas_decimais),
            'Cp [pu]': round(bank.Cp, casas_decimais),
            'Vng [pu]': round(bank.Vng, casas_decimais),
            'Vln [pu]': round(bank.Vln, casas_decimais),
            'Vcu [pu]': round(bank.Vcu, casas_decimais),
            'Vcu [pu_work]': round(bank.Vcu / fear_factor, casas_decimais),
            'Vg [pu]': round(bank.Vg, casas_decimais),
            'Ve [pu]': round(bank.Ve, casas_decimais),
            'Iu [pu]': round(bank.Iu, casas_decimais),
            'Ist [pu]': round(bank.Ist, casas_decimais),
            'Iph [pu]': round(bank.Iph, casas_decimais),
            'Ig [pu]': round(bank.Ig, casas_decimais),
            'In [pu]': round(bank.In, casas_decimais),
            'In [A]': round(base_current * bank.In, 2),
            'Vng [V]': round(base_voltage / np.sqrt(3) * bank.Vng, 2)
        }
        data_ieeec3799.append(row)

        data_units_and_elements = [
            {'series group line to neutral - S': S},
            {'total parallels units per phase - Pt': Pt},
            {'parallels units per phase in "left" wye': Pa},
            {'parallels units in affected string - P': P},
            {'(0=grounded, 1=ungrounded) - G': G},
            {'parallels elements inside a unit - N': N},
            {'series elements inside a unit - Su': Su}
        ]

    return data_ieeec3799, data_units_and_elements


def calculate_bank_parameters(frequency, bank_power, bank_voltage):
    angular_frequency = 2 * np.pi * frequency
    bank_current = bank_power / (np.sqrt(3) * bank_voltage)
    bank_reactance = bank_voltage ** 2 / bank_power
    bank_capacitance = 1 / (angular_frequency * bank_reactance)
    return (bank_current,
            bank_reactance,
            bank_capacitance)
