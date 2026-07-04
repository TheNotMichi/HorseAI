#!/usr/bin/env python3
"""
HorseAI Launcher
-----------------
Pequeño lanzador con interfaz de terminal: detecta los archivos .html
de la carpeta, te deja elegir cuál servir, y abre el navegador.

Uso:
    python3 serve.py                # menú interactivo
    python3 serve.py source.html    # lanza directo, sin preguntar
    python3 serve.py --port 8000
"""
import argparse
import http.server
import socketserver
import webbrowser
import os
import sys

BANNER = r"""
 _   _                    _    ___
| | | | ___  _ __ ___  ___/ \  |_ _|
| |_| |/ _ \| '__/ __|/ _ \ _ \ | |
|  _  | (_) | |  \__ \  __/ ___ \| |
|_| |_|\___/|_|  |___/\___\_/ \_\___|

        HorseAI · Launcher local
"""

def find_html_files(directory):
    return sorted(f for f in os.listdir(directory) if f.lower().endswith(".html"))

def choose_file(files):
    # Se mantiene por compatibilidad, pero ya no se usa
    print(BANNER)
    if not files:
        print("No encontré ningún archivo .html en esta carpeta.")
        sys.exit(1)

    print("¿Qué quieres lanzar?\n")
    for i, f in enumerate(files, start=1):
        print(f"  [{i}] {f}")
    print()

    while True:
        choice = input("Elige un número (Enter = 1): ").strip()
        if choice == "":
            return files[0]
        if choice.isdigit() and 1 <= int(choice) <= len(files):
            return files[int(choice) - 1]
        print("Opción no válida, intenta de nuevo.")

def main():
    parser = argparse.ArgumentParser(description="HorseAI Launcher: sirve un HTML local")
    parser.add_argument("file", nargs="?", help="Archivo a abrir (si lo omites, te pregunto)")
    parser.add_argument("--port", type=int, default=5500, help="Puerto (por defecto 5500)")
    parser.add_argument("--dir", default=".", help="Carpeta a servir (por defecto la actual)")
    args = parser.parse_args()

    os.chdir(args.dir)

    # Siempre mostramos el banner para que sepas que arrancó
    print(BANNER)

    target = args.file
    if not target:
        # Sin argumento: tomamos el primer .html sin preguntar
        files = find_html_files(".")
        if not files:
            print("❌ No encontré ningún archivo .html en esta carpeta.")
            sys.exit(1)
        target = files[0]
        print(f"▶ Sirviendo automáticamente: {target}")
    elif not os.path.isfile(target):
        print(f"❌ No encontré '{target}' en esta carpeta.")
        sys.exit(1)
    else:
        print(f"▶ Sirviendo: {target}")

    class Handler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
            super().end_headers()
        def log_message(self, fmt, *a):
            pass  # silencia el log de peticiones, más limpio

    try:
        with socketserver.TCPServer(("127.0.0.1", args.port), Handler) as httpd:
            url = f"http://127.0.0.1:{args.port}/{target}"
            print(f"\n🐴 HorseAI corriendo en {url}")
            print("   (Ctrl+C para detener)\n")
            webbrowser.open(url)
            httpd.serve_forever()
    except OSError as e:
        if "Address already in use" in str(e):
            print(f"❌ El puerto {args.port} ya está ocupado. Prueba con --port <otro>.")
        else:
            print(f"❌ Error al iniciar el servidor: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nServidor detenido. Hasta luego 👋")

if __name__ == "__main__":
    main()