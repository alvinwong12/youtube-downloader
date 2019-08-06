import youtube_dl

class UnsupportedOperationException(Exception):
    pass

class Options(object):
    VIDEO = 'video'
    AUDIO = 'audio'
    BOTH = 'both'


class YoutubeDownloader(object):

    class VideoNotFoundException(Exception):
        pass

    URL = "https://www.youtube.com/watch?v="
    
    @staticmethod
    def download(videoId, option=Options.BOTH):
        if not videoId:
            raise YoutubeDownloader.VideoNotFoundException
        
        option = option.lower()
        ydl_opts = {}
        if option == Options.VIDEO:
            # ydl_opts = {
            #     'format': 'bestvideo/best',
            #     'postprocessors': [{
            #         'key': 'FFmpegVideoConvertor',
            #         'preferredcodec': 'mp4',
            #     }],
            #     'ffmpeg_location': '.',
            #     'prefer_ffmpeg': True
            # }
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
                'prefer_ffmpeg': True
            }
        else:
            ydl_opts = {
                'format': 'best/best'
            }
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([YoutubeDownloader.URL + videoId])
        except DownloadError as e:
            raise e
        
if __name__ == "__main__":
    YoutubeDownloader.download("Qox0qDl4Kmg")

