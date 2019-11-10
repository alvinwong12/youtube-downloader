function startDownload() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        var videoId = document.getElementById("videoId").value;
        if (videoId == null || videoId == undefined || videoId == ""){
            videoId = tabs[0].url;
        }
        var options = document.getElementsByName('option'); 
        var option = "" 
        for(i = 0; i < options.length; i++) { 
            if(options[i].checked) {
                option = options[i].value; 
            }
        } 
        chrome.tabs.sendMessage(tabs[0].id, {type: "videoId", videoId: videoId, option: option});
    });
}

function setVideoId(){
    chrome.tabs.query({'active': true, 'currentWindow': true}, function (tabs) {
        var s = tabs[0].url.split("watch?v=");
        s = s[1].split("&");
        // document.getElementById('videoId').value = s.length > 1 ? s[0] : "";
        document.getElementById('videoId').value = s[0];
    });
}

document.getElementById('download-btn').addEventListener('click', startDownload);
document.getElementById('select-btn').addEventListener('click', setVideoId);

setVideoId();

