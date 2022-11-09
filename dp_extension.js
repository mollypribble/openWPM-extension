// our approach: 
// 1. run crawl for all websites we want. this gets data into a sqlite db. 
// 2. run python script to transform this data into a json file with url (key), totalCookies, total with HTTP==True, total with HostOnly==True, and top 3 common domain names.
// 3. require json file in this extension and on load store data in relevant variables
// 4. render pop up on page load
// 5. toggle pop up to minimize
// *** steps 1-2 done beforehand/need to be re-done if we want to add any more sites in the future ***


// get data
import { dataJson } from "./data.json"

// define style
let style = document.createElement('style');
  style.innerHTML = `
  @font-face {
    font-family: 'KanitBold';
    src: url(./dp_frontend/Kanit/Kanit-Bold.ttf);
  }
  @font-face {
    font-family: 'KanitLight';
    src: url(./dp_frontend/Kanit/Kanit-Light.ttf);
  }
  .popup-owpm {
    position: relative;
    display: inline-block;
  }
  .collapsed-owpm {
    position: relative;
    display: inline-block;
  }
  .popup-owpm .popup {
    visibility: visible;
    width: 360px;
    background-color: #FAFDFE;
    color: black;
    text-align: left;
    position: fixed;
    z-index: 100;
    bottom: 5; 
    right: 5;
    font-family: KanitLight;
    border: 1px solid #A2A2A2;
  }
  .collapsed-owpm .collapsed {
    visibility: hidden;
    width: 70px;
    color: #fff;
    text-align: center;
    position: fixed;
    z-index: 100;
    bottom: 5; 
    right: 5;
    opacity: 0.8;
  }
  .popup-owpm .show{
    visibility: hidden;
  }
  .collapsed-owpm .show{
    visibility: visible;
  }
  .header{
    display: flex;
    flex-direction: row;
  }`;


// define global variables
let numCookies = "XX" // PLACEHOLDER: PUT INFO FROM DB HERE ON LOAD
let numHTTP = "XX" // PLACEHOLDER: PUT INFO FROM DB HERE ON LOAD
let numHost = "XX" // PLACEHOLDER: PUT INFO FROM DB HERE ON LOAD
let numNotHTTP = "XX" // PLACEHOLDER: PUT INFO FROM DB HERE ON LOAD
let numNotHost = "XX" // PLACEHOLDER: PUT INFO FROM DB HERE ON LOAD
let url = "XX" // PLACEHOLDER: PUT INFO FROM PAGE HERE ON LOAD

// display common cookies
let cookies = ["Chocolate chip", "Sugar", "Lemon drop"] // PLACEHOLDER: PUT INFO FROM DB HERE (would be nice to grab the top 3 hosts when we query the DB so we don't have to do it here)

// define pop-up HTML
let popup = `<div class="popup-owpm"> 
                <div class="popup" id="popup-owpm-id">
                    <div class="header">
                        <img src="dp_frontend/cookies.png" width=60px style="margin:10px; margin-right:0px;">
                        <p style="font-family:KanitBold; margin:5px; font-size:32px; width:250px; margin-top:20px">The Cookie Jar</p>
                        <img src="dp_frontend/x.png" width=20px onclick="togglePopup()" style="cursor:pointer; margin:10px; margin-bottom: 50px; opacity: 0.7">
                    </div>
                    <p style="margin:10px; padding-left:10px; font-size:18px;"> We've detected ${numCookies} cookies on this page</p>
                    <p style="margin:10px; padding-left:10px; font-size:16px;"> ${numNotHTTP}/${numCookies} are visible to outside scripts</p>
                    <p style="margin:10px; padding-left:10px; font-size:16px;"> ${numNotHost}/${numCookies} are sent to multiple subdomains</p>
                    <p style="margin:10px; margin-bottom:0px; padding-left:10px; font-size:16px;">The most common cookies come from:</p>
                    <ul style="list-style-type: circle; font-size:14px; margin:7px;">
                      <li>${cookies[0]}</li>
                      <li>${cookies[1]}</li>
                      <li>${cookies[2]}</li>
                    </ul>
                    <a href="https://www.flaticon.com/free-icons/cookie"  style="margin:10px; opacity:0.8; text-decoration:none; color:grey; font-size:8px;">Cookie icons created by Freepik on Flaticon</a>
                </div> 
            </div>`;

// define collapsed pop-up
let collapsed = `<div class="collapsed-owpm" id="draggable">
                    <div class="collapsed" id="collapsed-owpm-id">
                        <img src="dp_frontend/cookies.png" width=60px onclick="togglePopup()" style="cursor:pointer; margin:5px;">
                    </div>
                </div>`;

// load extension
function loadExtension(){
  console.log("loaded");

  // append styling
  document.head.appendChild(style);

  // set url global var
  url = window.location.href;
  console.log("got url")
  console.log(url)

  // set data global var and then load popup
  getData();

  // render pop-up
  loadPopup();
};

// get data
function getData(){
  console.log("get data");
  dataObj = JSON.parse(dataJson);
  console.log(dataObj);
};

// load pop-up
function loadPopup(){
    let body = document.getElementsByTagName("body")[0]
    body.insertAdjacentHTML ("afterbegin", popup);
    body.style.width = '360px';
    body.style.height = '350px';
    body.insertAdjacentHTML ("afterbegin", collapsed);
};

// toggle pop-up
function togglePopup(){
    console.log("toggle popup")
    var localPopup = document.getElementById("popup-owpm-id");
    localPopup.classList.toggle("show");
    var localCollapse = document.getElementById("collapsed-owpm-id");
    localCollapse.classList.toggle("show");
};

// on page load: load extension --> will call functions to get appropriate data and append display to HTMl body
window.onload = loadExtension();