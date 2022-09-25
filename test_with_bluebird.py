from Scweet.scweet import scrape
from Scweet.user import  get_user_information
from Scweet.user import  get_users_followers
from Scweet.user import  get_users_following

env_path = ".env"
users = ['vasilisonka']

print("STARTED")
# users_info = get_user_information(users, headless=False)
# print(users_info)
# users_followers = get_users_following(users, env=env_path, headless=False, wait=2, limit=50, file_path='scweet_following_')
# print(users_followers)
users_followers = get_users_followers(users, headless=False, env=env_path, wait=2, limit=50, file_path="scweet_followers_")
print(users_followers)