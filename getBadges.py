import requests

# Get user X's badges, get titles for dictionary comparison
r = requests.get("https://tryhackme.com/api/badges/get/supadupalipa")
response = r.json()
userBadges = []
for i in response:
    userBadges.append(i['name'])

# Use below to create an dictionary of titles to images
r = requests.get("https://tryhackme.com/api/badges/get")
response = r.json()
allBadges = {}
for i in response:
    allBadges.update({ i['name'] : "https://tryhackme.com" + i['image']})

outputHTML = ""
with open("badges.html", "w") as outputFile:
    outputHTML += "<!DOCTYPE html>\n"
    outputHTML += "<html>\n"
    outputHTML += '<style> .badges\n {\ndisplay: grid;\ngrid-template-columns: repeat(4, 1fr);\ngrid-gap: 20px;\n}\n</style>\n'
    outputHTML += '<div class="badges"> \n'
    for i in userBadges:
        if i in allBadges:
            outputHTML += "<h3>" + i + "</h3>"
            outputHTML += '<img src=' + '"' + allBadges[i] + '">'
            outputHTML += "\n" 
    
    outputHTML += '<div>'
    outputHTML += "</html>\n"
    outputFile.write(outputHTML)