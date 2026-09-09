last updated/modified: 260909-093859

# file name-given rules

`{start-date-time}"."{end-date-time}".csv"`
- date-time format: refer to §date-time representation/general
- e.g., `2026-08-09-1230.2026-09-10-1615`

# date-time representation

- general: `{year.digit:4}"-"{month.digit:2}"-"{day.digit:2}"-"{24-hour.digit:2}{minute.digit:2}`
    - e.g., `2026-08-15-0830`
- data: `{year.digit:4}"-"{month.digit:2}"-"{day.digit:2}" "{24-hour.digit:2}":"{minute.digit:2}`
    - e.g., `2026-08-15 08:30`

# file format & field structure

- csv
    - date-time: refer to §date-time representation/data
    - qty: integer
    - state: single controlled selection

# file index

[file index](/file-index.md)