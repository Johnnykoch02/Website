class Timer {
    constructor(id) {
        console.log(id);
        this.value = document.getElementById("input-time"+id).value;
        this.time = this.value*60;
        this.timer = setInterval(updateTimer, 1000); 
    }
    async updaterTimer() {
        if(time == 0) clearInterval(timer);
        let minutes = Math.floor( this.time/60);  
        let seconds =  this.time % 60;
        this.seconds = seconds<10 ? '0' + seconds: seconds;
        let timeElem = document.getElementById("time-"+id);
        timeElem.innerHTML = (minutes+":"+seconds);
        this.time--;    
    }
} 