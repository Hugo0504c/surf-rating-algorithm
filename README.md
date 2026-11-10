# Surf Predictor
An algorithm that rates sea conditions on a 1-10 scale, so you can quickly decide whether it's worth going for a surf.

## How it works
The program asks for four inputs and combines them into a single weighted score:

| Input | Unit | Weight |
|-------|------|--------|
| Wave height | feet (ft) | 40% |
| Wave period | seconds (s) | 30% |
| Wind speed | knots (kn) | 30% |
| Wind direction | `of` offshore / `on` onshore / `ot` other | modifies the wind score |

### Scoring rules
**Wave height**
| Height | Score |
|--------|-------|
| < 2 ft | 1 |
| 2 – 3 ft | 5 |
| 3 – 6 ft | 9 |
| 6 – 10 ft | 7 |
| ≥ 10 ft | 3 |

**Wave period**
| Period | Score |
|--------|-------|
| < 6 s | 2 |
| 6 – 9 s | 5 |
| 9 – 12 s | 8 |
| ≥ 12 s | 10 |

**Wind speed**
| Speed | Score |
|-------|-------|
| < 5 kn | 10 |
| 5 – 10 kn | 6 |
| 10 – 15 kn | 3 |
| ≥ 15 kn | 1 |

**Wind direction** multiplies the wind score: offshore ×1, other ×0.8, onshore ×0.5.

Final score = `height × 0.4 + period × 0.3 + wind × 0.3`, clamped between 1 and 10 and rounded to one decimal.

### Verdict
| Score | Verdict |
|-------|---------|
| ≥ 8 | Epic day, go surf! |
| 6 – 7.9 | Good day, worth it. |
| 4 – 5.9 | Surfable, but nothing special. |
| < 4 | Stay at home. |

## Getting started
Requires Python 3 (no external dependencies).

```bash
git clone https://github.com/Hugo0504c/surf-rate-algorithm.git
cd surf-rate-algorithm
python main.py
```

### Example
```
----------Surf Wave Algorithm----------
Introduce wave height (ft): 4
Introduce wave period (s): 11
Introduce wind speed (kn): 3
of: offshore, on: onshore, ot: other
Introduce wind direction: of

Score: 9.0/10
Epic day, go surf!
```

## Technologies used in the project
- **Python 3** — standard library only (`input`, `float`, control flow)

## Possible improvements
- Fetch real-time forecast data from a marine weather API instead of manual input
- Take swell direction and tide into account
- Let users tune the weights for their favourite spot
