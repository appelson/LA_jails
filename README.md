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

_Last updated: 2026-07-01 03:02 UTC_

**Total inmates (latest scrape):** 26,723 across 72 parishes/jails

### Acadia Parish
**Total:** 189

| Race | Count | % |
|------|-------|---|
| White | 104 | 55.0% |
| Black | 83 | 43.9% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| White | 70 | 62.5% |
| Black | 39 | 34.8% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 524

| Race | Count | % |
|------|-------|---|
| Black | 281 | 53.6% |
| White | 210 | 40.1% |
| Unknown | 29 | 5.5% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| Unknown | 85 | 55.9% |
| White | 67 | 44.1% |

### Avoyelles Parish
**Total:** 350

| Race | Count | % |
|------|-------|---|
| Black | 193 | 55.1% |
| White | 153 | 43.7% |
| Unknown | 3 | 0.9% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| White | 105 | 69.5% |
| Black | 46 | 30.5% |

### Bienville Parish
**Total:** 40

| Race | Count | % |
|------|-------|---|
| White | 23 | 57.5% |
| Unknown | 17 | 42.5% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 33 | 68.8% |
| White | 15 | 31.2% |

### Bossier Parish
**Total:** 1,125

| Race | Count | % |
|------|-------|---|
| Black | 620 | 55.1% |
| White | 504 | 44.8% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,704

| Race | Count | % |
|------|-------|---|
| Black | 1,282 | 75.2% |
| White | 392 | 23.0% |
| Unknown | 28 | 1.6% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,091

| Race | Count | % |
|------|-------|---|
| Black | 611 | 56.0% |
| White | 437 | 40.1% |
| Unknown | 40 | 3.7% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 621

| Race | Count | % |
|------|-------|---|
| Black | 391 | 63.0% |
| White | 209 | 33.7% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 17 | 89.5% |
| Unknown | 1 | 5.3% |
| Black | 1 | 5.3% |

### Catahoula Parish
**Total:** 136

| Race | Count | % |
|------|-------|---|
| Black | 95 | 69.9% |
| White | 40 | 29.4% |
| Unknown | 1 | 0.7% |

### Claiborne Parish
**Total:** 680

| Race | Count | % |
|------|-------|---|
| Black | 421 | 61.9% |
| White | 259 | 38.1% |

### Concordia Parish
**Total:** 796

| Race | Count | % |
|------|-------|---|
| White | 452 | 56.8% |
| Black | 343 | 43.1% |
| Unknown | 1 | 0.1% |

### DeSoto Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| Black | 70 | 57.9% |
| White | 50 | 41.3% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,332

| Race | Count | % |
|------|-------|---|
| Black | 1,053 | 79.1% |
| White | 210 | 15.8% |
| Unknown | 67 | 5.0% |
| Asian/PacificIslander | 2 | 0.2% |

### East Feliciana Parish
**Total:** 272

| Race | Count | % |
|------|-------|---|
| Black | 175 | 64.3% |
| White | 96 | 35.3% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| Black | 95 | 56.5% |
| White | 72 | 42.9% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 841

| Race | Count | % |
|------|-------|---|
| Black | 550 | 65.4% |
| White | 281 | 33.4% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| Black | 9 | 69.2% |
| White | 3 | 23.1% |
| Unknown | 1 | 7.7% |

### Iberia Parish
**Total:** 452

| Race | Count | % |
|------|-------|---|
| Black | 263 | 58.2% |
| White | 178 | 39.4% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 35

| Race | Count | % |
|------|-------|---|
| Black | 20 | 57.1% |
| White | 15 | 42.9% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| White | 83 | 52.2% |
| Black | 72 | 45.3% |
| American Indian/Alaska Native | 3 | 1.9% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,143

| Race | Count | % |
|------|-------|---|
| Black | 737 | 64.5% |
| White | 401 | 35.1% |
| Unknown | 5 | 0.4% |

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
**Total:** 837

| Race | Count | % |
|------|-------|---|
| Black | 538 | 64.3% |
| White | 284 | 33.9% |
| Unknown | 14 | 1.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 753

| Race | Count | % |
|------|-------|---|
| Black | 385 | 51.1% |
| White | 364 | 48.3% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 375

| Race | Count | % |
|------|-------|---|
| Black | 279 | 74.4% |
| White | 93 | 24.8% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 826

| Race | Count | % |
|------|-------|---|
| White | 591 | 71.5% |
| Black | 223 | 27.0% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| Black | 114 | 80.3% |
| White | 27 | 19.0% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 217

| Race | Count | % |
|------|-------|---|
| Black | 153 | 70.5% |
| White | 64 | 29.5% |

### Natchitoches Parish
**Total:** 189

| Race | Count | % |
|------|-------|---|
| Black | 141 | 74.6% |
| White | 45 | 23.8% |
| Unknown | 3 | 1.6% |

### Oakdale Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| White | 2 | 100.0% |

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
**Total:** 1,305

| Race | Count | % |
|------|-------|---|
| Black | 872 | 66.8% |
| White | 419 | 32.1% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 673

| Race | Count | % |
|------|-------|---|
| Black | 435 | 64.6% |
| White | 212 | 31.5% |
| Unknown | 16 | 2.4% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 3 | 0.4% |

### Pointe Coupee Parish
**Total:** 111

| Race | Count | % |
|------|-------|---|
| Black | 68 | 61.3% |
| White | 40 | 36.0% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,044

| Race | Count | % |
|------|-------|---|
| Black | 666 | 63.8% |
| White | 361 | 34.6% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 45

| Race | Count | % |
|------|-------|---|
| Black | 23 | 51.1% |
| White | 21 | 46.7% |
| Asian/PacificIslander | 1 | 2.2% |

### Richland Parish
**Total:** 706

| Race | Count | % |
|------|-------|---|
| Black | 487 | 69.0% |
| White | 209 | 29.6% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 194

| Race | Count | % |
|------|-------|---|
| White | 107 | 55.2% |
| Black | 84 | 43.3% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 61

| Race | Count | % |
|------|-------|---|
| Black | 46 | 75.4% |
| White | 15 | 24.6% |

### St. Bernard Parish
**Total:** 224

| Race | Count | % |
|------|-------|---|
| Black | 134 | 59.8% |
| White | 87 | 38.8% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 195

| Race | Count | % |
|------|-------|---|
| Unknown | 116 | 59.5% |
| White | 79 | 40.5% |

### St. Helena Parish
**Total:** 53

| Race | Count | % |
|------|-------|---|
| Black | 37 | 69.8% |
| White | 15 | 28.3% |
| Unknown | 1 | 1.9% |

### St. James Parish
**Total:** 63

| Race | Count | % |
|------|-------|---|
| Black | 53 | 84.1% |
| White | 10 | 15.9% |

### St. John the Baptist Parish
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Unknown | 132 | 66.0% |
| White | 68 | 34.0% |

### St. Landry Parish
**Total:** 123

| Race | Count | % |
|------|-------|---|
| Black | 79 | 64.2% |
| White | 42 | 34.1% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 218

| Race | Count | % |
|------|-------|---|
| Black | 112 | 51.4% |
| White | 96 | 44.0% |
| Unknown | 9 | 4.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 296

| Race | Count | % |
|------|-------|---|
| Black | 154 | 52.0% |
| White | 141 | 47.6% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 873

| Race | Count | % |
|------|-------|---|
| White | 461 | 52.8% |
| Black | 371 | 42.5% |
| Unknown | 38 | 4.4% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 14 | 82.4% |
| Black | 3 | 17.6% |

### Tangipahoa Parish
**Total:** 674

| Race | Count | % |
|------|-------|---|
| Black | 428 | 63.5% |
| White | 245 | 36.4% |
| Unknown | 1 | 0.1% |

### Tensas Parish
**Total:** 568

| Race | Count | % |
|------|-------|---|
| Black | 379 | 66.7% |
| White | 177 | 31.2% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 506

| Race | Count | % |
|------|-------|---|
| Black | 271 | 53.6% |
| White | 225 | 44.5% |
| American Indian/Alaska Native | 9 | 1.8% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| White | 68 | 51.1% |
| Black | 61 | 45.9% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 2 | 1.5% |

### Vernon Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| White | 119 | 70.8% |
| Black | 47 | 28.0% |
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
**Total:** 197

| Race | Count | % |
|------|-------|---|
| White | 101 | 51.3% |
| Black | 96 | 48.7% |

### Webster Parish
**Total:** 445

| Race | Count | % |
|------|-------|---|
| Black | 238 | 53.5% |
| White | 201 | 45.2% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 88 | 67.7% |
| White | 36 | 27.7% |
| Unknown | 4 | 3.1% |
| Asian/PacificIslander | 2 | 1.5% |

### West Carroll Parish
**Total:** 28

| Race | Count | % |
|------|-------|---|
| White | 23 | 82.1% |
| Black | 5 | 17.9% |

### West Felician Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| Black | 127 | 64.8% |
| White | 69 | 35.2% |

### Winn Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| Black | 77 | 52.7% |
| White | 69 | 47.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
