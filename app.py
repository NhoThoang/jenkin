from flask import Flask
from redis import Redis

app = Flask(__name__)
#redis = Redis(host='redis', port=6379)
redis=202

@app.route('/')
def hello():
    #count = redis.incr('hits')
    count =112
    return 'Thế giớiThứ hai, 20/2/2023, 20:45 (GMT+7)\
          Cố vấn An ninh Quốc gia Mỹ cho biết Washington\
            của ông Biden đến Kiev nhằm tránh nguy cơ xung đột.\
          {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
