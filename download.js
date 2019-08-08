function download(videoId, option) {
    chrome.storage.sync.get('serverUrl', function(data) {
        var message = {type : "download", url: data.serverUrl + "/" + videoId + "?option=" +  option};
        chrome.runtime.sendMessage(message);
    });
    
}

chrome.runtime.onMessage.addListener(arg => {
    if (arg.type == "videoId"){
        download(arg.videoId, arg.option);
    }
});