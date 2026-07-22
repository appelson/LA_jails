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

_Last updated: 2026-07-22 02:13 UTC_

**Total inmates (latest scrape):** 26,851 across 72 parishes/jails

### Acadia Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 94 | 57.0% |
| Black | 70 | 42.4% |
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
**Total:** 514

| Race | Count | % |
|------|-------|---|
| Black | 274 | 53.3% |
| White | 204 | 39.7% |
| Unknown | 32 | 6.2% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| Unknown | 90 | 56.6% |
| White | 69 | 43.4% |

### Avoyelles Parish
**Total:** 353

| Race | Count | % |
|------|-------|---|
| Black | 199 | 56.4% |
| White | 151 | 42.8% |
| Unknown | 3 | 0.8% |

### Beauregard Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| White | 112 | 68.3% |
| Black | 52 | 31.7% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 21

| Race | Count | % |
|------|-------|---|
| White | 14 | 66.7% |
| Black | 7 | 33.3% |

### Bossier City Police Department
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 30 | 62.5% |
| White | 18 | 37.5% |

### Bossier Parish
**Total:** 1,116

| Race | Count | % |
|------|-------|---|
| Black | 632 | 56.6% |
| White | 482 | 43.2% |
| American Indian/Alaska Native | 1 | 0.1% |
| Unknown | 1 | 0.1% |

### Caddo Parish
**Total:** 1,709

| Race | Count | % |
|------|-------|---|
| Black | 1,287 | 75.3% |
| White | 396 | 23.2% |
| Unknown | 25 | 1.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,100

| Race | Count | % |
|------|-------|---|
| Black | 615 | 55.9% |
| White | 441 | 40.1% |
| Unknown | 42 | 3.8% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 611

| Race | Count | % |
|------|-------|---|
| Black | 384 | 62.8% |
| White | 212 | 34.7% |
| American Indian/Alaska Native | 15 | 2.5% |

### Cameron Parish
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 18 | 100.0% |

### Catahoula Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 92 | 71.3% |
| White | 36 | 27.9% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 646

| Race | Count | % |
|------|-------|---|
| Black | 399 | 61.8% |
| White | 247 | 38.2% |

### Concordia Parish
**Total:** 810

| Race | Count | % |
|------|-------|---|
| White | 462 | 57.0% |
| Black | 348 | 43.0% |

### DeSoto Parish
**Total:** 115

| Race | Count | % |
|------|-------|---|
| Black | 70 | 60.9% |
| White | 44 | 38.3% |
| Asian/PacificIslander | 1 | 0.9% |

### East Baton Rouge Parish
**Total:** 1,342

| Race | Count | % |
|------|-------|---|
| Black | 1,062 | 79.1% |
| White | 218 | 16.2% |
| Unknown | 58 | 4.3% |
| Asian/PacificIslander | 3 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 270

| Race | Count | % |
|------|-------|---|
| Black | 172 | 63.7% |
| White | 96 | 35.6% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| Black | 89 | 57.8% |
| White | 64 | 41.6% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 833

| Race | Count | % |
|------|-------|---|
| Black | 548 | 65.8% |
| White | 279 | 33.5% |
| Unknown | 6 | 0.7% |

### Hammond Police Department
**Total:** 24

| Race | Count | % |
|------|-------|---|
| Black | 14 | 58.3% |
| White | 10 | 41.7% |

### Iberia Parish
**Total:** 464

| Race | Count | % |
|------|-------|---|
| Black | 278 | 59.9% |
| White | 175 | 37.7% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 26 | 59.1% |
| White | 18 | 40.9% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| White | 84 | 52.8% |
| Black | 72 | 45.3% |
| American Indian/Alaska Native | 2 | 1.3% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,212

| Race | Count | % |
|------|-------|---|
| Black | 780 | 64.4% |
| White | 425 | 35.1% |
| Unknown | 6 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 77

| Race | Count | % |
|------|-------|---|
| White | 52 | 67.5% |
| Black | 24 | 31.2% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| Black | 550 | 66.7% |
| White | 260 | 31.5% |
| Unknown | 15 | 1.8% |

### Lafourche Parish
**Total:** 754

| Race | Count | % |
|------|-------|---|
| Black | 397 | 52.7% |
| White | 353 | 46.8% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 363

| Race | Count | % |
|------|-------|---|
| Black | 269 | 74.1% |
| White | 91 | 25.1% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 824

| Race | Count | % |
|------|-------|---|
| White | 580 | 70.4% |
| Black | 232 | 28.2% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| Black | 117 | 80.7% |
| White | 27 | 18.6% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Black | 149 | 72.0% |
| White | 58 | 28.0% |

### Natchitoches Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Black | 138 | 75.4% |
| White | 42 | 23.0% |
| Unknown | 3 | 1.6% |

### Oakdale Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 3 | 100.0% |

### Opelousas Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| African American | 1 | 100.0% |

### Orleans Parish
**Total:** 1,380

| Race | Count | % |
|------|-------|---|
| Black | 1,182 | 85.7% |
| White | 174 | 12.6% |
| Unknown | 21 | 1.5% |
| Asian/PacificIslander | 3 | 0.2% |

### Ouachita Parish
**Total:** 1,361

| Race | Count | % |
|------|-------|---|
| Black | 903 | 66.3% |
| White | 441 | 32.4% |
| Unknown | 17 | 1.2% |

### Plaquemines Parish
**Total:** 667

| Race | Count | % |
|------|-------|---|
| Black | 435 | 65.2% |
| White | 211 | 31.6% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 72 | 61.0% |
| White | 43 | 36.4% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,060

| Race | Count | % |
|------|-------|---|
| Black | 667 | 62.9% |
| White | 376 | 35.5% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 40

| Race | Count | % |
|------|-------|---|
| Black | 20 | 50.0% |
| White | 19 | 47.5% |
| Asian/PacificIslander | 1 | 2.5% |

### Richland Parish
**Total:** 672

| Race | Count | % |
|------|-------|---|
| Black | 467 | 69.5% |
| White | 196 | 29.2% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 194

| Race | Count | % |
|------|-------|---|
| White | 108 | 55.7% |
| Black | 83 | 42.8% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 34

| Race | Count | % |
|------|-------|---|
| Black | 25 | 73.5% |
| White | 9 | 26.5% |

### St. Bernard Parish
**Total:** 231

| Race | Count | % |
|------|-------|---|
| Black | 140 | 60.6% |
| White | 87 | 37.7% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 186

| Race | Count | % |
|------|-------|---|
| Unknown | 107 | 57.5% |
| White | 79 | 42.5% |

### St. Helena Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 32 | 68.1% |
| White | 15 | 31.9% |

### St. James Parish
**Total:** 71

| Race | Count | % |
|------|-------|---|
| Black | 60 | 84.5% |
| White | 11 | 15.5% |

### St. John the Baptist Parish
**Total:** 209

| Race | Count | % |
|------|-------|---|
| Unknown | 140 | 67.0% |
| White | 69 | 33.0% |

### St. Landry Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| Black | 82 | 67.8% |
| White | 37 | 30.6% |
| Unknown | 2 | 1.7% |

### St. Martin Parish
**Total:** 222

| Race | Count | % |
|------|-------|---|
| Black | 110 | 49.5% |
| White | 103 | 46.4% |
| Unknown | 8 | 3.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 281

| Race | Count | % |
|------|-------|---|
| Black | 150 | 53.4% |
| White | 130 | 46.3% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 879

| Race | Count | % |
|------|-------|---|
| White | 455 | 51.8% |
| Black | 379 | 43.1% |
| Unknown | 43 | 4.9% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| White | 10 | 76.9% |
| Black | 3 | 23.1% |

### Tangipahoa Parish
**Total:** 690

| Race | Count | % |
|------|-------|---|
| Black | 452 | 65.5% |
| White | 235 | 34.1% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 573

| Race | Count | % |
|------|-------|---|
| Black | 386 | 67.4% |
| White | 175 | 30.5% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 573

| Race | Count | % |
|------|-------|---|
| Black | 312 | 54.5% |
| White | 249 | 43.5% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| White | 60 | 49.2% |
| Black | 58 | 47.5% |
| Unknown | 3 | 2.5% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 110 | 67.5% |
| Black | 51 | 31.3% |
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
**Total:** 202

| Race | Count | % |
|------|-------|---|
| Black | 106 | 52.5% |
| White | 95 | 47.0% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 472

| Race | Count | % |
|------|-------|---|
| Black | 253 | 53.6% |
| White | 212 | 44.9% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 84 | 64.6% |
| White | 41 | 31.5% |
| Unknown | 3 | 2.3% |
| Asian/PacificIslander | 2 | 1.5% |

### West Carroll Parish
**Total:** 28

| Race | Count | % |
|------|-------|---|
| White | 22 | 78.6% |
| Black | 6 | 21.4% |

### West Felician Parish
**Total:** 194

| Race | Count | % |
|------|-------|---|
| Black | 124 | 63.9% |
| White | 70 | 36.1% |

### Winn Parish
**Total:** 153

| Race | Count | % |
|------|-------|---|
| White | 77 | 50.3% |
| Black | 76 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
