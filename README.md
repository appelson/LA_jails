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

_Last updated: 2026-08-14 01:32 UTC_

**Total inmates (latest scrape):** 27,154 across 72 parishes/jails

### Acadia Parish
**Total:** 161

| Race | Count | % |
|------|-------|---|
| White | 88 | 54.7% |
| Black | 71 | 44.1% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| White | 73 | 61.3% |
| Black | 42 | 35.3% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 519

| Race | Count | % |
|------|-------|---|
| Black | 271 | 52.2% |
| White | 211 | 40.7% |
| Unknown | 32 | 6.2% |
| Asian/PacificIslander | 5 | 1.0% |

### Assumption Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| Unknown | 98 | 58.3% |
| White | 70 | 41.7% |

### Avoyelles Parish
**Total:** 360

| Race | Count | % |
|------|-------|---|
| Black | 202 | 56.1% |
| White | 155 | 43.1% |
| Unknown | 3 | 0.8% |

### Beauregard Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| White | 115 | 63.2% |
| Black | 67 | 36.8% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 27

| Race | Count | % |
|------|-------|---|
| White | 19 | 70.4% |
| Black | 8 | 29.6% |

### Bossier City Police Department
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 33 | 70.2% |
| White | 14 | 29.8% |

### Bossier Parish
**Total:** 1,137

| Race | Count | % |
|------|-------|---|
| Black | 635 | 55.8% |
| White | 500 | 44.0% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,737

| Race | Count | % |
|------|-------|---|
| Black | 1,316 | 75.8% |
| White | 390 | 22.5% |
| Unknown | 30 | 1.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,106

| Race | Count | % |
|------|-------|---|
| Black | 596 | 53.9% |
| White | 466 | 42.1% |
| Unknown | 43 | 3.9% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 610

| Race | Count | % |
|------|-------|---|
| Black | 393 | 64.4% |
| White | 200 | 32.8% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 2 | 0.3% |

### Cameron Parish
**Total:** 22

| Race | Count | % |
|------|-------|---|
| White | 21 | 95.5% |
| Black | 1 | 4.5% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 90 | 68.7% |
| White | 39 | 29.8% |
| Unknown | 2 | 1.5% |

### Claiborne Parish
**Total:** 662

| Race | Count | % |
|------|-------|---|
| Black | 411 | 62.1% |
| White | 251 | 37.9% |

### Concordia Parish
**Total:** 826

| Race | Count | % |
|------|-------|---|
| White | 471 | 57.0% |
| Black | 355 | 43.0% |

### DeSoto Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 74 | 57.4% |
| White | 55 | 42.6% |

### East Baton Rouge Parish
**Total:** 1,296

| Race | Count | % |
|------|-------|---|
| Black | 1,011 | 78.0% |
| White | 225 | 17.4% |
| Unknown | 56 | 4.3% |
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
**Total:** 168

| Race | Count | % |
|------|-------|---|
| Black | 98 | 58.3% |
| White | 69 | 41.1% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 853

| Race | Count | % |
|------|-------|---|
| Black | 567 | 66.5% |
| White | 280 | 32.8% |
| Unknown | 4 | 0.5% |
| Asian/PacificIslander | 2 | 0.2% |

### Hammond Police Department
**Total:** 18

| Race | Count | % |
|------|-------|---|
| Black | 11 | 61.1% |
| White | 7 | 38.9% |

### Iberia Parish
**Total:** 464

| Race | Count | % |
|------|-------|---|
| Black | 278 | 59.9% |
| White | 174 | 37.5% |
| Unknown | 6 | 1.3% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 91

| Race | Count | % |
|------|-------|---|
| Black | 66 | 72.5% |
| White | 24 | 26.4% |
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
| White | 85 | 51.5% |
| Black | 78 | 47.3% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,236

| Race | Count | % |
|------|-------|---|
| Black | 806 | 65.2% |
| White | 424 | 34.3% |
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
| White | 49 | 61.3% |
| Black | 30 | 37.5% |
| Unknown | 1 | 1.2% |

### Lafayette Parish
**Total:** 840

| Race | Count | % |
|------|-------|---|
| Black | 549 | 65.4% |
| White | 280 | 33.3% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 776

| Race | Count | % |
|------|-------|---|
| Black | 389 | 50.1% |
| White | 383 | 49.4% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 372

| Race | Count | % |
|------|-------|---|
| Black | 280 | 75.3% |
| White | 88 | 23.7% |
| Unknown | 4 | 1.1% |

### Livingston Parish
**Total:** 829

| Race | Count | % |
|------|-------|---|
| White | 588 | 70.9% |
| Black | 233 | 28.1% |
| Unknown | 5 | 0.6% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 148

| Race | Count | % |
|------|-------|---|
| Black | 120 | 81.1% |
| White | 27 | 18.2% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Black | 145 | 72.5% |
| White | 55 | 27.5% |

### Natchitoches Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| Black | 140 | 76.9% |
| White | 38 | 20.9% |
| Unknown | 4 | 2.2% |

### Oakdale Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Black | 1 | 100.0% |

### Opelousas Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| African American | 1 | 100.0% |

### Orleans Parish
**Total:** 1,457

| Race | Count | % |
|------|-------|---|
| Black | 1,257 | 86.3% |
| White | 181 | 12.4% |
| Unknown | 14 | 1.0% |
| Asian/PacificIslander | 5 | 0.3% |

### Ouachita Parish
**Total:** 1,317

| Race | Count | % |
|------|-------|---|
| Black | 887 | 67.4% |
| White | 420 | 31.9% |
| Unknown | 10 | 0.8% |

### Plaquemines Parish
**Total:** 671

| Race | Count | % |
|------|-------|---|
| Black | 436 | 65.0% |
| White | 210 | 31.3% |
| Unknown | 13 | 1.9% |
| Asian/PacificIslander | 10 | 1.5% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 84 | 65.1% |
| White | 42 | 32.6% |
| Unknown | 2 | 1.6% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,048

| Race | Count | % |
|------|-------|---|
| Black | 666 | 63.5% |
| White | 363 | 34.6% |
| Unknown | 17 | 1.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 23 | 53.5% |
| White | 19 | 44.2% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 695

| Race | Count | % |
|------|-------|---|
| Black | 479 | 68.9% |
| White | 208 | 29.9% |
| Unknown | 5 | 0.7% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 181

| Race | Count | % |
|------|-------|---|
| White | 105 | 58.0% |
| Black | 74 | 40.9% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Shreveport Police Department
**Total:** 32

| Race | Count | % |
|------|-------|---|
| Black | 23 | 71.9% |
| White | 8 | 25.0% |
| Unknown | 1 | 3.1% |

### St. Bernard Parish
**Total:** 235

| Race | Count | % |
|------|-------|---|
| Black | 143 | 60.9% |
| White | 89 | 37.9% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 173

| Race | Count | % |
|------|-------|---|
| Unknown | 99 | 57.2% |
| White | 74 | 42.8% |

### St. Helena Parish
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 36 | 78.3% |
| White | 10 | 21.7% |

### St. James Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| Black | 63 | 84.0% |
| White | 12 | 16.0% |

### St. John the Baptist Parish
**Total:** 221

| Race | Count | % |
|------|-------|---|
| Unknown | 148 | 67.0% |
| White | 73 | 33.0% |

### St. Landry Parish
**Total:** 138

| Race | Count | % |
|------|-------|---|
| Black | 91 | 65.9% |
| White | 45 | 32.6% |
| Unknown | 2 | 1.4% |

### St. Martin Parish
**Total:** 229

| Race | Count | % |
|------|-------|---|
| Black | 113 | 49.3% |
| White | 108 | 47.2% |
| Unknown | 8 | 3.5% |

### St. Mary Parish
**Total:** 283

| Race | Count | % |
|------|-------|---|
| Black | 145 | 51.2% |
| White | 136 | 48.1% |
| Unknown | 1 | 0.4% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 866

| Race | Count | % |
|------|-------|---|
| White | 442 | 51.0% |
| Black | 380 | 43.9% |
| Unknown | 42 | 4.8% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 12 | 85.7% |
| Black | 2 | 14.3% |

### Tangipahoa Parish
**Total:** 716

| Race | Count | % |
|------|-------|---|
| Black | 470 | 65.6% |
| White | 242 | 33.8% |
| Unknown | 4 | 0.6% |

### Tensas Parish
**Total:** 565

| Race | Count | % |
|------|-------|---|
| Black | 381 | 67.4% |
| White | 170 | 30.1% |
| Unknown | 14 | 2.5% |

### Terrebonne Parish
**Total:** 585

| Race | Count | % |
|------|-------|---|
| Black | 332 | 56.8% |
| White | 239 | 40.9% |
| American Indian/Alaska Native | 13 | 2.2% |
| Asian/PacificIslander | 1 | 0.2% |

### Vermillion Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| Black | 58 | 49.6% |
| White | 56 | 47.9% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.9% |

### Vernon Parish
**Total:** 171

| Race | Count | % |
|------|-------|---|
| White | 121 | 70.8% |
| Black | 48 | 28.1% |
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
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Black | 94 | 51.4% |
| White | 88 | 48.1% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 442

| Race | Count | % |
|------|-------|---|
| Black | 229 | 51.8% |
| White | 207 | 46.8% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 88 | 65.7% |
| White | 42 | 31.3% |
| Unknown | 3 | 2.2% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 27

| Race | Count | % |
|------|-------|---|
| White | 21 | 77.8% |
| Black | 6 | 22.2% |

### West Felician Parish
**Total:** 199

| Race | Count | % |
|------|-------|---|
| Black | 127 | 63.8% |
| White | 72 | 36.2% |

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
