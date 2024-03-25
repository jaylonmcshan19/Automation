# import schedule
# import time
# from flask import Flask, request, jsonify
# import logging

# app = Flask(__name__)

# # Configure logging
# logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# handler = logging.StreamHandler()
# handler.setFormatter(formatter)
# app.logger.addHandler(handler)

# def job():
#     app.logger.info("I'm working...")

# # Schedule job to run every hour between 8 AM and 6 PM
# schedule.every().hour.at(":00").do(job).tag('working_hours')
# schedule.every().hour.at(":30").do(job).tag('working_hours')

# @app.route('/bot_endpoint', methods=['POST'])
# def bot_handler():
#     try:
#         app.logger.info('Received POST request to bot endpoint')
        
#         # Dummy response
#         bot_response = {
#             'message': 'Python bot endpoint is working!'
#         }
        
#         # Return the bot's response
#         return jsonify(bot_response), 200
#     except Exception as e:
#         # Log any exceptions
#         app.logger.error(f'An error occurred: {str(e)}')
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     while True:
#         # Run scheduled jobs
#         schedule.run_pending()
#         time.sleep(1)
        
#         # Run Flask app
#         app.run(debug=True)  # Run the Flask app in debug mode for development
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def index():
    # Your response logic here
    response = jsonify(message="Hello, this is your bot server!")
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(debug=True)
