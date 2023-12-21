import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)
  '''

  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data)) 
  # Filtramos por la columna 'Continent' y de ahí, 'South America'.
  
  countries = list(map(lambda x: x['Country'], data)) # Traemos la información de todos los países.
  percentages = list(map(lambda x: x['World Population Percentage'], data))  
  charts.generate_pie_chart(countries, percentages) # Traemos los porcentajes para realizar un 'Chart_pie'.
  
  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)
    # En esta linea hicimos que cada vez que generemos el bar_chart quede con el nombre del país del cual se está formando la gráfica.
    # Se hicieron modificaciones tanto en el archivo main.py como en chats.py, donde agregamos 'name' a las variables de la función.

if __name__ == '__main__':
  run()