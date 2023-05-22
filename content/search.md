+++
title = "🔎︎"
menu = "main"
weight = 30
+++

<style>
  @media screen and (max-width: 500px) {
     .search{
       padding-right: 25px;
     }

     .search input{
       width: 96%;
     }

     .search button{
       display: true;
     }
  }
  @media screen and (min-width: 500px) {
      .search{
        width: 500px;
      }

      .search input{
        width: 444px;
      }
  }

  .search{
    margin: auto;
  }

  .search input{
    outline: none;
    border: 2px solid #349D48;
    height: 32px;
    padding: 10px;
  }
  .search button{
    outline: none;
    border: 0px;
    height: 32px;
    width:32px;
    position:absolute;
    background-color: #349D48 ;
  }
  .search .icon{
    width: 16px;
    height: 16px;
  }
  a.post-link{
    color: black;
    text-decoration: none;
  }
    &:hover{
      color: #349D48;
    }
  a.read-more-link{
    padding: 8px 12px;
    border-radius: 4px;
    color: white;
    background-color: #349D48;
    text-decoration: none;
  }
  #search-tip{
    margin: 8px;
    font-size: 16px;
  }
</style>
<div class="search">
  <input type="text" placeholder="輸入搜尋內容" id="search-key" />
  <button onclick="search()">
    <svg t="1583982313567" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1271"
      width="200" height="200" xmlns:xlink="http://www.w3.org/1999/xlink">
      <defs>
        <style type="text/css"></style>
      </defs>
      <path d="M694.857143 475.428571q0-105.714286-75.142857-180.857142T438.857143 219.428571 258 294.571429 182.857143 475.428571t75.142857 180.857143T438.857143 731.428571t180.857143-75.142857T694.857143 475.428571z m292.571428 475.428572q0 29.714286-21.714285 51.428571t-51.428572 21.714286q-30.857143 0-51.428571-21.714286l-196-195.428571q-102.285714 70.857143-228 70.857143-81.714286 0-156.285714-31.714286t-128.571429-85.714286-85.714286-128.571428T36.571429 475.428571t31.714285-156.285714 85.714286-128.571428 128.571429-85.714286T438.857143 73.142857t156.285714 31.714286 128.571429 85.714286 85.714285 128.571428T841.142857 475.428571q0 125.714286-70.857143 228l196 196q21.142857 21.142857 21.142857 51.428572z"
        p-id="1272" fill="#ffffff"></path>
    </svg>
  </button>
</div>
<h1 id="search-tip" style="color: #349D48;text-align: center;display: none;">搜尋中</h1>
<br />
<div id="result"></div>

<script type="text/javascript">
  // enter
  window.onload = function() {
    document.onkeydown = function(ev) {
      var event = ev || event
      if (event.keyCode == 13) {
        search()
      }
    }
  }

  // search
  function search() {
    key = document.getElementById("search-key").value;
    if (key === "") {
      return;
    }
    document.getElementById("search-key").value = "";

    // tip
    document.getElementById("search-tip").innerText = "搜尋中";
    document.getElementById("search-tip").style.display = "block";

    // clear
    var el = document.getElementById('result');
    var childs = el.childNodes;
    for (var i = childs.length - 1; i >= 0; i--) {
      el.removeChild(childs[i]);
    }

    // xml
    xmltext = new XMLHttpRequest;
    xmltext.open("GET", "/index.xml", false);
    xmltext.send();
    resp = xmltext.responseXML;
    items = resp.getElementsByTagName("item");
    // search
    var i = 0;
    haveResult = false;
    while (i < items.length) {
      txt = items[i].getElementsByTagName("title")[0].innerHTML + items[i].getElementsByTagName("description")[0].innerHTML
      if (txt.indexOf(key) > -1) {
        haveResult = true;
        title = items[i].getElementsByTagName("title")[0].innerHTML;
        link = items[i].getElementsByTagName("link")[0].innerHTML;
        time = items[i].getElementsByTagName("pubDate")[0].innerHTML;
        mark = items[i].getElementsByTagName("description")[0].innerHTML;
        addItem(title, link, time, mark)
      }
      i++;
    }
    if (!haveResult) {
      document.getElementById("search-tip").innerText = "未找到相關內容!";
      document.getElementById("search-tip").style.display = "block";
    }
  }

  // add
  function addItem(title, link, time, mark) {
    document.getElementById("search-tip").style.display = "none";
    tmpl = "<article class=\"post\" style=\"padding: 8px 0px 16px 0px ; border-bottom: 1px solid #e6e6e6;\" >" +"<h3 class=\"post-title\"><a class=\"post-link\" href=\"" + link + "\" target=\"_blank\">" + title + "</a></h3>" +" </header>" +
      "<div class=\"post-content\">" +
      "<div class=\"post-summary\">" + mark + "</div>" +"<br>"+
      "<div class=\"read-more\">" +
      "<a href=\"" + link + "\" class=\"read-more-link\" target=\"_blank\">閱讀更多</a>" +
      "</div>" +
      " </div>" +
      "</article>"
    div = document.createElement("div")
    div.innerHTML = tmpl;
    document.getElementById('result').appendChild(div)
  }
</script>

