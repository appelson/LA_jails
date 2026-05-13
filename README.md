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

_Last updated: 2026-05-13 02:46 UTC_

**Total inmates (latest scrape):** 25,730 across 71 parishes/jails

### Acadia Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| White | 95 | 51.4% |
| Black | 86 | 46.5% |
| Asian/PacificIslander | 2 | 1.1% |
| Unknown | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| White | 74 | 61.7% |
| Black | 43 | 35.8% |
| American Indian/Alaska Native | 2 | 1.7% |
| Unknown | 1 | 0.8% |

### Ascension Parish
**Total:** 498

| Race | Count | % |
|------|-------|---|
| Black | 266 | 53.4% |
| White | 198 | 39.8% |
| Unknown | 30 | 6.0% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| Unknown | 77 | 54.2% |
| White | 65 | 45.8% |

### Avoyelles Parish
**Total:** 384

| Race | Count | % |
|------|-------|---|
| Black | 203 | 52.9% |
| White | 177 | 46.1% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 170

| Race | Count | % |
|------|-------|---|
| White | 120 | 70.6% |
| Black | 50 | 29.4% |

### Bienville Parish
**Total:** 37

| Race | Count | % |
|------|-------|---|
| White | 24 | 64.9% |
| Unknown | 13 | 35.1% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 50

| Race | Count | % |
|------|-------|---|
| Black | 32 | 64.0% |
| White | 18 | 36.0% |

### Bossier Parish
**Total:** 1,119

| Race | Count | % |
|------|-------|---|
| Black | 619 | 55.3% |
| White | 497 | 44.4% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,603

| Race | Count | % |
|------|-------|---|
| Black | 1,187 | 74.0% |
| White | 382 | 23.8% |
| Unknown | 32 | 2.0% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,032

| Race | Count | % |
|------|-------|---|
| Black | 569 | 55.1% |
| White | 421 | 40.8% |
| Unknown | 41 | 4.0% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 602

| Race | Count | % |
|------|-------|---|
| Black | 390 | 64.8% |
| White | 193 | 32.1% |
| American Indian/Alaska Native | 19 | 3.2% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 17 | 89.5% |
| Black | 2 | 10.5% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 93 | 70.5% |
| White | 38 | 28.8% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 652

| Race | Count | % |
|------|-------|---|
| Black | 395 | 60.6% |
| White | 257 | 39.4% |

### Concordia Parish
**Total:** 806

| Race | Count | % |
|------|-------|---|
| White | 453 | 56.2% |
| Black | 349 | 43.3% |
| Unknown | 4 | 0.5% |

### DeSoto Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 72 | 60.0% |
| White | 47 | 39.2% |
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
**Total:** 264

| Race | Count | % |
|------|-------|---|
| Black | 164 | 62.1% |
| White | 99 | 37.5% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 101

| Race | Count | % |
|------|-------|---|
| White | 51 | 50.5% |
| Black | 48 | 47.5% |
| Unknown | 2 | 2.0% |

### Franklin Parish
**Total:** 831

| Race | Count | % |
|------|-------|---|
| Black | 538 | 64.7% |
| White | 282 | 33.9% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 10

| Race | Count | % |
|------|-------|---|
| Black | 8 | 80.0% |
| White | 2 | 20.0% |

### Iberia Parish
**Total:** 452

| Race | Count | % |
|------|-------|---|
| Black | 279 | 61.7% |
| White | 165 | 36.5% |
| Asian/PacificIslander | 4 | 0.9% |
| Unknown | 3 | 0.7% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 109

| Race | Count | % |
|------|-------|---|
| Black | 68 | 62.4% |
| White | 39 | 35.8% |
| Unknown | 2 | 1.8% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| White | 71 | 48.6% |
| Black | 69 | 47.3% |
| American Indian/Alaska Native | 3 | 2.1% |
| Unknown | 2 | 1.4% |
| Asian/PacificIslander | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,176

| Race | Count | % |
|------|-------|---|
| Black | 763 | 64.9% |
| White | 400 | 34.0% |
| Unknown | 10 | 0.9% |
| Asian/PacificIslander | 3 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 73

| Race | Count | % |
|------|-------|---|
| White | 51 | 69.9% |
| Black | 21 | 28.8% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 857

| Race | Count | % |
|------|-------|---|
| Black | 551 | 64.3% |
| White | 295 | 34.4% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 749

| Race | Count | % |
|------|-------|---|
| Black | 387 | 51.7% |
| White | 355 | 47.4% |
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
| White | 554 | 71.1% |
| Black | 216 | 27.7% |
| Unknown | 7 | 0.9% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 105 | 78.4% |
| White | 28 | 20.9% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Black | 142 | 68.6% |
| White | 65 | 31.4% |

### Natchitoches Parish
**Total:** 199

| Race | Count | % |
|------|-------|---|
| Black | 150 | 75.4% |
| White | 45 | 22.6% |
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
**Total:** 1,279

| Race | Count | % |
|------|-------|---|
| Black | 853 | 66.7% |
| White | 409 | 32.0% |
| Unknown | 17 | 1.3% |

### Plaquemines Parish
**Total:** 638

| Race | Count | % |
|------|-------|---|
| Black | 418 | 65.5% |
| White | 199 | 31.2% |
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
**Total:** 1,009

| Race | Count | % |
|------|-------|---|
| Black | 628 | 62.2% |
| White | 362 | 35.9% |
| Unknown | 17 | 1.7% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 26 | 59.1% |
| White | 17 | 38.6% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 717

| Race | Count | % |
|------|-------|---|
| Black | 489 | 68.2% |
| White | 217 | 30.3% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sabine Parish
**Total:** 189

| Race | Count | % |
|------|-------|---|
| White | 110 | 58.2% |
| Black | 79 | 41.8% |

### Shreveport Police Department
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 38 | 82.6% |
| White | 8 | 17.4% |

### St. Bernard Parish
**Total:** 225

| Race | Count | % |
|------|-------|---|
| Black | 125 | 55.6% |
| White | 97 | 43.1% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 175

| Race | Count | % |
|------|-------|---|
| Unknown | 103 | 58.9% |
| White | 72 | 41.1% |

### St. Helena Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 56 | 71.8% |
| White | 17 | 21.8% |
| Unknown | 4 | 5.1% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 77

| Race | Count | % |
|------|-------|---|
| Black | 60 | 77.9% |
| White | 17 | 22.1% |

### St. John the Baptist Parish
**Total:** 206

| Race | Count | % |
|------|-------|---|
| Unknown | 131 | 63.6% |
| White | 75 | 36.4% |

### St. Landry Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 70 | 62.5% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| White | 94 | 48.7% |
| Black | 91 | 47.2% |
| Unknown | 7 | 3.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 253

| Race | Count | % |
|------|-------|---|
| Black | 131 | 51.8% |
| White | 121 | 47.8% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 809

| Race | Count | % |
|------|-------|---|
| White | 414 | 51.2% |
| Black | 353 | 43.6% |
| Unknown | 37 | 4.6% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 2 | 0.2% |

### Sulphur Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 14 | 82.4% |
| Black | 3 | 17.6% |

### Tangipahoa Parish
**Total:** 645

| Race | Count | % |
|------|-------|---|
| Black | 396 | 61.4% |
| White | 248 | 38.4% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 557

| Race | Count | % |
|------|-------|---|
| Black | 369 | 66.2% |
| White | 173 | 31.1% |
| Unknown | 15 | 2.7% |

### Terrebonne Parish
**Total:** 484

| Race | Count | % |
|------|-------|---|
| Black | 248 | 51.2% |
| White | 229 | 47.3% |
| American Indian/Alaska Native | 6 | 1.2% |
| Unknown | 1 | 0.2% |

### Vernon Parish
**Total:** 156

| Race | Count | % |
|------|-------|---|
| White | 104 | 66.7% |
| Black | 49 | 31.4% |
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
**Total:** 166

| Race | Count | % |
|------|-------|---|
| Black | 88 | 53.0% |
| White | 78 | 47.0% |

### Webster Parish
**Total:** 448

| Race | Count | % |
|------|-------|---|
| Black | 223 | 49.8% |
| White | 218 | 48.7% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 3 | 0.7% |

### West Baton Rouge Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 83 | 64.3% |
| White | 41 | 31.8% |
| Unknown | 4 | 3.1% |
| Asian/PacificIslander | 1 | 0.8% |

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
**Total:** 146

| Race | Count | % |
|------|-------|---|
| White | 74 | 50.7% |
| Black | 72 | 49.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
