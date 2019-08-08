function startDownload() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        var videoId = document.getElementById("videoId").value;
        if (videoId == null || videoId == undefined || videoId == ""){
            videoId = tabs[0].url;
        }
        chrome.tabs.sendMessage(tabs[0].id, {type: "videoId", videoId: videoId});
    });
}

document.getElementById('download-btn').addEventListener('click', startDownload);

chrome.tabs.query({'active': true, 'currentWindow': true}, function (tabs) {
    var s = tabs[0].url.split("watch?v=");    
    document.getElementById('videoId').value = s.length > 1 ? s[1] : "";
});

