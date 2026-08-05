# Louisiana Jail Data
An automated scraper that collects inmate roster data from Louisiana parish jails and police departments using GitHub Actions.
![Race Breakdown](race.png)
## Updates
- **`April 24th, 2026`**: Updated to fix the encryption, to instead make it a cypher. This allows us to compare encrypted names / encrypted dates of birth across time. We also condensed the past 30+ days of downloads with the previous rosters. This gives us 7,000,000+ records.
## What it does
Every day at 6:00 PM CST, the GitHub Actions workflow scrapes inmate roster tables from 72 Louisiana parish jails and police departments listed in `links.csv`. This includes 61 out of 64 parishes and 11 municipal jails. Scraped data is saved as a timestamped CSV in the `downloads/` folder and committed to the repo. Sensitive fields (`Name` and `DOB`) are encrypted using RSA public-key encryption before being committed. If you need this information, please contact me at `eappelson@laaclu.org`.
> [!NOTE] 
> This data includes both those held pretrial and post-conviction. Additionally, historical rosters were scraped from [here](https://jailrosters.org/), and the resulting dataframe is saved in `downloads` as `rosters.rds`. Sensitive data is hashed.
## Files
- `script.py`: Scrapes all jails and encrypts sensitive columns before saving
- `encrypt.py`: Encryption utility
- `decrypt.py`: Decrypts CSVs locally using the private key
- `jail_scraper.r`: Scrapes data from the past year saved [here](https://jailrosters.org/).
- `links.csv`: List of 80 jail roster URLs with associated jail names
- `.github/workflows/main.yml`: GitHub Actions workflow that runs the scraper
## Warning
This code should NEVER be replicated or repurposed to scrape and track individuals held in jail. This project exists solely for research and accountability purposes. Do not misuse this code or data to monitor, target, or surveil incarcerated individuals.

---

## Parish Breakdown

_Last updated: 2026-08-05 02:06 UTC_

**Total inmates (latest scrape):** 27,095 across 72 parishes/jails

### Acadia Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| White | 89 | 53.0% |
| Black | 77 | 45.8% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| White | 78 | 63.9% |
| Black | 40 | 32.8% |
| Unknown | 2 | 1.6% |
| American Indian/Alaska Native | 2 | 1.6% |

### Ascension Parish
**Total:** 518

| Race | Count | % |
|------|-------|---|
| Black | 272 | 52.5% |
| White | 209 | 40.3% |
| Unknown | 32 | 6.2% |
| Asian/PacificIslander | 5 | 1.0% |

### Assumption Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| Unknown | 91 | 57.2% |
| White | 68 | 42.8% |

### Avoyelles Parish
**Total:** 350

| Race | Count | % |
|------|-------|---|
| Black | 198 | 56.6% |
| White | 149 | 42.6% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| White | 124 | 66.3% |
| Black | 63 | 33.7% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 8 | 57.1% |
| Black | 6 | 42.9% |

### Bossier City Police Department
**Total:** 66

| Race | Count | % |
|------|-------|---|
| Black | 40 | 60.6% |
| White | 26 | 39.4% |

### Bossier Parish
**Total:** 1,129

| Race | Count | % |
|------|-------|---|
| Black | 637 | 56.4% |
| White | 490 | 43.4% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,737

| Race | Count | % |
|------|-------|---|
| Black | 1,306 | 75.2% |
| White | 402 | 23.1% |
| Unknown | 29 | 1.7% |

### Calcasieu Parish
**Total:** 1,099

| Race | Count | % |
|------|-------|---|
| Black | 599 | 54.5% |
| White | 457 | 41.6% |
| Unknown | 42 | 3.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 605

| Race | Count | % |
|------|-------|---|
| Black | 389 | 64.3% |
| White | 200 | 33.1% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 20

| Race | Count | % |
|------|-------|---|
| White | 20 | 100.0% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 92 | 70.2% |
| White | 38 | 29.0% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 650

| Race | Count | % |
|------|-------|---|
| Black | 402 | 61.8% |
| White | 248 | 38.2% |

### Concordia Parish
**Total:** 826

| Race | Count | % |
|------|-------|---|
| White | 469 | 56.8% |
| Black | 357 | 43.2% |

### DeSoto Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 71 | 57.3% |
| White | 52 | 41.9% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,278

| Race | Count | % |
|------|-------|---|
| Black | 998 | 78.1% |
| White | 221 | 17.3% |
| Unknown | 55 | 4.3% |
| Asian/PacificIslander | 3 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 280

| Race | Count | % |
|------|-------|---|
| Black | 182 | 65.0% |
| White | 96 | 34.3% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| Black | 93 | 58.9% |
| White | 64 | 40.5% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 851

| Race | Count | % |
|------|-------|---|
| Black | 565 | 66.4% |
| White | 282 | 33.1% |
| Unknown | 4 | 0.5% |

### Hammond Police Department
**Total:** 24

| Race | Count | % |
|------|-------|---|
| Black | 10 | 41.7% |
| White | 10 | 41.7% |
| Unknown | 4 | 16.7% |

### Iberia Parish
**Total:** 473

| Race | Count | % |
|------|-------|---|
| Black | 285 | 60.3% |
| White | 178 | 37.6% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.8% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 58

| Race | Count | % |
|------|-------|---|
| Black | 33 | 56.9% |
| White | 24 | 41.4% |
| Unknown | 1 | 1.7% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 86 | 52.8% |
| Black | 75 | 46.0% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,214

| Race | Count | % |
|------|-------|---|
| Black | 788 | 64.9% |
| White | 420 | 34.6% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 74

| Race | Count | % |
|------|-------|---|
| White | 48 | 64.9% |
| Black | 25 | 33.8% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 843

| Race | Count | % |
|------|-------|---|
| Black | 554 | 65.7% |
| White | 278 | 33.0% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 779

| Race | Count | % |
|------|-------|---|
| Black | 401 | 51.5% |
| White | 374 | 48.0% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 370

| Race | Count | % |
|------|-------|---|
| Black | 274 | 74.1% |
| White | 93 | 25.1% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 831

| Race | Count | % |
|------|-------|---|
| White | 587 | 70.6% |
| Black | 235 | 28.3% |
| Unknown | 6 | 0.7% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 150

| Race | Count | % |
|------|-------|---|
| Black | 121 | 80.7% |
| White | 28 | 18.7% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 201

| Race | Count | % |
|------|-------|---|
| Black | 149 | 74.1% |
| White | 52 | 25.9% |

### Natchitoches Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| Black | 140 | 76.1% |
| White | 40 | 21.7% |
| Unknown | 4 | 2.2% |

### Oakdale Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### Opelousas Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| African American | 1 | 100.0% |

### Orleans Parish
**Total:** 1,455

| Race | Count | % |
|------|-------|---|
| Black | 1,253 | 86.1% |
| White | 181 | 12.4% |
| Unknown | 17 | 1.2% |
| Asian/PacificIslander | 4 | 0.3% |

### Ouachita Parish
**Total:** 1,326

| Race | Count | % |
|------|-------|---|
| Black | 887 | 66.9% |
| White | 426 | 32.1% |
| Unknown | 13 | 1.0% |

### Plaquemines Parish
**Total:** 660

| Race | Count | % |
|------|-------|---|
| Black | 431 | 65.3% |
| White | 206 | 31.2% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 9 | 1.4% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| Black | 77 | 63.1% |
| White | 42 | 34.4% |
| Unknown | 2 | 1.6% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,049

| Race | Count | % |
|------|-------|---|
| Black | 665 | 63.4% |
| White | 368 | 35.1% |
| Unknown | 14 | 1.3% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 22 | 53.7% |
| White | 18 | 43.9% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 711

| Race | Count | % |
|------|-------|---|
| Black | 489 | 68.8% |
| White | 213 | 30.0% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| White | 109 | 57.4% |
| Black | 77 | 40.5% |
| Unknown | 3 | 1.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 40

| Race | Count | % |
|------|-------|---|
| Black | 26 | 65.0% |
| White | 14 | 35.0% |

### St. Bernard Parish
**Total:** 231

| Race | Count | % |
|------|-------|---|
| Black | 133 | 57.6% |
| White | 93 | 40.3% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 172

| Race | Count | % |
|------|-------|---|
| Unknown | 97 | 56.4% |
| White | 75 | 43.6% |

### St. Helena Parish
**Total:** 42

| Race | Count | % |
|------|-------|---|
| Black | 29 | 69.0% |
| White | 13 | 31.0% |

### St. James Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 67 | 85.9% |
| White | 11 | 14.1% |

### St. John the Baptist Parish
**Total:** 226

| Race | Count | % |
|------|-------|---|
| Unknown | 148 | 65.5% |
| White | 78 | 34.5% |

### St. Landry Parish
**Total:** 135

| Race | Count | % |
|------|-------|---|
| Black | 87 | 64.4% |
| White | 46 | 34.1% |
| Unknown | 2 | 1.5% |

### St. Martin Parish
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 106 | 49.5% |
| White | 100 | 46.7% |
| Unknown | 8 | 3.7% |

### St. Mary Parish
**Total:** 289

| Race | Count | % |
|------|-------|---|
| Black | 152 | 52.6% |
| White | 136 | 47.1% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 898

| Race | Count | % |
|------|-------|---|
| White | 456 | 50.8% |
| Black | 399 | 44.4% |
| Unknown | 41 | 4.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 12

| Race | Count | % |
|------|-------|---|
| White | 9 | 75.0% |
| Black | 3 | 25.0% |

### Tangipahoa Parish
**Total:** 696

| Race | Count | % |
|------|-------|---|
| Black | 462 | 66.4% |
| White | 231 | 33.2% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 563

| Race | Count | % |
|------|-------|---|
| Black | 379 | 67.3% |
| White | 172 | 30.6% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 574

| Race | Count | % |
|------|-------|---|
| Black | 322 | 56.1% |
| White | 240 | 41.8% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| White | 57 | 48.7% |
| Black | 57 | 48.7% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.9% |

### Vernon Parish
**Total:** 178

| Race | Count | % |
|------|-------|---|
| White | 124 | 69.7% |
| Black | 52 | 29.2% |
| Asian/PacificIslander | 1 | 0.6% |
| Unknown | 1 | 0.6% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 191

| Race | Count | % |
|------|-------|---|
| Black | 98 | 51.3% |
| White | 92 | 48.2% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 451

| Race | Count | % |
|------|-------|---|
| Black | 234 | 51.9% |
| White | 210 | 46.6% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 88 | 65.7% |
| White | 42 | 31.3% |
| Unknown | 3 | 2.2% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 29

| Race | Count | % |
|------|-------|---|
| White | 22 | 75.9% |
| Black | 7 | 24.1% |

### West Felician Parish
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Black | 130 | 64.0% |
| White | 73 | 36.0% |

### Winn Parish
**Total:** 149

| Race | Count | % |
|------|-------|---|
| Black | 75 | 50.3% |
| White | 74 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
