import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def check_flag_in_h1(soup):
    """
    Controlla se nella pagina c'è un tag <h1> che contiene la flag.
    L'ipotesi è che la flag abbia il formato tipico, ad esempio 'flag{...}'.
    """
    h1 = soup.find('h1')
    if h1:
        testo = h1.get_text(strip=True)
        if "flag{" in testo:
            return testo
    return None

def crawl_and_find_flag(url, visited=None):
    """
    Funzione ricorsiva che:
      - Visita una pagina e la aggiunge all'insieme dei visitati.
      - Cerca la flag all'interno del tag <h1>.
      - Se la flag non è trovata, estrae tutti i link della pagina (con find_all su <a>)
        e li visita ricorsivamente, limitandosi ai link interni.
      
    L'URL viene normalizzato includendo eventuali parametri della query, in modo
    da considerare una pagina con parametri differenti come univoca.
    """
    if visited is None:
        visited = set()

    # Normalizzazione dell'URL: considera lo schema, il dominio, il path ed eventuale query
    parsed = urlparse(url)
    url_normalizzato = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    if parsed.query:
        url_normalizzato += f"?{parsed.query}"

    # Se abbiamo già visitato questa pagina, non la processiamo nuovamente
    if url_normalizzato in visited:
        return None
    visited.add(url_normalizzato)
    
    print("Visitando:", url_normalizzato)
    
    try:
        risposta = requests.get(url)
        risposta.raise_for_status()
        pagina_html = risposta.text
        soup = BeautifulSoup(pagina_html, 'html.parser')
        
        # Controlla se la pagina contiene la flag nel tag <h1>
        flag = check_flag_in_h1(soup)
        if flag:
            print("Flag trovata:", flag)
            return flag
        
        # Se la flag non è stata trovata, estrai tutti i link <a>
        for a in soup.find_all('a', href=True):
            # Costruisci l'URL completo (gestisce link relativi ed assoluti)
            link_url = urljoin(url, a['href'])
            # Filtra e continua solo se il link è interno (stesso dominio)
            if urlparse(link_url).netloc == urlparse(url).netloc:
                flag_trovata = crawl_and_find_flag(link_url, visited)
                if flag_trovata:
                    return flag_trovata
    except requests.RequestException as e:
        print(f"Errore durante il recupero di {url}: {e}")
    
    return None

# URL di partenza
url_base = "http://web-16.challs.olicyber.it/"
flag = crawl_and_find_flag(url_base)

if flag:
    print("La flag è:", flag)
else:
    print("Flag non trovata.")
