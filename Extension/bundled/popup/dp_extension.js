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
  .header{
    display: flex;
    flex-direction: row;
  }`;

// display # of cookies
let numCookies = "25" // PLACEHOLDER: PUT INFO FROM DB HERE

// display http/host only details
let numHTTP = "1" // PLACEHOLDER: PUT INFO FROM DB HERE
let numHost = "3" // PLACEHOLDER: PUT INFO FROM DB HERE
let numNotHTTP = "24" // PLACEHOLDER: PUT INFO FROM DB HERE
let numNotHost = "21" // PLACEHOLDER: PUT INFO FROM DB HERE

// display common cookies
let cookies = ["Chocolate chip", "Sugar", "Lemon drop"] // PLACEHOLDER: PUT INFO FROM DB HERE (would be nice to grab the top 3 hosts when we query the DB so we don't have to do it here)

// define pop-up HTML
let popup = `<div class="popup-owpm"> 
                <div class="popup" id="popup-owpm-id">
                    <div class="header">
                        <img src="dp_frontend/cookies.png" width=60px style="margin:10px; margin-right:0px;">
                        <p style="font-family:KanitBold; margin:5px; font-size:32px; width:250px; margin-top:20px">The Cookie Jar</p>
                        <img src="dp_frontend/x.png" width=20px style="cursor:pointer; margin:10px; margin-bottom: 50px; opacity: 0.7">
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

// on page load:
// append style
// append pop-up/collapsed pop-up to body div (pop-up visibility --> visible, collapsed pop-up --> hidden)
console.log("loaded");
document.head.appendChild(style);
loadPopup();

function loadPopup(){
  let body = document.getElementsByTagName("body")[0];
  body.insertAdjacentHTML("afterbegin", popup);
  body.style.width = '360px';
  body.style.height = '350px';
};