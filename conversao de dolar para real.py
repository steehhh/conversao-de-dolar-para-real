print("\nvamos fazer uma conversao de dolar?")
print("\nprimeiro voce vai escrever qual é a cotacao do dolar.")

cotacaodolar = int(input("\n\nentao digite a cotação do dolar hj:  "))
print("\nvoce digitou a cotacao do dolar, que é: ", cotacaodolar, "")

valor_em_dolares = int(input("\n\nagora digite quantos dolares vc quer converter: "))
print("\nvoce digitou: ", valor_em_dolares,"dolares")

valor_em_reais = cotacaodolar * valor_em_dolares
print("\n\nvoce terá:", valor_em_reais, "reais")