import requests

def test_json_response():
    # Esegui una richiesta GET all'endpoint del server FastAPI
    response = requests.get("http://192.168.1.26:8000/events")

    # Verifica se la richiesta ha avuto successo
    assert response.status_code == 200

    # Verifica se il contenuto della risposta è JSON
    try:
        json_data = response.json()
        # Ora puoi lavorare con il JSON restituito
        print(json_data)
    except ValueError:
        # Se il contenuto non è JSON, stampa un messaggio di errore
        print("La risposta non è in formato JSON")

