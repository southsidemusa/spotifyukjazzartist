from flask import Flask, render_template
import pygal

app = Flask(__name__)

@app.route('/')
def index():
    chart = pygal.Bar()
    chart.add('Track 1', 10)
    chart.add('Track 2', 20)
    chart.add('Track 3', 30)
    chart_data_uri = chart.render_data_uri()
    return render_template('top_tracks_chart.html', chart_svg_data_uri=chart_data_uri)
