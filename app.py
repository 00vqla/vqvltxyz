from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Serve static files from the root directory
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

# Root route - serves root.html
@app.route('/')
def root():
    return send_from_directory('.', 'root.html')

# Home route - serves home.html
@app.route('/home')
def home():
    return send_from_directory('.', 'home.html')

# Forum route - serves forum.html
@app.route('/forum')
def forum():
    return send_from_directory('.', 'forum.html')

# DVD route - serves DVD.html
@app.route('/dvd')
def dvd():
    return send_from_directory('.', 'DVD.html')

# Shop route - serves shop.html
@app.route('/shop')
def shop():
    return send_from_directory('.', 'shop.html')

# About route - serves about.html
@app.route('/about')
def about():
    return send_from_directory('.', 'about.html')

# Contact route - serves contact.html
@app.route('/contact')
def contact():
    return send_from_directory('.', 'contact.html')

# Terms route - serves terms.html
@app.route('/terms')
def terms():
    return send_from_directory('.', 'terms.html')

# Privacy route - serves privacy.html
@app.route('/privacy')
def privacy():
    return send_from_directory('.', 'privacy.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000) 