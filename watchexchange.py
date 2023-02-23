import praw
import pandas as pd
import datetime

user_agent = "Searchbot_01"
reddit = praw.Reddit(username="Searchbot_01",
                     password ="aaaa1111",
                     client_id="Ai32qfXNqvGuMEvHFFMlAw",
                     client_secret="IG5XKjyUGkcG2cgXfBSwVvalMTxFRg",
                     user_agent=user_agent)

subreddit_name = "watchexchange"
subreddit = reddit.subreddit(subreddit_name)
#print(subreddit.display_name)


df = pd.DataFrame() # creating dataframe for displaying scraped data

# creating lists for storing scraped data
titles=[]
scores=[]
ids=[]
time_created = []
comments = []
url= []
author = []
price = ['USD', 'PRICE','$']
ratio = []
# username = comment.author
# looping over posts and scraping it
for submission in subreddit.top(limit=10):
    titles.append(submission.title)
    scores.append(submission.score) #upvotes
    ids.append(submission.id)
    author.append(submission.author)
    time_created.append(datetime.datetime.utcfromtimestamp(submission.created))
    ratio.append(submission.upvote_ratio)
    # if username == author:
    #     # username = comment.author.name
    #     comments.append(submission.comment)
        
        
    #if price in submission.comments:
     #   comments.append(submission.comment)
    
df['Title'] = titles
df['Id'] = ids
df['Upvotes'] = scores #upvotes
df['Time_Created'] = time_created
df['test_column'] = author
df['Upvote_Ratio'] = ratio
# try:
#     df['Comments'] = comments
# except:
#     df['Comments'] = df.fillna(0)

print(df.shape)
df.head(10)
print(df)