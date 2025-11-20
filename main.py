from Pontellini_001 import EsprReg

def main():
    # Lista di espressioni regolari da testare (sono quelle dell'esercizio precedente)
    regex_patterns = [
        r"^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$",   # Data italiana gg/mm/aaaa
        r"^(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-\d{4}$",   # Data americana mm-gg-aaaa
        r"^(?:1\d{2}|2[0-4]\d|25[0-5])(?:\.(?:1\d{2}|2[0-4]\d|25[0-5])){3}$", # IPv4
        r"^[A-Z]{6}\d{2}[ABCEHLMPRST]\d{2}[A-Z]\d{3}[A-Z]$", # Codice fiscale
        r"^IT\d{2}[A-Z0-9]{1}\d{5}\d{5}[A-Z0-9]{12}$",       # IBAN italiano
        r"^https?:\/\/(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}(?:\/[\w./?%&=-]*)?$", # URL
        r"^[1-5][ABCEGHIJKLMNOPQRST]$"                       # Classi scolastiche
    ]

    # Stringhe di esempio da validare
    test_strings = [
        "20/11/2025",   # Data italiana
        "11-20-2025",   # Data americana
        "192.168.100.200", # IPv4 valido
        "RSSMRA85M01H501Z", # Codice fiscale valido
        "IT60X0542811101000000123456", # IBAN valido
        "https://www.example.com/test", # URL valido
        "3B" # Classe scolastica valida
    ]

    # Ciclo for di test
    for pattern, text in zip(regex_patterns, test_strings):
        checker = EsprReg(pattern)
        print(f"Pattern: {pattern}")
        print(f"Testo: {text} → {checker.validate(text)}\n")

if __name__ == "__main__":
    main()