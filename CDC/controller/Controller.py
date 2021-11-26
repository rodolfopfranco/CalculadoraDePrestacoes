# Referências:
# p. 105-109 https://educapes.capes.gov.br/bitstream/capes/430116/2/eBook_Matem%C3%A1tica_Financeira_UFBA.pdf
# https://pt.wikipedia.org/wiki/Tabela_Price#cite_note-3

class MesTabelaPrice:
    """Classe utilizada para a organização de dados dos meses"""
    def __init__(self, mes, juros, amortizacao, saldo_devedor):
        self.mes = mes
        self.juros = juros
        self.amortizacao = amortizacao
        self.saldo_devedor = saldo_devedor


def cf_calculo(juros, parcelas):
    """Calcula o coeficiente de financiamento"""
    i = juros / 100
    n = parcelas
    cf = i / (1 - ((1 + i) ** -n))
    return cf


def valor_a_prazo(taxa_de_juros, n_de_prestacoes, preco_a_vista):
    """Encontra o valor à prazo usando os juros, prestação e preço à vista"""
    return n_de_prestacoes*(preco_a_vista*cf_calculo(taxa_de_juros, n_de_prestacoes))


def valor_parcela(valor_financiado, juros, parcelas):
    """Encontra o valor da parcela usando o valor financiado, juros e quantidade de parcelas"""
    cf = cf_calculo(juros,parcelas)
    return valor_financiado * cf


def percentual_pago_a_mais(valor_inicial,valor_final):
    """Encontra o percentual à mais a partir do valor final e do inicial"""
    A = valor_final
    y = valor_inicial
    percentual_pago_a_mais = (A - y) / A * 100
    return percentual_pago_a_mais


def saldo_devedor(valor_da_prestacao, juros, numero_de_prestacoes, prestacao_atual):
    """Encontra o saldo devedor em uma mensalidade específica"""
    r = valor_da_prestacao
    i = juros / 100
    n = numero_de_prestacoes
    t = prestacao_atual
    return r*((((1+i)**(n-t))-1)/(i*(1+i)**(n-t)))


def amortizacao(valor_parcela, juros, meses):
    """Encontra a amortização para todos os meses a partir dos dados passados"""
    pmt = valor_parcela
    i = juros / 100
    valores_amortizados = [0] * (meses+1)
    for j in range(meses, 0, -1):
        amortizacao = pmt / ((1 + i) ** j)
        mes = meses-j+1
        valores_amortizados[mes] = amortizacao
    return valores_amortizados


def juros_mes_atual(juros, saldo_devedor_mes_anterior):
    """O saldo devedor deve ser o do mês anterior ao do juros de agora"""
    i = juros / 100
    PV = saldo_devedor_mes_anterior
    J = i * PV
    return J


def priceTable(numero_de_parcelas, preco_a_vista, taxa_juros):
    """ Gera a Tabela Price (sem o uso do pmt como parâmetro, pois é gerado dentro)"""
    p = numero_de_parcelas
    t = taxa_juros
    y = preco_a_vista
    tabela_price = []
    primeiro_mes = MesTabelaPrice(0,t,0,y)
    tabela_price.append(primeiro_mes)
    # pmt gerado aqui:
    parcela = valor_parcela(y, t, p)
    # Inclui os objetos de cada mês com juros, parcela e saldo
    for i in range(0,p):
        mes = i+1
        juros = juros_mes_atual(t,tabela_price[i].saldo_devedor)
        saldo = saldo_devedor(parcela,t,p,mes)
        mes_atual = MesTabelaPrice(mes,juros,0,saldo)
        tabela_price.append(mes_atual)
    # Inclui a amortização para os meses:
    valores_amortizados = amortizacao(parcela,t,p)
    for mes in range(0,len(tabela_price)):
        tabela_price[mes].amortizacao = valores_amortizados[mes]
    #Transforma a estrutura de dados para matriz:
    matriz_tabela_price = []
    matriz_tabela_price.append(['Mês', 'Prestação', 'Juros', 'Amortização', 'Saldo Devedor '])
    for registro in tabela_price:
        linha = [registro.mes, parcela, registro.juros, registro.amortizacao, registro.saldo_devedor]
        matriz_tabela_price.append(linha)
    # remove a linha com os registros iniciais para poder passar nos testes:
    matriz_tabela_price.pop(1)
    # inclui a linha de total:
    total_prestacoes = 0
    total_juros = 0
    total_amortizacao = 0
    total_saldo_devedor = 0
    for registro in matriz_tabela_price:
        if registro[0]=='Mês':
            continue
        total_prestacoes += float(registro[1])
        total_juros += float(registro[2])
        total_amortizacao += float(registro[3])
        total_saldo_devedor = float(registro[4])
    linha = ['Total', total_prestacoes, total_juros, total_amortizacao, total_saldo_devedor]
    matriz_tabela_price.append(linha)
    return matriz_tabela_price


def getInterest(preco_a_prazo, preco_a_vista, numero_de_prestacoes):
    """Encontra a taxa de juros"""
    x = preco_a_prazo
    y = preco_a_vista
    p = numero_de_prestacoes
    t = x/y
    t_anterior = 10
    interacao = 0
    while (t_anterior-t >= 0.0001):
        a = (1 + t) ** (-p)
        b = (1 + t)** (-p-1)
        f = y*t - ((x / p)*(1-a))
        fd = y - (x * b)
        t_anterior = t
        t = t - (f/fd)
        interacao += 1
    return t*100, interacao


def valor_presente_no_tempo_0(valor_final_do_emprestimo, numero_de_parcelas, taxa_de_juros, entrada):
    """Encontra o valor à vista a partir do valor financiado"""
    # A = Valor_a_vista
    x = valor_final_do_emprestimo
    p = numero_de_parcelas
    t = taxa_de_juros
    CF = cf_calculo(taxa_de_juros,numero_de_parcelas)
    if entrada:
        FE = 1 + t
    else:
        FE = 1
    A = x / p * (FE / CF)
    return A
