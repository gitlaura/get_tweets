## Python Script to Download Tweets

Use the script `get_tweets.py` to download the last 100 tweets (or whatever number you choose) from any Twitter user.

### Setup
(1) You need to get your Twitter API Credentials by creating a new app at [apps.twitter.com](apps.twitter.com).

(2) This script uses Tweepy. If you don't have Tweepy installed you need to run this command on the terminal first:

```
$ sudo pip install tweepy
```

### Clone and use the Python script
Now you're ready to clone and use the get_tweets script.

```
$ git clone https://github.com/gitlaura/get_tweets.git
$ cd get_tweets
```
Enter the appropriate keys from your Twitter app in lines 11-15 of `get_tweets.py` using any text editor.

Finally you can run the script by entering one Twitter username at the command line:

```
$ python get_tweets.py [twitter_username]
```

#### More details on my blog:
[http://www.getlaura.com/how-to-download-tweets-from-the-twitter-api/](http://www.getlaura.com/how-to-download-tweets-from-the-twitter-api/)
