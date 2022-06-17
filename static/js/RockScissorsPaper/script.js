function getRandomNumber(min, max) {
    min = Math.ceil(min)
    max = Math.floor(max)
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
let playButton = document.getElementById("play-button");
let userWinCounter = document.getElementById("user-win-counter");
let userLoseCounter = document.getElementById("user-lose-counter");
let pcWinCounter = document.getElementById("pc-win-counter");
let pcLoseCounter = document.getElementById("pc-lose-counter");
let userPlayResult = document.getElementById("user-play-result");
let pcPlayResult = document.getElementById("pc-play-result");
playButton.addEventListener("click", () => {
    let userNumber = getRandomNumber(1, 3);
    let pcNumber = getRandomNumber(1, 3);
    if (userNumber > pcNumber) {
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
    }
    else if (userNumber < pcNumber) {
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
    }
    else {
        pcPlayResult.innerText = "Draw";
        pcPlayResult.style.color = "#F7D716";
        userPlayResult.innerText = "Draw";
        userPlayResult.style.color = "#F7D716";
    }
})