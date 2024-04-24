//in this code we do promise chaining , first i download image , then i save it, then i return the address



console.log("program start");
x = Promise.resolve("file downloaded");
y= x.then(function exec(res,rej){
    if(res != null)
    {
        console.log("file downloaded");
        return "img";
    }})

z= y.then(function res(string){
    console.log("saved in file");
    return "fileadrress";
})

q=z.then(function last(string){
    console.log("downloadfile is stored at: ",string);
})