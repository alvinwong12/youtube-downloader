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
          filename: "test.txt",
          saveAs: false
        }, function(downloadId){
            if (downloadId == undefined){
                console.error("Cannot download");
            } else{
                console.log(downloadId)
            }
        });
      }
  });