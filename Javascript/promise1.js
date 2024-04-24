console.log("program start");

function getRand(max)
{
    return Math.floor(Math.random()*max);
}

const x = new Promise(function promFunc(f,r){
    let y = getRand(5);
    if(y%2 == 0){
        f (y);
    }
    else{
        r (y);
    }



})

