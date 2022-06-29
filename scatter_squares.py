import matplotlib.pyplot as plt

# Calculando dados automaticamente.

x_values = (range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolors='none', s=40)

# Define o título do gráfico e nomeia os eixos

plt.title('Números ao quadrado', fontsize=24)
plt.xlabel('Valor', fontsize=14)
plt.ylabel('Quadrado do valor', fontsize=14)

# Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('squares_plot.png', bbox_inches='tight')
