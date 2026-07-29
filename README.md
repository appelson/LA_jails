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

_Last updated: 2026-07-29 02:11 UTC_

**Total inmates (latest scrape):** 26,914 across 72 parishes/jails

### Acadia Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| White | 91 | 57.2% |
| Black | 67 | 42.1% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| White | 75 | 62.0% |
| Black | 42 | 34.7% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 501

| Race | Count | % |
|------|-------|---|
| Black | 265 | 52.9% |
| White | 200 | 39.9% |
| Unknown | 32 | 6.4% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 150

| Race | Count | % |
|------|-------|---|
| Unknown | 83 | 55.3% |
| White | 67 | 44.7% |

### Avoyelles Parish
**Total:** 352

| Race | Count | % |
|------|-------|---|
| Black | 199 | 56.5% |
| White | 150 | 42.6% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| White | 120 | 68.2% |
| Black | 56 | 31.8% |

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
**Total:** 57

| Race | Count | % |
|------|-------|---|
| Black | 40 | 70.2% |
| White | 17 | 29.8% |

### Bossier Parish
**Total:** 1,121

| Race | Count | % |
|------|-------|---|
| Black | 632 | 56.4% |
| White | 487 | 43.4% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,711

| Race | Count | % |
|------|-------|---|
| Black | 1,293 | 75.6% |
| White | 392 | 22.9% |
| Unknown | 26 | 1.5% |

### Calcasieu Parish
**Total:** 1,108

| Race | Count | % |
|------|-------|---|
| Black | 615 | 55.5% |
| White | 451 | 40.7% |
| Unknown | 41 | 3.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 600

| Race | Count | % |
|------|-------|---|
| Black | 385 | 64.2% |
| White | 199 | 33.2% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 19 | 100.0% |

### Catahoula Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 91 | 71.1% |
| White | 36 | 28.1% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 660

| Race | Count | % |
|------|-------|---|
| Black | 410 | 62.1% |
| White | 250 | 37.9% |

### Concordia Parish
**Total:** 809

| Race | Count | % |
|------|-------|---|
| White | 457 | 56.5% |
| Black | 352 | 43.5% |

### DeSoto Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 72 | 61.0% |
| White | 45 | 38.1% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,336

| Race | Count | % |
|------|-------|---|
| Black | 1,046 | 78.3% |
| White | 228 | 17.1% |
| Unknown | 59 | 4.4% |
| Asian/PacificIslander | 2 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 279

| Race | Count | % |
|------|-------|---|
| Black | 183 | 65.6% |
| White | 94 | 33.7% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| Black | 92 | 59.4% |
| White | 62 | 40.0% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 844

| Race | Count | % |
|------|-------|---|
| Black | 560 | 66.4% |
| White | 280 | 33.2% |
| Unknown | 4 | 0.5% |

### Hammond Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 15 | 65.2% |
| White | 7 | 30.4% |
| Unknown | 1 | 4.3% |

### Iberia Parish
**Total:** 470

| Race | Count | % |
|------|-------|---|
| Black | 282 | 60.0% |
| White | 176 | 37.4% |
| Unknown | 6 | 1.3% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 50

| Race | Count | % |
|------|-------|---|
| Black | 32 | 64.0% |
| White | 18 | 36.0% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 84 | 51.9% |
| Black | 75 | 46.3% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,188

| Race | Count | % |
|------|-------|---|
| Black | 760 | 64.0% |
| White | 422 | 35.5% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| White | 2 | 100.0% |

### LaSalle Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| White | 51 | 68.0% |
| Black | 23 | 30.7% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 837

| Race | Count | % |
|------|-------|---|
| Black | 551 | 65.8% |
| White | 272 | 32.5% |
| Unknown | 14 | 1.7% |

### Lafourche Parish
**Total:** 763

| Race | Count | % |
|------|-------|---|
| Black | 389 | 51.0% |
| White | 370 | 48.5% |
| American Indian/Alaska Native | 3 | 0.4% |
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
| Black | 272 | 74.5% |
| White | 90 | 24.7% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 835

| Race | Count | % |
|------|-------|---|
| White | 596 | 71.4% |
| Black | 228 | 27.3% |
| Unknown | 8 | 1.0% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| Black | 124 | 80.0% |
| White | 30 | 19.4% |
| Unknown | 1 | 0.6% |

### Morehouse Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Black | 152 | 73.4% |
| White | 55 | 26.6% |

### Natchitoches Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Black | 139 | 76.0% |
| White | 41 | 22.4% |
| Unknown | 3 | 1.6% |

### Oakdale Police Department
**Total:** 4

| Race | Count | % |
|------|-------|---|
| White | 4 | 100.0% |

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
**Total:** 1,337

| Race | Count | % |
|------|-------|---|
| Black | 892 | 66.7% |
| White | 429 | 32.1% |
| Unknown | 16 | 1.2% |

### Plaquemines Parish
**Total:** 659

| Race | Count | % |
|------|-------|---|
| Black | 428 | 64.9% |
| White | 207 | 31.4% |
| Unknown | 13 | 2.0% |
| Asian/PacificIslander | 9 | 1.4% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| Black | 71 | 60.7% |
| White | 43 | 36.8% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,045

| Race | Count | % |
|------|-------|---|
| Black | 661 | 63.3% |
| White | 367 | 35.1% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 21 | 51.2% |
| White | 19 | 46.3% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 708

| Race | Count | % |
|------|-------|---|
| Black | 490 | 69.2% |
| White | 209 | 29.5% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| White | 106 | 57.3% |
| Black | 76 | 41.1% |
| Unknown | 2 | 1.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 36

| Race | Count | % |
|------|-------|---|
| Black | 27 | 75.0% |
| White | 9 | 25.0% |

### St. Bernard Parish
**Total:** 227

| Race | Count | % |
|------|-------|---|
| Black | 132 | 58.1% |
| White | 90 | 39.6% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Unknown | 106 | 57.9% |
| White | 77 | 42.1% |

### St. Helena Parish
**Total:** 45

| Race | Count | % |
|------|-------|---|
| Black | 31 | 68.9% |
| White | 13 | 28.9% |
| Unknown | 1 | 2.2% |

### St. James Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| Black | 62 | 82.7% |
| White | 13 | 17.3% |

### St. John the Baptist Parish
**Total:** 221

| Race | Count | % |
|------|-------|---|
| Unknown | 146 | 66.1% |
| White | 75 | 33.9% |

### St. Landry Parish
**Total:** 126

| Race | Count | % |
|------|-------|---|
| Black | 84 | 66.7% |
| White | 40 | 31.7% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 210

| Race | Count | % |
|------|-------|---|
| Black | 104 | 49.5% |
| White | 98 | 46.7% |
| Unknown | 8 | 3.8% |

### St. Mary Parish
**Total:** 289

| Race | Count | % |
|------|-------|---|
| Black | 155 | 53.6% |
| White | 133 | 46.0% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 888

| Race | Count | % |
|------|-------|---|
| White | 454 | 51.1% |
| Black | 391 | 44.0% |
| Unknown | 41 | 4.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 11 | 78.6% |
| Black | 3 | 21.4% |

### Tangipahoa Parish
**Total:** 704

| Race | Count | % |
|------|-------|---|
| Black | 461 | 65.5% |
| White | 239 | 33.9% |
| Unknown | 4 | 0.6% |

### Tensas Parish
**Total:** 563

| Race | Count | % |
|------|-------|---|
| Black | 381 | 67.7% |
| White | 170 | 30.2% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 580

| Race | Count | % |
|------|-------|---|
| Black | 318 | 54.8% |
| White | 250 | 43.1% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| White | 59 | 49.2% |
| Black | 58 | 48.3% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 177

| Race | Count | % |
|------|-------|---|
| White | 121 | 68.4% |
| Black | 54 | 30.5% |
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
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Black | 97 | 51.6% |
| White | 90 | 47.9% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 462

| Race | Count | % |
|------|-------|---|
| Black | 246 | 53.2% |
| White | 209 | 45.2% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 87 | 65.4% |
| White | 41 | 30.8% |
| Unknown | 3 | 2.3% |
| Asian/PacificIslander | 2 | 1.5% |

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
| Black | 131 | 64.5% |
| White | 72 | 35.5% |

### Winn Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Black | 76 | 50.3% |
| White | 75 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
