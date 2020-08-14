import json
import urllib.request
from pathlib import Path
from urllib.error import HTTPError

import requests
print("Just Dance Now Downloader by Yunyl 1.0.0")
SONG_JSON_PATH = './songs.json'
SONG_BASE_URL = 'http://jdnowweb-s.cdn.ubi.com/uat/release_tu2/20150928_1740/songs/'
LOCAL_PATH = 'songs/'

files_to_download = [
    "/assets/web/{1}.jpg",
    "/assets/web/{1}_small.jpg",
    "/assets/web/pictos-sprite.png",
    "/assets/web/pictos-sprite.css",
    "/assets/web/pictos-sprite.css",
    "/assets/web/{0}.ogg",
    "/assets/web/{0}.mp3",
    "/assets/common/coaches/{1}_coach_1.png",
    "/assets/common/coaches/{1}_coach_2.png",
    "/assets/common/coaches/{1}_coach_3.png",
    "/assets/common/coaches/{1}_coach_4.png",
    "/assets/common/coaches/{1}_coach_1_big.png",
    "/assets/common/coaches/{1}_coach_2_big.png",
    "/assets/common/coaches/{1}_coach_3_big.png",
    "/assets/common/coaches/{1}_coach_4_big.png",
    "/data/moves/{0}_moves0.json",
    "/data/moves/{0}_moves1.json",
    "/data/moves/{0}_moves2.json",
    "/data/moves/{0}_moves3.json",
	"/dist/bundle/{0}.zip",
	"/dist/bundle/{0}_1.zip",
	"/dist/bundle/{0}_2.zip",
	"/dist/bundle/{0}_3.zip",
	"/dist/bundle/{0}_4.zip",
	"/dist/bundle/{0}_5.zip",
	"/dist/bundle/{0}_6.zip",
	"/dist/bundle/{0}_7.zip",
	"/dist/bundle/{0}_8.zip",
	"/dist/bundle/{0}_9.zip",
	"/dist/bundle/{0}_10.zip",
]

if __name__ == '__main__':
    with open(SONG_JSON_PATH) as json_file:
        obj = json.load(json_file)
    song_names = obj[0]['songs']

    file_count = 0

    for i, song_name in enumerate(song_names, 1):
        print(f"\n\nDownloading song: {song_name} ({i}/{len(song_names)})", end='')

        for file_path in files_to_download:
            # create the remote url and local path strings
            remote_url = SONG_BASE_URL + song_name + file_path.format(song_name, song_name.lower())
            local_path = LOCAL_PATH + song_name + file_path.format(song_name, song_name.lower())

            print(f"\nDownloading file:", remote_url, end='')

            # create folders
            folder = "/".join(local_path.split("/")[:-1])
            Path(folder).mkdir(parents=True, exist_ok=True)

            # download and place files
            try:
                urllib.request.urlretrieve(remote_url, local_path)
                file_count += 1

            except HTTPError:
                print(" | Could not be found on the server!", end='')

    print(f"Successfully downloaded {len(song_names)} and {file_count} files.")
