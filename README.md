# Get your TryHackMe Badges

A simple python script which retrieves a given user's tryhackme badges. Intended for displaying a user's badges on their personal website.

The script utilises tryhackme's public api. It does the following:
* Retrieves all badges user has achieved
* Retrives all possible badges a user could have
* Compare the achieved badges with all possible badges
* Output a html file containing a basic grid displaying:
    * Badge Image
    * Badge Title
    * Badge Description

To modify the script to display YOUR username's badges please modify the username variable at the beginning of getBadges.py

```python
username = "JohnHammond"
```