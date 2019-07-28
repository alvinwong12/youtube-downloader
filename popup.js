function startDownload() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        var downloadUrl = document.getElementById("download-url").value;
        if (downloadUrl == null || downloadUrl == undefined || downloadUrl == ""){
            downloadUrl = tabs[0].url;
        }
        chrome.tabs.sendMessage(tabs[0].id, {type: "download-url", downloadUrl: downloadUrl});
    });
}

document.getElementById('download-btn').addEventListener('click', startDownload);

chrome.tabs.query({'active': true, 'currentWindow': true}, function (tabs) {
    document.getElementById('download-url').value = tabs[0].url;
});

