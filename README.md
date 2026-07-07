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

_Last updated: 2026-07-07 02:41 UTC_

**Total inmates (latest scrape):** 26,804 across 72 parishes/jails

### Acadia Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| White | 96 | 57.8% |
| Black | 68 | 41.0% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 111

| Race | Count | % |
|------|-------|---|
| White | 66 | 59.5% |
| Black | 42 | 37.8% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 523

| Race | Count | % |
|------|-------|---|
| Black | 279 | 53.3% |
| White | 209 | 40.0% |
| Unknown | 31 | 5.9% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 153

| Race | Count | % |
|------|-------|---|
| Unknown | 85 | 55.6% |
| White | 68 | 44.4% |

### Avoyelles Parish
**Total:** 360

| Race | Count | % |
|------|-------|---|
| Black | 198 | 55.0% |
| White | 158 | 43.9% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| White | 106 | 70.2% |
| Black | 45 | 29.8% |

### Bienville Parish
**Total:** 42

| Race | Count | % |
|------|-------|---|
| White | 22 | 52.4% |
| Unknown | 20 | 47.6% |

### Bogalusa Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 10 | 58.8% |
| Black | 7 | 41.2% |

### Bossier City Police Department
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 27 | 57.4% |
| White | 20 | 42.6% |

### Bossier Parish
**Total:** 1,141

| Race | Count | % |
|------|-------|---|
| Black | 642 | 56.3% |
| White | 497 | 43.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Unknown | 1 | 0.1% |

### Caddo Parish
**Total:** 1,703

| Race | Count | % |
|------|-------|---|
| Black | 1,282 | 75.3% |
| White | 392 | 23.0% |
| Unknown | 28 | 1.6% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,111

| Race | Count | % |
|------|-------|---|
| Black | 611 | 55.0% |
| White | 456 | 41.0% |
| Unknown | 41 | 3.7% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 621

| Race | Count | % |
|------|-------|---|
| Black | 390 | 62.8% |
| White | 210 | 33.8% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 17 | 94.4% |
| Black | 1 | 5.6% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 91 | 69.5% |
| White | 39 | 29.8% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 667

| Race | Count | % |
|------|-------|---|
| Black | 413 | 61.9% |
| White | 254 | 38.1% |

### Concordia Parish
**Total:** 796

| Race | Count | % |
|------|-------|---|
| White | 448 | 56.3% |
| Black | 347 | 43.6% |
| Unknown | 1 | 0.1% |

### DeSoto Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 69 | 58.5% |
| White | 48 | 40.7% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,347

| Race | Count | % |
|------|-------|---|
| Black | 1,068 | 79.3% |
| White | 210 | 15.6% |
| Unknown | 68 | 5.0% |
| Asian/PacificIslander | 1 | 0.1% |

### East Feliciana Parish
**Total:** 271

| Race | Count | % |
|------|-------|---|
| Black | 174 | 64.2% |
| White | 96 | 35.4% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 170

| Race | Count | % |
|------|-------|---|
| Black | 93 | 54.7% |
| White | 76 | 44.7% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 843

| Race | Count | % |
|------|-------|---|
| Black | 555 | 65.8% |
| White | 278 | 33.0% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| Black | 13 | 76.5% |
| White | 3 | 17.6% |
| Unknown | 1 | 5.9% |

### Iberia Parish
**Total:** 471

| Race | Count | % |
|------|-------|---|
| Black | 272 | 57.7% |
| White | 189 | 40.1% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.8% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 33

| Race | Count | % |
|------|-------|---|
| White | 18 | 54.5% |
| Black | 15 | 45.5% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 90 | 54.5% |
| Black | 72 | 43.6% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,143

| Race | Count | % |
|------|-------|---|
| Black | 733 | 64.1% |
| White | 404 | 35.3% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 77

| Race | Count | % |
|------|-------|---|
| White | 51 | 66.2% |
| Black | 25 | 32.5% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 822

| Race | Count | % |
|------|-------|---|
| Black | 541 | 65.8% |
| White | 265 | 32.2% |
| Unknown | 15 | 1.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 760

| Race | Count | % |
|------|-------|---|
| Black | 394 | 51.8% |
| White | 362 | 47.6% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 371

| Race | Count | % |
|------|-------|---|
| Black | 277 | 74.7% |
| White | 91 | 24.5% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 826

| Race | Count | % |
|------|-------|---|
| White | 585 | 70.8% |
| Black | 228 | 27.6% |
| Unknown | 11 | 1.3% |
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
| Black | 156 | 71.9% |
| White | 61 | 28.1% |

### Natchitoches Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| Black | 141 | 75.4% |
| White | 42 | 22.5% |
| Unknown | 4 | 2.1% |

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
**Total:** 1,318

| Race | Count | % |
|------|-------|---|
| Black | 880 | 66.8% |
| White | 423 | 32.1% |
| Unknown | 15 | 1.1% |

### Plaquemines Parish
**Total:** 686

| Race | Count | % |
|------|-------|---|
| Black | 442 | 64.4% |
| White | 218 | 31.8% |
| Unknown | 15 | 2.2% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 4 | 0.6% |

### Pointe Coupee Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| Black | 73 | 62.9% |
| White | 40 | 34.5% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,029

| Race | Count | % |
|------|-------|---|
| Black | 654 | 63.6% |
| White | 359 | 34.9% |
| Unknown | 14 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 42

| Race | Count | % |
|------|-------|---|
| Black | 21 | 50.0% |
| White | 20 | 47.6% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 682

| Race | Count | % |
|------|-------|---|
| Black | 473 | 69.4% |
| White | 200 | 29.3% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 198

| Race | Count | % |
|------|-------|---|
| White | 111 | 56.1% |
| Black | 84 | 42.4% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 49

| Race | Count | % |
|------|-------|---|
| Black | 39 | 79.6% |
| White | 9 | 18.4% |
| Unknown | 1 | 2.0% |

### St. Bernard Parish
**Total:** 228

| Race | Count | % |
|------|-------|---|
| Black | 134 | 58.8% |
| White | 90 | 39.5% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 194

| Race | Count | % |
|------|-------|---|
| Unknown | 119 | 61.3% |
| White | 75 | 38.7% |

### St. Helena Parish
**Total:** 50

| Race | Count | % |
|------|-------|---|
| Black | 34 | 68.0% |
| White | 15 | 30.0% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 68

| Race | Count | % |
|------|-------|---|
| Black | 54 | 79.4% |
| White | 14 | 20.6% |

### St. John the Baptist Parish
**Total:** 206

| Race | Count | % |
|------|-------|---|
| Unknown | 132 | 64.1% |
| White | 74 | 35.9% |

### St. Landry Parish
**Total:** 125

| Race | Count | % |
|------|-------|---|
| Black | 84 | 67.2% |
| White | 39 | 31.2% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 212

| Race | Count | % |
|------|-------|---|
| Black | 108 | 50.9% |
| White | 94 | 44.3% |
| Unknown | 9 | 4.2% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 293

| Race | Count | % |
|------|-------|---|
| Black | 155 | 52.9% |
| White | 137 | 46.8% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 875

| Race | Count | % |
|------|-------|---|
| White | 463 | 52.9% |
| Black | 372 | 42.5% |
| Unknown | 38 | 4.3% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 13 | 86.7% |
| Black | 2 | 13.3% |

### Tangipahoa Parish
**Total:** 660

| Race | Count | % |
|------|-------|---|
| Black | 432 | 65.5% |
| White | 227 | 34.4% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 566

| Race | Count | % |
|------|-------|---|
| Black | 376 | 66.4% |
| White | 178 | 31.4% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 556

| Race | Count | % |
|------|-------|---|
| Black | 302 | 54.3% |
| White | 241 | 43.3% |
| American Indian/Alaska Native | 11 | 2.0% |
| Unknown | 2 | 0.4% |

### Vermillion Parish
**Total:** 137

| Race | Count | % |
|------|-------|---|
| White | 69 | 50.4% |
| Black | 65 | 47.4% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.7% |

### Vernon Parish
**Total:** 174

| Race | Count | % |
|------|-------|---|
| White | 122 | 70.1% |
| Black | 50 | 28.7% |
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
**Total:** 205

| Race | Count | % |
|------|-------|---|
| White | 103 | 50.2% |
| Black | 102 | 49.8% |

### Webster Parish
**Total:** 447

| Race | Count | % |
|------|-------|---|
| Black | 240 | 53.7% |
| White | 201 | 45.0% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.2% |
| White | 35 | 26.3% |
| Unknown | 4 | 3.0% |
| Asian/PacificIslander | 2 | 1.5% |

### West Carroll Parish
**Total:** 32

| Race | Count | % |
|------|-------|---|
| White | 25 | 78.1% |
| Black | 7 | 21.9% |

### West Felician Parish
**Total:** 194

| Race | Count | % |
|------|-------|---|
| Black | 126 | 64.9% |
| White | 68 | 35.1% |

### Winn Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| Black | 80 | 51.9% |
| White | 74 | 48.1% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
