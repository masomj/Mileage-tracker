let endTime = document.getElementById("end-time")
let startTime = document.getElementById("start-time")
let dateToday = new Date()

let curTime = dateToday.getHours() + ":" + dateToday.getMinutes()

startTime.addEventListener("click", setTime)
endTime.addEventListener("click", setTime)

function setTime(evt){
    evt.currentTarget.value = curTime
}


