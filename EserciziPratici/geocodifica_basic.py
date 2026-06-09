import requests
import xml.etree.ElementTree as ET

# Inserisci qui la tua chiave API di Google (opzionale)
# Per usare il servizio didattico, lascia API_KEY = None
API_KEY = None  # Es: 'AIzaSy___IDByT70'

# Scegli l'endpoint in base alla presenza della chiave
if API_KEY is None:
    # Servizio didattico (accetta chiave fittizia 42, risponde in XML)
    SERVICE_URL = 'http://py4e-data.dr-chuck.net/xml?'
    USE_GOOGLE = False
else:
    # Google Geocoding API (JSON è lo standard moderno)
    SERVICE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?'
    USE_GOOGLE = True

while True:
    address = input('Enter location: ')
    if not address.strip():
        break

    # Prepara i parametri della richiesta
    params = {'address': address}
    if USE_GOOGLE:
        params['key'] = API_KEY
    else:
        params['key'] = 42  # Chiave fittizia per il servizio didattico

    try:
        # Richiesta HTTP con timeout di 10 secondi (buona pratica)
        response = requests.get(SERVICE_URL, params=params, timeout=10)
        response.raise_for_status()  # Solleva eccezione per errori HTTP (4xx, 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Errore di connessione: {e}")
        continue

    data = response.text
    print(f"Retrieved {len(data)} characters")

    # Parsing della risposta (XML o JSON)
    if USE_GOOGLE:
        # Risposta JSON (Google)
        try:
            js = response.json()
        except ValueError:
            print("Errore nel parsing JSON")
            continue

        if js['status'] != 'OK':
            print(f"Errore API: {js['status']}")
            continue

        if not js['results']:
            print("Nessun risultato trovato.")
            continue

        result = js['results'][0]
        lat = result['geometry']['location']['lat']
        lng = result['geometry']['location']['lng']
        location = result['formatted_address']
    else:
        # Risposta XML (servizio didattico)
        try:
            tree = ET.fromstring(data)
        except ET.ParseError:
            print("Errore nel parsing XML")
            continue

        results = tree.findall('result')
        if not results:
            print("Nessun risultato trovato.")
            continue

        result = results[0]
        # Navigazione sicura con find (evita AttributeError)
        geometry = result.find('geometry')
        if geometry is None:
            print("Dati geometry mancanti")
            continue
        location_elem = geometry.find('location')
        if location_elem is None:
            print("Dati location mancanti")
            continue
        lat_elem = location_elem.find('lat')
        lng_elem = location_elem.find('lng')
        if lat_elem is None or lng_elem is None:
            print("Coordinate mancanti")
            continue
        lat = lat_elem.text
        lng = lng_elem.text
        formatted = result.find('formatted_address')
        location = formatted.text if formatted is not None else "Indirizzo non disponibile"

    print(f'lat {lat}, lng {lng}')
    print(location)
    