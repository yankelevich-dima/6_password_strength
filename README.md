# 6_password_strength

## Usage

 - Run `python password_strength.py <password>`
 - Note that first run require downloading ~20MB of data (blacklist of passwords)

## Scores

Script returns result score from 1 to 10 (the bigger, the better)

  - \+ 1 point if password contains digits
  - \+ 2 points if length more or equal 6
  - \+ 2 points if length more or equal 10
  - \+ 2 points if password contains special symbols
  - \+ 2 points if password contains both uppercase and lowercase symbols

Note that if password is contained in blacklist, script returns 1 point.  
Default blacklist of password you can find [here](https://dazzlepod.com/site_media/txt/passwords.txt).
