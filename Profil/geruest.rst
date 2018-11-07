Erstelle dein eigenes Git Repository
====================================

Als erstes brauchst du einen GitHub Account, den du mit deinem persönlichen Octocat-Kostüm schmückst. |smile| Danach erstellst du ein *public repository* und klonst es, damit wir die Dateien lokal auf dem Computer bearbeiten können.

|exercise| Erinnerst du dich an die einzelnen Schritte aus der Einführung? Wenn nicht, blättere einfach zurück...


readme Datei
------------

Als readme oder "Lies mich" wird eine Datei bezeichnet, die überlicherweise mit der Software mitgeliefert wird und wichtige Informationen über diese enthält. Oft wird der Benutzer vor der Installation und vor der ersten Verwendung der Software über wichtige Details informiert, die für den Gebrauch wichtig sind.
Wir werden in diese Datei dein Inhaltsverzeichnis schreiben, damit sich alle User auf deiner Page auch gut zurecht finden!

Template
--------

Template ist ein englisches Wort für *Schablone*. Diese Schablone stellt eine Art Gerüst dar, das einen Teil der Gestaltung deiner Page vorgibt. Du kannst die fehlenden Teile nur noch einsetzen und so die Vorlage zu einer vollständigen Homepage ergänzen.

Das template fügen wir in den Konfigurationen, sprich den *Einstellungen*, ein. Diese Datei heisst ``config.py``. Dort fügst du an gegebener Stelle den folgenden Code ein:

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


|exercise| Findest du die Stelle im ``config.py`` file? Kopiere den Code rein und schaue dir dein neues Template an! |smile|







.. |smile| replace:: 😃
.. |exercise| replace:: ✏️