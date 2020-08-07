
import re
import tweepy
from datetime import  datetime
from datetime import datetime as dt


#class to format the time
class Datetime():

    def get_formatted_date(self, date):
        self.date = date
        new_datetime = datetime.strftime(datetime.strptime(date, '%b %d %Y'), '%Y-%m-%d')
        return new_datetime

    def get_time_difference(self,time):
        self.time = time
        time = dt.strptime(time, '%Y-%m-%d %H:%M:%S')
        time_difference = datetime.now() - time
        time_difference = int(time_difference.total_seconds() / 60 / 60)
        return time_difference




class Twitter_Client():
    from secrets import access_token_secret,consumer_key,consumer_secret,access_token_key


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)

    #automatically delete tweet after certain amount of hours has passed
    def delete_tweet_after_time(self):
        datetime_OBJ = Datetime()
        myTweets = self.api.user_timeline("twittterauto1")
        user_input = int(input("Enter the hour(s) after tweet creation you want to delete it: "))
        for tweet in myTweets:
            time_difference = datetime_OBJ.get_time_difference(str(tweet.created_at))
            if(time_difference>=user_input):
                print("Deleting...: " + " " + str(tweet.text))
                self.api.destroy_status(tweet.id)

    #automatically delete tweets between two dates

    def delete_tweet_at_date(self):
        fromatdateOBJ = Datetime()
        print("please enter the dates you want to delete tweet from(example: Oct 09 2020)")
        beggining_date = input("The beggining date:")
        beggining_date =  fromatdateOBJ.get_formatted_date(beggining_date)

        end_date = input("The end date:")
        end_date =  fromatdateOBJ.get_formatted_date(end_date)

        myTweets = self.api.user_timeline("twittterauto1")
        for tweet in myTweets:

            dateoftweet = str(tweet.created_at)
            match = re.search(r'\d{4}-\d{2}-\d{2}', dateoftweet)
            created_at = str(datetime.strptime(match.group(), '%Y-%m-%d').date())
            if (created_at>= beggining_date and created_at <=end_date):
                print("Deleting...: "+ " " + str(tweet.text))
                self.api.destroy_status(tweet.id)






twitter = Twitter_Client()
twitter.delete_tweet_at_date()




