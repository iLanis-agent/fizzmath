# Fizz Math

Sparkling water maker honesty. The cylinder says sixty liters, and strong fizz was always
going to spend it first.

- Landing: `index.html`
- App: `app.html` (loads `engine.js`)

## What it does

The sixty liters on the box are counted at the gentlest press. Every extra push of the
button spends the cylinder faster, so the strong fizz everyone actually wants pours a
fraction of the label. Three panels of honest arithmetic:

- **The fizz truth** - cylinders times the labeled yield for your fizz level:
  60 gentle, 40 medium, 25 strong.
- **The bottle truth** - liters on hand counted into one-liter or half-liter bottles,
  with the remainder.
- **The cost truth** - exchange price spread over the real liters, against the store's
  liter price: saved, more, or exactly matched, rounded to cents first so the figures
  always agree.

## Norms used (labeled, illustrative)

- Yield per 60 L cylinder: 60 L gentle, 40 L medium, 25 L strong.

Every figure is hypothetical arithmetic on labeled norms, not a statement about any real
machine, cylinder or store. Follow the machine's manual, and never carbonate anything but
plain water.

## Tests

`oracle.py` generates `expected.json` from a Python mirror of the engine (same operation
order, same rounding). `node test.js` checks the JavaScript engine against it:

```
python3 oracle.py
node test.js
```
