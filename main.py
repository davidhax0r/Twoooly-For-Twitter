#Import The Tweepy Module
import tweepy

class Twoooly(object):

    def __init__(self,API_KEY,API_SECRET,TOKEN,TOKEN_SECRET):
        self.auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
        self.auth.set_access_token(TOKEN,TOKEN_SECRET)
        self.twitter = tweepy.API(self.auth)
        self.me = self.twitter.me()
        self.name = self.me.name

    def auto_follow(self):
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
        print 'Setting up....'
        for each_friend in self.following:
            if each_friend not in self.followers:
                self.twitter.destroy_friendship(each_friend)
                print "-" * 30
                print "Unfollowed The User.."
            else:
                print "-" * 30
                print "He is following you.."

    def clear_timeline(self,count = 100):
        print "Getting all tweets....."
        self.timeline_tweets = self.twitter.user_timeline(count = count) #350 is the limit of tweets/hour
        print "Found: %d" % (len(self.timeline_tweets))
        print "Removing, please wait..."
        for t in self.timeline_tweets:
            self.twitter.destroy_status(t.id)
        print "Done"

    def favorite_tweets(self,search,num_of_tweets = 10):
        search = '#'+search
        cursor = tweepy.Cursor(self.twitter.search,q=search,lang='en').items(int(num_of_tweets))
        print 'Please wait while the tweets are fetched......'
        print 'It might take some time....'
        for each_tweet in cursor:
            self.twitter.create_favorite(each_tweet.id)
        print 'Done, go check it out...'

    def retweet_tweets(self,search,num_of_tweets = 10):
        search = '#'+search
        cursor = tweepy.Cursor(self.twitter.search, q=search, lang='en').items(int(num_of_tweets))
        print 'Please wait while the tweets are fetched......'
        print 'It might take some time....'
        for each_tweet in cursor:
            self.twitter.retweet(each_tweet.id)
            print each_tweet.id
        print 'Done, go check it out...'

    def follow_user_with_tweets(self,search,num_of_users = 10):
        search = '#'+search
        self.following = self.twitter.friends_ids(self.name)
        print 'Getting Tweets Related To The Search.......'
        cursor = tweepy.Cursor(self.twitter.search,q=search,lang='en').items(int(num_of_users))
        print 'Please be patient.....'
        for each_tweet in cursor:
            if each_tweet.user.screen_name not in self.following:
                self.twitter.create_friendship(each_tweet.user.screen_name)
                print "-" * 35
                print 'Followed The User %s' % (each_tweet.user.screen_name)
            else:
                print "-" * 35
                print 'You Are Already Following %s' % (each_tweet.user.screen_name)
        print "-" * 35
        print 'DONE Following'

    def create_list_of_user_with_tweets(self,search,list_name,num_of_users = 10):
        search = '#'+search
        cursor = tweepy.Cursor(self.twitter.search,q=search,lang='en').items(int(num_of_users))
        try:
            self.twitter.create_list(list_name,'My List')
        except tweepy.TweepError:
            print 'An Error Has Occured'
        for each_tweet in cursor:
            self.twitter.add_list_member()