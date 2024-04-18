# Fide

Fide è un'applicazione web basata su FastAPI per gestire le finanze personali.

## Requisiti

- Python 3.7 o versioni successive
- Pip (preferibilmente Pipenv per la gestione delle dipendenze)

## Installazione

1. Clona il repository:

    ```bash
    git clone https://github.com/tuonome/fide.git
    ```

2. Naviga nella directory del progetto:

    ```bash
    cd fide
    ```

3. Crea un ambiente virtuale (opzionale, ma consigliato):

    ```bash
    python -m venv venv
    ```

4. Attiva l'ambiente virtuale (se hai creato uno):

    - Su Windows:

    ```bash
    venv\Scripts\activate
    ```

    - Su macOS e Linux:

    ```bash
    source venv/bin/activate
    ```

5. Installa le dipendenze:

    ```bash
    pip install -r requirements.txt
    ```

## Configurazione

1. Copia il file `.env.example` in un nuovo file chiamato `.env`:

    ```bash
    cp .env.example .env
    ```

2. Modifica il file `.env` secondo le tue esigenze.

## Utilizzo

1. Avvia il server FastAPI:

    ```bash
    uvicorn app.main:app --reload
    ```

2. Visita `http://localhost:8000` nel tuo browser per utilizzare l'applicazione.

## Contribuisci

Se vuoi contribuire a Fide, segui questi passaggi:

1. Fork il repository (https://github.com/tuonome/fide/fork)
2. Crea un branch con il tuo lavoro: `git checkout -b feature/nuova-funzionalita`
3. Fai il commit delle tue modifiche: `git commit -am 'Aggiungi una nuova funzionalità'`
4. Pusha il tuo branch: `git push origin feature/nuova-funzionalita`
5. Invia una pull request

## Licenza

Questo progetto è distribuito sotto i termini della licenza MIT. Vedi il file `LICENSE` per maggiori informazioni.

