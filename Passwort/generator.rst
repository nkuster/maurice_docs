Passwort-Generator
==================

Passwörter schützen deinen Computer, deine E-Mails und deine Daten vor fremdem Zugriff. In deiner ersten Aufgabe erstellst du ein Tool (Werkzeug), das für dich sichere und einprägsame Passwörter erfindet.

Mit dem Passwort-Generator kannst du Wörter, Zahlen und Zeichen zu starken Passwörtern kombinieren. Wenn du das Programm ausführst, zeigt es ein Passwort an. Du kannst dir weitere Passwörter erstellen lassen, bis dir eins gefällt.

Gute Passwörter sind leicht zu merken, aber schwer zu erraten - oder zu knacken. Schauen wir uns einmal ein paar Beispiele an:

+----------------------------+-----------------------------------------------------------------------+
|.. image:: images/lock1.png | Namen sind zwar leicht zu merken, aber dafür auch leicht zu erraten.. |
|   :width: 125 px           |                                                                       |
+----------------------------+-----------------------------------------------------------------------+
|.. image:: images/lock2.png | Etwas komplizierter, aber Hacker können es in 2 Sekunden knacken!     |
|   :width: 125 px           |                                                                       |
+----------------------------+-----------------------------------------------------------------------+
|.. image:: images/lock3.png | Bei diesem Passwort braucht der Hacker etwas Zeit..                   |
|   :width: 125 px           |                                                                       |
+----------------------------+-----------------------------------------------------------------------+
|.. image:: images/lock4.png | Dieses ist sicher und leicht zu merken!                               |
|   :width: 125 px           |                                                                       |
+----------------------------+-----------------------------------------------------------------------+

In dieser Aufgabe lernst du das Modul ``random`` kennen. Das Programm trifft aus Gruppen von Adjektiven, Nomen, Zahlen und Satzzeichen eine zufällige Auswahl und kombiniert daraus Passwörter. Deine Passwörter sind ab jetzt so irre, dass du sie nie vergessen wirst!

.. note:: **Adjektiv** + **Nomen** + **Zahl** + **Satzzeichen**

.. line-block::

   Adjektiv   = Eigenschaftswort (z.B. schlafend, flauschig, haarig)
   Substantiv = Nomen (z.B. Apfel, Fahrrad, Dinosaurier)




Prinzip
-------

Das Programm wählt die vier Teile des Passworts zufällig aus, setzt sie zusammen und zeigt das Passwort im Shell-Fenster an. Wenn du das Passwort nicht magst, wiederholt es die Schritte, gefällt es dir, endet das Programm.

Module einfügen
^^^^^^^^^^^^^^^

.. todo:: |exercise| Wie erwähnt, müssen wir nicht das ganze Programm selber schreiben! Wir gehen einfach einmal in die Bibliothek und schauen uns ein wenig um. Denke daran, dass du zwei dinge brauchst: ein Modul, dass Worte auch als solche erkennt und ein weiteres Modul, dass den Zufallsgenerator spielt.

   Findest du aus den untenstehenden Modulen die richtigen?

   ``pandas`` ; ``random`` ; ``os`` ; ``string`` ; ``numpy``

Die Module kannst du gerade zu Beginn aus der Bibliothek importieren, denn dann kannst du sie später ohne weiteren Aufwand im Code verwenden.

Wortlisten
^^^^^^^^^^

Zum Erstellen neuer Passwörter brauchst du eine Liste für Adjektive und eine für Nomen. In Python kannst du zusammengehörige Elemente in Listen speichern. Setze die ganze Liste in ``[]``-Klammern und trenne die Elemente durch Kommas.

Adjektive
"""""""""
.. code-block:: python

   die_adjektive = ['schläfrig', 'lahm', 'rot', 'tapfer', 'flauschig', 'stolz']

Nomen
"""""

.. code-block:: python

   die_nomen = ['Apfel', 'Dinosaurier', 'Drachen', 'Panda', 'Kartoffel', 'Haus', 'Mixer']


Für dein Passwort muss das Programm zufällig ein Adjektiv und ein Nomen auswählen. Dazu verwendest du die Funktion ``choice()`` (englisch für 'Auswahl') im Modul ``random``. Mit dieser Funktion kannst du immer zufällige Elemente aus einer Liste wählen lassen. Du musst ihr nur die Variable mit den Elementen übergeben.

.. code-block:: python

   # die Variable 'adjektiv' enthält ein zufällig gewähltes Element aus der Adjektiv-Liste
   adjektiv = random.choice(die_adjektive)

.. todo:: |exercise| Definiere mit Hilfe der obigen Beschreibung für ``adjektiv`` die Variable ``nomen`` und füge sie direkt in deinen Code!






.. execute_code::
   :hide_headers:
   :linenos:

.. |exercise| replace:: ✏️