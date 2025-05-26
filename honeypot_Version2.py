from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(asctime)s %(message)s')

@app.route('/admin', methods=['GET', 'POST'])
def fake_admin():
    user_agent = request.headers.get('User-Agent')
    logging.info(f"Admin honeypot accessed: IP={request.remote_addr}, Method={request.method}, UA={user_agent}, Data={request.data}")
    return "404 Not Found", 404

@app.route('/login', methods=['GET', 'POST'])
def fake_login():
    user_agent = request.headers.get('User-Agent')
    logging.info(f"Login honeypot accessed: IP={request.remote_addr}, Method={request.method}, UA={user_agent}, Data={request.data}")
    return "404 Not Found", 404

@app.route('/wp-admin', methods=['GET', 'POST'])
def fake_wp_admin():
    user_agent = request.headers.get('User-Agent')
    logging.info(f"WP-Admin honeypot accessed: IP={request.remote_addr}, Method={request.method}, UA={user_agent}, Data={request.data}")
    return "404 Not Found", 404

@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    user_agent = request.headers.get('User-Agent')
    logging.info(f"Honeypot accessed: Path=/{path}, IP={request.remote_addr}, Method={request.method}, UA={user_agent}, Data={request.data}")
    return "404 Not Found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)