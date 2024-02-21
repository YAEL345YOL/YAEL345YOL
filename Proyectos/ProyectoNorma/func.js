function generar(n){
    let array = [];
    for(let i=0;i<n;++i){
        array[i] = i+1;
    }
    return array;
}

console.log(generar(10));