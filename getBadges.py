import requests

# Change this to your username
username = "JohnHammond"

# Get user X's badges
r = requests.get("https://tryhackme.com/api/badges/get/" + username)
response = r.json()

# Create list of badge names to compare to ALL badges availiable
userBadges = []
for i in response:
    userBadges.append(i['name'])

# Get all possible badges
r = requests.get("https://tryhackme.com/api/badges/get")
response = r.json()

'''
Create two dictionaries, both with badge name as the key.
allBadges value will be the image location for the badge
badgeText value will be the description of the badge
'''
allBadges = {}
badgeText = {}
for i in response:
    allBadges.update({ i['name'] : "https://tryhackme.com" + i['image']})
    badgeText.update( {i['name'] : i['description']})

# Just basic HTML and some CSS to make the output readable
outputHTML = ""
outputHTML += "<!DOCTYPE html>\n"
outputHTML += "<html>\n"
outputHTML += '<style> .badges\n {\ndisplay: grid;\ngrid-template-columns: repeat(4, 1fr);\ngrid-gap: 20px;\nmargin-top: 20px;\n}\n'
outputHTML += 'img\n {\nwidth: 100px;\n}\n'
outputHTML += '.title\n {\nfont-weight: bold;\n}\n</style>\n'
outputHTML += '<div class="badges"> \n'

with open("badges.html", "w") as outputFile:
    for i in userBadges:
        # If a user has one of the possible badges, add the info to the html doc
        if i in allBadges:
            outputHTML += '<div>'
            outputHTML += '<img src=' + '"' + allBadges[i] + '">'
            outputHTML += '<p class="title">' + i + '</p>'
            outputHTML += "<p>" + badgeText[i] + "</p>"
            outputHTML += '</div>'
            outputHTML += "\n" 
    
    outputHTML += '<div>'
    outputHTML += "</html>\n"
    outputFile.write(outputHTML)