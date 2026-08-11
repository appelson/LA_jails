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

_Last updated: 2026-08-11 01:22 UTC_

**Total inmates (latest scrape):** 27,133 across 72 parishes/jails

### Acadia Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| White | 89 | 54.3% |
| Black | 73 | 44.5% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| White | 72 | 61.5% |
| Black | 41 | 35.0% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 514

| Race | Count | % |
|------|-------|---|
| Black | 272 | 52.9% |
| White | 206 | 40.1% |
| Unknown | 31 | 6.0% |
| Asian/PacificIslander | 5 | 1.0% |

### Assumption Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| Unknown | 94 | 57.7% |
| White | 69 | 42.3% |

### Avoyelles Parish
**Total:** 354

| Race | Count | % |
|------|-------|---|
| Black | 199 | 56.2% |
| White | 152 | 42.9% |
| Unknown | 3 | 0.8% |

### Beauregard Parish
**Total:** 181

| Race | Count | % |
|------|-------|---|
| White | 114 | 63.0% |
| Black | 67 | 37.0% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 9 | 60.0% |
| Black | 6 | 40.0% |

### Bossier City Police Department
**Total:** 58

| Race | Count | % |
|------|-------|---|
| Black | 42 | 72.4% |
| White | 16 | 27.6% |

### Bossier Parish
**Total:** 1,124

| Race | Count | % |
|------|-------|---|
| Black | 632 | 56.2% |
| White | 490 | 43.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,723

| Race | Count | % |
|------|-------|---|
| Black | 1,311 | 76.1% |
| White | 383 | 22.2% |
| Unknown | 29 | 1.7% |

### Calcasieu Parish
**Total:** 1,106

| Race | Count | % |
|------|-------|---|
| Black | 597 | 54.0% |
| White | 465 | 42.0% |
| Unknown | 43 | 3.9% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 603

| Race | Count | % |
|------|-------|---|
| Black | 385 | 63.8% |
| White | 202 | 33.5% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 23

| Race | Count | % |
|------|-------|---|
| White | 21 | 91.3% |
| Black | 2 | 8.7% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 91 | 69.5% |
| White | 38 | 29.0% |
| Unknown | 2 | 1.5% |

### Claiborne Parish
**Total:** 654

| Race | Count | % |
|------|-------|---|
| Black | 405 | 61.9% |
| White | 249 | 38.1% |

### Concordia Parish
**Total:** 828

| Race | Count | % |
|------|-------|---|
| White | 473 | 57.1% |
| Black | 355 | 42.9% |

### DeSoto Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 75 | 57.7% |
| White | 55 | 42.3% |

### East Baton Rouge Parish
**Total:** 1,300

| Race | Count | % |
|------|-------|---|
| Black | 1,007 | 77.5% |
| White | 230 | 17.7% |
| Unknown | 59 | 4.5% |
| Asian/PacificIslander | 3 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 270

| Race | Count | % |
|------|-------|---|
| Black | 174 | 64.4% |
| White | 94 | 34.8% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| Black | 95 | 58.3% |
| White | 67 | 41.1% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 854

| Race | Count | % |
|------|-------|---|
| Black | 567 | 66.4% |
| White | 282 | 33.0% |
| Unknown | 4 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 18

| Race | Count | % |
|------|-------|---|
| Black | 10 | 55.6% |
| White | 8 | 44.4% |

### Iberia Parish
**Total:** 463

| Race | Count | % |
|------|-------|---|
| Black | 277 | 59.8% |
| White | 174 | 37.6% |
| Unknown | 6 | 1.3% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 56

| Race | Count | % |
|------|-------|---|
| Black | 36 | 64.3% |
| White | 20 | 35.7% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| White | 84 | 51.2% |
| Black | 78 | 47.6% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,225

| Race | Count | % |
|------|-------|---|
| Black | 803 | 65.6% |
| White | 416 | 34.0% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 80

| Race | Count | % |
|------|-------|---|
| White | 50 | 62.5% |
| Black | 29 | 36.2% |
| Unknown | 1 | 1.2% |

### Lafayette Parish
**Total:** 836

| Race | Count | % |
|------|-------|---|
| Black | 551 | 65.9% |
| White | 275 | 32.9% |
| Unknown | 10 | 1.2% |

### Lafourche Parish
**Total:** 783

| Race | Count | % |
|------|-------|---|
| Black | 394 | 50.3% |
| White | 385 | 49.2% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 370

| Race | Count | % |
|------|-------|---|
| Black | 276 | 74.6% |
| White | 90 | 24.3% |
| Unknown | 4 | 1.1% |

### Livingston Parish
**Total:** 838

| Race | Count | % |
|------|-------|---|
| White | 595 | 71.0% |
| Black | 234 | 27.9% |
| Unknown | 6 | 0.7% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Black | 116 | 81.1% |
| White | 26 | 18.2% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Black | 146 | 73.0% |
| White | 53 | 26.5% |
| Unknown | 1 | 0.5% |

### Natchitoches Parish
**Total:** 191

| Race | Count | % |
|------|-------|---|
| Black | 148 | 77.5% |
| White | 39 | 20.4% |
| Unknown | 4 | 2.1% |

### Oakdale Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### Opelousas Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| African American | 1 | 100.0% |

### Orleans Parish
**Total:** 1,450

| Race | Count | % |
|------|-------|---|
| Black | 1,250 | 86.2% |
| White | 182 | 12.6% |
| Unknown | 14 | 1.0% |
| Asian/PacificIslander | 4 | 0.3% |

### Ouachita Parish
**Total:** 1,346

| Race | Count | % |
|------|-------|---|
| Black | 904 | 67.2% |
| White | 429 | 31.9% |
| Unknown | 13 | 1.0% |

### Plaquemines Parish
**Total:** 674

| Race | Count | % |
|------|-------|---|
| Black | 434 | 64.4% |
| White | 215 | 31.9% |
| Unknown | 13 | 1.9% |
| Asian/PacificIslander | 10 | 1.5% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 84 | 64.1% |
| White | 44 | 33.6% |
| Unknown | 2 | 1.5% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,058

| Race | Count | % |
|------|-------|---|
| Black | 681 | 64.4% |
| White | 361 | 34.1% |
| Unknown | 14 | 1.3% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 24 | 54.5% |
| White | 19 | 43.2% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 700

| Race | Count | % |
|------|-------|---|
| Black | 485 | 69.3% |
| White | 207 | 29.6% |
| Unknown | 5 | 0.7% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| White | 110 | 58.8% |
| Black | 75 | 40.1% |
| Unknown | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 35

| Race | Count | % |
|------|-------|---|
| Black | 25 | 71.4% |
| White | 8 | 22.9% |
| Unknown | 2 | 5.7% |

### St. Bernard Parish
**Total:** 225

| Race | Count | % |
|------|-------|---|
| Black | 134 | 59.6% |
| White | 87 | 38.7% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 180

| Race | Count | % |
|------|-------|---|
| Unknown | 105 | 58.3% |
| White | 75 | 41.7% |

### St. Helena Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 36 | 76.6% |
| White | 10 | 21.3% |
| Unknown | 1 | 2.1% |

### St. James Parish
**Total:** 79

| Race | Count | % |
|------|-------|---|
| Black | 65 | 82.3% |
| White | 14 | 17.7% |

### St. John the Baptist Parish
**Total:** 225

| Race | Count | % |
|------|-------|---|
| Unknown | 146 | 64.9% |
| White | 79 | 35.1% |

### St. Landry Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 90 | 67.2% |
| White | 42 | 31.3% |
| Unknown | 2 | 1.5% |

### St. Martin Parish
**Total:** 223

| Race | Count | % |
|------|-------|---|
| Black | 113 | 50.7% |
| White | 102 | 45.7% |
| Unknown | 8 | 3.6% |

### St. Mary Parish
**Total:** 285

| Race | Count | % |
|------|-------|---|
| Black | 144 | 50.5% |
| White | 139 | 48.8% |
| Unknown | 1 | 0.4% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 879

| Race | Count | % |
|------|-------|---|
| White | 453 | 51.5% |
| Black | 385 | 43.8% |
| Unknown | 39 | 4.4% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 13 | 86.7% |
| Black | 2 | 13.3% |

### Tangipahoa Parish
**Total:** 710

| Race | Count | % |
|------|-------|---|
| Black | 467 | 65.8% |
| White | 240 | 33.8% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 567

| Race | Count | % |
|------|-------|---|
| Black | 382 | 67.4% |
| White | 171 | 30.2% |
| Unknown | 14 | 2.5% |

### Terrebonne Parish
**Total:** 581

| Race | Count | % |
|------|-------|---|
| Black | 331 | 57.0% |
| White | 236 | 40.6% |
| American Indian/Alaska Native | 13 | 2.2% |
| Asian/PacificIslander | 1 | 0.2% |

### Vermillion Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| White | 57 | 48.7% |
| Black | 57 | 48.7% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.9% |

### Vernon Parish
**Total:** 177

| Race | Count | % |
|------|-------|---|
| White | 124 | 70.1% |
| Black | 51 | 28.8% |
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
**Total:** 184

| Race | Count | % |
|------|-------|---|
| Black | 95 | 51.6% |
| White | 88 | 47.8% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 445

| Race | Count | % |
|------|-------|---|
| Black | 230 | 51.7% |
| White | 208 | 46.7% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 88 | 65.7% |
| White | 42 | 31.3% |
| Unknown | 3 | 2.2% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 28

| Race | Count | % |
|------|-------|---|
| White | 22 | 78.6% |
| Black | 6 | 21.4% |

### West Felician Parish
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Black | 128 | 64.0% |
| White | 72 | 36.0% |

### Winn Parish
**Total:** 148

| Race | Count | % |
|------|-------|---|
| Black | 76 | 51.4% |
| White | 72 | 48.6% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
