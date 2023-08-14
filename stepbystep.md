### VS Code

Visual Studio Code ist eine kostenlose, plattformübergreifende Code-Editor-Software, die von Microsoft entwickelt wurde. Sie bietet Unterstützung für Hunderte von Programmiersprachen und Erweiterungen, die die Funktionalität des Editors erweitern. VS Code ist eine der beliebtesten Code-Editor-Software auf dem Markt und wird von vielen Entwicklern und Datenwissenschaftlern verwendet.
[VS Code in 100 Sekunden](https://www.youtube.com/watch?v=KMxo3T_MTvY&ab_channel=Fireship)

#### Installation

Die Installation von VS Code ist sehr einfach. Laden Sie einfach die Installationsdatei von der [VS Code-Website](https://code.visualstudio.com/) herunter und führen Sie sie aus. Die Installation ist in wenigen Minuten abgeschlossen.

### Chocolatey oder Homebrew

Chocolatey und Homebrew sind Paketmanager für Windows und MacOS. Sie ermöglichen es Ihnen, Software von der Kommandozeile aus zu installieren und zu verwalten. Sie sind sehr nützlich, um die Installation von Software zu automatisieren und zu vereinfachen. In diesem Studium werden wir Chocolatey für Windows und Homebrew für MacOS verwenden.

#### Installation

<details>
<summary>Installation von Chocolatey auf Windows</summary>

   - cmd.exe als Administrator öffnen
   - Folgenden Befehl ausführen:
        ```bash
        @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
        ```
   - Wenn die Installation abgeschlossen ist kann mit dem Befehl `choco` geartbeitet werden. Versucht doch mal `choco -?` auszuführen um die Hilfe aufzurufen...
   - Eine Liste mit verfügbaren Chocolatey-Paketen findet ihr [hier](https://community.chocolatey.org/packages).

</details>

<details>
<summary>Installation von Homebrew auf MacOS</summary>

<!-- Anleitung zur Installation -->

</details>

### Sonstiges

#### Python

Python ist eine einfach zu erlernende, aber dennoch leistungsstarke Programmiersprache. Sie ist sehr beliebt für Datascience und Machine Learning. Während dem Studium werden wir Python für viele Programmieraufgaben verwenden. [Mehr erfahren](https://www.python.org/about/)

- installieren
   - Windows: `choco install python -y`
   - macOS:

#### R language

R ist eine Programmiersprache für statistisches Rechnen, das analysieren und bearbeiten von Daten und bietet viele Möglichkeiten zur Datenvisualisierung. Während dem Studium werden wir R dafür immer mal wieder verwenden. [Mehr erfahren](https://www.r-project.org/about.html)

- installieren
   - Windows: `choco install r.project -y`
   - macOS:
   
#### Docker-Desktop

Docker Desktop ist eine Anwendung, die es ermöglicht, Anwendungen in isolierten Umgebungen, sogenannten Containern, auf deinem Computer auszuführen. Diese Container enthalten alle benötigten Ressourcen, wie Code, Bibliotheken und Konfigurationen, um die Anwendung reibungslos zu betreiben. Durch die Verwendung von Docker kannst du Anwendungen in konsistenten und portablen Umgebungen entwickeln, testen und ausführen, unabhängig von den Unterschieden zwischen deinem Entwicklungsrechner und Produktionsumgebungen. [Mehr erfahren](https://www.docker.com/why-docker)

- installieren
   - Windows: `choco install docker-desktop -y`
   - macOS:

#### Git

Git ist ein Versionskontrollsystem, das es dir ermöglicht, Änderungen an Dateien zu verfolgen und diese Änderungen zu verwalten. Während dem Studium werden wir Git verwenden, um unsere Projekte zu verwalten und zu teilen. [Mehr erfahren](https://git-scm.com/about)

- installieren
   - Windows: `choco install git -y`
   - macOS:

### Visual Studio Code Extensions