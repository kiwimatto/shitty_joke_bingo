# shitty_joke_bingo

Simple Python script generating shitty joke bingo sheets. Have a look at shitty_jokes.py, it's fairly self-explanatory.

Requirements:
* Python  (obv)
* wkhtmltopdf  (http://wkhtmltopdf.org/)
* pdftk (https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/)

Notes: 
* wkhtmltopdf might take a looong time to convert stuff into pdfs if your OS takes ages to make printers available (e.g. default printer is off-line).
* Currently the script generates a 4x4 grid, but it's easy to adapt. Just make sure you define at least as many jokes as grid-elements.

