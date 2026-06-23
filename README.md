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

_Last updated: 2026-06-23 02:51 UTC_

**Total inmates (latest scrape):** 26,754 across 72 parishes/jails

### Acadia Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| White | 98 | 53.3% |
| Black | 84 | 45.7% |
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
**Total:** 529

| Race | Count | % |
|------|-------|---|
| Black | 282 | 53.3% |
| White | 210 | 39.7% |
| Unknown | 33 | 6.2% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| Unknown | 83 | 54.6% |
| White | 69 | 45.4% |

### Avoyelles Parish
**Total:** 351

| Race | Count | % |
|------|-------|---|
| Black | 193 | 55.0% |
| White | 154 | 43.9% |
| Unknown | 3 | 0.9% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| White | 106 | 68.4% |
| Black | 49 | 31.6% |

### Bienville Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| White | 24 | 61.5% |
| Unknown | 15 | 38.5% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 39

| Race | Count | % |
|------|-------|---|
| Black | 28 | 71.8% |
| White | 10 | 25.6% |
| Asian/PacificIslander | 1 | 2.6% |

### Bossier Parish
**Total:** 1,099

| Race | Count | % |
|------|-------|---|
| Black | 600 | 54.6% |
| White | 498 | 45.3% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,677

| Race | Count | % |
|------|-------|---|
| Black | 1,264 | 75.4% |
| White | 385 | 23.0% |
| Unknown | 26 | 1.6% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,102

| Race | Count | % |
|------|-------|---|
| Black | 617 | 56.0% |
| White | 444 | 40.3% |
| Unknown | 38 | 3.4% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 628

| Race | Count | % |
|------|-------|---|
| Black | 398 | 63.4% |
| White | 209 | 33.3% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 23

| Race | Count | % |
|------|-------|---|
| White | 19 | 82.6% |
| Black | 4 | 17.4% |

### Catahoula Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 93 | 69.9% |
| White | 39 | 29.3% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 668

| Race | Count | % |
|------|-------|---|
| Black | 414 | 62.0% |
| White | 254 | 38.0% |

### Concordia Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| White | 468 | 56.7% |
| Black | 355 | 43.0% |
| Unknown | 2 | 0.2% |

### DeSoto Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 71 | 57.3% |
| White | 52 | 41.9% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,346

| Race | Count | % |
|------|-------|---|
| Black | 1,070 | 79.5% |
| White | 210 | 15.6% |
| Unknown | 64 | 4.8% |
| Asian/PacificIslander | 2 | 0.1% |

### East Feliciana Parish
**Total:** 265

| Race | Count | % |
|------|-------|---|
| Black | 169 | 63.8% |
| White | 95 | 35.8% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 150

| Race | Count | % |
|------|-------|---|
| Black | 83 | 55.3% |
| White | 66 | 44.0% |
| Unknown | 1 | 0.7% |

### Franklin Parish
**Total:** 843

| Race | Count | % |
|------|-------|---|
| Black | 549 | 65.1% |
| White | 283 | 33.6% |
| Unknown | 11 | 1.3% |

### Hammond Police Department
**Total:** 9

| Race | Count | % |
|------|-------|---|
| Black | 6 | 66.7% |
| White | 3 | 33.3% |

### Iberia Parish
**Total:** 453

| Race | Count | % |
|------|-------|---|
| Black | 263 | 58.1% |
| White | 180 | 39.7% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 92

| Race | Count | % |
|------|-------|---|
| Black | 61 | 66.3% |
| White | 30 | 32.6% |
| Unknown | 1 | 1.1% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 87 | 53.4% |
| Black | 72 | 44.2% |
| American Indian/Alaska Native | 3 | 1.8% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,131

| Race | Count | % |
|------|-------|---|
| Black | 734 | 64.9% |
| White | 391 | 34.6% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 74

| Race | Count | % |
|------|-------|---|
| White | 50 | 67.6% |
| Black | 23 | 31.1% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 861

| Race | Count | % |
|------|-------|---|
| Black | 559 | 64.9% |
| White | 289 | 33.6% |
| Unknown | 13 | 1.5% |

### Lafourche Parish
**Total:** 745

| Race | Count | % |
|------|-------|---|
| Black | 384 | 51.5% |
| White | 356 | 47.8% |
| American Indian/Alaska Native | 4 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 367

| Race | Count | % |
|------|-------|---|
| Black | 276 | 75.2% |
| White | 88 | 24.0% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 814

| Race | Count | % |
|------|-------|---|
| White | 580 | 71.3% |
| Black | 223 | 27.4% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Black | 114 | 79.7% |
| White | 28 | 19.6% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 215

| Race | Count | % |
|------|-------|---|
| Black | 152 | 70.7% |
| White | 63 | 29.3% |

### Natchitoches Parish
**Total:** 198

| Race | Count | % |
|------|-------|---|
| Black | 147 | 74.2% |
| White | 46 | 23.2% |
| Unknown | 5 | 2.5% |

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
| White | 442 | 32.5% |
| Unknown | 16 | 1.2% |

### Plaquemines Parish
**Total:** 680

| Race | Count | % |
|------|-------|---|
| Black | 450 | 66.2% |
| White | 208 | 30.6% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 6 | 0.9% |
| American Indian/Alaska Native | 4 | 0.6% |

### Pointe Coupee Parish
**Total:** 107

| Race | Count | % |
|------|-------|---|
| Black | 66 | 61.7% |
| White | 38 | 35.5% |
| Unknown | 2 | 1.9% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,040

| Race | Count | % |
|------|-------|---|
| Black | 665 | 63.9% |
| White | 357 | 34.3% |
| Unknown | 16 | 1.5% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 24 | 54.5% |
| White | 19 | 43.2% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 723

| Race | Count | % |
|------|-------|---|
| Black | 497 | 68.7% |
| White | 215 | 29.7% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 191

| Race | Count | % |
|------|-------|---|
| White | 103 | 53.9% |
| Black | 85 | 44.5% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 67

| Race | Count | % |
|------|-------|---|
| Black | 52 | 77.6% |
| White | 15 | 22.4% |

### St. Bernard Parish
**Total:** 225

| Race | Count | % |
|------|-------|---|
| Black | 133 | 59.1% |
| White | 89 | 39.6% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 191

| Race | Count | % |
|------|-------|---|
| Unknown | 111 | 58.1% |
| White | 80 | 41.9% |

### St. Helena Parish
**Total:** 51

| Race | Count | % |
|------|-------|---|
| Black | 35 | 68.6% |
| White | 15 | 29.4% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 67

| Race | Count | % |
|------|-------|---|
| Black | 56 | 83.6% |
| White | 11 | 16.4% |

### St. John the Baptist Parish
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Unknown | 130 | 64.0% |
| White | 73 | 36.0% |

### St. Landry Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| Black | 73 | 62.9% |
| White | 41 | 35.3% |
| Unknown | 2 | 1.7% |

### St. Martin Parish
**Total:** 210

| Race | Count | % |
|------|-------|---|
| Black | 107 | 51.0% |
| White | 93 | 44.3% |
| Unknown | 9 | 4.3% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 280

| Race | Count | % |
|------|-------|---|
| Black | 145 | 51.8% |
| White | 134 | 47.9% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 872

| Race | Count | % |
|------|-------|---|
| White | 456 | 52.3% |
| Black | 375 | 43.0% |
| Unknown | 38 | 4.4% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 16 | 88.9% |
| Black | 2 | 11.1% |

### Tangipahoa Parish
**Total:** 661

| Race | Count | % |
|------|-------|---|
| Black | 412 | 62.3% |
| White | 248 | 37.5% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 561

| Race | Count | % |
|------|-------|---|
| Black | 376 | 67.0% |
| White | 175 | 31.2% |
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
**Total:** 136

| Race | Count | % |
|------|-------|---|
| White | 67 | 49.3% |
| Black | 65 | 47.8% |
| Unknown | 3 | 2.2% |
| Asian/PacificIslander | 1 | 0.7% |

### Vernon Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 111 | 68.1% |
| Black | 49 | 30.1% |
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
| Black | 96 | 50.3% |
| White | 95 | 49.7% |

### Webster Parish
**Total:** 446

| Race | Count | % |
|------|-------|---|
| Black | 238 | 53.4% |
| White | 202 | 45.3% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 89 | 70.1% |
| White | 34 | 26.8% |
| Unknown | 3 | 2.4% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 24 | 80.0% |
| Black | 6 | 20.0% |

### West Felician Parish
**Total:** 189

| Race | Count | % |
|------|-------|---|
| Black | 124 | 65.6% |
| White | 65 | 34.4% |

### Winn Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| Black | 73 | 51.4% |
| White | 69 | 48.6% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
