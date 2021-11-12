from flask import Flask,jsonify
from flask import render_template, request

app = Flask(__name__)

sensor = 'sensormapfile'
gps='gpsmapfile'
temp='tempmapfile'
dist='distmapfile'

fdsens = os.open(sensor, os.O_RDONLY)
bufsens = mmap.mmap(fdsens,0, mmap.MAP_SHARED, mmap.PROT_READ)

fdgps = os.open(gps, os.O_RDONLY)
bufgps = mmap.mmap(fdgps,0, mmap.MAP_SHARED, mmap.PROT_READ)

fdtemp = os.open(temp, os.O_RDONLY)
buftemp = mmap.mmap(fdtemp,0, mmap.MAP_SHARED, mmap.PROT_READ)

fddist = os.open(dist, os.O_RDONLY)
bufdist = mmap.mmap(fdtemp,0, mmap.MAP_SHARED, mmap.PROT_READ)

@app.route("/")
def index():
    readings={}
    bufsens.seek(0)
    readings["front"] = int(bufsens.readline())
    readings["back"]=int(bufsens.readline())
    readings["right"]=int(bufsens.readline())
    readings["left"]=int(bufsens.readline())
    bufgps.seek(0)
    readings["lattitude"]=float(bufgps.readline())
    readings["longitude"]=float(bufgps.readline())
    readings["altitude"]=float(bufgps.readline())
    buftemp.seek(0)
    readings["temp"]=float(buftemp.readline())
    bufdist.seek(0)
    readings["distance"]=float(bufdist.readline())
    readings["speed"]=float(bufspeed.readline())
    return jsonify(readings)
