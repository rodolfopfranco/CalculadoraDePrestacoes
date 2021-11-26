import unittest

from ..controller.Controller import cf_calculo, valor_a_prazo, valor_parcela, percentual_pago_a_mais, saldo_devedor, \
    amortizacao, juros_mes_atual, priceTable, getInterest, valor_presente_no_tempo_0


class CalcTest(unittest.TestCase ):

    def test_cf_calculo(self):
        juros = 1.6594
        parcelas = 12
        cf_teste = cf_calculo(juros, parcelas)
        self.assertEqual(round(cf_teste, 4), 0.0926)

    def test_valor_a_prazo(self):
        taxa_de_juros = 1.6594
        n_de_prestacoes = 12
        preco_a_vista = 1889.10
        valor_a_prazo_teste = valor_a_prazo(taxa_de_juros, n_de_prestacoes, preco_a_vista)
        self.assertEqual(round(valor_a_prazo_teste, 2), 2099.00)

    def test_valor_parcela(self):
        valor_financiado = 1889.10
        juros = 1.66
        parcelas = 12
        valor_parcela_teste = valor_parcela(valor_financiado, juros, parcelas)
        self.assertEqual(round(valor_parcela_teste, 2), 174.92)

    def test_percentual_pago_a_mais(self):
        valor_inicial = 1889.10
        valor_final = 2099.00
        percentual_pago_a_mais_teste = percentual_pago_a_mais(valor_inicial,valor_final)
        self.assertEqual(round(percentual_pago_a_mais_teste,2),10.00)

    def test_saldo_devedor(self):
        valor_da_prestacao = 269.03
        juros = 3
        numero_de_prestacoes = 4
        prestacao_atual = 2
        saldo_devedor_mes_2 = saldo_devedor(valor_da_prestacao, juros, numero_de_prestacoes, prestacao_atual)
        self.assertEqual(saldo_devedor_mes_2, 514.7807521915352)

    def test_amortizacao(self):
        valor_parcela =174.91
        juros = 1.66
        meses = 12
        amortizacao_teste = amortizacao(valor_parcela, juros, meses)
        self.assertEqual(amortizacao_teste, [0, 143.55336441846723, 145.9363502678138, 148.3588936822595,
                                             150.821651317385, 153.32529072925357, 155.8704905553592,
                                             158.45794069857814, 161.0883425141745, 163.76240899990984,
                                             166.4808649893083, 169.24444734813082, 172.0539051741098])

    def test_juros_mes_atual(self):
        juros = 3
        saldo_devedor_mes_anterior = 514.7807521915352
        juros_mes_3_teste = juros_mes_atual(juros, saldo_devedor_mes_anterior)
        self.assertEqual(juros_mes_3_teste, 15.443422565746054)

    def test_price_table(self):
        numero_de_parcelas = 12
        preco_a_vista = 1889.10
        taxa_juros = 1.6594
        price_table_teste = priceTable(numero_de_parcelas, preco_a_vista, taxa_juros)
        self.assertEqual(price_table_teste,
                         [['Mês', 'Prestação', 'Juros', 'Amortização', 'Saldo Devedor '],
                          [1, 174.91701547592277, 31.3477254, 143.56929007592277, 1745.5307099240777],
                          [2, 174.91701547592277, 28.965336600480146, 145.95167887544264, 1599.5790310486348],
                          [3, 174.91701547592277, 26.543414441221046, 148.37360103470172, 1451.2054300139325],
                          [4, 174.91701547592277, 24.0813029056512, 150.83571257027157, 1300.3697174436609],
                          [5, 174.91701547592277, 21.57833509126011, 153.33868038466267, 1147.031037058999],
                          [6, 174.91701547592277, 19.03383302895703, 155.88318244696575, 991.1478546120323],
                          [7, 174.91701547592277, 16.447107499432065, 158.4699079764907, 832.6779466355424],
                          [8, 174.91701547592277, 13.817457846470191, 161.09955762945256, 671.5783890060903],
                          [9, 174.91701547592277, 11.144171787167064, 163.7728436887557, 507.8055453173346],
                          [10, 174.91701547592277, 8.42652521899585, 166.4904902569269, 341.31505506040725],
                          [11, 174.91701547592277, 5.663782023672399, 169.25323345225036, 172.06182160815698],
                          [12, 174.91701547592277, 2.855193867765757, 172.061821608157, 0.0],
                          ['Total', 2099.0041857110728, 209.90418571107287, 1889.1000000000004, 0.0]])

    def test_get_interest(self):
        preco_a_prazo = 2099.00
        preco_a_vista = 1889.10
        numero_de_prestacoes = 12
        getInterest_teste = getInterest(preco_a_prazo, preco_a_vista, numero_de_prestacoes)
        self.assertEqual(getInterest_teste, (1.6593678678975252, 7))

    def test_valor_presente_no_tempo_0(self):
        valor_final = 2099.00
        numero_de_parcelas = 12
        taxa_de_juros = 1.6594
        entrada = False
        valor_a_vista_teste = valor_presente_no_tempo_0(valor_final, numero_de_parcelas, taxa_de_juros, entrada)
        self.assertEqual(valor_a_vista_teste, 1889.096232867546)