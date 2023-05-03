"""
Name:  Tenzing Nyima
Email: Tenzing.Nyima71@myhunter.cuny.edu
Resources:  Used python.org as a reminder of Python 3 print statements.
"""
import re
def rm_tags(data):
    """ This function takes one input:
    data: a multiline string
    Returns a string with HTML formatting removed.
    If teh string was palin text, the contents are
    returned analtered as a string."""
    pattern3 = re.compile(r'<.*?>') #paragraphs
    answer = pattern3.sub('', data)
    #print(answer)
    return answer

def test_rm_tags(rm_tags_rnc):
    """rm_tags_fnc: a function that takes a string and returns a string.
    Returns True if the inputtted function correctly strips out from
    the test from HTML file adn False other wise.
    """
    #print(rm_tags_rnc)
    answer = "hellowor dasdfk"
    answer2 = """<html>
    <head><title>Simple HTML File</title></head>

    <body>
      <p> Here's a link for <a href="http://www.hunter.cuny.edu/csci">Hunter CS Department</a>
      and for <a href="https://stjohn.github.io/teaching/data/fall21/index.html">CSci 39542</a>.  </p>
  
      <p> And for <a href="https://www.google.com/">google</a>
    </body>
</html>
    """
    return False

def make_dict(data):
    """ This function takes one input:
    Uses regular expressions() to find all external liks in data
    and store teh link text as the key and URL value in dictionary
    style.
    Title and URL in teh csv file specified by the user.
    For the URL, keep the leading https://or http://
    reutrns the resulting dictionary."""
    content = data
    #pattern4 = re.compile(r'("http[s^s]://[a-zA-Z]+.[a-z]+|[A-Za-z]+.[a-zA-Z]+)"')
    pattern = re.compile(r'<a(.*)/a>')
    #pattern5 = re.compile(r'>[a-zA-Z ]+<')
    matches = pattern.findall(content)
    dict = {}
    keys = []
    items = []
    for match in matches:
        #print(match)
        pattern3 = re.compile(r'>[a-zA-Z0-9 ]+<')
        matches3 = pattern3.findall(match)
        #print("match2")
        for match3 in matches3:
            #print(match3)
            key = match3[1:-1]
            keys.append(key)
        #remove https
        #print(match)
        pattern2 = re.compile(r'"(.*)"')
        matches2 = pattern2.findall(match)
        for match2 in matches2:
            #print(match2)
            item = match2
            items.append(item)

    for num in range(len(keys)):
        key = keys[num]
        #print("key",key)
        #print("item:",items[num])
        dict[key] = items[num]
    return dict

def test_make_dict(make_dict_fnc):
    answer = ""
    answer2 = """<html>
    <head><title>Simple HTML File</title></head>

    <body>
      <p> Here's a link for <a href="http://www.hunter.cuny.edu/csci">Hunter CS Department</a>
      and for <a href="https://stjohn.github.io/teaching/data/fall21/index.html">CSci 39542</a>.  </p>

      <p> And for <a href="https://www.google.com/">google</a>
    </body>
</html>
    """
    if make_dict_fnc(answer2) == make_dict(answer2):
        return True
    return False
