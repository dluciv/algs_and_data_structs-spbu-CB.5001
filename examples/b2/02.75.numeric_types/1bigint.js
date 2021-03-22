// https://github.com/v8/v8/blob/6.8.137/src/objects/bigint.cc

function sum_n(about, how_many=1000000n) {
    let res = about;
    for(let z = 0n; z < how_many; z++){
        res += about;
        res --;
        res -= about;
        res *= 2n;
        res += 2n;
        res /= 2n;
    }
    return res;
}

function tttn() {
    console.log("Starting...");
    for(const v of [300n, 2n**30n, 2n**50n, 2n**70n]) {
        console.time(v);
        for(let n = 0n; n < 10n; ++n)
            sum_n(v);
        console.timeEnd(v);
    }
}

function sum_f(about, how_many=1000000n) {
    let res = about;
    for(let z = 0n; z < how_many; z++){
        res += about;
        res --;
        res -= about;
        res *= 2;
        res += 2;
        res /= 2;
    }
    return res;
}

function tttf() {
    console.log("Starting...");
    for(const v of [300, 2**30, 2**50, 2**70]) {
        console.time(v);
        for(let n = 0n; n < 10n; ++n)
            sum_f(v);
        console.timeEnd(v);
    }
}

tttn();
tttf();
