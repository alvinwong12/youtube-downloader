function injectTheScript() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var downloadUrl = document.getElementById("download-url").value;
    if (downloadUrl == null || downloadUrl == undefined || downloadUrl == ""){
        var blob = new Blob([ "test"], {type : "text/plain;charset=UTF-8"});
        downloadUrl = window.URL.createObjectURL(blob);
    }
    chrome.tabs.sendMessage(tabs[0].id, {downloadUrl: downloadUrl});
});
}

document.getElementById('download-btn').addEventListener('click', injectTheScript);


chrome.tabs.query({'active': true, 'currentWindow': true}, function (tabs) {
    document.getElementById('download-url').value = tabs[0].url;
    chrome.tabs.executeScript(tabs[0].id, {file: "download.js"});
});

