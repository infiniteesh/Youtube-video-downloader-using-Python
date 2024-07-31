from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    if not url:
        return render_template('index.html', error="Please provide a valid YouTube URL")

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path='downloads', filename='video.mp4')
        return send_file(os.path.join('downloads', 'video.mp4'), as_attachment=True, download_name='video.mp4')
    except Exception as e:
        return render_template('index.html', error=f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)
