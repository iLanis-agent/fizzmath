import math, json

def plural(n, one, many):
    return one if n == 1 else many

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

def cents(x):
    return math.floor(x * 100 + 0.5)

def money(c):
    return f"${c / 100:.2f}"

LEVEL = ["gentle", "medium", "strong"]
YIELD = [60, 40, 25]
TAIL = [
    "the box's own number honestly",
    "two-thirds of the box honestly",
    "the box was counting gentler presses honestly",
]
BOTTLE = [1, 0.5]
BNAME = ["one-liter", "half-liter"]

def fizz_truth(cyl, level):
    if not (cyl > 0):
        raise ValueError("the cylinders must be above zero")
    liters = YIELD[level] * cyl
    return f"{cyl} 60-liter {plural(cyl, 'cylinder', 'cylinders')} at {LEVEL[level]} fizz {plural(cyl, 'pours', 'pour')} {liters} {plural(liters, 'liter', 'liters')} of seltzer - {TAIL[level]}."

def bottle_truth(liters, size_idx):
    if not (liters > 0):
        raise ValueError("the seltzer liters must be above zero")
    size = BOTTLE[size_idx]
    bottles = math.floor(liters / size + 1e-9)
    left = liters - bottles * size
    if left == 0:
        tail = "nothing left over"
    else:
        word = "liter" if fixed1(left) == "1.0" else "liters"
        tail = f"with {fixed1(left)} {word} left over"
    return f"{liters} {plural(liters, 'liter', 'liters')} of seltzer {plural(liters, 'fills', 'fill')} {bottles} {BNAME[size_idx]} {plural(bottles, 'bottle', 'bottles')}, {tail} honestly."

def cost_truth(exchange, liters, store):
    if not (exchange > 0):
        raise ValueError("the exchange price must be above zero")
    if not (liters > 0):
        raise ValueError("the liters must be above zero")
    if not (store > 0):
        raise ValueError("the store price must be above zero")
    ec = cents(exchange)
    hc = math.floor(ec / liters + 0.5)
    sc = cents(store)
    dm = sc - hc
    if dm > 0:
        verdict = f"leaves {money(dm)} saved a liter honestly"
    elif dm < 0:
        verdict = f"costs {money(-dm)} more a liter honestly"
    else:
        verdict = "matches the store exactly honestly"
    return f"A {money(ec)} exchange over {liters} {plural(liters, 'liter', 'liters')} puts seltzer at {money(hc)} a liter; the store's {money(sc)} {verdict}."

FNS = {"fizzTruth": fizz_truth, "bottleTruth": bottle_truth, "costTruth": cost_truth}

CASES = [
    ("fizzTruth", [1, 2]),
    ("fizzTruth", [2, 0]),
    ("fizzTruth", [1, 1]),
    ("fizzTruth", [3, 2]),
    ("fizzTruth", [2, 1]),
    ("fizzTruth", [1, 0]),
    ("fizzTruth", [0, 1]),
    ("fizzTruth", [-2, 0]),
    ("bottleTruth", [25, 0]),
    ("bottleTruth", [25, 1]),
    ("bottleTruth", [26.5, 0]),
    ("bottleTruth", [10, 1]),
    ("bottleTruth", [1, 1]),
    ("bottleTruth", [0.5, 0]),
    ("bottleTruth", [7.5, 0]),
    ("bottleTruth", [40, 1]),
    ("bottleTruth", [0, 0]),
    ("costTruth", [15, 25, 0.85]),
    ("costTruth", [15, 60, 0.85]),
    ("costTruth", [15, 40, 0.50]),
    ("costTruth", [15, 25, 0.50]),
    ("costTruth", [15, 25, 0.60]),
    ("costTruth", [20, 25, 0.85]),
    ("costTruth", [10, 10, 2.0]),
    ("costTruth", [15, 30, 0.45]),
    ("costTruth", [0, 25, 0.85]),
    ("costTruth", [15, 0, 0.85]),
    ("costTruth", [15, 25, 0]),
]

out = []
for fn, args in CASES:
    rec = {"fn": fn, "args": args}
    try:
        rec["out"] = FNS[fn](*args)
    except ValueError as e:
        rec["err"] = str(e)
    out.append(rec)
    print(fn, args, "->", rec.get("out") or ("ERR: " + rec["err"]))

with open("expected.json", "w") as f:
    json.dump(out, f, indent=1)
    f.write("\n")
print(f"{len(out)} cases written to expected.json")
