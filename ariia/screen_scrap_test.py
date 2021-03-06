import urllib2
import cookielib

cookieJar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))

city = "Paris"

url = "http://www.yr.no/place/France/%C3%8Ele-de-France/" + city + "/"
request = urllib2.Request(url)
page = opener.open(request)

# This is one big string
rawdata = page.read()

# This breaks it up into lines
lines_of_data = rawdata.split('\n')

# This is one line in the raw data that looks interesing.  I'm going to
# filter the raw data based on the "og:title" text.
# 
#'<meta name="og:title" content="Beijing, Beijing | 31&deg; | Clear" />

# The "if line.find(" bit is the filter. 
special_lines = [line for line in lines_of_data if line.find('og:description')>-1]
print special_lines

# Now we clean up - this is very crude, but you can improve it with
# exactly what you want to do.

info = special_lines[0].replace('"','').split('content=')[1]
sections = info.split(':')
sectionsRefined = sections[3].split(',')
print sectionsRefined