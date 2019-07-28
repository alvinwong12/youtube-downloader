function download(url) {
    var message = {type : "download", url: url};
    chrome.runtime.sendMessage(message);
}

chrome.runtime.onMessage.addListener(arg => {
    if (arg.type == "download-url"){
        download(arg.downloadUrl);
    }
});