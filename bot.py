import praw
import time
import prawcore

user = '' #Bot Username
user_pass = '' #Bot Password
c_id = '' #Bot Client ID
c_secret = '' #Bot Client Secret

itemKeywords = ['Example', 'Example1'] #To add more keywords, just add more apostrophes separated by commas

reddit = praw.Reddit(
    username = user,
    password = user_pass,
    client_id = c_id,
    client_secret = c_secret,
    user_agent = 'Item Alert Bot by Rubix'
)

def main():
    sub = reddit.subreddit('')  # Subreddit you want the bot to run in

    for submission in sub.stream.submissions():
        title = submission.title.lower() #Makes the title completely lowercase
        for phrase in itemKeywords:
            if phrase in title:
                reddit.redditor('').message('An Item Has Been Posted!', 'A submission with a keyword you chose has been posted here: ' + submission) #Enter your username in the redditor box


if __name__ == '__main__':
    while True:
        try:
            main()
        except BaseException:
            time.sleep(5)
