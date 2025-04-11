def generate_df_stylized(df, Vcu_max=1.1, Vcu_max_work=1.1):
    # Filtro para Vcu [pu] < Vcu_max
    filtro_vcu = df['Vcu [pu]'] < Vcu_max
    # Filtro para Vcu [pu_work] < Vcu_max_work
    filtro_vcu_work = df['Vcu [pu_work]'] < Vcu_max_work

    # Encontrar o índice da linha com Vcu [pu] < 1.1 mais próximo de 1.1
    idx_mais_proximo_vcu = None
    idx_acima_vcu = None
    if filtro_vcu.any():
        df_filtro_vcu = df[filtro_vcu].copy()
        df_filtro_vcu['diferenca_vcu'] = abs(df_filtro_vcu['Vcu [pu]'] - Vcu_max)
        idx_mais_proximo_vcu = df_filtro_vcu['diferenca_vcu'].idxmin()
        # Índice da linha imediatamente acima (se existir)
        idx_acima_vcu = idx_mais_proximo_vcu - 1 if idx_mais_proximo_vcu > df.index[0] else None

    # Encontrar o índice da linha com Vcu [pu_work] < 1.1 mais próximo de 1.1
    idx_mais_proximo_vcu_work = None
    if filtro_vcu_work.any():
        df_filtro_vcu_work = df[filtro_vcu_work].copy()
        df_filtro_vcu_work['diferenca_vcu_work'] = abs(df_filtro_vcu_work['Vcu [pu_work]'] - Vcu_max_work)
        idx_mais_proximo_vcu_work = df_filtro_vcu_work['diferenca_vcu_work'].idxmin()

    # Função para colorir as linhas
    def colorir_linhas(linha):
        if linha.name == idx_mais_proximo_vcu_work:  # Linha com Vcu [pu_work] mais próximo de Vcu_max_work
            return ['background-color: lightcoral'] * len(linha)  # Vermelho suave
        elif linha.name == idx_mais_proximo_vcu:  # Linha com Vcu [pu] mais próximo de Vcu_max
            return ['background-color: lightyellow'] * len(linha)  # Amarelo suave
        elif linha.name == idx_acima_vcu:  # Linha imediatamente acima de Vcu [pu]
            return ['background-color: lightblue'] * len(linha)  # Azul suave
        return [''] * len(linha)

    # Criar o objeto estilizado
    df_stylized = df.style.apply(colorir_linhas, axis=1)

    # Definir formatação para cada coluna
    format_dict = {}
    for i, col in enumerate(df.columns):
        if i == 0:  # Primeira coluna: inteiro
            format_dict[col] = '{:.0f}'
        elif i >= len(df.columns) - 2:  # Duas últimas colunas: 2 casas decimais
            format_dict[col] = '{:.2f}'
        else:  # Demais colunas: 4 casas decimais
            format_dict[col] = '{:.4f}'

    # Aplicar formatação
    df_stylized = df_stylized.format(format_dict)
    trip_current_max = df.loc[idx_mais_proximo_vcu_work, 'In [A]']
    trip_voltage_max = df.loc[idx_mais_proximo_vcu_work, 'Vng [V]']

    return df_stylized, trip_current_max, trip_voltage_max
