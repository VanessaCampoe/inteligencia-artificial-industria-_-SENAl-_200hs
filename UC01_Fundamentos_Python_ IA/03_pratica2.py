# Imports necessários
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

class MonitorTemperatura:
    def __init__(self, limite_min=20, limite_max=80):
        self.leituras = []
        self.limite_min = limite_min
        self.limite_max = limite_max

    def adicionar_leitura(self, temperatura):
        print(f"Nova leitura adicionada: {temperatura}°C")
        self.leituras.append(temperatura)

    def calcular_estatisticas(self):
        if not self.leituras:
            print("Nenhuma leitura registrada.")
            return None

        dados = np.array(self.leituras)
        estatisticas = {
            'mínima': np.min(dados),
            'máxima': np.max(dados),
            'média': np.mean(dados)
        }

        print("\nEstatísticas de Temperatura:")
        print(f"Mínima: {estatisticas['mínima']}°C")
        print(f"Máxima: {estatisticas['máxima']}°C")
        print(f"Média: {estatisticas['média']:.2f}°C")

        return estatisticas

    def verificar_segurança(self):
        print("\nVerificação de segurança:")
        for i, temp in enumerate(self.leituras):
            if temp < self.limite_min or temp > self.limite_max:
                print(f"Alerta! Leitura {i+1}: {temp}°C fora do intervalo seguro ({self.limite_min}°C - {self.limite_max}°C)")
            else:
                print(f"Leitura {i+1}: {temp}°C dentro do intervalo seguro.")

#  uso
if __name__ == "__main__":
    monitor = MonitorTemperatura()
    leituras_exemplo = [22, 75, 19, 85, 60, 40]

    for leitura in leituras_exemplo:
        monitor.adicionar_leitura(leitura)

    monitor.calcular_estatisticas()
    monitor.verificar_segurança()
