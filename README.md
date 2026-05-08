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

_Last updated: 2026-05-08 02:42 UTC_

**Total inmates (latest scrape):** 25,789 across 72 parishes/jails

### Acadia Parish
**Total:** 175

| Race | Count | % |
|------|-------|---|
| White | 94 | 53.7% |
| Black | 79 | 45.1% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| White | 73 | 60.8% |
| Black | 44 | 36.7% |
| American Indian/Alaska Native | 2 | 1.7% |
| Unknown | 1 | 0.8% |

### Ascension Parish
**Total:** 495

| Race | Count | % |
|------|-------|---|
| Black | 263 | 53.1% |
| White | 197 | 39.8% |
| Unknown | 31 | 6.3% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| Unknown | 76 | 52.4% |
| White | 69 | 47.6% |

### Avoyelles Parish
**Total:** 381

| Race | Count | % |
|------|-------|---|
| Black | 200 | 52.5% |
| White | 176 | 46.2% |
| Unknown | 4 | 1.0% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 169

| Race | Count | % |
|------|-------|---|
| White | 118 | 69.8% |
| Black | 51 | 30.2% |

### Bienville Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| White | 23 | 59.0% |
| Unknown | 16 | 41.0% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 45

| Race | Count | % |
|------|-------|---|
| Black | 29 | 64.4% |
| White | 16 | 35.6% |

### Bossier Parish
**Total:** 1,115

| Race | Count | % |
|------|-------|---|
| Black | 614 | 55.1% |
| White | 498 | 44.7% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,614

| Race | Count | % |
|------|-------|---|
| Black | 1,188 | 73.6% |
| White | 390 | 24.2% |
| Unknown | 33 | 2.0% |
| Asian/PacificIslander | 3 | 0.2% |

### Calcasieu Parish
**Total:** 1,025

| Race | Count | % |
|------|-------|---|
| Black | 561 | 54.7% |
| White | 420 | 41.0% |
| Unknown | 42 | 4.1% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 611

| Race | Count | % |
|------|-------|---|
| Black | 398 | 65.1% |
| White | 193 | 31.6% |
| American Indian/Alaska Native | 20 | 3.3% |

### Cameron Parish
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 16 | 94.1% |
| Black | 1 | 5.9% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.7% |
| White | 39 | 29.5% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 661

| Race | Count | % |
|------|-------|---|
| Black | 403 | 61.0% |
| White | 258 | 39.0% |

### Concordia Parish
**Total:** 815

| Race | Count | % |
|------|-------|---|
| White | 456 | 56.0% |
| Black | 355 | 43.6% |
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
**Total:** 265

| Race | Count | % |
|------|-------|---|
| Black | 163 | 61.5% |
| White | 101 | 38.1% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 90

| Race | Count | % |
|------|-------|---|
| White | 46 | 51.1% |
| Black | 43 | 47.8% |
| Unknown | 1 | 1.1% |

### Franklin Parish
**Total:** 845

| Race | Count | % |
|------|-------|---|
| Black | 547 | 64.7% |
| White | 287 | 34.0% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| Black | 13 | 81.2% |
| White | 3 | 18.8% |

### Iberia Parish
**Total:** 440

| Race | Count | % |
|------|-------|---|
| Black | 273 | 62.0% |
| White | 160 | 36.4% |
| Unknown | 3 | 0.7% |
| Asian/PacificIslander | 3 | 0.7% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 109

| Race | Count | % |
|------|-------|---|
| Black | 67 | 61.5% |
| White | 40 | 36.7% |
| Unknown | 2 | 1.8% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| White | 71 | 49.0% |
| Black | 68 | 46.9% |
| American Indian/Alaska Native | 3 | 2.1% |
| Unknown | 2 | 1.4% |
| Asian/PacificIslander | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,198

| Race | Count | % |
|------|-------|---|
| Black | 784 | 65.4% |
| White | 401 | 33.5% |
| Unknown | 9 | 0.8% |
| Asian/PacificIslander | 4 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Black | 1 | 100.0% |

### LaSalle Parish
**Total:** 71

| Race | Count | % |
|------|-------|---|
| White | 50 | 70.4% |
| Black | 20 | 28.2% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 855

| Race | Count | % |
|------|-------|---|
| Black | 543 | 63.5% |
| White | 300 | 35.1% |
| Unknown | 12 | 1.4% |

### Lafourche Parish
**Total:** 738

| Race | Count | % |
|------|-------|---|
| Black | 379 | 51.4% |
| White | 352 | 47.7% |
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
| Black | 275 | 75.1% |
| White | 89 | 24.3% |
| Unknown | 2 | 0.5% |

### Livingston Parish
**Total:** 788

| Race | Count | % |
|------|-------|---|
| White | 563 | 71.4% |
| Black | 216 | 27.4% |
| Unknown | 7 | 0.9% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 103 | 77.4% |
| White | 29 | 21.8% |
| Unknown | 1 | 0.8% |

### Morehouse Parish
**Total:** 202

| Race | Count | % |
|------|-------|---|
| Black | 138 | 68.3% |
| White | 64 | 31.7% |

### Natchitoches Parish
**Total:** 194

| Race | Count | % |
|------|-------|---|
| Black | 144 | 74.2% |
| White | 46 | 23.7% |
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
**Total:** 1,281

| Race | Count | % |
|------|-------|---|
| Black | 854 | 66.7% |
| White | 413 | 32.2% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 637

| Race | Count | % |
|------|-------|---|
| Black | 412 | 64.7% |
| White | 205 | 32.2% |
| Unknown | 12 | 1.9% |
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
**Total:** 995

| Race | Count | % |
|------|-------|---|
| Black | 622 | 62.5% |
| White | 354 | 35.6% |
| Unknown | 17 | 1.7% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| Black | 24 | 61.5% |
| White | 14 | 35.9% |
| Asian/PacificIslander | 1 | 2.6% |

### Richland Parish
**Total:** 716

| Race | Count | % |
|------|-------|---|
| Black | 489 | 68.3% |
| White | 217 | 30.3% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 181

| Race | Count | % |
|------|-------|---|
| White | 107 | 59.1% |
| Black | 74 | 40.9% |

### Shreveport Police Department
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 34 | 82.9% |
| White | 7 | 17.1% |

### St. Bernard Parish
**Total:** 219

| Race | Count | % |
|------|-------|---|
| Black | 129 | 58.9% |
| White | 87 | 39.7% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 180

| Race | Count | % |
|------|-------|---|
| Unknown | 100 | 55.6% |
| White | 80 | 44.4% |

### St. Helena Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 56 | 71.8% |
| White | 17 | 21.8% |
| Unknown | 4 | 5.1% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 79

| Race | Count | % |
|------|-------|---|
| Black | 63 | 79.7% |
| White | 16 | 20.3% |

### St. John the Baptist Parish
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Unknown | 125 | 62.5% |
| White | 75 | 37.5% |

### St. Landry Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 70 | 62.5% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| Black | 92 | 48.4% |
| White | 90 | 47.4% |
| Unknown | 7 | 3.7% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 247

| Race | Count | % |
|------|-------|---|
| Black | 128 | 51.8% |
| White | 118 | 47.8% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 814

| Race | Count | % |
|------|-------|---|
| White | 411 | 50.5% |
| Black | 362 | 44.5% |
| Unknown | 36 | 4.4% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 2 | 0.2% |

### Sulphur Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| White | 14 | 87.5% |
| Black | 2 | 12.5% |

### Tangipahoa Parish
**Total:** 633

| Race | Count | % |
|------|-------|---|
| Black | 385 | 60.8% |
| White | 247 | 39.0% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 556

| Race | Count | % |
|------|-------|---|
| Black | 365 | 65.6% |
| White | 175 | 31.5% |
| Unknown | 16 | 2.9% |

### Terrebonne Parish
**Total:** 477

| Race | Count | % |
|------|-------|---|
| Black | 244 | 51.2% |
| White | 225 | 47.2% |
| American Indian/Alaska Native | 8 | 1.7% |

### Vermillion Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| White | 68 | 53.1% |
| Black | 58 | 45.3% |
| Unknown | 2 | 1.6% |

### Vernon Parish
**Total:** 153

| Race | Count | % |
|------|-------|---|
| White | 102 | 66.7% |
| Black | 48 | 31.4% |
| Unknown | 2 | 1.3% |
| Asian/PacificIslander | 1 | 0.7% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| Black | 86 | 53.8% |
| White | 74 | 46.2% |

### Webster Parish
**Total:** 438

| Race | Count | % |
|------|-------|---|
| Black | 216 | 49.3% |
| White | 215 | 49.1% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 3 | 0.7% |

### West Baton Rouge Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 86 | 65.2% |
| White | 42 | 31.8% |
| Unknown | 3 | 2.3% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 26 | 86.7% |
| Black | 3 | 10.0% |
| Unknown | 1 | 3.3% |

### West Felician Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| Black | 109 | 61.9% |
| White | 67 | 38.1% |

### Winn Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| White | 77 | 50.7% |
| Black | 75 | 49.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
