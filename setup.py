"""
Copyright 2014 Nauman Ahmad

This file is part of the Twoooly library.

Twoooly is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option) any
later version.

Twoooly is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Twoooly.
If not, see http://www.gnu.org/licenses/.
"""
import main

API_KEY = "pKxKEHl6hyFwQBrh0GTZV8BBn"
API_SECRET  ="sQ4xh1gZ8elA4Yq4sz8EtTlOZfT14FG3HH8RFMG8vHH9LI1XBU"
TOKEN = "2447417772-Ul4fvWF7KZ3HM5LLKmM6yv81ZXJLsQfPUcpSU7A"
TOKEN_SECRET = "I3unuCz3rlw4Jcf9f93r25SOkVXnvHf6ZggPXJVavrbCA"

twooly = main.Twoooly(API_KEY,API_SECRET,TOKEN,TOKEN_SECRET)
twooly.create_list_of_user_with_tweets('Android','An Geeks',num_of_users= 5)
