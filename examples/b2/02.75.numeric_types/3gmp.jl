#!/usr/bin/env julia

function sum_n(about)
    res = about
    for z in 1:1000000
        res += about
        res -= 1
        res -= about
        res *= 2
        res += 2
        res /= 2
    end
    res == 0
end

function measure_v(w)
    @time begin
        for n in 1:10
            sum_n(w)
        end
    end
end


v = BigInt(1)
for i in 1:40
    global v
    v *= 65536
    print(v)
    measure_v(v)
end
