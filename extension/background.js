chrome.runtime.onInstalled.addListener(function() {
    chrome.declarativeContent.onPageChanged.removeRules(undefined, function () {
        chrome.declarativeContent.onPageChanged.addRules([{
            conditions: [new chrome.declarativeContent.PageStateMatcher({
                pageUrl: { hostEquals: 'www.youtube.com'},
            })
            ],
            actions: [new chrome.declarativeContent.ShowPageAction()]
        }]);
    });
});

chrome.runtime.onMessage.addListener(
    function(arg, sender, sendResponse) {
      if(arg.type == "download"){
        chrome.downloads.download({
          url: arg.url,
          saveAs: false,
          method: "GET"
        }, function(downloadId){
            if (downloadId == undefined){
                console.error("Cannot download");
            } else{
                console.log(downloadId)
            }
        });
    }
});

chrome.management.getSelf(function(extensionInfo){

    if(extensionInfo.installType == "development"){
        chrome.storage.sync.set({serverUrl: 'http://localhost:5000'}, function() {});
    } else {
        chrome.storage.sync.set({serverUrl: 'basic-ingress.alvinwong12.usw1.kubesail.io'}, function() {}); // change to prod url later
    }
});