### VS Code
***In diesem Programm wirst du deinen zukünftigen Code verfassen!*** <br>
Visual Studio Code ist eine kostenlose, plattformübergreifende Code-Editor-Software, die von Microsoft entwickelt wurde. Sie bietet Unterstützung für Hunderte von Programmiersprachen und Erweiterungen, die die Funktionalität des Editors erweitern. VS Code ist eine der beliebtesten Code-Editor-Software auf dem Markt und wird von vielen Entwicklern und Datenwissenschaftlern verwendet. <br>
[VS Code in 100 Sekunden](https://www.youtube.com/watch?v=KMxo3T_MTvY&ab_channel=Fireship)

#### Installation

Die Installation von VS Code ist sehr einfach. Laden Sie einfach die Installationsdatei von der [VS Code-Website](https://code.visualstudio.com/) herunter und führen Sie sie aus. Die Installation ist in wenigen Minuten abgeschlossen.

### Chocolatey
***Deine Installationshilfe im Studium um Programme einfach und Problemlos zu installieren*** <br>
Chocolatey ist ein Paketmanager für Windows. Er ermöglicht dir, Software von der Kommandozeile aus zu installieren und zu verwalten. Chocolatey ist sehr nützlich, um die Installation von Software zu automatisieren und zu vereinfachen. Ein weiterer grosser Vorteil ist, dass Software die mit Chocolatey installiert wurde auch wieder vollständig deinstalliert werden kann - etwas das bei Windows sonst leider nicht ganz so einfach ist.

#### Installation


   - cmd.exe als Administrator öffnen</br>
   (Windows-Taste drücken, cmd.exe eingeben, Rechtsklick auf cmd.exe und "Als Administrator ausführen" auswählen)
   - Folgenden Befehl ausführen:
        ```bash
        @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
        ```
   - Wenn die Installation abgeschlossen ist kann mit dem Befehl `choco` geartbeitet werden.</br> Versucht doch mal `choco -?` auszuführen um die Hilfe aufzurufen...
   - Mit dem Befehl `choco list` könnt ihr alle installierten Chocolatey-Pakete auflisten.
   - Mit dem Befehl `choco search "name"` könnt ihr nach verfügbaren Chocolatey-Paketen suchen.
   - Eine Liste mit verfügbaren Chocolatey-Paketen findet ihr auch [hier](https://community.chocolatey.org/packages).

### Sonstiges

#### Python

Python ist eine einfach zu erlernende, aber dennoch leistungsstarke Programmiersprache. Sie ist sehr beliebt für Datascience und Machine Learning. Während dem Studium werden wir Python für viele Programmieraufgaben verwenden. <br>
[Mehr über Python erfahren](https://www.python.org/about/) <br>


- Chocolatey Befehl zur Installation:<br>
   `choco install python -y` (-y steht für yes, damit die Installation automatisch durchgeführt wird)

#### R language

R ist eine Programmiersprache für statistisches Rechnen, das analysieren und bearbeiten von Daten und bietet viele Möglichkeiten zur Datenvisualisierung. Während dem Studium werden wir R dafür immer mal wieder verwenden. <br>
[Mehr erfahren](https://www.r-project.org/about.html)

- Chocolatey Befehl zur Installation:<br>
   `choco install r.project -y`
   
- Um von der Konsole aus die Kontrolle über R zu bekommen, muss noch der Pfad zu dem Interpreter angelegt werden. Der einfachste Weg um das zu erreichen ist direkt von der Konsole aus. Dazu wieder cmd als Administrator ausführen und folgenden Befehl eingeben:<br>
   ```bash
   setx PATH "%PATH%;C:\Program Files\R\R-4.3.1\bin"
   ```
   Dabei muss der Pfad allenfalls angepasst werden, dass er mit eurer Installation übereinstimmt.

Danach startet ihr R mal als Administrator es sollte eine Verknüpfung auf dem Desktop sein oder testet gleich einmal den angelegten Pfad indem ihr cmd als Administrator ausführt und einfach mal `R` eingebt - das sollte euch eine R Konsole im Terminal öffnen.<br>
Führt folgende Befehle aus:<br>

```R
install.packages('devtools', repos='https://stat.ethz.ch/CRAN/')
```

```R
install.packages(
        "pak",
        repos = sprintf("https://r-lib.github.io/p/pak/stable/%s/%s/%s",
        .Platform$pkgType,
        R.Version()$os,
        R.Version()$arch),
        clean = TRUE
    )
```


   
#### Docker-Desktop

Docker Desktop ist eine Anwendung, die es ermöglicht, Anwendungen in isolierten Umgebungen, sogenannten Containern, auf deinem Computer auszuführen. Diese Container enthalten alle benötigten Ressourcen, wie Code, Bibliotheken und Konfigurationen, um die Anwendung reibungslos zu betreiben. Durch die Verwendung von Docker kannst du Anwendungen in konsistenten und portablen Umgebungen entwickeln, testen und ausführen, unabhängig von den Unterschieden zwischen deinem Entwicklungsrechner und Produktionsumgebungen. <br>
[Mehr erfahren](https://www.docker.com/why-docker)

- Chocolatey Befehl zur Installation:<br>
`choco install docker-desktop -y`
            

#### Git
***Github wird dir dabei behilflich sein, in einem im Team Codes verwalten und Teilen*** <br>
***Du kannst sie auch mit der Community teilen und deine eigenen Projekte verfassen*** <br>
Git ist ein Versionskontrollsystem, das es dir ermöglicht, Änderungen an Dateien zu verfolgen und diese Änderungen zu verwalten. Während dem Studium werden wir Git verwenden, um unsere Projekte zu verwalten und zu teilen. <br>
[Mehr erfahren](https://git-scm.com/about)

- Chocolatey Befehl zur Installation:<br>
`choco install git -y`

#### VS Code Extensions

In VS Code können Erweiterungen installiert werden, um die Funktionalität des Editors zu erweitern. Während dem Studium werden wir einige Erweiterungen verwenden, um unsere Arbeit zu vereinfachen. Folgende Erweiterungen könnt ihr gleich einmal installieren:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [R](https://marketplace.visualstudio.com/items?itemName=Ikuyadeu.r)
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)



#### Lass uns nun gemeinsam Python im Visualstudio Code testen. 
Ladet das File RockPaperScisors.ipynb herunter und öffnet es in Visualstudio Code...