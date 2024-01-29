# File Type
FileType = input('Enter filetype (mp3, wav, ...) for Playlist: ')

# Raw Tracks and Track Names
Track1_raw = input('Enter raw format filename for Track 1 (Track-mm:ss.raw): ')
Track1_name = input('Enter song name for Track 1: ')
Track2_raw = input('Enter raw format filename for Track 2 (Track-mm:ss.raw): ')
Track2_name = input('Enter song name for Track 2: ')
Track3_raw = input('Enter raw format filename for Track 3 (Track-mm:ss.raw): ')
Track3_name = input('Enter song name for Track 3: ')

# Constants
TRACK_NAMES = [Track1_name, Track2_name, Track3_name]
TRACK_NUM = [1, 2, 3]

# Track Number choice
choice = int(input('Enter Track number (1-3) of filename to display: '))

# Track time to numerical value
Track1_Min = int(Track1_raw[6:8])
Track2_Min = int(Track2_raw[6:8])
Track3_Min = int(Track3_raw[6:8])
Track_Length_Sec = (Track1_Min + Track2_Min + Track3_Min) * 60
Track1_Sec = int(Track1_raw[9:11])
Track2_Sec = int(Track2_raw[9:11])
Track3_Sec = int(Track3_raw[9:11])
Playlist_Total_Sec = Track_Length_Sec + Track1_Sec + Track2_Sec + Track3_Sec

# Playlist Total Time Algorithm
Playlist_Length = (Playlist_Total_Sec // 60)
Length_Remainder = (Playlist_Total_Sec % 60)

# Average Track Time Algorithm 
Avg_Track_Length = Playlist_Length // 3
Avg_Length_Rem = round(Length_Remainder / 3)

# outputs
print('Playlist total time is ' + str(Playlist_Length) + ' minutes and ' + str(Length_Remainder) + ' seconds.')
print('Average track time is ' + str(Avg_Track_Length) + ' minutes and ' + str(Avg_Length_Rem) + ' seconds.')
print('0' + str(TRACK_NUM[choice-1]) + '-' + str(TRACK_NAMES[choice-1]) +'.' + str(FileType))