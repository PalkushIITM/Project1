# B1 & B2: Security Checks
import os

def B12(filepath):  # B1 & B2: Security Checks
    if filepath.startswith('/data'):
        return True
    else:
        return False

# B3: Fetch Data from an API
def B3(url, save_path):
    if not B12(save_path):  # Security check (B1 & B2)
        return None
    import requests
    response = requests.get(url)
    with open(save_path, 'w') as file:
        file.write(response.text)

# B4: Clone a Git Repo and Make a Commit
# def B4(repo_url, commit_message):  # B4: Git Repository Handling
#     import subprocess
#     subprocess.run(["git", "clone", repo_url, "/data/repo"])
#     subprocess.run(["git", "-C", "/data/repo", "commit", "-m", commit_message])

# B5: Run SQL Query
def B5(db_path, query, output_filename):  # B5: SQL Query Execution
    if not B12(db_path):  # Security check (B1 & B2)
        return None
    import sqlite3, duckdb
    conn = sqlite3.connect(db_path) if db_path.endswith('.db') else duckdb.connect(db_path)
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    conn.close()
    with open(output_filename, 'w') as file:
        file.write(str(result))
    return result

# B6: Web Scraping
def B6(url, output_filename):  # B6: Web Scraping
    import requests
    result = requests.get(url).text
    with open(output_filename, 'w') as file:
        file.write(str(result))

# B7: Image Processing
def B7(image_path, output_path, resize=None):  # B7: Image Processing
    from PIL import Image
    if not B12(image_path) or not B12(output_path):  # Security check (B1 & B2)
        return None
    img = Image.open(image_path)
    if resize:
        img = img.resize(resize)
    img.save(output_path)

# B8: Audio Transcription
# def B8(audio_path):  # B8: Audio Transcription
#     import openai
#     if not B12(audio_path):  # Security check (B1 & B2)
#         return None
#     with open(audio_path, 'rb') as audio_file:
#         return openai.Audio.transcribe("whisper-1", audio_file)

# B9: Markdown to HTML Conversion
def B9(md_path, output_path):  # B9: Markdown to HTML Conversion
    import markdown
    if not B12(md_path) or not B12(output_path):  # Security check (B1 & B2)
        return None
    with open(md_path, 'r') as file:
        html = markdown.markdown(file.read())
    with open(output_path, 'w') as file:
        file.write(html)

#B10: API Endpoint for CSV Filtering
#from flask import Flask, request, jsonify
#app = Flask(__name__)
# @app.route('/filter_csv', methods=['POST'])  # B10: CSV Filtering API
# def B10():
#     import pandas as pd
#     data = request.json
#     csv_path, filter_column, filter_value = data['csv_path'], data['filter_column'], data['filter_value']
#     B12(csv_path)  # Security check (B1 & B2)
#     df = pd.read_csv(csv_path)
#     filtered = df[df[filter_column] == filter_value]
#     return jsonify(filtered.to_dict(orient='records'))
