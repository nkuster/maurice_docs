Erstelle dein eigenes Git Repository
====================================

Als erstes brauchst du einen GitHub Account, den du mit deinem persönlichen Octocat-Kostüm schmückst. |smile| Danach erstellst du ein *public repository* und klonst es, damit wir die Dateien lokal auf dem Computer bearbeiten können.

.. todo:: |exercise| Erstelle dein Git-Repository und klone es.

   Erinnerst du dich an die einzelnen Schritte aus der Einführung? Wenn nicht, blättere einfach zurück...

Deine Homepage berechnen
------------------------

Um deine Notizen und Bilder in eine Homepage zu verwandeln, musst du einige Befehle über die Konsole eingeben. Kontrolliere als erstes, ob du im richtigen Ordner bist.

Alles richtig? Na dann los! |smile| Du kannst deine Page wie folgt anschauen:

.. code-block:: bash

   $ make html
   $ open _build/html/index.html

Das sieht zugegeben noch etwas langweilig aus.. ab zum nächsten Schritt! Bring Farbe auf deine Page .. |rocket|

Template
^^^^^^^^

Template ist das englische Wort für *Schablone*. Diese Schablone stellt eine Art Gerüst dar, das einen Teil der Gestaltung deiner Page vorgibt. Du kannst die fehlenden Teile nur noch einsetzen und so die Vorlage zu einer vollständigen Homepage ergänzen.

Das template fügen wir in den Konfigurationen, sprich den *Einstellungen*, ein. Diese Datei heisst ``config.py``. Dort kopierst du an gegebener Stelle den folgenden Code hin:

.. code-block:: python

   html_theme = 'sphinx_rtd_theme'

   # Theme options are theme-specific and customize the look and feel of a theme
   # further.  For a list of options available for each theme, see the
   # documentation.
   #
   html_theme_options = {
       'canonical_url': '',
       'analytics_id': 'UA-128752678-1',
       'logo_only': False,
       'display_version': True,
       'prev_next_buttons_location': 'bottom',
       'style_external_links': False,
       # Toc options
       'collapse_navigation': True,
       'sticky_navigation': True,
       'navigation_depth': 4,
       'includehidden': True,
       'titles_only': False
   }


.. todo:: |exercise| Findest du die Stelle im ``config.py`` file? Kopiere den Code rein und schaue dir dein neues Template an!

   Besser, oder? Gratulation! |muscle|







.. |smile| replace:: 😃
.. |exercise| replace:: ✏️
.. |muscle| replace:: 💪
.. |rocket| replace:: 🚀