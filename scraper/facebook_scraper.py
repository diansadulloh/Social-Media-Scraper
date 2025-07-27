from facebook_scraper import get_posts
import datetime

def scrape_facebook(keyword, limit=10):
    posts = []
    
    for post in get_posts(keyword, pages=1, extra_info=True):
        if len(posts) >= limit:
            break
            
        posts.append({
            'username': post['username'] or post['user_id'],
            'content': post['text'],
            'likes': post['likes'],
            'comments': post['comments'],
            'shares': post['shares'] if 'shares' in post else 0,
            'date': post['time'].strftime('%Y-%m-%d %H:%M:%S'),
            'url': post['post_url']
        })
    
    return posts