import ntplib
from flask import Flask

app = Flask(__name__)


def get_time():
    '''
    Get time from the internet.
    '''
    ntp_client = ntplib.NTPClient()
    ntp_response = ntp_client.request('pool.ntp.org')
    time_string = str(ntp_response.tx_time)
    return time_string

@app.route('/', methods=['GET'])
def home():
    '''
    Run the time function and return the value.
    '''
    epoch_time = get_time()
    return epoch_time


if __name__ == "__main__":
    app.run(debug=True)
