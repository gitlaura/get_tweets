#get_tweets.py: Python Script to Download Tweets

Use this script to download the last 100 (or whatever number you choose) from any Twitter user.

##Installation & How To Use

```'''```
$ git clone https://github.com/gitlaura/get_tweets.git
$ cd get_tweets
```
Then you need to get your Twitter API Credentials by creating a new app at apps.twitter.com. Enter the appropriate API keys in lines 11-15 of get_tweets.py.

Then you can run the script by entering one username at the command line:

```'''```
$ python get_tweets.py [twitter_username]
```

<br>or you can use interactive mode

```'''```
$ python
>>> from get_tweets import get_tweets
>>> get_tweets("[twitter_username]")
```

##More
http://www.getlaura.com/how-to-download-tweets-from-the-twitter-api/
