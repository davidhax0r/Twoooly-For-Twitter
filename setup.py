import main

API_KEY = "pKxKEHl6hyFwQBrh0GTZV8BBn"
API_SECRET  ="sQ4xh1gZ8elA4Yq4sz8EtTlOZfT14FG3HH8RFMG8vHH9LI1XBU"
TOKEN = "2447417772-Ul4fvWF7KZ3HM5LLKmM6yv81ZXJLsQfPUcpSU7A"
TOKEN_SECRET = "I3unuCz3rlw4Jcf9f93r25SOkVXnvHf6ZggPXJVavrbCA"

twooly = main.Twoooly(API_KEY,API_SECRET,TOKEN,TOKEN_SECRET)
twooly.create_list_of_user_with_tweets('Android','An Geeks',num_of_users= 5)
