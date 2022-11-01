// define style
let style = document.createElement('style');
  style.innerHTML = `
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
    width: 160px;
    background-color: #555;
    color: #fff;
    text-align: center;
    position: fixed;
    z-index: 1;
    top: 5; 
    right: 5;
  }
  .collapsed-owpm .collapsed {
    visibility: hidden;
    width: 160px;
    background-color: #555;
    color: #fff;
    text-align: center;
    position: fixed;
    z-index: 1;
    top: 5; 
    right: 5;
  }
  .popup-owpm .show{
    visibility: hidden;
  }
  .collapsed-owpm .show{
    visibility: visible;
  }`;

// define pop-up HTML
let popup = `<div class="popup-owpm"> 
                <div class="popup" id="popup-owpm-id">
                    <p>Open</p>
                    <p onclick="togglePopup()" style="cursor:pointer;">Click me to collapse</p>
                </div> 
            </div>`;

// define collapsed pop-up
let collapsed = `<div class="collapsed-owpm">
                    <div class="collapsed" id="collapsed-owpm-id">
                        <p>Collapsed</p>
                        <p onclick="togglePopup()" style="cursor:pointer;">Click me to open</p>
                    </div>
                </div>`;

// on page load:
// append style
// append pop-up/collapsed pop-up to body div (pop-up visibility --> visible, collapsed pop-up --> hidden)
console.log("loaded");
document.head.appendChild(style);
loadPopup();

function loadPopup(){
    let body = document.getElementsByTagName("body")[0]
    body.insertAdjacentHTML ("afterbegin", popup);
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

// define content
let tab1Input = `this is tab 1`
let tab2Input = `this tab 2`
let tab1Content = ``;
let tab2Content = ``;


// tab clicks:
// altnerate between tabs click
// change color on hover
function changeTabs(){
};

// TO DO 
// make UI for collapsed and expanded versions
// make tabs/toggle between tabs in expanded version
// determine what to display/connect to DB