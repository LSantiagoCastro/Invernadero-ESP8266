import requests
import time

def data_request(url):
    # La direccion IP del ESP32
    
    
    try:
        response = requests.get(url)
        
        # verifica si la solicitud fue exitosa
        if response.status_code == 200:
            print(f'Estatus: {response.status_code}')
            print(f'Sensores: {response.text}')
            
            return response.text
        else:
            print(f'Error: Codigo de estado {response.status_code}')
    except requests.exceptions.RequestException as e:
        # Maneja excepciones que pueden ocurrir al hacer la solicitud
        print('Error al conectar al ESP32', e)
        
if __name__ == "__main__":
    data_request()