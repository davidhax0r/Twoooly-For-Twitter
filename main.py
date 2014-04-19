#Import The Tweepy Module
import tweepy

class Twooly(object):

    def __init__(self,API_KEY,API_SECRET,TOKEN,TOKEN_SECRET):
        self.auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
        self.auth.set_access_token(TOKEN,TOKEN_SECRET)
        self.twitter = tweepy.API(self.auth)
        self.me = self.twitter.me()
        self.name = self.me.name

    def follow_followers(self):
        self.followers = self.twitter.followers_ids(self.name)
        self.following = self.twitter.friends_ids(self.name)

        for each_follower in self.followers:
            if each_follower not in self.following:
                self.twitter.create_friendship(each_follower)
                print "-" * 30
                print "Following The User.."
            else:
                print "-" * 30
                print "You Are Already Following Him!"

    def auto_unfollow(self):
        self.followers = self.twitter.followers_ids(self.name)
        self.following = self.twitter.friends_ids(self.name)

        for each_friend in self.following:
            if each_friend not in self.followers:
                self.twitter.destroy_friendship(each_friend)
                print "-" * 30
                print "Unfollowed The User.."
            else:
                print "-" * 30
                print "He is following you.."

    def clear_timeline(self):
        print "Getting all tweets....."
        self.timeline_tweets = self.twitter.user_timeline(count = 300) #350 is the limit of tweets/hour
        print "Found: %d" % (len(self.timeline_tweets))
        print "Removing, please wait..."
        for t in self.timeline_tweets:
            self.twitter.destroy_status(t.id)
        print "Done"
