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
[Mehr erfahren](https://www.python.org/about/)

- Chocolatey Befehl zur Installation:<br>
   `choco install python -y` (-y steht für yes, damit die Installation automatisch durchgeführt wird)
  
#### R language

R ist eine Programmiersprache für statistisches Rechnen, das analysieren und bearbeiten von Daten und bietet viele Möglichkeiten zur Datenvisualisierung. Während dem Studium werden wir R dafür immer mal wieder verwenden. <br>
[Mehr erfahren](https://www.r-project.org/about.html)

- Chocolatey Befehl zur Installation:<br>
   `choco install r.project -y`
   
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

#### Anaconda "virtuelle Umgebung"
*** Damit du deine Coding Pakete nicht einfach wild auf deinem Laptop herunter lädst, probieren wir diese mit Conda zu zähmen***
Damit du VS Studio Code bestmöglich nutzen kannst werden wir nun eine virtuelle Umgebung auf deinem Rechner installieren.
Mach dich schon mal mit dem Namen Conda bekannt.
Zunächst einmal, dass du hörst was sind die Vor und Nachteile.
Conda_Vorteile

- Konsistent über alle Platformen
- Installiert auch in Windows-Umgebungen alle Abhängigkeiten korrekt (Data Science)
- Jupyter Notebook schon enthalten
- Automatischer Download verschiedener Versionen beim Erzeugen einer virtuellen Umgebung
- Keine Probleme mit Berechtigungen bei Firmen-Computern
- Zugang zu weiteren Paketquellen neben pip
- Unterstützt Python und R

Conda_Nachteile

- Pakete sind nicht immer auf dem aktuellsten Stand
- In neu erzeugte Umgebungen werden bereits ein paar Pakete installiert, die im Zweifel gar nicht gebraucht werden


Die Begriffe die du im Terminal öffters nutzen wirst ist zum einen conda deactivate, und conda activate. Wichtig ist erscheint neben deinen Namen beim Terminal (base), befindest du dich bereits in Conda. Um Conda zu deactivieren. Schreibe einfach den Befehl Conda deactivate rein.

Im Visual Studio, wirst du als Standart Kernel jeweils Conda auswählen müssen, dabei kannst du zwischen den Programmiersprachen wechseln.


hier noch zusätzliche Links zu Anaconda, falls du darüber mehr erfahren willst
- [What is Anaconda for Python & Why Should You Learn it?](https://blog.hubspot.com/website/anaconda-python)

- [Weitere informationen zu Anaconda in einem Video, installation und Why?(auf englisch)](https://www.youtube.com/watch?v=YJC6ldI3hWk&t=61s)



#### Lass uns nun gemeinsam Python im Visualstudio Code testen. 
Ladet das file RockPaperScisors.ipynb herunter und öffnet es in Visualstudio Code...