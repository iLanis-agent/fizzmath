// Fizz Math engine - hypothetical arithmetic on labeled norms only.
// Cylinder yields, bottle counts and exchange prices are labeled norms,
// not measurements of your machine, your water or your store.

function plural(n, one, many) { return n === 1 ? one : many; }
function tenths(x) { return Math.floor(x * 10 + 0.5) / 10; }
function fixed1(x) { return tenths(x).toFixed(1); }
function cents(x) { return Math.floor(x * 100 + 0.5); }
function money(c) { return "$" + (c / 100).toFixed(2); }

const LEVEL = ["gentle", "medium", "strong"];
const YIELD = [60, 40, 25]; // labeled norm: liters per 60 L cylinder by fizz level
const TAIL = [
  "the box's own number honestly",
  "two-thirds of the box honestly",
  "the box was counting gentler presses honestly",
];
const BOTTLE = [1, 0.5];
const BNAME = ["one-liter", "half-liter"];

function fizzTruth(cyl, level) {
  if (!(cyl > 0)) throw new Error("the cylinders must be above zero");
  const liters = YIELD[level] * cyl;
  return `${cyl} 60-liter ${plural(cyl, "cylinder", "cylinders")} at ${LEVEL[level]} fizz ${plural(cyl, "pours", "pour")} ${liters} ${plural(liters, "liter", "liters")} of seltzer - ${TAIL[level]}.`;
}

function bottleTruth(liters, sizeIdx) {
  if (!(liters > 0)) throw new Error("the seltzer liters must be above zero");
  const size = BOTTLE[sizeIdx];
  const bottles = Math.floor(liters / size + 1e-9);
  const left = liters - bottles * size;
  const tail = left === 0
    ? "nothing left over"
    : `with ${fixed1(left)} ${fixed1(left) === "1.0" ? "liter" : "liters"} left over`;
  return `${liters} ${plural(liters, "liter", "liters")} of seltzer ${plural(liters, "fills", "fill")} ${bottles} ${BNAME[sizeIdx]} ${plural(bottles, "bottle", "bottles")}, ${tail} honestly.`;
}

function costTruth(exchange, liters, store) {
  if (!(exchange > 0)) throw new Error("the exchange price must be above zero");
  if (!(liters > 0)) throw new Error("the liters must be above zero");
  if (!(store > 0)) throw new Error("the store price must be above zero");
  const ec = cents(exchange);
  const hc = Math.floor(ec / liters + 0.5); // home cost per liter, rounded to cents first
  const sc = cents(store);
  const dm = sc - hc;
  let verdict;
  if (dm > 0) verdict = `leaves ${money(dm)} saved a liter honestly`;
  else if (dm < 0) verdict = `costs ${money(-dm)} more a liter honestly`;
  else verdict = "matches the store exactly honestly";
  return `A ${money(ec)} exchange over ${liters} ${plural(liters, "liter", "liters")} puts seltzer at ${money(hc)} a liter; the store's ${money(sc)} ${verdict}.`;
}

if (typeof module !== "undefined") {
  module.exports = { fizzTruth, bottleTruth, costTruth };
}
