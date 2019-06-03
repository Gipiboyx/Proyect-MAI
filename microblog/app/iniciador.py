from app import *

form = cgi.FieldStorage()
if form.has_key('opcion'):
    if (form['opcion'].value=="1"):
    	principal()