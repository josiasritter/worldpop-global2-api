import requests
import time
import os

iso3_codes = ['AUT', 'NLD']
refyear = 2020

def download_url(url, download_path="./"):
    """Download data from a given url to a given download path on the hard drive"""
    while True:
        try:
            response = requests.get(url, timeout=30)
        except:
            print("    *** WARNING! Download froze, likely due to network instability. Restarting download...")
            time.sleep(2)
        else:
            if response.ok:
                # inmemory = tiff.imread(io.BytesIO(response.content))  # reads download data directly to memory (without writing to disk)
                with open(download_path, 'wb') as savefile:
                    savefile.write(response.content)  # write download data to disk
                break

def worldpop_download(wp_url, download_filepath):
    if not os.path.exists(download_filepath):
        print("        *** DOWNLOADING WORLDPOP POPULATION DENSITY MAP ***")
        print('        URL: ', wp_url)
        print('        Download Path: ', download_filepath)
        download_url(wp_url, download_path=download_filepath)
    map = download_filepath
    return map

for iso3 in iso3_codes:
    #'https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/DZA/v1/100m/constrained/dza_pop_2020_CN_100m_R2025A_v1.tif'
    wp_url = 'https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/' + str(refyear) + '/' + iso3 + '/v1/100m/constrained/' + iso3.lower() + '_pop_' + str(refyear) + '_CN_100m_R2025A_v1.tif'
    #download_filepath = 'WorldPop/' + str(refyear) + '/' + iso3.lower() + '_pop_' + str(refyear) + '.tif'
    download_filepath = iso3.lower() + '_pop_' + str(refyear) + '.tif'
    map = worldpop_download(wp_url, download_filepath)

