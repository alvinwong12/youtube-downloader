from download import YoutubeDownloader, Options
import unittest

class TestYoutubeDownloader(unittest.TestCase):

    def test_getFileNameOnSuccess(self):
        videoId = 'abc'
        option = Options.AUDIO
        YoutubeDownloader.status[videoId] =  {'status': None, 'filename': "", 'ext': option}
        YoutubeDownloader.promise({'status': 'finished', "filename": 'def-abc.webm'})
        self.assertEquals(YoutubeDownloader.status[videoId]['filename'], "abc.mp3")

if __name__ == "__main__":
    unittest.main()