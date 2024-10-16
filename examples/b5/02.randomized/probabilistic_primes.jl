### A Pluto.jl notebook ###
# v0.20.0

using Markdown
using InteractiveUtils

# This Pluto notebook uses @bind for interactivity. When running this notebook outside of Pluto, the following 'mock version' of @bind gives bound variables a default value (instead of an error).
macro bind(def, element)
    quote
        local iv = try Base.loaded_modules[Base.PkgId(Base.UUID("6e696c72-6542-2067-7265-42206c756150"), "AbstractPlutoDingetjes")].Bonds.initial_value catch; b -> missing; end
        local el = $(esc(element))
        global $(esc(def)) = Core.applicable(Base.get, el) ? Base.get(el) : iv(el)
        el
    end
end

# ╔═╡ a4d49bda-47f9-11ed-2630-93e53521cf7b
begin
	using Primes
	using Printf
	using ProgressBars
	using Mods
	using PlutoUI
	using ProgressLogging
	
	md"""
	# Тест Ферма
	
	https://rosettacode.org/wiki/Fermat_numbers#Julia
	"""
end

# ╔═╡ 496ae66b-6082-4ef2-a132-b616aa45b613
"""
Вычисление символа Якоби \$\\left(\\frac{a}{n}\\right)\$

    jakobi(a, n)

[Реализация](https://rosettacode.org/wiki/Jacobi_symbol#Julia)
"""
function jacobi(a, n)
    a %= n
    result = 1
    while a != 0
        while iseven(a)
            a ÷= 2
            ((n % 8) in [3, 5]) && (result *= -1)
        end
        a, n = n, a
        (a % 4 == n % 4 == 3) && (result *= -1)
        a %= n
    end
    return n == 1 ? result : 0
end

# ╔═╡ 41c8044f-b08a-4952-9fe6-5bf8b7fe0d56
"""
Тест Ферма с длинной арифметикой
"""
function fpprime(n; iterations = 10, only_consider_coprimes=false)
    for a in rand(2:n-1, iterations)
        if only_consider_coprimes && gcd(n, a) != 1
            # Вообще, если gcd(n, a) != 1, можно и сразу false вернуть, но gcd(n, a) здесь не для этого,
            # а как раз для того, чтобы помочь тесту Ферма обмануться (см. ниже числа Кармайкла).
            # В "боевом" режиме таким пользоваться конечно нельзя, т.к. gcd небыстрый.
            continue
        end
        if mod(big(a)^(n - 1), n) != 1
            return false
        end
    end
    return true
end

# ╔═╡ acd839bb-1be8-4834-894f-fa36f36fc366
"""
Тест Ферма без явной длинной арифмметики, но потенциально бесполезный =)
"""
function fpprimem(n; iterations = 10, only_consider_coprimes=false)
    for a in rand(2:n-1, iterations)
        if only_consider_coprimes && gcd(n, a) != 1
            # Аналогично, если gcd(n, a) != 1, можно и сразу false вернуть, но gcd(n, a) здесь не для этого,
            # а как раз для того, чтобы помочь тесту Ферма обмануться (см. ниже числа Кармайкла).
            # В "боевом" режиме таким пользоваться конечно нельзя, т.к. gcd небыстрый.
            continue
        end
        if powermod(a, n - 1, n) != 1 # Mod(a, n) ^ (n - 1) != 1  # Slooooow
            return false
        end
    end
    return true
end

# ╔═╡ cf8e8dd2-2ac6-4ede-8e85-9686a2a316da
@bind fpprimemmode Radio(["software" => "Software long integers", "hardware" => "Hardware integers"], default="hardware")

# ╔═╡ 096c3609-4e24-4a8d-9f24-da640f86fc8f
begin
	print("Только взаимно простые n и a")
	@bind only_coprimes CheckBox()
end

# ╔═╡ ffcd757f-5c8c-4abd-9247-5c4d6b3e0fa8
@bind fermat_iterations NumberField(5:100, default=if only_coprimes 25 else 10 end)

# ╔═╡ 3fce9229-ab56-40b2-8d8a-347c4bd5f5ac
begin
	fpf = if fpprimemmode == "software"
		fpprime
	else
		fpprimem
	end
end

# ╔═╡ d21b75ab-922f-4467-934a-abc75a994c15
@progress for n = 3:3000000
	if fpf(n, iterations=fermat_iterations, only_consider_coprimes=only_coprimes) != Primes.isprime(n)
		println("Fail on $(n)")
	end
end;

# ╔═╡ 34d14494-83d4-4c6e-afb0-a289123060b5
first_сarmichael_numbers = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361]

# ╔═╡ e596a53e-ad98-4778-8800-28de305440dd
md"""
## Числа Кармайкла

**Число Кармайкла** — составное число $n$, которое удовлетворяет $а^{n-1}\equiv 1\pmod{n}$ для всех целых $а$, взаимно простых $n$

Первые — $(join(first_сarmichael_numbers, ", ")). Если среди случайных не встретилось не взаимно простых с числами Кармайкла, тест Ферма на них ошибается
"""

# ╔═╡ f8a7c173-0897-497e-902e-d0c0f60d4912
@progress for n in first_сarmichael_numbers
    println("На $(n) $(if fpprimem(n, only_consider_coprimes=false) "" else "не " end) ошибся.")
end

# ╔═╡ fabcf136-3369-4e95-bc95-8a2be531aa5a
"""
Тест Соловея-Штрассена

    sstprimem(n; [iterations])

сообщает, что `n` — простое с вероятностью \$1 - 2^{-\\mathit{iterations}}\$
"""
function sstprimem(n; iterations = 10)
    if iseven(n)
        return false
    end

    for a in rand(2:n-1, iterations)
        x = jacobi(a, n)
        if x == 0 || powermod(a, (n-1)÷2, n) != mod(x, n) #  mod(big(a) ^ ((n - 1)÷2) - x, n) != 0
            return false
        end 
    end
    return true
end

# ╔═╡ 6f7524c8-8636-45fd-82ac-43add155d81a
@progress for n in 3:76000
    if sstprimem(n) != Primes.isprime(n)
        println("Fail on $(n)")
    end
end;

# ╔═╡ ebdd9dfb-c133-42c0-ae5a-68c1b44c79ea
@bind strassenCharmichael Radio(["charmichael" => "Только числа Кармайкла", "random" => "Произвольные числа"], default="random")

# ╔═╡ 40936f93-7f36-46a8-b256-79712c9caf3b
strassen_test = if strassenCharmichael == "charmichael"
	first_сarmichael_numbers
else
	rand(3:76000, length(first_сarmichael_numbers))
end

# ╔═╡ e1208101-cae5-4250-b0f4-2b6539450491
@progress for _ in 1:100000
    for n in strassen_test
        if sstprimem(n)
            println("Тест Соловея-Штрассена ошибся на $(n)!!!")
        end
    end
end;

# ╔═╡ 00000000-0000-0000-0000-000000000001
PLUTO_PROJECT_TOML_CONTENTS = """
[deps]
Mods = "7475f97c-0381-53b1-977b-4c60186c8d62"
PlutoUI = "7f904dfe-b85e-4ff6-b463-dae2292396a8"
Primes = "27ebfcd6-29c5-5fa9-bf4b-fb8fc14df3ae"
Printf = "de0858da-6303-5e67-8744-51eddeeeb8d7"
ProgressBars = "49802e3a-d2f1-5c88-81d8-b72133a6f568"
ProgressLogging = "33c8b6b6-d38a-422a-b730-caa89a2f386c"

[compat]
Mods = "~1.3.2"
PlutoUI = "~0.7.48"
Primes = "~0.5.6"
ProgressBars = "~1.4.1"
ProgressLogging = "~0.1.4"
"""

# ╔═╡ 00000000-0000-0000-0000-000000000002
PLUTO_MANIFEST_TOML_CONTENTS = """
# This file is machine-generated - editing it directly is not advised

julia_version = "1.11.0"
manifest_format = "2.0"
project_hash = "ca36636dc9d7f2c37d340b7d48c2d6e14a311a5a"

[[deps.AbstractPlutoDingetjes]]
deps = ["Pkg"]
git-tree-sha1 = "8eaf9f1b4921132a4cff3f36a1d9ba923b14a481"
uuid = "6e696c72-6542-2067-7265-42206c756150"
version = "1.1.4"

[[deps.ArgTools]]
uuid = "0dad84c5-d112-42e6-8d28-ef12dabb789f"
version = "1.1.2"

[[deps.Artifacts]]
uuid = "56f22d72-fd6d-98f1-02f0-08ddc0907c33"
version = "1.11.0"

[[deps.Base64]]
uuid = "2a0f44e3-6c83-55bd-87e4-b1978d98bd5f"
version = "1.11.0"

[[deps.ColorTypes]]
deps = ["FixedPointNumbers", "Random"]
git-tree-sha1 = "eb7f0f8307f71fac7c606984ea5fb2817275d6e4"
uuid = "3da002f7-5984-5a60-b8a6-cbb66c0b333f"
version = "0.11.4"

[[deps.CompilerSupportLibraries_jll]]
deps = ["Artifacts", "Libdl"]
uuid = "e66e0078-7015-5450-92f7-15fbd957f2ae"
version = "1.1.1+0"

[[deps.Dates]]
deps = ["Printf"]
uuid = "ade2ca70-3891-5945-98fb-dc099432e06a"
version = "1.11.0"

[[deps.Downloads]]
deps = ["ArgTools", "FileWatching", "LibCURL", "NetworkOptions"]
uuid = "f43a241f-c20a-4ad4-852c-f6b1247861c6"
version = "1.6.0"

[[deps.FileWatching]]
uuid = "7b1f6079-737a-58dc-b8bc-7a2ca5c1b5ee"
version = "1.11.0"

[[deps.FixedPointNumbers]]
deps = ["Statistics"]
git-tree-sha1 = "335bfdceacc84c5cdf16aadc768aa5ddfc5383cc"
uuid = "53c48c17-4a7d-5ca2-90c5-79b7896eea93"
version = "0.8.4"

[[deps.Hyperscript]]
deps = ["Test"]
git-tree-sha1 = "8d511d5b81240fc8e6802386302675bdf47737b9"
uuid = "47d2ed2b-36de-50cf-bf87-49c2cf4b8b91"
version = "0.0.4"

[[deps.HypertextLiteral]]
deps = ["Tricks"]
git-tree-sha1 = "7134810b1afce04bbc1045ca1985fbe81ce17653"
uuid = "ac1192a8-f4b3-4bfe-ba22-af5b92cd3ab2"
version = "0.9.5"

[[deps.IOCapture]]
deps = ["Logging", "Random"]
git-tree-sha1 = "f7be53659ab06ddc986428d3a9dcc95f6fa6705a"
uuid = "b5f81e59-6552-4d32-b1f0-c071b021bf89"
version = "0.2.2"

[[deps.IntegerMathUtils]]
git-tree-sha1 = "b8ffb903da9f7b8cf695a8bead8e01814aa24b30"
uuid = "18e54dd8-cb9d-406c-a71d-865a43cbb235"
version = "0.1.2"

[[deps.InteractiveUtils]]
deps = ["Markdown"]
uuid = "b77e0a4c-d291-57a0-90e8-8db25a27a240"
version = "1.11.0"

[[deps.JSON]]
deps = ["Dates", "Mmap", "Parsers", "Unicode"]
git-tree-sha1 = "31e996f0a15c7b280ba9f76636b3ff9e2ae58c9a"
uuid = "682c06a0-de6a-54ab-a142-c8b1cf79cde6"
version = "0.21.4"

[[deps.LibCURL]]
deps = ["LibCURL_jll", "MozillaCACerts_jll"]
uuid = "b27032c2-a3e7-50c8-80cd-2d36dbcbfd21"
version = "0.6.4"

[[deps.LibCURL_jll]]
deps = ["Artifacts", "LibSSH2_jll", "Libdl", "MbedTLS_jll", "Zlib_jll", "nghttp2_jll"]
uuid = "deac9b47-8bc7-5906-a0fe-35ac56dc84c0"
version = "8.6.0+0"

[[deps.LibGit2]]
deps = ["Base64", "LibGit2_jll", "NetworkOptions", "Printf", "SHA"]
uuid = "76f85450-5226-5b5a-8eaa-529ad045b433"
version = "1.11.0"

[[deps.LibGit2_jll]]
deps = ["Artifacts", "LibSSH2_jll", "Libdl", "MbedTLS_jll"]
uuid = "e37daf67-58a4-590a-8e99-b0245dd2ffc5"
version = "1.7.2+0"

[[deps.LibSSH2_jll]]
deps = ["Artifacts", "Libdl", "MbedTLS_jll"]
uuid = "29816b5a-b9ab-546f-933c-edad1886dfa8"
version = "1.11.0+1"

[[deps.Libdl]]
uuid = "8f399da3-3557-5675-b5ff-fb832c97cbdb"
version = "1.11.0"

[[deps.LinearAlgebra]]
deps = ["Libdl", "OpenBLAS_jll", "libblastrampoline_jll"]
uuid = "37e2e46d-f89d-539d-b4ee-838fcccc9c8e"
version = "1.11.0"

[[deps.Logging]]
uuid = "56ddb016-857b-54e1-b83d-db4d58db5568"
version = "1.11.0"

[[deps.MIMEs]]
git-tree-sha1 = "65f28ad4b594aebe22157d6fac869786a255b7eb"
uuid = "6c6e2e6c-3030-632d-7369-2d6c69616d65"
version = "0.1.4"

[[deps.Markdown]]
deps = ["Base64"]
uuid = "d6f4376e-aef5-505a-96c1-9c027394607a"
version = "1.11.0"

[[deps.MbedTLS_jll]]
deps = ["Artifacts", "Libdl"]
uuid = "c8ffd9c3-330d-5841-b78e-0817d7145fa1"
version = "2.28.6+0"

[[deps.Mmap]]
uuid = "a63ad114-7e13-5084-954f-fe012c677804"
version = "1.11.0"

[[deps.Mods]]
git-tree-sha1 = "7416683a2cc6e8c9caee75b569c993cfe34e522d"
uuid = "7475f97c-0381-53b1-977b-4c60186c8d62"
version = "1.3.2"

[[deps.MozillaCACerts_jll]]
uuid = "14a3606d-f60d-562e-9121-12d972cd8159"
version = "2023.12.12"

[[deps.NetworkOptions]]
uuid = "ca575930-c2e3-43a9-ace4-1e988b2c1908"
version = "1.2.0"

[[deps.OpenBLAS_jll]]
deps = ["Artifacts", "CompilerSupportLibraries_jll", "Libdl"]
uuid = "4536629a-c528-5b80-bd46-f80d51c5b363"
version = "0.3.27+1"

[[deps.Parsers]]
deps = ["Dates", "PrecompileTools", "UUIDs"]
git-tree-sha1 = "8489905bcdbcfac64d1daa51ca07c0d8f0283821"
uuid = "69de0a69-1ddd-5017-9359-2bf0b02dc9f0"
version = "2.8.1"

[[deps.Pkg]]
deps = ["Artifacts", "Dates", "Downloads", "FileWatching", "LibGit2", "Libdl", "Logging", "Markdown", "Printf", "Random", "SHA", "TOML", "Tar", "UUIDs", "p7zip_jll"]
uuid = "44cfe95a-1eb2-52ea-b672-e2afdf69b78f"
version = "1.11.0"

    [deps.Pkg.extensions]
    REPLExt = "REPL"

    [deps.Pkg.weakdeps]
    REPL = "3fa0cd96-eef1-5676-8a61-b3b8758bbffb"

[[deps.PlutoUI]]
deps = ["AbstractPlutoDingetjes", "Base64", "ColorTypes", "Dates", "FixedPointNumbers", "Hyperscript", "HypertextLiteral", "IOCapture", "InteractiveUtils", "JSON", "Logging", "MIMEs", "Markdown", "Random", "Reexport", "URIs", "UUIDs"]
git-tree-sha1 = "efc140104e6d0ae3e7e30d56c98c4a927154d684"
uuid = "7f904dfe-b85e-4ff6-b463-dae2292396a8"
version = "0.7.48"

[[deps.PrecompileTools]]
deps = ["Preferences"]
git-tree-sha1 = "5aa36f7049a63a1528fe8f7c3f2113413ffd4e1f"
uuid = "aea7be01-6a6a-4083-8856-8a6e6704d82a"
version = "1.2.1"

[[deps.Preferences]]
deps = ["TOML"]
git-tree-sha1 = "9306f6085165d270f7e3db02af26a400d580f5c6"
uuid = "21216c6a-2e73-6563-6e65-726566657250"
version = "1.4.3"

[[deps.Primes]]
deps = ["IntegerMathUtils"]
git-tree-sha1 = "cb420f77dc474d23ee47ca8d14c90810cafe69e7"
uuid = "27ebfcd6-29c5-5fa9-bf4b-fb8fc14df3ae"
version = "0.5.6"

[[deps.Printf]]
deps = ["Unicode"]
uuid = "de0858da-6303-5e67-8744-51eddeeeb8d7"
version = "1.11.0"

[[deps.ProgressBars]]
deps = ["Printf"]
git-tree-sha1 = "806ebc92e1b4b4f72192369a28dfcaf688566b2b"
uuid = "49802e3a-d2f1-5c88-81d8-b72133a6f568"
version = "1.4.1"

[[deps.ProgressLogging]]
deps = ["Logging", "SHA", "UUIDs"]
git-tree-sha1 = "80d919dee55b9c50e8d9e2da5eeafff3fe58b539"
uuid = "33c8b6b6-d38a-422a-b730-caa89a2f386c"
version = "0.1.4"

[[deps.Random]]
deps = ["SHA"]
uuid = "9a3f8284-a2c9-5f02-9a11-845980a1fd5c"
version = "1.11.0"

[[deps.Reexport]]
git-tree-sha1 = "45e428421666073eab6f2da5c9d310d99bb12f9b"
uuid = "189a3867-3050-52da-a836-e630ba90ab69"
version = "1.2.2"

[[deps.SHA]]
uuid = "ea8e919c-243c-51af-8825-aaa63cd721ce"
version = "0.7.0"

[[deps.Serialization]]
uuid = "9e88b42a-f829-5b0c-bbe9-9e923198166b"
version = "1.11.0"

[[deps.Statistics]]
deps = ["LinearAlgebra"]
git-tree-sha1 = "ae3bb1eb3bba077cd276bc5cfc337cc65c3075c0"
uuid = "10745b16-79ce-11e8-11f9-7d13ad32a3b2"
version = "1.11.1"

    [deps.Statistics.extensions]
    SparseArraysExt = ["SparseArrays"]

    [deps.Statistics.weakdeps]
    SparseArrays = "2f01184e-e22b-5df5-ae63-d93ebab69eaf"

[[deps.TOML]]
deps = ["Dates"]
uuid = "fa267f1f-6049-4f14-aa54-33bafae1ed76"
version = "1.0.3"

[[deps.Tar]]
deps = ["ArgTools", "SHA"]
uuid = "a4e569a6-e804-4fa4-b0f3-eef7a1d5b13e"
version = "1.10.0"

[[deps.Test]]
deps = ["InteractiveUtils", "Logging", "Random", "Serialization"]
uuid = "8dfed614-e22c-5e08-85e1-65c5234f0b40"
version = "1.11.0"

[[deps.Tricks]]
git-tree-sha1 = "7822b97e99a1672bfb1b49b668a6d46d58d8cbcb"
uuid = "410a4b4d-49e4-4fbc-ab6d-cb71b17b3775"
version = "0.1.9"

[[deps.URIs]]
git-tree-sha1 = "67db6cc7b3821e19ebe75791a9dd19c9b1188f2b"
uuid = "5c2747f8-b7ea-4ff2-ba2e-563bfd36b1d4"
version = "1.5.1"

[[deps.UUIDs]]
deps = ["Random", "SHA"]
uuid = "cf7118a7-6976-5b1a-9a39-7adc72f591a4"
version = "1.11.0"

[[deps.Unicode]]
uuid = "4ec0a83e-493e-50e2-b9ac-8f72acf5a8f5"
version = "1.11.0"

[[deps.Zlib_jll]]
deps = ["Libdl"]
uuid = "83775a58-1f1d-513f-b197-d71354ab007a"
version = "1.2.13+1"

[[deps.libblastrampoline_jll]]
deps = ["Artifacts", "Libdl"]
uuid = "8e850b90-86db-534c-a0d3-1478176c7d93"
version = "5.11.0+0"

[[deps.nghttp2_jll]]
deps = ["Artifacts", "Libdl"]
uuid = "8e850ede-7688-5339-a07c-302acd2aaf8d"
version = "1.59.0+0"

[[deps.p7zip_jll]]
deps = ["Artifacts", "Libdl"]
uuid = "3f19e933-33d8-53b3-aaab-bd5110c3b7a0"
version = "17.4.0+2"
"""

# ╔═╡ Cell order:
# ╟─a4d49bda-47f9-11ed-2630-93e53521cf7b
# ╟─496ae66b-6082-4ef2-a132-b616aa45b613
# ╠═41c8044f-b08a-4952-9fe6-5bf8b7fe0d56
# ╠═acd839bb-1be8-4834-894f-fa36f36fc366
# ╠═cf8e8dd2-2ac6-4ede-8e85-9686a2a316da
# ╠═096c3609-4e24-4a8d-9f24-da640f86fc8f
# ╠═ffcd757f-5c8c-4abd-9247-5c4d6b3e0fa8
# ╠═3fce9229-ab56-40b2-8d8a-347c4bd5f5ac
# ╠═d21b75ab-922f-4467-934a-abc75a994c15
# ╟─34d14494-83d4-4c6e-afb0-a289123060b5
# ╟─e596a53e-ad98-4778-8800-28de305440dd
# ╟─f8a7c173-0897-497e-902e-d0c0f60d4912
# ╠═fabcf136-3369-4e95-bc95-8a2be531aa5a
# ╠═6f7524c8-8636-45fd-82ac-43add155d81a
# ╠═ebdd9dfb-c133-42c0-ae5a-68c1b44c79ea
# ╠═40936f93-7f36-46a8-b256-79712c9caf3b
# ╠═e1208101-cae5-4250-b0f4-2b6539450491
# ╟─00000000-0000-0000-0000-000000000001
# ╟─00000000-0000-0000-0000-000000000002
