import os
import ntplib
from flask import Flask, send_file, Response

app = Flask(__name__)


def get_time():
    '''
    Get time from the internet.
    '''
    ntp_client = ntplib.NTPClient()
    ntp_response = ntp_client.request('pool.ntp.org')
    return ntp_response.tx_time

@app.route('/', methods=['GET'])
def home():
    '''
    Run the time function and return the value.
    '''
    epoch_time = get_time()
    return epoch_time


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
