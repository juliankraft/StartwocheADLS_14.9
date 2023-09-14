### MAC USER ONLY
Bist du dir unsicher ob du einen M1/M2 Chip oder einen Intel Processor besitzt? 

Überprüfe dies bevor du den Download startest. Ganz oben links auf deinem Desktop siehst du das <span style="color: #FF5733">Apple Symbol</span>. Klicke dort drauf -> <span style="color: #FF5733">Über diesen Mac.</span> Bei der Rubrik Chip siehst du deinen Prozessor.

### XCode App

Zwei Möglichkeiten um Xcode zu installieren:

- Erste Möglichkeit: Gehe in de Appstore und suche nach XCode.!!!! - Nur diese führen wir durch


"""(Zusatzinfo für euch, aber nicht im Unterricht durchführen)
- Zweite Möglichkeit, wenn du mit dem Terminal herumspielen willst(DIes dauert erheblich länger das Erbnis ist am Ende das Gleiche):

Es gibt eine Möglichkeit, auf denn Appstore mit dem Terminal zu navigieren.

Zuerst müssen wir dafür "mas" installieren

<span style="color: #FF5733">- brew install mas</span>

Wenn die Installation reibungslosgeklappt hat, können wir nun mit mas zu Xcode Navigieren

<span style="color: #FF5733">- mas search xcode </span>


Wenn du dies ausführst siehst du etwa so etwas(kann sein dass du bisschen hoch scrollen musst):
meggie@Fuchsli ~ % mas search xcode


         640199958      Apple Developer                                    (10.4.1)
         497799835      Xcode                                              (14.3.1)
         1388020431     DevCleaner for Xcode                               (2.4.0)
         -2143041818    GPT Code Creator for Xcode                         (1.8)
         1504940162     RocketSim for Xcode Simulator                      (11.2.0)
Wir brauchen Xcode: 497799835 

<span style="color: #FF5733">- mas install 497799835</span>
Melde dich nun mit deiner Apple ID an
"""


#### VS Code
***In diesem Programm wirst du deinen zukünftigen Code verfassen!*** <br>
Visual Studio Code ist eine kostenlose, plattformübergreifende Code-Editor-Software, die von Microsoft entwickelt wurde. Sie bietet Unterstützung für Hunderte von Programmiersprachen und Erweiterungen, die die Funktionalität des Editors erweitern. VS Code ist eine der beliebtesten Code-Editor-Software auf dem Markt und wird von vielen Entwicklern und Datenwissenschaftlern verwendet. <br>
[VS Code in 100 Sekunden](https://www.youtube.com/watch?v=KMxo3T_MTvY&ab_channel=Fireship)

#### VS Code Extensions

In VS Code können Erweiterungen installiert werden, um die Funktionalität des Editors zu erweitern. Während dem Studium werden wir einige Erweiterungen verwenden, um unsere Arbeit zu vereinfachen. Folgende Erweiterungen könnt ihr gleich einmal installieren:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [R](https://marketplace.visualstudio.com/items?itemName=Ikuyadeu.r)
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

#### Installation

Die Installation von VS Code ist sehr einfach. Laden Sie einfach die Installationsdatei von der [VS Code-Website](https://code.visualstudio.com/) herunter und führen Sie sie aus. Die Installation ist in wenigen Minuten abgeschlossen.

### Homebrew
***Deine Installationshilfe im Studium um Programme einfach und Problemlos zu installieren*** <br>
Homebrew ist ein Paketmanager für MacOS. Sie ermöglichen es Ihnen, Software von der Kommandozeile aus zu installieren und zu verwalten. Sie sind sehr nützlich, um die Installation von Software zu automatisieren und zu vereinfachen.

#### Installation von Homebrew

- Terminal des Macbooks öffnen: Tippe in der Suchzeile des Macs Terminal ein.
- Gebe diesen Befehll ins Terminal ein:<br>
bash<br>
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
- Gebe nun dein Mac Password ein (Wichtig du wirst keine Sternchen sehen, oder dass du etwas eingibst)
Klicke enter. Hat dies funktioniert. Drücke Nochmals enter um den Download zu bestätigen. 
Erschein das Feld Succesfull, weisst du dass es funktioniert hat. 
- Kopiere nun den Link bei Next Steps und füge in in der Commando Zeile ein. Drücke erneut enter. Um zu sehen ob dies funktioniert hat, rufe `brew help` auf, nun siehst du alle Funktionen die dir zu Verfügung stehen
- Mit dem Befehl: `brew search "name"` kannst du diverse Programme abrufen.
Wichtig `brew list`, zeigt dir an welche Programme/Extensions du mit brew herunter geladen hast, nicht die liste aller möglichen Programme von HOMEBREW
</details>

#### Docker-Desktop

Docker Desktop ist eine Anwendung, die es ermöglicht, Anwendungen in isolierten Umgebungen, sogenannten Containern, auf deinem Computer auszuführen. Diese Container enthalten alle benötigten Ressourcen, wie Code, Bibliotheken und Konfigurationen, um die Anwendung reibungslos zu betreiben. Durch die Verwendung von Docker kannst du Anwendungen in konsistenten und portablen Umgebungen entwickeln, testen und ausführen, unabhängig von den Unterschieden zwischen deinem Entwicklungsrechner und Produktionsumgebungen. <br>
[Mehr erfahren](https://www.docker.com/why-docker)

- installieren
   - macOS:  `brew update`, dannach `brew -- cask docker`

#### Instalation R in Homebrew +VS Code
brew install r <br>
dann tippe R <br>
tippe : install.packages("languageserver")
Wähle die Sprache aus 62 für Schweiz
brew install fribidi <br>
brew install libtiff <br>
brew install harfbuzz <br>
brew install freetype2 <br>
brew install libgit2 <br>

dann tippe R
install.packages('devtools')<br>
install.packages('pak')<br>


#### R in VS Code

R ist eine Programmiersprache für statistisches Rechnen, das analysieren und bearbeiten von Daten und bietet viele Möglichkeiten zur Datenvisualisierung. Während dem Studium werden wir R dafür immer mal wieder verwenden. <br>
[Mehr erfahren](https://www.r-project.org/about.html)

R extension for Visual Studio Code installieren
Mit Shift Command X, kannst du die Erweiterungen öffnen. Tippe R ein. <br>



#### Python installieren

Python ist eine einfach zu erlernende, aber dennoch leistungsstarke Programmiersprache. Sie ist sehr beliebt für Datascience und Machine Learning. Während dem Studium werden wir Python für viele Programmieraufgaben verwenden. <br>
[Mehr erfahren](https://www.python.org/about/)
Hast du python bereits auf deinem Rechner? überprüfe dies mit 'python --version'
- installieren
   - macOS: `brew install python3`


               

#### Git
***Github wird dir dabei behilflich sein, in einem im Team Codes verwalten und Teilen*** <br>
***Du kannst sie auch mit der Community teilen und deine eigenen Projekte verfassen*** <br>
Git ist ein Versionskontrollsystem, das es dir ermöglicht, Änderungen an Dateien zu verfolgen und diese Änderungen zu verwalten. Während dem Studium werden wir Git verwenden, um unsere Projekte zu verwalten und zu teilen. <br>
[Mehr erfahren](https://git-scm.com/about)

- installieren
   - macOS: `brew install git`<br>
   git config --global user.name 'Dein Name'<br>
   git config --global user.email 'dein_name.@students.zhaw.ch'<br>

#### VS Code Extensions

In VS Code können Erweiterungen installiert werden, um die Funktionalität des Editors zu erweitern. Während dem Studium werden wir einige Erweiterungen verwenden, um unsere Arbeit zu vereinfachen. Folgende Erweiterungen könnt ihr gleich einmal installieren:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [R](https://marketplace.visualstudio.com/items?itemName=Ikuyadeu.r)
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)




#### Lass uns nun gemeinsam Python im Visualstudio Code testen. 
Ladet das file RockPaperScisors.py herunter und öffnet es in Visualstudio Code...