import os
import json
import pandas as pd


# Obtiene la ruta absoluta del directorio donde se encuentra este script
current_script_path = os.path.abspath(__file__)
# Obtiene la ruta del directorio del proyecto (asumiendo que este script está en la raíz del proyecto)
project_directory = os.path.dirname(current_script_path)
# Construye la ruta a la carpeta 'schedules' dentro del directorio del proyecto
path = os.path.join(project_directory, 'schedules')

# Lista para almacenar todos los datos
data = []
# Recorrer todos los archivos JSON en el directorio
for filename in os.listdir(path):
    if filename.endswith('.json'):
        file_path = os.path.join(path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            # Extraer la información relevante
            for unit in json_data.get('units', []):
                if 'competitors' in unit:
                    for competitor in unit['competitors']:
                        results = competitor.get('results', {})
                        data.append({
                            'DisciplineName': unit.get('disciplineName'),
                            'EventUnitName': unit.get('eventUnitName'),
                            'ID': unit.get('id'),
                            'DisciplineCode': unit.get('disciplineCode'),
                            'GenderCode': unit.get('genderCode'),
                            'EventCode': unit.get('eventCode'),
                            'PhaseCode': unit.get('phaseCode'),
                            'EventID': unit.get('eventId'),
                            'EventName': unit.get('eventName'),
                            'PhaseID': unit.get('phaseId'),
                            'PhaseName': unit.get('phaseName'),
                            'DisciplineID': unit.get('disciplineId'),
                            'EventOrder': unit.get('eventOrder'),
                            'PhaseType': unit.get('phaseType'),
                            'EventUnitType': unit.get('eventUnitType'),
                            'OlympicDay': unit.get('olympicDay'),
                            'StartDate': unit.get('startDate'),
                            'EndDate': unit.get('endDate'),
                            'Venue': unit.get('venue'),
                            'VenueDescription': unit.get('venueDescription'),
                            'Location': unit.get('location'),
                            'LocationDescription': unit.get('locationDescription'),
                            'Status': unit.get('status'),
                            'StatusDescription': unit.get('statusDescription'),
                            'CompetitorCode': competitor.get('code'),
                            'NOC': competitor.get('noc'),
                            'CompetitorName': competitor.get('name'),
                            'Position': results.get('position'),
                            'Mark': results.get('mark'),
                            'MedalType': results.get('medalType'),
                            'IRM': results.get('irm')
                        })

# Convertir la lista de diccionarios en un DataFrame de pandas
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv('resultados_olimpiadas.csv', index=False, encoding='utf-8')

print(f"Archivo CSV guardado en 'resultados_olimpiadas.csv'")
