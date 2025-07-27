from instaloader import Instaloader, Profile, Post
import time

L = Instaloader()

def scrape_instagram(keyword, limit=10):
    try:
        posts = []
        profile = Profile.from_username(L.context, keyword)
        
        for post in profile.get_posts():
            if len(posts) >= limit:
                break
                
            posts.append({
                'username': profile.username,
                'caption': post.caption,
                'likes': post.likes,
                'comments': post.comments,
                'date': post.date.strftime('%Y-%m-%d %H:%M:%S'),
                'url': f'https://www.instagram.com/p/{post.shortcode}/'
            })
            
            time.sleep(1)  # Avoid rate limiting
            
        return posts
        
    except Exception as e:
        print(f"Error scraping Instagram: {e}")
        return []