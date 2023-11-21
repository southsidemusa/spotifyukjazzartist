import json
import requests
import pygal
from django.shortcuts import render, redirect
from pygal.style import LightColorizedStyle

# Create your views here.
def allrepos(request):
    headers = {
        "X-RapidAPI-Key": "783a8398d8msh4c4967057428d1ap11cc5fjsn13f6d96ce840",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }
    response = requests.get("https://spotify23.p.rapidapi.com/top_200_tracks", headers=headers)
    top_tracks = response.json()
    context = {
        "top_tracks": top_tracks,
    }
    return render(request, "allrepos.html", context)

def table_view(request):
    response = requests.get("https://ws.audioscrobbler.com/2.0/", params={
        'method': 'tag.gettoptracks',
        'tag': 'jazz',
        'api_key': 'YOUR_LASTFM_API_KEY',
        'format': 'json'
    })
    jazz_data = response.json()['tracks']['track']
    context = {'jazz_data': jazz_data}
    return render(request, 'table.html', context)

def top_tracks_chart(request):
    headers = {
        "X-RapidAPI-Key": "783a8398d8msh4c4967057428d1ap11cc5fjsn13f6d96ce840",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    response = requests.get("https://spotify23.p.rapidapi.com/top_200_tracks", headers=headers)
    data = response.json()cc5fjsn13f6d96ce840", "X-RapidAPI-Host": "spotify23.p.rapidap
    chart_data = {}
    for track in data["tracks"]:
        chart_data[track["name"]] = track["streams"]
    chart = pygal.Bar(style=LightColorizedStyle)
    chart.title = "Top Tracks"
    chart.x_labels = chart_data.keys()
    chart.add("Streams", chart_data.values())
    chart_data_uri = chart.render_to_png()
    context = {"chart_data_uri": chart_data_uri}
    return render(request, "top_tracks_chart.html", context)

def chart(request):
    response = requests.get("https://ws.audioscrobbler.com/2.0/", params={
        'method': 'tag.gettopartists',
        'tag': 'jazz',
        'api_key': 'YOUR_LASTFM_API_KEY',
        'format': 'json'
    })
    jazz_data = response.json()['topartists']['artist']
    chart = pygal.Bar(title='Top Jazz Artists', x_title='Artist', y_title='Listeners')
    for artist in jazz_data:
        chart.add(artist['name'], artist['listeners'])
    chart_data_uri = chart.render_to_png()
    context = {'chart_data_uri': chart_data_uri}
    return render(request, 'chart.html', context)

def homepage_view(request):
    headers = {
        "X-RapidAPI-Key": "783a8398d8msh4c4967057428d1ap11cc5fjsn13f6d96ce840",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }
    response = requests.get("https://spotify23.p.rapidapi.com/top_200_tracks", headers=headers)
    data = response.json()
    context = {"tracks": data["tracks"]}
    return render(request, "homepage_view.html", context)

#charts -----
def create_chart(top_tracks):
    chart = pygal.Bar(style=LightColorizedStyle)
    chart.title = 'Top Spotify Tracks'
    for track in top_tracks[:10]: # Limit to the top 10 tracks for better visualization
        chart.add(track['name'], track['streams'])
    return chart.render_data_uri()

def data_chart(request):
    headers = {
        "X-RapidAPI-Key": "783a8398d8msh4c4967057428d1ap11cc5fjsn13f6d96ce840",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }
    response = requests.get("https://spotify23.p.rapidapi.com/top_200_tracks", headers=headers)
    top_tracks = response.json()
    chart = pygal.Bar(title='Top Spotify Tracks', x_title='Track', y_title='Streams')
    for track in top_tracks[:10]: # Limit to the top 10 tracks for better visualization
        chart.add(track['name'], track['streams'])
    chart_data_uri = chart.render_to_png()
    context = {'chart_data_uri': chart_data_uri}
    return render(request, 'data_chart.html', context)

