import pandas as pd
from data_frame_estilizado import generate_df_stylized
from loop_over_burned_fuses import various_burned_fused, calculate_bank_parameters



def master_internal_fuses(f1, power_bank_rated, voltage_bank_rated, voltage_bank_work,
                          S, Pt, Pa, P, G, N, Su):
    (bank_current_rated,
     bank_reactance_rated,
     bank_capacitance_rated) = calculate_bank_parameters(f1, power_bank_rated, voltage_bank_rated)

    data_internal_fused, data_units_and_elements = various_burned_fused(base_voltage=voltage_bank_rated,
                                                                        base_current=bank_current_rated,
                                                                        voltage_bank_work=voltage_bank_work,
                                                                        S=S, Pt=Pt, Pa=Pa, P=P, G=G, N=N, Su=Su)

    df_data_internal_fused = pd.DataFrame(data_internal_fused)
    df_stylized, trip_current_max, trip_voltage_max = \
        generate_df_stylized(df=df_data_internal_fused, Vcu_max=1.1, Vcu_max_work=1.1)

    excel_file_name = 'capacitor_bank_results.xlsx'
    df_stylized.to_excel(excel_file_name, sheet_name='ieee_c37_99', index=False, engine='openpyxl')

    return df_stylized, trip_current_max, trip_voltage_max
