from flask import Flask, render_template_string
import os

app = Flask(__name__)

KANALLAR = [
    {"ad": "beIN Sports 1", "url": "https://hls.imrantoy7384.workers.dev/https://corestream.ronaldovurdu.help//hls/bein-sports-1.m3u8"},
    {"ad": "TRT Spor", "url": "https://tv-trtspor1.medya.trt.com.tr/master_720.m3u8"}
]

HTML_KODU = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background: #000; color: #0f0; text-align: center; font-family: sans-serif; }
        .btn { background: #222; color: #fff; padding: 20px; border: 1px solid #0f0; display: block; margin: 10px; text-decoration: none; border-radius: 10px; font-weight: bold; }
    </style>
</head>
<body>
    <h2 style="color: #0f0;">BACKDOR9 TV</h2>
    {% for k in kanallar %}
    <a href="intent://{{ k.url.split('://')[1] }}#Intent;scheme=https;type=application/x-mpegURL;package=com.mxtech.videoplayer.ad;S.title={{ k.ad }};end" class="btn">
        {{ k.ad }}
    </a>
    {% endfor %}
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_KODU, kanallar=KANALLAR)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
