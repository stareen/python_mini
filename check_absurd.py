import urllib

def read_text():
    words = open("C:\Users\hp\Desktop\mini_python_projects")
    contents_of_file = words.read()
    print(contents_of_file)
    words.close()
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
read_text()
