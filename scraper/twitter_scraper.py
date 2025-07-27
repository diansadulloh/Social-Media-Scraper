import snscrape.modules.twitter as sntwitter
import datetime

def scrape_twitter(keyword, limit=10):
    tweets = []
    
    query = f'{keyword} lang:id since:{datetime.date.today() - datetime.timedelta(days=7)}'
    
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        if i >= limit:
            break
            
        tweets.append({
            'username': tweet.user.username,
            'content': tweet.content,
            'likes': tweet.likeCount,
            'retweets': tweet.retweetCount,
            'date': tweet.date.strftime('%Y-%m-%d %H:%M:%S'),
            'url': tweet.url
        })
    
    return tweets