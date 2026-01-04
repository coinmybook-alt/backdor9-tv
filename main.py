from flask import Flask, render_template_string
import os

app = Flask(__name__)

KANALLAR = [
    {"ad": "beIN Sports 1", "url": "https://hls.imrantoy7384.workers.dev/https://corestream.ronaldovurdu.help//hls/bein-sports-1.m3u8"},
    {"ad": "beIN Sports 2", "url": "https://hls.imrantoy7384.workers.dev/https://corestream.ronaldovurdu.help//hls/bein-sports-2.m3u8"},
    {"ad": "S Sport 1", "url": "https://hls.imrantoy7384.workers.dev/https://corestream.ronaldovurdu.help//hls/s-sport.m3u8"},
    {"ad": "TRT Spor", "url": "https://tv-trtspor1.medya.trt.com.tr/master_720.m3u8"}
]

@app.route('/')
def index():
    return render_template_string("""
    <html><body style="background:#000; color:#0f0; text-align:center; font-family:sans-serif;">
        <h2>BACKDOR9 TV PRO</h2>
        {% for k in kanallar %}
        <a href="intent://{{ k.url.split('://')[1] }}#Intent;scheme=https;type=application/x-mpegURL;package=com.mxtech.videoplayer.ad;S.title={{ k.ad }};end" 
           style="display:block; background:#222; color:#fff; padding:20px; margin:10px; border:1px solid #0f0; text-decoration:none; border-radius:10px; font-weight:bold;">
           {{ k.ad }}
        </a>
        {% endfor %}
    </body></html>
    """, kanallar=KANALLAR)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
