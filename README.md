# PYZRepositoryDummyTemplate
Python3 FGL

-----------------------------------------------------------------------------------
Neues Repository anhand dieser Vorlage erstellen, das Jython kann.<BR>
Merke: Üblicherweise fange ich die Repository Namen mit "Project_" an.

-------------------------------
Hier ist die Beschreibung wie diese Projekt anhand einer Vorlage erstellt wurde.<BR>
Zudem ist dort auch die Berschreibung von Besonderheiten / Sinn von einigen Ordner, etc.<BR>
https://github.com/firak01/Project_JAZRepositoryDummyTemplate#projekt_jazrepositorydummytemplate


-------------------------------------
Es gilt die Konvention:<BR>
Debug Scripte, die mit JYZ enden als Jython starten.<BR>
Debug Scripte, die mit PYZ enden alsl Python starten.<BR>

Für die Nutzung der Klassen aus anderen Projekten gilt:<BR>
Der PythonPath wird durch die Angabe der Sourcefolder zwar erweitert.<BR>
Wenn es aber identische Pfade in einen anderen/zweiten Sourcefolder (z.B. tryout) gibt, 
dann werden die Klassen darin nicht gefunden.<BR>
Grund: Die Reihenfolge der Sourcefolder, die man im Eclipse Projekt angibt ist wichtig. Nur der oberste gilt!!!!
<BR>
Das kann man testen. Es gibt im src Sourcefolder und im tryout Sourcefolder jeweils eine pyz.Hello....PYZ Klasse.<BR>
Nur die aus sem src Sourcefolder ist aus einem anderen Pythonprojekt importierbar über:<BR>



-------------------------------------
------------
Für die Benennung der pyDev Package-Namen:
Es gab Probleme beim import, wenn der Packagname openai lautete.

Was ist hier passiert?
Du hattest urspr�nglich ein lokales Python-Package namens openai. Damit gab es zwei gleichnamige Pakete:
- Dein lokales Package unter tryout\openai
- Das installierte OpenAI-SDK unter site-packages\openai
Python importierte das lokale Package zuerst. Durch die Umbenennung hast du diesen Namenskonflikt beseitigt.
Eclipse hat beim Refactoring allerdings auch die Importanweisungen angepasst. Das ist bei einer Paketumbenennung grunds�tzlich beabsichtigt, aber hier unerw�nscht: import openai soll weiterhin das externe OpenAI-SDK laden und nicht auf dein umbenanntes Testpaket verweisen.
Was du daraus f�r deine Python-Projekte mitnehmen kannst
1. Keine lokalen Packages nach externen Bibliotheken benennen. Das gilt beispielsweise f�r openai, requests, json, typing oder logging.
2. Nach einem Refactoring externe Imports kontrollieren. Eclipse kann nicht immer erkennen, ob eine Importanweisung auf ein externes Paket oder ein eigenes Projektmodul zielt.
3. Den Importpfad pr�fen, wenn ein unerkl�rlicher Fehler auftritt. print(openai.__file__) war hier der entscheidende Diagnosehinweis.
Dein abschlie�ender Test best�tigt nun alle drei Punkte:
- SDK-Version: 3.37.0
- Importpfad: C:\python\3.13.17\Lib\site-packages\openai\__init__.py
- Versionsattribut vorhanden: True