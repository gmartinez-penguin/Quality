#!/usr/bin/python36

import cgi
import os

"""
forms = '<form action>' + \
'Serial Number: <input type = "text" name = "sn"><br />' + \
'<input type = "submit" value = "Submit" />' + \
'</form>' 
"""


form = cgi.FieldStorage()

sns = form.getvalue('sn')




#print ("<h2> sns is %s </h2>" % (sns))

print('Content-type: text/html\r\n\r\n')

#print ("<h2> sns is %s </h2>" % (sns))

#<form action = method = "post">
#Serial Number: <input type = "text" name = "sn"><br />
#<input type = "submit" value = "Submit" />
#</form>

if form.getvalue('sn'):
   styles = '<style> table, th, td {border: 1px solid black;border-collapse=collapse;} th, td {  padding: 10px; } </style>'


#   strTable = "<html><body style=background-color:powderblue>" + styles + "<table><tr><th>Hardware</th><th>Quantity</th><th>Result</th></tr>"

   strTable = "<html><body style=background-color:powderblue>" + styles

   sns = form.getvalue('sn').upper()

   pns = sns.split(",")

   for sns in pns:

      files = "/Penguin/" + sns.upper()      

      exists = os.path.isfile(files)
      if exists:

         strTable = strTable + "<h2> The follow are the test results for  %s </h2>" % (sns)

         strTable = strTable + "<table><tr><th>OMS Part ID</th><th>Hardware</th><th>Quantity</th><th>Result</th></tr>" 



         infile = open(files, "r")
         for line in infile:
            items = line.strip().split(",")
#            strRW = "<tr><td>" + str(items[0]) + "</td><td>" + str(items[1]) + "</td><td>" +  '<font size="5" color="red">' +  str(items[2]) + '</font>' + "</td></tr>"
  
            strRW = "<tr><td>" + str(items[0]) + \
                    "</td><td>" + str(items[1]) + \
                    "</td><td>" + str(items[2]) +  "</td><td>"

            if items[3] == "PASS":
               strRW = strRW +  '<font size="5" color="green">' +  str(items[3]) + '</font>' + "</td></tr>"
            else:
               strRW = strRW +  '<font size="5" color="red">' +  str(items[3]) + '</font>' + "</td></tr>"


            strTable = strTable + strRW

         strTable = strTable + "</table>"
         infile.close()



      else:
         print("<h2> The file %s does NOT exist </h2>" % files)
#         break


   strTable = strTable + "</body></html>"
   print (strTable)


#   strTable = strTable + "</body></html>"

#   print (strTable)

else:

   forms = '<form action>' + \
   'Serial Number: <input type = "text" size=40 name="sn"><br />' + \
   '<input type = "submit" value = "Submit" />' + \
   '</form>' 
   print ("<h1> Welcome to the Penguin Server QA Program </h1>" )
   print ("<h2> Enter the Penguin Serial Number to check </h2>" )
   initForm = "<html><body style=background-color:powderblue>" + forms + "</body></html>"
   print(initForm)






