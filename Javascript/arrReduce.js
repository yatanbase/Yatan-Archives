let arr = [ 1,2,3,4,5];

function multiply(i,j)   //i = prevResult  , j = NewResult
{
    return i*j;
}

let res = arr.reduce(multiply);
console.log(res);