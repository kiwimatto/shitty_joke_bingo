import os, sys, time
import numpy as np
#import pdfkit

jokes = [ ["What's brown and runny?", "Usain Bolt"], \
          ["What do hipster jeans and a cheap hotel have in common?", "No ballroom"], \
          ["Did you hear about the duck with a drug problem?", "He was a quackhead"], \
          ["And the Lord said to John, \"Come forth and you shall receive eternal life\"...", "But John came fifth and won a toaster"], \
          ["What's brown and rhymes with snoop?", "Dr. Dre"], \
          ["Two TV aerials got married...", "The wedding was rubbish but the reception was excellent"], \
          ["I went to buy some camouflage trousers the other day...", "but I couldn't find any"], \
          ["A man walks into a bar with a slab of asphalt under his arm. The bartender says:", "\"I'll serve you, but not your friend, he looks like a bit of a cycle path\""], \
          ["What's orange and sounds like a parrot?", "A carrot"], \
          ["I was scared of gardening...", "...until I grew a pear"], \
          ["What do you give an elephant with diarrhoea?", "Lots of room"], \
          ["Why can you never hear if a pterodactyl is in the bathroom?", "because the p is silent"], \
          ["What did one physicist say when he wanted to fight another physicist?", "Let me atom."], \
          ["What's the difference between a cat and a comma?", "One has claws at the end of its paws and one is a pause at the end of a clause."], \
          ["Who lives in the herb garden and says 'thankyouverymuch'?", "Elvis Parsley"], \
          ["What time does Sean Connery go to Wimbledon?", "Tennish"], \
          ["What did the cowboy say when he went into the car showroom in Germany?", "Audi"], \
          ["Where do you find a dog with no legs?", "Where you left it."], \
          ["How do you know if there's an elephant in your fridge?", "The door won't shut."], \
          ["How do you make an egg laugh?", "Tell it a yolk"], \
          ["What's red and invisible?", "No tomatoes"], \
          ["What kind of potatoes wear glasses?", "Spectaters"], \
          ["What did the suspenders say to the trousers?", "What's up britches!"], \
          ["I'll always remember my grandfathers last words...", "\"A truck!\""], \
          ["How many Germans does it take to screw in a lightbulb?", "Nein!"], \
          ["What do you call a pair of crows?", "Attempted murder"], \
          ["What do you get when you cross an octopus with a cow?", "A reprimand from the Scientific Integrity and Professional Ethics Committee" ] ]


head = """
<html>
<style>
table {
  width: 90%;
  border: 1px solid black;
  display: table;
}
td {
  width: 25.00%;
  position: relative;
  border: 1px solid black;
}
td:after {
  content: '';
  display: block;
  margin-top: 100%;
}
td .content {
  display:table-cell;
  vertical-align:middle;
  position: absolute;
  top: 50;
  bottom: 0;
  left: 0;
  right: 0;
  background: white;
  text-align: center;
}
span {  
  display: inline-block;
  vertical-align: middle;
  line-height: normal;
  font-family: "Comic Sans MS", cursive, sans-serif;
}
p {
  font-family: "Comic Sans MS", cursive, sans-serif;
}
</style>
<body>
<center><b> Shitty joke bingo </b></center><br><br>
"""

foot = """
</body>
</html>
"""

NUMBER_OF_BINGO_SHEETS = 10


def make_table():
    p = np.random.permutation(range(len(jokes)))
    p = p[:16]
    string = "<table>\n"
    for i in range(4):
        string += "  <tr>\n"
        for j in range(4):
            string += '    <td><div class="content"><span>' + jokes[p[4*i+j]][1] + '</span></div></td>\n'
        string += "  </tr>"
    string += "</table>"
    return string

def write_pdf(html):
    with open('temp.html','w') as fid:
        fid.write( html )
        fid.close()
    os.system('wkhtmltopdf temp.html temp.pdf')    

def make_bingo_sheet():
    html = head + make_table() + foot
    write_pdf(html)

def make_questions_sheet():
    html = head
    for joke in jokes:
        html += "<div><p>"+joke[0]+"</p></div>"
    write_pdf(html)

# make bingo sheets and question sheet
pdftkstring = ' temp.pdf'
for i in range(NUMBER_OF_BINGO_SHEETS):
    make_bingo_sheet()
    os.rename('temp.pdf', 'bingo_sheet_%d.pdf' % i)
    pdftkstring += ' bingo_sheet_%d.pdf' % i
make_questions_sheet()

# combine all into a single pdf
os.system('pdftk' + pdftkstring + ' cat output shitty_joke_bingo.pdf')

# clean up
os.remove('temp.html')
os.remove('temp.pdf')
[os.remove('bingo_sheet_%d.pdf' % i) for i in range(NUMBER_OF_BINGO_SHEETS)]

