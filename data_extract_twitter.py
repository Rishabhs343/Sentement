#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = '1356067753-meH0a1Mkq656me99o3kEzFmXh9Y4BQ20ZFNVXj6'
access_token_secret = '22usq1xTu3IV3jqspDjY1wOrpX15yEFETW9n961vUBbff'
consumer_key = 'v4g7MB8ws2c9CE5gnz0EXaivG'
consumer_secret = 'V5rmJr56ZwNo8OBubnCk0jBo8WkQoSA1IIQnybdgbLHJ55kyZw'


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['RailMinIndia','@RailwaySeva','@mumbairailusers','#indianrailway','RailwaySeva','@RailMinIndia','#RailwaySeva','#RailMinIndia','indianrailway','@indianrailway'])
