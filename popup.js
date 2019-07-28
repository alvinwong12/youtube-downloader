function injectTheScript() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    // query the active tab, which will be only one tab
    //and inject the script in it
    chrome.tabs.executeScript(tabs[0].id, {file: "download.js"});
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
});

