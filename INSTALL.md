# Instalacja narzędzi — AiSD

## 1. Pascal (Lazarus) — WYMAGANY do C3

**Windows (rekomendowane):**
1. Wejdź na https://www.lazarus-ide.org/index.php?page=downloads
2. Pobierz instalator `lazarus-4.x-x86_64-win64.exe` (wersja stable dla Windows).
3. Uruchom jako administrator, instaluj domyślnie do `C:\Lazarus`.
4. Po instalacji otwórz Lazarus → `Tools > Options > Environment > Compiler path` — ścieżka do `C:\Lazarus\fpc\...\bin\ppc486.exe` powinna być ustawiona automatycznie.
5. Test w wierszu polecenia:
   ```
   "C:\Lazarus\fpc\3.2.2\bin\x86_64-win64\fpc.exe" -iV
   ```
   (wersja może się różnić — ważne, żeby wypisała numer).

**Alternatywa tylko kompilator (FPC), bez IDE:** https://www.freepascal.org/download.html → `fpc-3.2.2.x86_64-win64.exe`.

**WSL (jeśli wolisz bez Windows):**
```
sudo apt update && sudo apt install -y fpc
fpc -iV
```
Uwaga: w WSL działa tylko konsola Pascal, nie Lazarus IDE — do ćwiczeń wystarczy `fpc` + dowolny edytor.

## 2. Python 3 — już zainstalowany (3.14.9)

Jeśli chcesz mieć systemowy Python w Windows: https://www.python.org/downloads/ → zaznacz **Add Python to PATH**.

## 3. GitHub

**gh CLI (GitHub CLI):**
- Windows: https://cli.github.com/ → `GitHubCLI-windows-<wersja>.msi`
- WSL: `sudo apt install gh`
- Potem: `gh auth login` → wybierz GitHub.com → HTTPS → `Login with a web browser`.

**Alternatywa bez gh:** utwórz pusty repo na https://github.com/new (Public/Private — jak wolisz), a potem daj mi jego adres. Ja dodam `remote` i zrobię `git push` używając tokenu z `GH_TOKEN`/`GITHUB_TOKEN` albo poproszę Cię o `gh auth login`.

## 4. Diagramy / dokumenty

Do generowania schematów i PDF używam: Graphviz (`dot`), Python `matplotlib` i `reportlab` — już dostępne. Jeśli chcesz edytować schematy sam: https://www.diagrams.net/ (darmowy, działa w przeglądarce) lub LibreOffice Writer / Draw: https://www.libreoffice.org/download/download/

## 5. Jak uruchomić gotowe rozwiązania

```bash
cd C2_python && python3 a06_c2_zad1_rownanie.py
cd C2_python && python3 run_all_tests.py
cd C3_python && python3 run_all_tests.py
```

Dokumenty zbiorcze: `docs/AiSD_C1.pdf`, `docs/AiSD_C2.pdf`, `docs/AiSD_C3.pdf`.
