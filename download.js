function download(url) {
    var message = {type : "download", url: url};
    chrome.runtime.sendMessage(message);
}

// download();

chrome.runtime.onMessage.addListener(msg => {
    console.log(msg.downloadUrl);
    download(msg.downloadUrl);
});