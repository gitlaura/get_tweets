#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import json

#http://www.tweepy.org/
import tweepy

#Get your Twitter API credentials and enter them here
consumer_key = "ciLVxZjy5BqcEXqXuChgR75ot"
consumer_secret = "yyTTmqaI30ZJnQpb7Q9EGFwm98qnvyTP6dt7dQX06xFdu9OypK"
# access_key = "your_access_key"
# access_secret = "your_access_secret"
access_token = "1497606285218435073-9LDJ66YSkkqvR4MZvun1otPEUdAJo5"
access_token_secret = "xsnlAICVhsJrjsLIccrEp8x5gtdSPB9lV4W1gRqIWeayq"
# bearer_token = "AAAAAAAAAAAAAAAAAAAAAOXehQEAAAAAOeWIn%2F7Gh9fXPbBrNtDfVr3EZHQ%3DTIV5gfCvOqEYPQ6ffxulgeSICN098ztYSg9iQLVO4qsX40FGKl"
# api_key_secret = "yyTTmqaI30ZJnQpb7Q9EGFwm98qnvyTP6dt7dQX06xFdu9OypK"
# api_key = "ciLVxZjy5BqcEXqXuChgR75ot"

# OAUTH2 Client ID
# client_id = "dFpfWll0b050aWExY1JGeVVfUHA6MTpjaQ"
# client_secret = "3ZJ6hRimTreSmkDV4eyQslMxlWwRiU8gcVpjvgY-DJwEWlaHbm"
    
#method to get a user's followers
def get_followers(username):

	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	# authorization of consumer key and consumer secret
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	# set access to user's access key and access secret 
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

    # getting all the followers
	print("Getting followers for " + username)
	# try and catch error in case of rate limit error
	followers_obj = {}
	final_obj = {}
	try:
		# followers = api.get_followers(screen_name = username)
		c = tweepy.Cursor(api.get_followers, screen_name=username).items(1000)
		for f in c:
			# print(f)
			follower = f._json
			followers_obj[follower['id_str']] = follower
		# for property, value in vars(followers).items():
		# for num in range(len(followers)):
		# 	follower = followers[num]._json
		# 	followers_obj[num] = follower
			obj = {}
			obj['name'] = follower['name']
			obj['screen_name'] = follower['screen_name']
			obj['description'] = follower['description']
			obj['followers_count'] = follower['followers_count']
			obj['followings_count'] = follower['friends_count']
			obj['url'] = follower['url']
			obj['location'] = follower['location']
			final_obj[follower['id_str']] = obj

		# an object made of the screen_name of each follower
		fol_names_for_csv = [[f['screen_name'], f['name'], f['followers_count']] for k,f in final_obj.items()]
		# add an empty array to the start of fol_names_for_csv
		fol_names_for_csv.insert(0, ["screen name", "name", "followers"])

		# print(json.dumps(final_obj, indent=4))
		print(fol_names_for_csv)
		# print out a statement indicating that the username and follower count
		print(">> " + username + " has " + str(len(followers_obj)) + " followers.")

		#write to a new csv file from the array of tweets
		outfile = username + "_tweets.csv"
		with open(outfile, 'w+') as file:
			writer = csv.writer(file, delimiter=',')
			writer.writerows(fol_names_for_csv)
		print("Saved to " + outfile)
	except tweepy.errors.TooManyRequests:
		print(final_obj)
		print("Too many requests")
		return
	except Exception as e:
		print(e)
		print("Error getting followers for " + username)
		return


#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
	print(sys.argv)
	if len(sys.argv) >= 2:
		users = sys.argv[1:]
		for user in users:
			get_followers(user)
	else:
		print("Error: Enter at least one username")

    #alternative method: loop through multiple users
	# users = ['user1','user2']

