function updateTimer(deadline) {
    var time = deadline - new Date();
    return {
        days: Math.floor(time / (1000 * 60 * 60 * 24)),
        hours: Math.floor((time / (1000 * 60 * 60)) % 24),
        minutes: Math.floor((time / 1000 / 60) % 60),
        seconds: Math.floor((time / 1000) % 60),
        total: time
    };
}

function animateClock(span) {
    span.className = "animate__flipOutY";
    setTimeout(function () {
        span.className = "";
    }, 1000);
}

function startTimer(id, deadline) {
    var timerInterval = setInterval(function () {
        var clock = document.getElementById(id);
        var timer = updateTimer(deadline);

        if (timer.total < 0) {
            clearInterval(timerInterval);
            var b = document.querySelector(".main-wrapper")
            b.setAttribute("style", "display:block")
            var a = document.querySelector("#main")
            a.setAttribute("style", "display:none")
       }
        
        clock.innerHTML =
            "<span>" +
            timer.days +
            "</span>" +
            "<span>" +
            timer.hours +
            "</span>" +
            "<span>" +
            timer.minutes +
            "</span>" +
            "<span>" +
            timer.seconds +
            "</span>";

        // animation
        var spans = clock.getElementsByTagName("span");
        animateClock(spans[3]);
        if (timer.seconds == 59) animateClock(spans[2]);
        if (timer.minutes == 59 && timer.seconds == 59) animateClock(spans[1]);
        if (timer.hours == 23 && timer.minutes == 59 && timer.seconds == 59)
            animateClock(spans[0]);
        
    }, 1000);
}

window.onload = function () {
    var deadline = new Date("August 3, 2020 12:00:00");
    startTimer("clock", deadline);
};
