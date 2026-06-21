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

_Last updated: 2026-06-21 03:40 UTC_

**Total inmates (latest scrape):** 26,707 across 72 parishes/jails

### Acadia Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| White | 98 | 53.6% |
| Black | 83 | 45.4% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| White | 72 | 64.3% |
| Black | 37 | 33.0% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 525

| Race | Count | % |
|------|-------|---|
| Black | 279 | 53.1% |
| White | 210 | 40.0% |
| Unknown | 32 | 6.1% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 157

| Race | Count | % |
|------|-------|---|
| Unknown | 86 | 54.8% |
| White | 71 | 45.2% |

### Avoyelles Parish
**Total:** 355

| Race | Count | % |
|------|-------|---|
| Black | 197 | 55.5% |
| White | 154 | 43.4% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 157

| Race | Count | % |
|------|-------|---|
| White | 108 | 68.8% |
| Black | 49 | 31.2% |

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
**Total:** 56

| Race | Count | % |
|------|-------|---|
| Black | 39 | 69.6% |
| White | 16 | 28.6% |
| Asian/PacificIslander | 1 | 1.8% |

### Bossier Parish
**Total:** 1,095

| Race | Count | % |
|------|-------|---|
| Black | 595 | 54.3% |
| White | 499 | 45.6% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,684

| Race | Count | % |
|------|-------|---|
| Black | 1,266 | 75.2% |
| White | 390 | 23.2% |
| Unknown | 26 | 1.5% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,096

| Race | Count | % |
|------|-------|---|
| Black | 616 | 56.2% |
| White | 439 | 40.1% |
| Unknown | 38 | 3.5% |
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
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 91 | 70.0% |
| White | 38 | 29.2% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 663

| Race | Count | % |
|------|-------|---|
| Black | 410 | 61.8% |
| White | 253 | 38.2% |

### Concordia Parish
**Total:** 814

| Race | Count | % |
|------|-------|---|
| White | 462 | 56.8% |
| Black | 350 | 43.0% |
| Unknown | 2 | 0.2% |

### DeSoto Parish
**Total:** 126

| Race | Count | % |
|------|-------|---|
| Black | 73 | 57.9% |
| White | 52 | 41.3% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,326

| Race | Count | % |
|------|-------|---|
| Black | 1,047 | 79.0% |
| White | 211 | 15.9% |
| Unknown | 65 | 4.9% |
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
**Total:** 841

| Race | Count | % |
|------|-------|---|
| Black | 546 | 64.9% |
| White | 284 | 33.8% |
| Unknown | 11 | 1.3% |

### Hammond Police Department
**Total:** 9

| Race | Count | % |
|------|-------|---|
| Black | 6 | 66.7% |
| White | 3 | 33.3% |

### Iberia Parish
**Total:** 458

| Race | Count | % |
|------|-------|---|
| Black | 265 | 57.9% |
| White | 182 | 39.7% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 95

| Race | Count | % |
|------|-------|---|
| Black | 63 | 66.3% |
| White | 31 | 32.6% |
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
| White | 86 | 52.8% |
| Black | 73 | 44.8% |
| American Indian/Alaska Native | 3 | 1.8% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,138

| Race | Count | % |
|------|-------|---|
| Black | 744 | 65.4% |
| White | 388 | 34.1% |
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
**Total:** 849

| Race | Count | % |
|------|-------|---|
| Black | 554 | 65.3% |
| White | 282 | 33.2% |
| Unknown | 13 | 1.5% |

### Lafourche Parish
**Total:** 758

| Race | Count | % |
|------|-------|---|
| Black | 391 | 51.6% |
| White | 362 | 47.8% |
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
**Total:** 810

| Race | Count | % |
|------|-------|---|
| White | 578 | 71.4% |
| Black | 221 | 27.3% |
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
**Total:** 1,335

| Race | Count | % |
|------|-------|---|
| Black | 890 | 66.7% |
| White | 429 | 32.1% |
| Unknown | 16 | 1.2% |

### Plaquemines Parish
**Total:** 669

| Race | Count | % |
|------|-------|---|
| Black | 442 | 66.1% |
| White | 205 | 30.6% |
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
**Total:** 1,050

| Race | Count | % |
|------|-------|---|
| Black | 663 | 63.1% |
| White | 369 | 35.1% |
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
**Total:** 725

| Race | Count | % |
|------|-------|---|
| Black | 501 | 69.1% |
| White | 214 | 29.5% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 191

| Race | Count | % |
|------|-------|---|
| White | 104 | 54.5% |
| Black | 84 | 44.0% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 70

| Race | Count | % |
|------|-------|---|
| Black | 56 | 80.0% |
| White | 14 | 20.0% |

### St. Bernard Parish
**Total:** 226

| Race | Count | % |
|------|-------|---|
| Black | 136 | 60.2% |
| White | 87 | 38.5% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| Unknown | 113 | 61.4% |
| White | 71 | 38.6% |

### St. Helena Parish
**Total:** 49

| Race | Count | % |
|------|-------|---|
| Black | 34 | 69.4% |
| White | 14 | 28.6% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 69

| Race | Count | % |
|------|-------|---|
| Black | 57 | 82.6% |
| White | 12 | 17.4% |

### St. John the Baptist Parish
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Unknown | 130 | 64.0% |
| White | 73 | 36.0% |

### St. Landry Parish
**Total:** 115

| Race | Count | % |
|------|-------|---|
| Black | 74 | 64.3% |
| White | 39 | 33.9% |
| Unknown | 2 | 1.7% |

### St. Martin Parish
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 107 | 50.0% |
| White | 97 | 45.3% |
| Unknown | 9 | 4.2% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 278

| Race | Count | % |
|------|-------|---|
| Black | 148 | 53.2% |
| White | 129 | 46.4% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 876

| Race | Count | % |
|------|-------|---|
| White | 458 | 52.3% |
| Black | 374 | 42.7% |
| Unknown | 41 | 4.7% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 15 | 88.2% |
| Black | 2 | 11.8% |

### Tangipahoa Parish
**Total:** 666

| Race | Count | % |
|------|-------|---|
| Black | 414 | 62.2% |
| White | 250 | 37.5% |
| Unknown | 2 | 0.3% |

### Tensas Parish
**Total:** 560

| Race | Count | % |
|------|-------|---|
| Black | 372 | 66.4% |
| White | 178 | 31.8% |
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
**Total:** 183

| Race | Count | % |
|------|-------|---|
| White | 92 | 50.3% |
| Black | 91 | 49.7% |

### Webster Parish
**Total:** 443

| Race | Count | % |
|------|-------|---|
| Black | 237 | 53.5% |
| White | 200 | 45.1% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 82 | 69.5% |
| White | 32 | 27.1% |
| Unknown | 3 | 2.5% |
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
