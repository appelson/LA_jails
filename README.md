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

_Last updated: 2026-05-12 02:40 UTC_

**Total inmates (latest scrape):** 25,867 across 72 parishes/jails

### Acadia Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| White | 94 | 51.4% |
| Black | 85 | 46.4% |
| Asian/PacificIslander | 2 | 1.1% |
| Unknown | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| White | 73 | 61.3% |
| Black | 43 | 36.1% |
| American Indian/Alaska Native | 2 | 1.7% |
| Unknown | 1 | 0.8% |

### Ascension Parish
**Total:** 497

| Race | Count | % |
|------|-------|---|
| Black | 266 | 53.5% |
| White | 198 | 39.8% |
| Unknown | 29 | 5.8% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Unknown | 77 | 53.8% |
| White | 66 | 46.2% |

### Avoyelles Parish
**Total:** 381

| Race | Count | % |
|------|-------|---|
| Black | 199 | 52.2% |
| White | 177 | 46.5% |
| Unknown | 4 | 1.0% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 172

| Race | Count | % |
|------|-------|---|
| White | 122 | 70.9% |
| Black | 50 | 29.1% |

### Bienville Parish
**Total:** 37

| Race | Count | % |
|------|-------|---|
| White | 23 | 62.2% |
| Unknown | 14 | 37.8% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 53

| Race | Count | % |
|------|-------|---|
| Black | 36 | 67.9% |
| White | 17 | 32.1% |

### Bossier Parish
**Total:** 1,126

| Race | Count | % |
|------|-------|---|
| Black | 623 | 55.3% |
| White | 500 | 44.4% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,600

| Race | Count | % |
|------|-------|---|
| Black | 1,188 | 74.2% |
| White | 377 | 23.6% |
| Unknown | 32 | 2.0% |
| Asian/PacificIslander | 3 | 0.2% |

### Calcasieu Parish
**Total:** 1,033

| Race | Count | % |
|------|-------|---|
| Black | 565 | 54.7% |
| White | 426 | 41.2% |
| Unknown | 41 | 4.0% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 605

| Race | Count | % |
|------|-------|---|
| Black | 392 | 64.8% |
| White | 193 | 31.9% |
| American Indian/Alaska Native | 20 | 3.3% |

### Cameron Parish
**Total:** 21

| Race | Count | % |
|------|-------|---|
| White | 19 | 90.5% |
| Black | 2 | 9.5% |

### Catahoula Parish
**Total:** 136

| Race | Count | % |
|------|-------|---|
| Black | 95 | 69.9% |
| White | 40 | 29.4% |
| Unknown | 1 | 0.7% |

### Claiborne Parish
**Total:** 655

| Race | Count | % |
|------|-------|---|
| Black | 398 | 60.8% |
| White | 257 | 39.2% |

### Concordia Parish
**Total:** 806

| Race | Count | % |
|------|-------|---|
| White | 455 | 56.5% |
| Black | 347 | 43.1% |
| Unknown | 4 | 0.5% |

### DeSoto Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| Black | 76 | 63.9% |
| White | 42 | 35.3% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,046

| Race | Count | % |
|------|-------|---|
| Black | 798 | 76.3% |
| White | 196 | 18.7% |
| Unknown | 51 | 4.9% |
| Asian/PacificIslander | 1 | 0.1% |

### East Feliciana Parish
**Total:** 267

| Race | Count | % |
|------|-------|---|
| Black | 164 | 61.4% |
| White | 102 | 38.2% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 95

| Race | Count | % |
|------|-------|---|
| White | 48 | 50.5% |
| Black | 45 | 47.4% |
| Unknown | 2 | 2.1% |

### Franklin Parish
**Total:** 830

| Race | Count | % |
|------|-------|---|
| Black | 539 | 64.9% |
| White | 280 | 33.7% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 10

| Race | Count | % |
|------|-------|---|
| Black | 8 | 80.0% |
| White | 2 | 20.0% |

### Iberia Parish
**Total:** 447

| Race | Count | % |
|------|-------|---|
| Black | 277 | 62.0% |
| White | 162 | 36.2% |
| Asian/PacificIslander | 4 | 0.9% |
| Unknown | 3 | 0.7% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 108

| Race | Count | % |
|------|-------|---|
| Black | 66 | 61.1% |
| White | 40 | 37.0% |
| Unknown | 2 | 1.9% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| White | 72 | 49.7% |
| Black | 67 | 46.2% |
| American Indian/Alaska Native | 3 | 2.1% |
| Unknown | 2 | 1.4% |
| Asian/PacificIslander | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,196

| Race | Count | % |
|------|-------|---|
| Black | 778 | 65.1% |
| White | 405 | 33.9% |
| Unknown | 10 | 0.8% |
| Asian/PacificIslander | 3 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 72

| Race | Count | % |
|------|-------|---|
| White | 50 | 69.4% |
| Black | 21 | 29.2% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 868

| Race | Count | % |
|------|-------|---|
| Black | 556 | 64.1% |
| White | 301 | 34.7% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 745

| Race | Count | % |
|------|-------|---|
| Black | 385 | 51.7% |
| White | 353 | 47.4% |
| American Indian/Alaska Native | 5 | 0.7% |
| Unknown | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 366

| Race | Count | % |
|------|-------|---|
| Black | 274 | 74.9% |
| White | 89 | 24.3% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 779

| Race | Count | % |
|------|-------|---|
| White | 558 | 71.6% |
| Black | 212 | 27.2% |
| Unknown | 7 | 0.9% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 137

| Race | Count | % |
|------|-------|---|
| Black | 107 | 78.1% |
| White | 29 | 21.2% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 204

| Race | Count | % |
|------|-------|---|
| Black | 140 | 68.6% |
| White | 64 | 31.4% |

### Natchitoches Parish
**Total:** 199

| Race | Count | % |
|------|-------|---|
| Black | 147 | 73.9% |
| White | 48 | 24.1% |
| Unknown | 3 | 1.5% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 5

| Race | Count | % |
|------|-------|---|
| White | 4 | 80.0% |
| Black | 1 | 20.0% |

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
**Total:** 1,276

| Race | Count | % |
|------|-------|---|
| Black | 847 | 66.4% |
| White | 413 | 32.4% |
| Unknown | 16 | 1.3% |

### Plaquemines Parish
**Total:** 641

| Race | Count | % |
|------|-------|---|
| Black | 418 | 65.2% |
| White | 202 | 31.5% |
| Unknown | 13 | 2.0% |
| Asian/PacificIslander | 7 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Pointe Coupee Parish
**Total:** 103

| Race | Count | % |
|------|-------|---|
| Black | 68 | 66.0% |
| White | 34 | 33.0% |
| Unknown | 1 | 1.0% |

### Rapides Parish
**Total:** 998

| Race | Count | % |
|------|-------|---|
| Black | 617 | 61.8% |
| White | 362 | 36.3% |
| Unknown | 17 | 1.7% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 40

| Race | Count | % |
|------|-------|---|
| Black | 25 | 62.5% |
| White | 14 | 35.0% |
| Asian/PacificIslander | 1 | 2.5% |

### Richland Parish
**Total:** 718

| Race | Count | % |
|------|-------|---|
| Black | 491 | 68.4% |
| White | 216 | 30.1% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sabine Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| White | 108 | 57.4% |
| Black | 80 | 42.6% |

### Shreveport Police Department
**Total:** 50

| Race | Count | % |
|------|-------|---|
| Black | 40 | 80.0% |
| White | 10 | 20.0% |

### St. Bernard Parish
**Total:** 228

| Race | Count | % |
|------|-------|---|
| Black | 130 | 57.0% |
| White | 95 | 41.7% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 173

| Race | Count | % |
|------|-------|---|
| Unknown | 104 | 60.1% |
| White | 69 | 39.9% |

### St. Helena Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 56 | 71.8% |
| White | 17 | 21.8% |
| Unknown | 4 | 5.1% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 80

| Race | Count | % |
|------|-------|---|
| Black | 63 | 78.8% |
| White | 17 | 21.2% |

### St. John the Baptist Parish
**Total:** 205

| Race | Count | % |
|------|-------|---|
| Unknown | 129 | 62.9% |
| White | 76 | 37.1% |

### St. Landry Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 70 | 62.5% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| White | 94 | 49.0% |
| Black | 90 | 46.9% |
| Unknown | 7 | 3.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 253

| Race | Count | % |
|------|-------|---|
| Black | 130 | 51.4% |
| White | 122 | 48.2% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 802

| Race | Count | % |
|------|-------|---|
| White | 406 | 50.6% |
| Black | 353 | 44.0% |
| Unknown | 39 | 4.9% |
| American Indian/Alaska Native | 2 | 0.2% |
| Asian/PacificIslander | 2 | 0.2% |

### Sulphur Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| White | 14 | 87.5% |
| Black | 2 | 12.5% |

### Tangipahoa Parish
**Total:** 639

| Race | Count | % |
|------|-------|---|
| Black | 388 | 60.7% |
| White | 250 | 39.1% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 557

| Race | Count | % |
|------|-------|---|
| Black | 368 | 66.1% |
| White | 174 | 31.2% |
| Unknown | 15 | 2.7% |

### Terrebonne Parish
**Total:** 482

| Race | Count | % |
|------|-------|---|
| Black | 247 | 51.2% |
| White | 228 | 47.3% |
| American Indian/Alaska Native | 6 | 1.2% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| White | 72 | 55.4% |
| Black | 56 | 43.1% |
| Unknown | 2 | 1.5% |

### Vernon Parish
**Total:** 156

| Race | Count | % |
|------|-------|---|
| White | 105 | 67.3% |
| Black | 48 | 30.8% |
| Unknown | 2 | 1.3% |
| Asian/PacificIslander | 1 | 0.6% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 167

| Race | Count | % |
|------|-------|---|
| Black | 88 | 52.7% |
| White | 79 | 47.3% |

### Webster Parish
**Total:** 439

| Race | Count | % |
|------|-------|---|
| Black | 218 | 49.7% |
| White | 214 | 48.7% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 3 | 0.7% |

### West Baton Rouge Parish
**Total:** 138

| Race | Count | % |
|------|-------|---|
| Black | 90 | 65.2% |
| White | 43 | 31.2% |
| Unknown | 4 | 2.9% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 26 | 86.7% |
| Black | 3 | 10.0% |
| Unknown | 1 | 3.3% |

### West Felician Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| Black | 115 | 63.2% |
| White | 67 | 36.8% |

### Winn Parish
**Total:** 147

| Race | Count | % |
|------|-------|---|
| White | 74 | 50.3% |
| Black | 73 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
