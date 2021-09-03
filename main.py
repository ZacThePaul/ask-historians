import praw
import time

reddit = praw.Reddit(client_id='dO4fTH1iyzrhAHvrk1AHyQ',
                     client_secret='qbemHJv537faCzxF38d4fEsAxqDcQw',
                     user_agent='redditdev scraper by u/T_CLAVDIVS_CAESAR',
                     username='T-CLAVDIVS-CAESAR',
                     password='Banaszac17!')

ask_historians = reddit.subreddit('AskHistorians')

mod_list = []

for moderator in ask_historians.moderator():
    mod_list.append(moderator)

for submission in ask_historians.comments(limit=25):
    for mod in mod_list:
        if submission.author == mod:
            print(submission.author)

print('hi')