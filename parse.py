import sys
import StringIO
do_print = False

#Job title to search for
word = "Product"

#URL to search for
url_code = "https://"

#imports the "body" argument passed above by zapier as a text string
corpus = input.get('body')

#truncates first 70 characters of text string e.x. "Linkedin Jobs..."
corpus = corpus[70:]

#Stops searching when it sees this text
breakpt = "See all matching jobs"

s = StringIO.StringIO(corpus)
s2 = StringIO.StringIO(corpus)
s3 = StringIO.StringIO(corpus)

company = "company"
job = "job"
url = "url"
c = 1
d = 1
e = 1

#save lines after those containing "Product" in the title as #companies
for line in s:
    if breakpt in line:
    	break 
    if do_print:
        output[company+str(c)]=line
        do_print = False
        c += 1
    if word in line:
        do_print = True

#save lines containing "Product" in the title as job titles
for line in s2:
    if breakpt in line:
    	break 
    if word in line:
        output[job+str(d)]=line
        d += 1
        
#save urls
for line in s3:
    if breakpt in line:
    	break 
    if url_code in line:
        output[url+str(e)]=line[10:]
        e += 1
        
#force desired output when email parser is not working   
'''
return {'job1': 'Sr. PM', 'job2': 'Sr. PM', 'job3': 'Sr. PM', 'job4': 'Sr. PM', 'job5': 'Sr. PM', 'job6': 'Sr. PM', 'job7': 'Sr. PM', 'job8': 'Sr. PM', 'job9': 'Sr. PM', 'company1': 'Autodesk Labs', 'company2': 'Autodesk Labs', 'company3': 'Autodesk Labs', 'company4': 'Autodesk Labs', 'company5': 'Autodesk Labs', 'company6': 'Autodesk Labs', 'company7': 'Autodesk Labs', 'company8': 'Autodesk Labs', 'company9': 'Autodesk Labs'}
'''
return output