from flask import Flask, render_template, request, jsonify
from scraper.twitter_scraper import scrape_twitter
from scraper.instagram_scraper import scrape_instagram
from scraper.facebook_scraper import scrape_facebook
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    keyword = request.form.get('keyword')
    platform = request.form.get('platform')
    limit = int(request.form.get('limit', 10))
    
    results = []
    
    try:
        if platform == 'twitter':
            results = scrape_twitter(keyword, limit)
        elif platform == 'instagram':
            results = scrape_instagram(keyword, limit)
        elif platform == 'facebook':
            results = scrape_facebook(keyword, limit)
        else:
            return jsonify({'error': 'Platform not supported'}), 400
            
        return jsonify({'data': results})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)