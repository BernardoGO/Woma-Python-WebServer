import io as strIO

codeOut = strIO.StringIO()
sys.stdout = codeOut
sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)