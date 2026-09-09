last updated/modified: 260909-093859

# file name-given rules

`{start-time}"."{end-time}".csv"`
- time format: refer to §date-time representation/general

e.g., `2026-08-09-1230.2026-09-10-1615`

# date-time representation

- general: `{year.digit:4}"-"{month.digit:2}"-"{day.digit:2}"-"{24-hour.digit:2}{minute.digit:2}`
- data: ISO 8601 Date-Time `{year.digit:4}"-"{month.digit:2}"-"{day.digit:2}"T"{24-hour.digit:2}"T"{minute.digit:2}`

# file format & field structure

- csv
    - date-time: refer to §date-time representation/data
    - qty: integer
    - state: single controlled selection

# file index

|#|start|end|file|
|:-:|:-:|:-:|:-:|
|1|2026-07-14-2245|2026-08-13-1430|[csv](/2026-07-14-2245.2026-08-13-1430.csv)
