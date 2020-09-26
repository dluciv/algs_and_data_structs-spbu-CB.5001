#!/usr/bin/env julia

import Printf
import SpecialFunctions

Printf.@printf("%d threads\n", Threads.nthreads())

function analytic_V1(n)
    pi ^ (n/2) / SpecialFunctions.gamma(n/2 + 1)
end

function mc_K_N(n, iterations)
    k = zeros(Int, Threads.nthreads())
    Threads.@threads for _ = 1:iterations
        s = 0.0
        for d = 1:n
            s += rand()^2
            if s > 1.0 break end
        end
        if s <= 1.0 k[Threads.threadid()] += 1 end
    end
    sum(k) / iterations
end

MCN = 1000000

function calc()
    for d = 1:10
        av = analytic_V1(d)
        mv = mc_K_N(d, MCN)  * 2 ^ d
        Printf.@printf("D: %d,\tAN: %f,\tMC: %f,\tAE: %f,\tRE: %f\n",
            d, av, mv,
            abs(av-mv),
            abs(av-mv) / av
        )
    end
end

@time(calc())
println("======================")

PN = 1000
PEPS = 0.02
PD = 3

av1q = analytic_V1(PD) / 2 ^ PD

function pmepsilon()
    ge_epsilon = zeros(Int, Threads.nthreads())
    Threads.@threads for _ = 1:PN
        kn = mc_K_N(PD, MCN)
        if abs(av1q - kn) >= PEPS
            ge_epsilon[Threads.threadid()] += 1
        end
    end
    return sum(ge_epsilon) / PN
end

pgeepsilon = @time(pmepsilon())
rightside = av1q * (1.0 - av1q) / (PN * PEPS^2 * 1.0)

Printf.@printf("Left: %f, Right: %f", pgeepsilon, rightside)
