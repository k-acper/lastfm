import csv
import arrow

# Make sure the first line of the csv is the following:
# "artist,album,track,date"

# Put the csv in the same folder as this py file and put the filename in the next line
your_csv_filename = 'lastfm.csv'

# Make sure to have python and arrow via pip installed
# 'pip install arrow' or 'pip3 install arrow' should do the trick

#artists
def prepare_csv_artists(filename):
    artists = {}
    dates = []

    # Read in all the data
    with open(filename, 'r', encoding="utf-8") as _filehandler:
        csv_file_reader = csv.DictReader(_filehandler)
        for row in csv_file_reader:
            # Read in the csv values for this row
            artist = row['artist']
            if not row['date']:
                date = year + '' + month #uses the previous entry's date
            else:
                month = arrow.get(row['date'], 'DD MMM YYYY HH:mm').format('MMMM')
                year = arrow.get(row['date'], 'DD MMM YYYY HH:mm').format('YYYY')
                date = year + ' ' + month

            # Add a new artist to the dict if needed
            if artist not in artists:
                artists[artist] = {}

            # Add a new date to the artists dict with start counter one or
            # if already present add one for this date
            if date not in artists[artist]:
                artists[artist][date] = 1
            else:
                artists[artist][date] += 1

            # Add this date to the list of all dates if needed
            if date not in dates:
                dates.insert(0, date)

    # Accumulate the counts
    artistsSum = {}
    for artist in artists:
        sum = 0
        artistsSum[artist] = {'artist':artist}
        for date in dates:
            if date in artists[artist]:
                # Add overall plays for this artist
                sum += artists[artist][date]
                artistsSum[artist][date] = sum


    # Write all the data
    dates.insert(0, 'artist')
    with open("lastfm-processed-artists.csv", 'w') as out:
        csvOut = csv.DictWriter(out, dates)
        csvOut.writeheader()
        for artist in artistsSum:
            csvOut.writerow(artistsSum[artist])

#albums
def prepare_csv_albums(filename):
    albums = {}
    dates = []

    # Read in all the data
    with open(filename, 'r', encoding="utf-8") as _filehandler:
        csv_file_reader = csv.DictReader(_filehandler)
        for row in csv_file_reader:
            # Read in the csv values for this row
            album = row['album']
            if not row['date']:
                date = year + '' + month #uses the previous entry's date
            else:
                month = arrow.get(row['date'], 'DD MMM YYYY HH:mm').format('MMMM')
                year = arrow.get(row['date'], 'DD MMM YYYY HH:mm').format('YYYY')
                date = year + ' ' + month

            # Add a new album to the dict if needed
            if album not in albums:
                albums[album] = {}

            # Add a new date to the albums dict with start counter one or
            # if already present add one for this date
            if date not in albums[album]:
                albums[album][date] = 1
            else:
                albums[album][date] += 1

            # Add this date to the list of all dates if needed
            if date not in dates:
                dates.insert(0, date)

    # Accumulate the counts
    albumsSum = {}
    for album in albums:
        sum = 0
        albumsSum[album] = {'album':album}
        for date in dates:
            if date in albums[album]:
                # Add overall plays for this album
                sum += albums[album][date]
                albumsSum[album][date] = sum

    # Write all the data
    dates.insert(0, 'album')
    with open("lastfm-processed-albums.csv", 'w') as out:
        csvOut = csv.DictWriter(out, dates)
        csvOut.writeheader()
        for album in albumsSum:
            csvOut.writerow(albumsSum[album])

#Tracks
def prepare_csv_tracks(filename):
    tracks = {}
    dates = []

    # Read in all the data
    with open(filename, 'r', encoding="utf-8") as _filehandler:
        csv_file_reader = csv.DictReader(_filehandler)
        for row in csv_file_reader:
            # Read in the csv values for this row
            track = row['track']
            if not row['date']:
                date = year + '' + month #uses the previous entry's date
            else:
                month = arrow.get(row['date'], 'DD MMM YYYY HH:mm').format('MMMM')
                year = arrow.get(row['date'], 'DD MMM YYYY HH:mm').format('YYYY')
                date = year + ' ' + month

            # Add a new track to the dict if needed
            if track not in tracks:
                tracks[track] = {}

            # Add a new date to the tracks dict with start counter one or
            # if already present add one for this date
            if date not in tracks[track]:
                tracks[track][date] = 1
            else:
                tracks[track][date] += 1

            # Add this date to the list of all dates if needed
            if date not in dates:
                dates.insert(0, date)

    # Accumulate the counts
    tracksSum = {}
    for track in tracks:
        sum = 0
        tracksSum[track] = {'track':track}
        for date in dates:
            if date in tracks[track]:
                # Add overall plays for this track
                sum += tracks[track][date]
                tracksSum[track][date] = sum

    # Write all the data
    dates.insert(0, 'track')
    with open("lastfm-processed-tracks.csv", 'w') as out:
        csvOut = csv.DictWriter(out, dates)
        csvOut.writeheader()
        for track in tracksSum:
            csvOut.writerow(tracksSum[track])

prepare_csv_artists(your_csv_filename)
print("Artists csv saved!")
prepare_csv_albums(your_csv_filename)
print("Albums csv saved!")
prepare_csv_tracks(your_csv_filename)
print("Tracks csv saved!")
