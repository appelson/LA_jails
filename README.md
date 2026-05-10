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

_Last updated: 2026-05-10 02:37 UTC_

**Total inmates (latest scrape):** 25,797 across 72 parishes/jails

### Acadia Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| White | 95 | 54.0% |
| Black | 79 | 44.9% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| White | 72 | 60.5% |
| Black | 44 | 37.0% |
| American Indian/Alaska Native | 2 | 1.7% |
| Unknown | 1 | 0.8% |

### Ascension Parish
**Total:** 499

| Race | Count | % |
|------|-------|---|
| Black | 266 | 53.3% |
| White | 199 | 39.9% |
| Unknown | 30 | 6.0% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| Unknown | 74 | 52.1% |
| White | 68 | 47.9% |

### Avoyelles Parish
**Total:** 380

| Race | Count | % |
|------|-------|---|
| Black | 198 | 52.1% |
| White | 177 | 46.6% |
| Unknown | 4 | 1.1% |
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
| White | 23 | 62.2% |
| Unknown | 14 | 37.8% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 52

| Race | Count | % |
|------|-------|---|
| Black | 33 | 63.5% |
| White | 19 | 36.5% |

### Bossier Parish
**Total:** 1,117

| Race | Count | % |
|------|-------|---|
| Black | 619 | 55.4% |
| White | 495 | 44.3% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,598

| Race | Count | % |
|------|-------|---|
| Black | 1,184 | 74.1% |
| White | 380 | 23.8% |
| Unknown | 31 | 1.9% |
| Asian/PacificIslander | 3 | 0.2% |

### Calcasieu Parish
**Total:** 1,030

| Race | Count | % |
|------|-------|---|
| Black | 562 | 54.6% |
| White | 426 | 41.4% |
| Unknown | 41 | 4.0% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 611

| Race | Count | % |
|------|-------|---|
| Black | 398 | 65.1% |
| White | 193 | 31.6% |
| American Indian/Alaska Native | 20 | 3.3% |

### Cameron Parish
**Total:** 25

| Race | Count | % |
|------|-------|---|
| White | 24 | 96.0% |
| Black | 1 | 4.0% |

### Catahoula Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.2% |
| White | 40 | 30.1% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 660

| Race | Count | % |
|------|-------|---|
| Black | 401 | 60.8% |
| White | 259 | 39.2% |

### Concordia Parish
**Total:** 817

| Race | Count | % |
|------|-------|---|
| White | 458 | 56.1% |
| Black | 355 | 43.5% |
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
**Total:** 93

| Race | Count | % |
|------|-------|---|
| White | 47 | 50.5% |
| Black | 44 | 47.3% |
| Unknown | 2 | 2.2% |

### Franklin Parish
**Total:** 833

| Race | Count | % |
|------|-------|---|
| Black | 540 | 64.8% |
| White | 282 | 33.9% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 10

| Race | Count | % |
|------|-------|---|
| Black | 7 | 70.0% |
| White | 3 | 30.0% |

### Iberia Parish
**Total:** 445

| Race | Count | % |
|------|-------|---|
| Black | 275 | 61.8% |
| White | 162 | 36.4% |
| Asian/PacificIslander | 4 | 0.9% |
| Unknown | 3 | 0.7% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 67 | 59.8% |
| White | 43 | 38.4% |
| Unknown | 2 | 1.8% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 148

| Race | Count | % |
|------|-------|---|
| White | 74 | 50.0% |
| Black | 68 | 45.9% |
| American Indian/Alaska Native | 3 | 2.0% |
| Unknown | 2 | 1.4% |
| Asian/PacificIslander | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,175

| Race | Count | % |
|------|-------|---|
| Black | 765 | 65.1% |
| White | 397 | 33.8% |
| Unknown | 9 | 0.8% |
| Asian/PacificIslander | 4 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 71

| Race | Count | % |
|------|-------|---|
| White | 50 | 70.4% |
| Black | 20 | 28.2% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 863

| Race | Count | % |
|------|-------|---|
| Black | 548 | 63.5% |
| White | 304 | 35.2% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 737

| Race | Count | % |
|------|-------|---|
| Black | 380 | 51.6% |
| White | 350 | 47.5% |
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
**Total:** 365

| Race | Count | % |
|------|-------|---|
| Black | 275 | 75.3% |
| White | 89 | 24.4% |
| Unknown | 1 | 0.3% |

### Livingston Parish
**Total:** 780

| Race | Count | % |
|------|-------|---|
| White | 556 | 71.3% |
| Black | 215 | 27.6% |
| Unknown | 7 | 0.9% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 135

| Race | Count | % |
|------|-------|---|
| Black | 105 | 77.8% |
| White | 29 | 21.5% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 205

| Race | Count | % |
|------|-------|---|
| Black | 140 | 68.3% |
| White | 65 | 31.7% |

### Natchitoches Parish
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Black | 149 | 74.5% |
| White | 47 | 23.5% |
| Unknown | 3 | 1.5% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 4

| Race | Count | % |
|------|-------|---|
| White | 3 | 75.0% |
| Black | 1 | 25.0% |

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
| Black | 844 | 66.1% |
| White | 416 | 32.6% |
| Unknown | 16 | 1.3% |

### Plaquemines Parish
**Total:** 632

| Race | Count | % |
|------|-------|---|
| Black | 412 | 65.2% |
| White | 200 | 31.6% |
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
**Total:** 992

| Race | Count | % |
|------|-------|---|
| Black | 611 | 61.6% |
| White | 362 | 36.5% |
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
**Total:** 717

| Race | Count | % |
|------|-------|---|
| Black | 489 | 68.2% |
| White | 218 | 30.4% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| White | 106 | 58.2% |
| Black | 75 | 41.2% |
| Unknown | 1 | 0.5% |

### Shreveport Police Department
**Total:** 51

| Race | Count | % |
|------|-------|---|
| Black | 42 | 82.4% |
| White | 9 | 17.6% |

### St. Bernard Parish
**Total:** 224

| Race | Count | % |
|------|-------|---|
| Black | 128 | 57.1% |
| White | 93 | 41.5% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 170

| Race | Count | % |
|------|-------|---|
| Unknown | 101 | 59.4% |
| White | 69 | 40.6% |

### St. Helena Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 56 | 71.8% |
| White | 17 | 21.8% |
| Unknown | 4 | 5.1% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 81

| Race | Count | % |
|------|-------|---|
| Black | 63 | 77.8% |
| White | 18 | 22.2% |

### St. John the Baptist Parish
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Unknown | 129 | 63.5% |
| White | 74 | 36.5% |

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
| White | 92 | 48.4% |
| Black | 90 | 47.4% |
| Unknown | 7 | 3.7% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 249

| Race | Count | % |
|------|-------|---|
| Black | 127 | 51.0% |
| White | 121 | 48.6% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 824

| Race | Count | % |
|------|-------|---|
| White | 418 | 50.7% |
| Black | 364 | 44.2% |
| Unknown | 37 | 4.5% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 2 | 0.2% |

### Sulphur Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| White | 14 | 87.5% |
| Black | 2 | 12.5% |

### Tangipahoa Parish
**Total:** 641

| Race | Count | % |
|------|-------|---|
| Black | 388 | 60.5% |
| White | 252 | 39.3% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 553

| Race | Count | % |
|------|-------|---|
| Black | 366 | 66.2% |
| White | 172 | 31.1% |
| Unknown | 15 | 2.7% |

### Terrebonne Parish
**Total:** 483

| Race | Count | % |
|------|-------|---|
| Black | 252 | 52.2% |
| White | 224 | 46.4% |
| American Indian/Alaska Native | 6 | 1.2% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| White | 69 | 53.9% |
| Black | 57 | 44.5% |
| Unknown | 2 | 1.6% |

### Vernon Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| White | 101 | 66.9% |
| Black | 47 | 31.1% |
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
**Total:** 164

| Race | Count | % |
|------|-------|---|
| Black | 87 | 53.0% |
| White | 77 | 47.0% |

### Webster Parish
**Total:** 437

| Race | Count | % |
|------|-------|---|
| Black | 217 | 49.7% |
| White | 213 | 48.7% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 3 | 0.7% |

### West Baton Rouge Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 83 | 63.8% |
| White | 42 | 32.3% |
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
**Total:** 176

| Race | Count | % |
|------|-------|---|
| Black | 109 | 61.9% |
| White | 67 | 38.1% |

### Winn Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| White | 76 | 50.3% |
| Black | 75 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
