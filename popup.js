chrome.tabs.getSelected(null,function(tab) {
    var tablink = tab.url;
});

chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url;
    // use `url` here inside the callback because it's asynchronous!
});
