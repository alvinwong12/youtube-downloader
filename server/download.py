import youtube_dl
from youtube_dl import DownloadError

class UnsupportedOperationException(Exception):
    pass

class Options(object):
    VIDEO = ''
    AUDIO = '.mp3'
    BOTH = '.mp4'


class YoutubeDownloader(object):

    class VideoNotFoundException(Exception):
        pass

    URL = "https://www.youtube.com/watch?v="
    status = {}
    
    @staticmethod
    def download(videoId, option=Options.BOTH):
        if not videoId:
            raise YoutubeDownloader.VideoNotFoundException
        
        option = option.lower()
        ydl_opts = {}
        if option == Options.VIDEO:
            raise UnsupportedOperationException
        elif option == Options.AUDIO:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }],
                'ffmpeg_location': '.',
                'prefer_ffmpeg': True,
                'progress_hooks': [YoutubeDownloader.promise],
            }
        else:
            ydl_opts = {
                'format': 'best/best',
                'progress_hooks': [YoutubeDownloader.promise]
            }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                YoutubeDownloader.status[videoId] = {'status': None, 'filename': "", 'ext': option}
                ydl.download([YoutubeDownloader.URL + videoId])
                while not YoutubeDownloader.status.get(videoId, {}).get('status', None): pass

                if YoutubeDownloader.status[videoId]['status'] == 'finished':
                    return YoutubeDownloader.status[videoId].get('filename', "")
                else:
                    return None
        except DownloadError as e:
            raise e
    
    @staticmethod
    def promise(d):
        if d['status'] == 'finished':
            videoId = YoutubeDownloader.getVideoId(d['filename'])
            YoutubeDownloader.status[videoId]['status'] = d['status']
            YoutubeDownloader.status[videoId]['filename'] = d['filename'].replace(".webm", YoutubeDownloader.status[videoId]['ext'])
        elif d['status'] == 'error':
            YoutubeDownloader.status[videoId]['status'] = d['status']
    
    @staticmethod
    def getVideoId(s):
        tmp, add = "", False
        for c in s[::-1]:
            if c == "-" and add and tmp[::-1] in YoutubeDownloader.status: break   
            if add: tmp += c
            if c == ".": add = True
              
        return tmp[::-1]
