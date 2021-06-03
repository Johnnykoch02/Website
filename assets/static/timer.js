class Timer {
    constructor(id) {
        console.log(id);
        this.id = id;
        this.value = document.getElementById("input-time"+this.id).value;
        this.time = this.value*60;
        this.updateTimer();
    }
        async updateTimer() {
        if(this.time == 0) timeElem.innerHTML = ("!00:00!");
        else {
            let minutes = Math.floor( this.time/60);  
            let seconds =  this.time % 60;
            seconds = seconds<10 ? '0' + seconds: seconds;
            let timeElem = document.getElementById("time-"+this.id);
            timeElem.innerHTML = (minutes+":"+seconds);
            setTimeout(empty, 1000);
            this.updateTimer();
        }
    }
} 
function empty() {
}