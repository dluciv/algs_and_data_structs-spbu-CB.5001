#!/usr/bin/env julia

import Printf
import SpecialFunctions

Printf.@printf("%d threads\n", Threads.nthreads())

function analytic_V1(n)
    pi ^ (n/2) / SpecialFunctions.gamma(n/2 + 1)    
end

function mc_V1(n, iterations)
    k = zeros(Int, Threads.nthreads())
    Threads.@threads for i = 1:iterations
        s = 0.0
        for d = 1:n
            s += rand()^2
            if s > 1.0 break end
        end
        if s <= 1.0 k[Threads.threadid()] += 1 end
    end
    sum(k) / iterations * 2 ^ n
end

MCN = 1000000

function calc()
    for d = 1:10
        av = analytic_V1(d)
        mv = mc_V1(d, MCN)
        Printf.@printf("D: %d,\tAN: %f,\tMC: %f,\tAE: %f,\tRE: %f\n",
            d, av, mv,
            abs(av-mv),
            abs(av-mv) / av
        )
    end
end

@time(calc())
