**Twoooly For Twitter**
===================
**Twoooly** is a Python twitter bot that automatically follows users that match a specified search query on Twitter and can unfollow users that are not following you back.If you want to help just fork the repo and send pull requests. It's up to you, add any feature that you like.
Hit me up on [Twitter](http://twitter.com/itsnauman) if you wanna ask something or just want to say hi :)

**Disclaimer**
---------------
I hold no liability for what you do with this script or what happens to you by using this script. Abusing this script *can* get you banned from Twitter, so make sure to read up on proper usage of the Twitter API.

**Dependencies**
----------------
You will need to install Python's `tweepy` library first:

```easy_install tweepy```
or
```pip install tweepy```

You will also need to create an app account on https://dev.twitter.com/apps

1. Sign in with your Twitter account
2. Create a new app account
3. Modify the settings for that app account to allow read & write
4. Generate a new OAuth token with those permissions
5. Manually edit this script and put those tokens in the script

**Usage**
----------

####Running Twoooly for the first time
Open the file `setup.py` and add your Twitter information


  ```API_KEY = ""```
  ```API_SECRET  =""```
  ```TOKEN = ""```
  ```TOKEN_SECRET = ""```
