# Time to download all instances of all instances of every words spoken.
# By considering the internet speed of the broadband.

# Equivalent size of every words ever spoken in about 5 EB.(exabytes)
# 1 EB = 1e12 MB

print('Welcome to the program',
'This program is to calculate the time to download all instances of all instances',
'of every words spoken by considering the internet speed of the broadband.')

#Input of size and internet speed
size_words = int(input('Enter the size of all words ever spoken in EB(exabytes): '))
size_words_mb = size_words*1e12
internet_speed = float(input('Enter the speed of your internet connection in mbps: '))

#Calculate the time required
time_to_download = size_words_mb/internet_speed
time_to_download_min = time_to_download/60
time_to_download_hours = time_to_download_min/60

#Output
print('It would take about', format(time_to_download,'.2e'),'seconds/',
    format(time_to_download_min,'.2e'),'minutes/',format(time_to_download_hours,'.2e'),'hours',
    'to dowload all the instances of every word spoken.')
