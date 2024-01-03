import matplotlib.pyplot as plt
# Para crear las gráficas

def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots() # (fig) y (ax) son variables de matplotlib
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png') # Esta línea nos permite guardar las imagenes que generemos en la carpeta imágenes, con su respectivo nombre.
  plt.close() # Esta línea nos permite guardar la imagen sin necesidad de detener el programa (main.py), como cuando se tiene 'plt.show()'.

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels) # Aquí se le indica cuales son los lebels.
  ax.axis('equal')
  plt.savefig('chart_pie_01.png') # Guarda el archivo.
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  # generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)