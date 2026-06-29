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

_Last updated: 2026-06-29 03:01 UTC_

**Total inmates (latest scrape):** 26,718 across 72 parishes/jails

### Acadia Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| White | 102 | 54.5% |
| Black | 83 | 44.4% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 114

| Race | Count | % |
|------|-------|---|
| White | 72 | 63.2% |
| Black | 39 | 34.2% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 523

| Race | Count | % |
|------|-------|---|
| Black | 277 | 53.0% |
| White | 213 | 40.7% |
| Unknown | 29 | 5.5% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 150

| Race | Count | % |
|------|-------|---|
| Unknown | 83 | 55.3% |
| White | 67 | 44.7% |

### Avoyelles Parish
**Total:** 351

| Race | Count | % |
|------|-------|---|
| Black | 192 | 54.7% |
| White | 155 | 44.2% |
| Unknown | 3 | 0.9% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 149

| Race | Count | % |
|------|-------|---|
| White | 104 | 69.8% |
| Black | 45 | 30.2% |

### Bienville Parish
**Total:** 45

| Race | Count | % |
|------|-------|---|
| White | 26 | 57.8% |
| Unknown | 19 | 42.2% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 28 | 63.6% |
| White | 16 | 36.4% |

### Bossier Parish
**Total:** 1,115

| Race | Count | % |
|------|-------|---|
| Black | 620 | 55.6% |
| White | 494 | 44.3% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,709

| Race | Count | % |
|------|-------|---|
| Black | 1,287 | 75.3% |
| White | 392 | 22.9% |
| Unknown | 28 | 1.6% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,095

| Race | Count | % |
|------|-------|---|
| Black | 613 | 56.0% |
| White | 441 | 40.3% |
| Unknown | 38 | 3.5% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 625

| Race | Count | % |
|------|-------|---|
| Black | 393 | 62.9% |
| White | 211 | 33.8% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 20

| Race | Count | % |
|------|-------|---|
| White | 19 | 95.0% |
| Black | 1 | 5.0% |

### Catahoula Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.2% |
| White | 40 | 30.1% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 682

| Race | Count | % |
|------|-------|---|
| Black | 420 | 61.6% |
| White | 262 | 38.4% |

### Concordia Parish
**Total:** 808

| Race | Count | % |
|------|-------|---|
| White | 455 | 56.3% |
| Black | 352 | 43.6% |
| Unknown | 1 | 0.1% |

### DeSoto Parish
**Total:** 123

| Race | Count | % |
|------|-------|---|
| Black | 72 | 58.5% |
| White | 50 | 40.7% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,313

| Race | Count | % |
|------|-------|---|
| Black | 1,040 | 79.2% |
| White | 204 | 15.5% |
| Unknown | 67 | 5.1% |
| Asian/PacificIslander | 2 | 0.2% |

### East Feliciana Parish
**Total:** 275

| Race | Count | % |
|------|-------|---|
| Black | 176 | 64.0% |
| White | 98 | 35.6% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| Black | 93 | 57.1% |
| White | 69 | 42.3% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 846

| Race | Count | % |
|------|-------|---|
| Black | 556 | 65.7% |
| White | 280 | 33.1% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| Black | 10 | 66.7% |
| White | 4 | 26.7% |
| Unknown | 1 | 6.7% |

### Iberia Parish
**Total:** 460

| Race | Count | % |
|------|-------|---|
| Black | 269 | 58.5% |
| White | 180 | 39.1% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 34

| Race | Count | % |
|------|-------|---|
| Black | 18 | 52.9% |
| White | 16 | 47.1% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 87 | 52.7% |
| Black | 74 | 44.8% |
| American Indian/Alaska Native | 3 | 1.8% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,124

| Race | Count | % |
|------|-------|---|
| Black | 723 | 64.3% |
| White | 395 | 35.1% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 72

| Race | Count | % |
|------|-------|---|
| White | 47 | 65.3% |
| Black | 24 | 33.3% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 839

| Race | Count | % |
|------|-------|---|
| Black | 540 | 64.4% |
| White | 284 | 33.8% |
| Unknown | 14 | 1.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 752

| Race | Count | % |
|------|-------|---|
| Black | 384 | 51.1% |
| White | 363 | 48.3% |
| American Indian/Alaska Native | 4 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 369

| Race | Count | % |
|------|-------|---|
| Black | 276 | 74.8% |
| White | 90 | 24.4% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 830

| Race | Count | % |
|------|-------|---|
| White | 591 | 71.2% |
| Black | 228 | 27.5% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 140

| Race | Count | % |
|------|-------|---|
| Black | 111 | 79.3% |
| White | 28 | 20.0% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 212

| Race | Count | % |
|------|-------|---|
| Black | 150 | 70.8% |
| White | 62 | 29.2% |

### Natchitoches Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| Black | 142 | 74.0% |
| White | 47 | 24.5% |
| Unknown | 3 | 1.6% |

### Oakdale Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

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
**Total:** 1,302

| Race | Count | % |
|------|-------|---|
| Black | 871 | 66.9% |
| White | 418 | 32.1% |
| Unknown | 13 | 1.0% |

### Plaquemines Parish
**Total:** 673

| Race | Count | % |
|------|-------|---|
| Black | 436 | 64.8% |
| White | 211 | 31.4% |
| Unknown | 16 | 2.4% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 3 | 0.4% |

### Pointe Coupee Parish
**Total:** 110

| Race | Count | % |
|------|-------|---|
| Black | 67 | 60.9% |
| White | 40 | 36.4% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,043

| Race | Count | % |
|------|-------|---|
| Black | 660 | 63.3% |
| White | 366 | 35.1% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 27 | 57.4% |
| White | 19 | 40.4% |
| Asian/PacificIslander | 1 | 2.1% |

### Richland Parish
**Total:** 717

| Race | Count | % |
|------|-------|---|
| Black | 496 | 69.2% |
| White | 211 | 29.4% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| White | 105 | 55.3% |
| Black | 82 | 43.2% |
| Unknown | 2 | 1.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 69

| Race | Count | % |
|------|-------|---|
| Black | 52 | 75.4% |
| White | 17 | 24.6% |

### St. Bernard Parish
**Total:** 219

| Race | Count | % |
|------|-------|---|
| Black | 128 | 58.4% |
| White | 88 | 40.2% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 191

| Race | Count | % |
|------|-------|---|
| Unknown | 117 | 61.3% |
| White | 74 | 38.7% |

### St. Helena Parish
**Total:** 50

| Race | Count | % |
|------|-------|---|
| Black | 35 | 70.0% |
| White | 14 | 28.0% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 64

| Race | Count | % |
|------|-------|---|
| Black | 54 | 84.4% |
| White | 10 | 15.6% |

### St. John the Baptist Parish
**Total:** 201

| Race | Count | % |
|------|-------|---|
| Unknown | 130 | 64.7% |
| White | 71 | 35.3% |

### St. Landry Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 83 | 64.3% |
| White | 44 | 34.1% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 219

| Race | Count | % |
|------|-------|---|
| Black | 112 | 51.1% |
| White | 97 | 44.3% |
| Unknown | 9 | 4.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 297

| Race | Count | % |
|------|-------|---|
| Black | 154 | 51.9% |
| White | 142 | 47.8% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 877

| Race | Count | % |
|------|-------|---|
| White | 469 | 53.5% |
| Black | 368 | 42.0% |
| Unknown | 37 | 4.2% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| White | 14 | 87.5% |
| Black | 2 | 12.5% |

### Tangipahoa Parish
**Total:** 672

| Race | Count | % |
|------|-------|---|
| Black | 429 | 63.8% |
| White | 242 | 36.0% |
| Unknown | 1 | 0.1% |

### Tensas Parish
**Total:** 571

| Race | Count | % |
|------|-------|---|
| Black | 381 | 66.7% |
| White | 180 | 31.5% |
| Unknown | 10 | 1.8% |

### Terrebonne Parish
**Total:** 506

| Race | Count | % |
|------|-------|---|
| Black | 271 | 53.6% |
| White | 225 | 44.5% |
| American Indian/Alaska Native | 9 | 1.8% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 135

| Race | Count | % |
|------|-------|---|
| White | 70 | 51.9% |
| Black | 62 | 45.9% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.7% |

### Vernon Parish
**Total:** 170

| Race | Count | % |
|------|-------|---|
| White | 118 | 69.4% |
| Black | 49 | 28.8% |
| Unknown | 2 | 1.2% |
| Asian/PacificIslander | 1 | 0.6% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| White | 102 | 52.8% |
| Black | 91 | 47.2% |

### Webster Parish
**Total:** 448

| Race | Count | % |
|------|-------|---|
| Black | 236 | 52.7% |
| White | 206 | 46.0% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 123

| Race | Count | % |
|------|-------|---|
| Black | 83 | 67.5% |
| White | 36 | 29.3% |
| Unknown | 3 | 2.4% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 31

| Race | Count | % |
|------|-------|---|
| White | 25 | 80.6% |
| Black | 6 | 19.4% |

### West Felician Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| Black | 125 | 64.8% |
| White | 68 | 35.2% |

### Winn Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Black | 74 | 51.7% |
| White | 69 | 48.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
