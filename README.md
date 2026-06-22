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

_Last updated: 2026-06-22 03:45 UTC_

**Total inmates (latest scrape):** 26,798 across 72 parishes/jails

### Acadia Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| White | 99 | 53.8% |
| Black | 83 | 45.1% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 113

| Race | Count | % |
|------|-------|---|
| White | 72 | 63.7% |
| Black | 38 | 33.6% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 532

| Race | Count | % |
|------|-------|---|
| Black | 284 | 53.4% |
| White | 211 | 39.7% |
| Unknown | 33 | 6.2% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| Unknown | 86 | 55.5% |
| White | 69 | 44.5% |

### Avoyelles Parish
**Total:** 355

| Race | Count | % |
|------|-------|---|
| Black | 196 | 55.2% |
| White | 155 | 43.7% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 156

| Race | Count | % |
|------|-------|---|
| White | 107 | 68.6% |
| Black | 49 | 31.4% |

### Bienville Parish
**Total:** 38

| Race | Count | % |
|------|-------|---|
| White | 24 | 63.2% |
| Unknown | 14 | 36.8% |

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
| Black | 39 | 75.0% |
| White | 12 | 23.1% |
| Asian/PacificIslander | 1 | 1.9% |

### Bossier Parish
**Total:** 1,098

| Race | Count | % |
|------|-------|---|
| Black | 596 | 54.3% |
| White | 501 | 45.6% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,685

| Race | Count | % |
|------|-------|---|
| Black | 1,269 | 75.3% |
| White | 388 | 23.0% |
| Unknown | 26 | 1.5% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,102

| Race | Count | % |
|------|-------|---|
| Black | 620 | 56.3% |
| White | 441 | 40.0% |
| Unknown | 38 | 3.4% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 626

| Race | Count | % |
|------|-------|---|
| Black | 396 | 63.3% |
| White | 209 | 33.4% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 23

| Race | Count | % |
|------|-------|---|
| White | 20 | 87.0% |
| Black | 3 | 13.0% |

### Catahoula Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 93 | 69.9% |
| White | 38 | 28.6% |
| Unknown | 2 | 1.5% |

### Claiborne Parish
**Total:** 662

| Race | Count | % |
|------|-------|---|
| Black | 409 | 61.8% |
| White | 253 | 38.2% |

### Concordia Parish
**Total:** 817

| Race | Count | % |
|------|-------|---|
| White | 464 | 56.8% |
| Black | 351 | 43.0% |
| Unknown | 2 | 0.2% |

### DeSoto Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 73 | 57.5% |
| White | 53 | 41.7% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,339

| Race | Count | % |
|------|-------|---|
| Black | 1,061 | 79.2% |
| White | 211 | 15.8% |
| Unknown | 64 | 4.8% |
| Asian/PacificIslander | 3 | 0.2% |

### East Feliciana Parish
**Total:** 266

| Race | Count | % |
|------|-------|---|
| Black | 170 | 63.9% |
| White | 95 | 35.7% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 149

| Race | Count | % |
|------|-------|---|
| Black | 84 | 56.4% |
| White | 64 | 43.0% |
| Unknown | 1 | 0.7% |

### Franklin Parish
**Total:** 840

| Race | Count | % |
|------|-------|---|
| Black | 547 | 65.1% |
| White | 282 | 33.6% |
| Unknown | 11 | 1.3% |

### Hammond Police Department
**Total:** 10

| Race | Count | % |
|------|-------|---|
| Black | 7 | 70.0% |
| White | 3 | 30.0% |

### Iberia Parish
**Total:** 459

| Race | Count | % |
|------|-------|---|
| Black | 266 | 58.0% |
| White | 182 | 39.7% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 93

| Race | Count | % |
|------|-------|---|
| Black | 63 | 67.7% |
| White | 29 | 31.2% |
| Unknown | 1 | 1.1% |

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
**Total:** 1,141

| Race | Count | % |
|------|-------|---|
| Black | 748 | 65.6% |
| White | 387 | 33.9% |
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
| White | 48 | 66.7% |
| Black | 23 | 31.9% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 851

| Race | Count | % |
|------|-------|---|
| Black | 556 | 65.3% |
| White | 282 | 33.1% |
| Unknown | 13 | 1.5% |

### Lafourche Parish
**Total:** 752

| Race | Count | % |
|------|-------|---|
| Black | 386 | 51.3% |
| White | 361 | 48.0% |
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
| Black | 280 | 75.9% |
| White | 86 | 23.3% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 816

| Race | Count | % |
|------|-------|---|
| White | 584 | 71.6% |
| Black | 221 | 27.1% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| Black | 115 | 79.9% |
| White | 28 | 19.4% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 217

| Race | Count | % |
|------|-------|---|
| Black | 153 | 70.5% |
| White | 64 | 29.5% |

### Natchitoches Parish
**Total:** 198

| Race | Count | % |
|------|-------|---|
| Black | 147 | 74.2% |
| White | 46 | 23.2% |
| Unknown | 5 | 2.5% |

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
**Total:** 1,351

| Race | Count | % |
|------|-------|---|
| Black | 899 | 66.5% |
| White | 436 | 32.3% |
| Unknown | 16 | 1.2% |

### Plaquemines Parish
**Total:** 668

| Race | Count | % |
|------|-------|---|
| Black | 441 | 66.0% |
| White | 205 | 30.7% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 6 | 0.9% |
| American Indian/Alaska Native | 4 | 0.6% |

### Pointe Coupee Parish
**Total:** 106

| Race | Count | % |
|------|-------|---|
| Black | 66 | 62.3% |
| White | 37 | 34.9% |
| Unknown | 2 | 1.9% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,051

| Race | Count | % |
|------|-------|---|
| Black | 663 | 63.1% |
| White | 370 | 35.2% |
| Unknown | 16 | 1.5% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 24 | 55.8% |
| White | 18 | 41.9% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 731

| Race | Count | % |
|------|-------|---|
| Black | 505 | 69.1% |
| White | 215 | 29.4% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 4 | 0.5% |

### Sabine Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| White | 105 | 54.7% |
| Black | 84 | 43.8% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 60 | 76.9% |
| White | 17 | 21.8% |
| Unknown | 1 | 1.3% |

### St. Bernard Parish
**Total:** 228

| Race | Count | % |
|------|-------|---|
| Black | 136 | 59.6% |
| White | 89 | 39.0% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| Unknown | 111 | 60.3% |
| White | 73 | 39.7% |

### St. Helena Parish
**Total:** 49

| Race | Count | % |
|------|-------|---|
| Black | 34 | 69.4% |
| White | 14 | 28.6% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 67

| Race | Count | % |
|------|-------|---|
| Black | 55 | 82.1% |
| White | 12 | 17.9% |

### St. John the Baptist Parish
**Total:** 202

| Race | Count | % |
|------|-------|---|
| Unknown | 131 | 64.9% |
| White | 71 | 35.1% |

### St. Landry Parish
**Total:** 115

| Race | Count | % |
|------|-------|---|
| Black | 73 | 63.5% |
| White | 40 | 34.8% |
| Unknown | 2 | 1.7% |

### St. Martin Parish
**Total:** 213

| Race | Count | % |
|------|-------|---|
| Black | 107 | 50.2% |
| White | 96 | 45.1% |
| Unknown | 9 | 4.2% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 279

| Race | Count | % |
|------|-------|---|
| Black | 147 | 52.7% |
| White | 131 | 47.0% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 885

| Race | Count | % |
|------|-------|---|
| White | 463 | 52.3% |
| Black | 379 | 42.8% |
| Unknown | 40 | 4.5% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 16 | 88.9% |
| Black | 2 | 11.1% |

### Tangipahoa Parish
**Total:** 668

| Race | Count | % |
|------|-------|---|
| Black | 417 | 62.4% |
| White | 249 | 37.3% |
| Unknown | 2 | 0.3% |

### Tensas Parish
**Total:** 558

| Race | Count | % |
|------|-------|---|
| Black | 372 | 66.7% |
| White | 176 | 31.5% |
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
**Total:** 137

| Race | Count | % |
|------|-------|---|
| White | 68 | 49.6% |
| Black | 65 | 47.4% |
| Unknown | 3 | 2.2% |
| Asian/PacificIslander | 1 | 0.7% |

### Vernon Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| White | 112 | 68.3% |
| Black | 49 | 29.9% |
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
**Total:** 191

| Race | Count | % |
|------|-------|---|
| Black | 97 | 50.8% |
| White | 94 | 49.2% |

### Webster Parish
**Total:** 444

| Race | Count | % |
|------|-------|---|
| Black | 237 | 53.4% |
| White | 201 | 45.3% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 123

| Race | Count | % |
|------|-------|---|
| Black | 86 | 69.9% |
| White | 33 | 26.8% |
| Unknown | 3 | 2.4% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 31

| Race | Count | % |
|------|-------|---|
| White | 24 | 77.4% |
| Black | 7 | 22.6% |

### West Felician Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| Black | 127 | 66.1% |
| White | 65 | 33.9% |

### Winn Parish
**Total:** 141

| Race | Count | % |
|------|-------|---|
| Black | 73 | 51.8% |
| White | 68 | 48.2% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
