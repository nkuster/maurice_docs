Robot-Zeichner
==============

.. image:: images/turtle.png
   :align: left
   :width: 350 px

In Python kann man ganz leicht zeichnen. Mit dem Modul ``turtle`` kannst du eine Schildkröte über den Bildschirm bewegen, die einen Stift hat und damit Bilder zeichnet. In diesem Projekt, programmierst du die Turtle so, dass sie mehr und mehr Bilder von Robotern zeichnet!

Führst du das Programm aus aus, legt die Python-Turtle los und bewegt sich über den Bildschirm. Dabei wird ein Roboter gezeichnet. Du siehst zu, wie der Roboter Stück für Stück in verschiedenen Farben entsteht.

Prinzip
-------

Zuerst schreibst du eine Funktion, die Rechtecke zeichnet. Dann stelsst du die Rechtecke zu einem Roboter zusammen. Ihre Farbe und Grösse kannst du anhand der Parameter ändern, die3 dur der Funktion übergibst. Lange, dünne Rechtecke können also die Beine bilden, quadratische die Augen und so weiter.

.. note:: Mit dem Modul ``turtle`` steuerst du eine Roboterschildkröte, die einen Stift bei sich trägt. Du kannst Turtle sagen, wann sie den Stift aufsetzen und zeichnen soll und wann sie ihn heben soll, sodass sie sich an eine neue Position begeben kann, ohne eine Spur zu hinterlassen.

Die Turtle geht zum Beispiel 100 Pixel vorwärts, dreht sich um 90 Grad und geht 50 Pixel vorwärts mit folgendem Befehl:

.. code-block:: python

   t.forward(100)
   t.left(90)
   t.forward(50)

Rechtecke zeichnen
------------------

.. todo:: |exercise| Lade in deinem neuen Programm das Modul ``turtle`` aus der Bibliothek.

   Tipp: Du kannst dem Modul eine Abkürzung zuordnen, dann musst du den Namen nicht mehr ausschreiben und sparst dir eine Menge Tipparbeit! |smile|




.. |smile| replace:: 😃
.. |exercise| replace:: ✏️
.. |muscle| replace:: 💪
.. |rocket| replace:: 🚀