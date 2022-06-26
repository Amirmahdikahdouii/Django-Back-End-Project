let statusCode = 0;

function getRandomNumber(min, max) {
    min = Math.ceil(min)
    max = Math.floor(max)
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

let playButtons = [...document.getElementsByClassName("play-button")];
let userWinCounter = document.getElementById("user-win-counter");
let userLoseCounter = document.getElementById("user-lose-counter");
let pcWinCounter = document.getElementById("pc-win-counter");
let pcLoseCounter = document.getElementById("pc-lose-counter");
let userPlayResult = document.getElementById("user-play-result");
let pcPlayResult = document.getElementById("pc-play-result");
let userPictureTag = document.getElementById("user-action-picture");
let pcPictureTag = document.getElementById("computer-action-picture");
let ajaxRequest = new XMLHttpRequest();
playButtons.forEach((button, index) => {
    button.addEventListener("click", () => {
        let url = "/Games/rock-scissors-paper/";
        let userNumber = index + 1;
        let userPictureChooseSrc;
        if (userNumber == 1) {
            userPictureChooseSrc = "../../static/img/RockScissorsPaper/rock-user.jpg";
        } else if (userNumber == 2) {
            userPictureChooseSrc = "../../static/img/RockScissorsPaper/scissors-user.jpg";
        } else {
            userPictureChooseSrc = "../../static/img/RockScissorsPaper/paper-user.jpg";
        }
        userPictureTag.src = userPictureChooseSrc;
        let pcNumber = getRandomNumber(1, 3);
        if (pcNumber == 1) {
            userPictureChooseSrc = "../../static/img/RockScissorsPaper/rock-pc.jpg";
        } else if (pcNumber == 2) {
            userPictureChooseSrc = "../../static/img/RockScissorsPaper/scissors-pc.jpg";
        } else {
            userPictureChooseSrc = "../../static/img/RockScissorsPaper/paper-pc.jpg";
        }
        pcPictureTag.src = userPictureChooseSrc;
        const ajaxRequestOnloadMethod = () => {
            let JsonResponse = ajaxRequest.responseText;
            JsonResponse = JSON.parse(JsonResponse);
            if (JsonResponse["userAuthenticated"] === true) {
                let userTotalWin = document.getElementById("user-total-win-counter");
                let userTotalLose = document.getElementById("user-total-lose-counter");
                userTotalWin.innerText = JsonResponse["winCount"];
                userTotalLose.innerText = JsonResponse["loseCount"];
            }
        }
        if ((userNumber == 1 && pcNumber == 2) || (userNumber == 2 && pcNumber == 3) || (userNumber == 3 && pcNumber == 1)) {
            let lastScore = parseInt(userWinCounter.innerText);
            lastScore++;
            userWinCounter.innerText = lastScore;
            lastScore = parseInt(pcLoseCounter.innerText);
            lastScore++;
            pcLoseCounter.innerText = lastScore;
            userPlayResult.innerText = "Win";
            userPlayResult.style.color = "#fff";
            pcPlayResult.innerText = "Lose";
            pcPlayResult.style.color = "#F24C4C";
            url = url + "1/";
            ajaxRequest.onload = ajaxRequestOnloadMethod;
            ajaxRequest.open("GET", url, true);
            ajaxRequest.send()
        } else if ((userNumber == 1 && pcNumber == 3) || (userNumber == 2 && pcNumber == 1) || (userNumber == 3 && pcNumber == 2)) {
            let lastScore = parseInt(userLoseCounter.innerText);
            lastScore++;
            userLoseCounter.innerText = lastScore;
            lastScore = parseInt(pcWinCounter.innerText);
            lastScore++;
            pcWinCounter.innerText = lastScore;
            pcPlayResult.innerText = "Win";
            pcPlayResult.style.color = "#fff";
            userPlayResult.innerText = "Lose";
            userPlayResult.style.color = "#F24C4C";
            url = url + "2/";
            ajaxRequest.onload = ajaxRequestOnloadMethod;
            ajaxRequest.open("GET", url, true);
            ajaxRequest.send()
        } else {
            pcPlayResult.innerText = "Draw";
            pcPlayResult.style.color = "#F7D716";
            userPlayResult.innerText = "Draw";
            userPlayResult.style.color = "#F7D716";
        }
    })
})