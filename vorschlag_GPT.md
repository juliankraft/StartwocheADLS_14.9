## Installation und Kurzeinführung der neuen ADLS Studies
**Datum: 14. September 2023**

### Agenda:

1. **Begrüßung und Einführung** (15 Minuten)
   - Vorstellung der Veranstaltung
   - Zielsetzung und Bedeutung der vorgestellten Tools
   
2. **Grundlegende Installationsvorbereitungen** (20 Minuten)
   - Einführung in die Verwendung von Package Managern: Homebrew (MAC) und Chocolatey (Windows)
   - Installation von Homebrew (MAC) und Chocolatey (Windows)

3. **Installieren von Chocolatey**
   - cmd.exe als Administrator öffnen
   - Folgenden Befehl ausführen:
   ```bash
   @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
   ```

   
4. **Installieren der Basistools** (30 Minuten)
   - Docker-Desktop: Installation und Konfiguration
   - Git: Installation und Erste Schritte
   - Python 3.12: Herunterladen und Installieren
   
5. **Entwicklungsumgebung einrichten** (25 Minuten)
   - Visual Studio Code: Installation und Grundlagen
   - Verwendung von Extensions für effiziente Entwicklung
   
6. **R-Programmierung in Visual Studio Code** (20 Minuten)
   - Einrichten der R-Umgebung in VS Code
   - Grundlegende R-Programmierung und Debugging in VS Code
   
7. **Best Practices und Empfehlungen** (15 Minuten)
   - Tipps für effektive Nutzung der installierten Tools
   - Empfehlungen zur strukturierten Arbeitsweise
   
8. **Fragen und Diskussion** (15 Minuten)
   - Offene Runde für Fragen der Teilnehmer
   
9. **Abschluss und Ausblick** (10 Minuten)
   - Nächste Schritte nach der Installation und Kurzeinführung
   - Mögliche zukünftige Schulungen oder Unterstützung

### Zusätzliche Überlegungen:

- **Peer-Demonstration:** Ein kurzes Video, in dem die Organisatoren als "Peers" die Installationsschritte auf ihren eigenen Systemen durchführen und dabei Tipps und Fallstricke teilen könnten.

- **Technisches GitHub-Video:** Ein Video, das die Installationsschritte und Konfigurationen in einem technischen Detail zeigt und dabei GitHub für den Code-Austausch und die Zusammenarbeit verwendet.

- **Deutschsprachige Ressourcen:** Verlinkung zu deutschsprachigen YouTube-Tutorials und Dokumentationen, die den Teilnehmern bei weiteren Fragen und Vertiefung helfen können.
