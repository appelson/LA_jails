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

_Last updated: 2026-08-12 01:31 UTC_

**Total inmates (latest scrape):** 27,151 across 72 parishes/jails

### Acadia Parish
**Total:** 161

| Race | Count | % |
|------|-------|---|
| White | 87 | 54.0% |
| Black | 72 | 44.7% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| White | 72 | 61.0% |
| Black | 42 | 35.6% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 514

| Race | Count | % |
|------|-------|---|
| Black | 271 | 52.7% |
| White | 207 | 40.3% |
| Unknown | 31 | 6.0% |
| Asian/PacificIslander | 5 | 1.0% |

### Assumption Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| Unknown | 94 | 57.3% |
| White | 70 | 42.7% |

### Avoyelles Parish
**Total:** 354

| Race | Count | % |
|------|-------|---|
| Black | 200 | 56.5% |
| White | 151 | 42.7% |
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
**Total:** 26

| Race | Count | % |
|------|-------|---|
| White | 18 | 69.2% |
| Black | 8 | 30.8% |

### Bossier City Police Department
**Total:** 58

| Race | Count | % |
|------|-------|---|
| Black | 41 | 70.7% |
| White | 17 | 29.3% |

### Bossier Parish
**Total:** 1,128

| Race | Count | % |
|------|-------|---|
| Black | 635 | 56.3% |
| White | 491 | 43.5% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,726

| Race | Count | % |
|------|-------|---|
| Black | 1,310 | 75.9% |
| White | 385 | 22.3% |
| Unknown | 31 | 1.8% |

### Calcasieu Parish
**Total:** 1,100

| Race | Count | % |
|------|-------|---|
| Black | 596 | 54.2% |
| White | 461 | 41.9% |
| Unknown | 42 | 3.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 604

| Race | Count | % |
|------|-------|---|
| Black | 385 | 63.7% |
| White | 203 | 33.6% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 22

| Race | Count | % |
|------|-------|---|
| White | 21 | 95.5% |
| Black | 1 | 4.5% |

### Catahoula Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 90 | 69.2% |
| White | 38 | 29.2% |
| Unknown | 2 | 1.5% |

### Claiborne Parish
**Total:** 652

| Race | Count | % |
|------|-------|---|
| Black | 402 | 61.7% |
| White | 250 | 38.3% |

### Concordia Parish
**Total:** 827

| Race | Count | % |
|------|-------|---|
| White | 471 | 57.0% |
| Black | 356 | 43.0% |

### DeSoto Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 74 | 57.8% |
| White | 54 | 42.2% |

### East Baton Rouge Parish
**Total:** 1,297

| Race | Count | % |
|------|-------|---|
| Black | 1,012 | 78.0% |
| White | 224 | 17.3% |
| Unknown | 57 | 4.4% |
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
**Total:** 855

| Race | Count | % |
|------|-------|---|
| Black | 566 | 66.2% |
| White | 284 | 33.2% |
| Unknown | 4 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| Black | 10 | 58.8% |
| White | 7 | 41.2% |

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
**Total:** 93

| Race | Count | % |
|------|-------|---|
| Black | 67 | 72.0% |
| White | 25 | 26.9% |
| Unknown | 1 | 1.1% |

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
**Total:** 1,224

| Race | Count | % |
|------|-------|---|
| Black | 802 | 65.5% |
| White | 416 | 34.0% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| White | 2 | 100.0% |

### LaSalle Parish
**Total:** 79

| Race | Count | % |
|------|-------|---|
| White | 50 | 63.3% |
| Black | 28 | 35.4% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 844

| Race | Count | % |
|------|-------|---|
| Black | 555 | 65.8% |
| White | 279 | 33.1% |
| Unknown | 10 | 1.2% |

### Lafourche Parish
**Total:** 780

| Race | Count | % |
|------|-------|---|
| Black | 389 | 49.9% |
| White | 387 | 49.6% |
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
| Black | 278 | 74.7% |
| White | 90 | 24.2% |
| Unknown | 4 | 1.1% |

### Livingston Parish
**Total:** 836

| Race | Count | % |
|------|-------|---|
| White | 592 | 70.8% |
| Black | 235 | 28.1% |
| Unknown | 6 | 0.7% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| Black | 118 | 81.4% |
| White | 26 | 17.9% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| Black | 144 | 73.1% |
| White | 53 | 26.9% |

### Natchitoches Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| Black | 147 | 77.4% |
| White | 39 | 20.5% |
| Unknown | 4 | 2.1% |

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
**Total:** 1,450

| Race | Count | % |
|------|-------|---|
| Black | 1,250 | 86.2% |
| White | 181 | 12.5% |
| Unknown | 14 | 1.0% |
| Asian/PacificIslander | 5 | 0.3% |

### Ouachita Parish
**Total:** 1,337

| Race | Count | % |
|------|-------|---|
| Black | 903 | 67.5% |
| White | 422 | 31.6% |
| Unknown | 12 | 0.9% |

### Plaquemines Parish
**Total:** 665

| Race | Count | % |
|------|-------|---|
| Black | 430 | 64.7% |
| White | 210 | 31.6% |
| Unknown | 13 | 2.0% |
| Asian/PacificIslander | 10 | 1.5% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 85 | 65.4% |
| White | 42 | 32.3% |
| Unknown | 2 | 1.5% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,051

| Race | Count | % |
|------|-------|---|
| Black | 677 | 64.4% |
| White | 357 | 34.0% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 23 | 52.3% |
| White | 20 | 45.5% |
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
**Total:** 185

| Race | Count | % |
|------|-------|---|
| White | 108 | 58.4% |
| Black | 75 | 40.5% |
| Unknown | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 34

| Race | Count | % |
|------|-------|---|
| Black | 25 | 73.5% |
| White | 8 | 23.5% |
| Unknown | 1 | 2.9% |

### St. Bernard Parish
**Total:** 232

| Race | Count | % |
|------|-------|---|
| Black | 139 | 59.9% |
| White | 89 | 38.4% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 177

| Race | Count | % |
|------|-------|---|
| Unknown | 103 | 58.2% |
| White | 74 | 41.8% |

### St. Helena Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 36 | 76.6% |
| White | 10 | 21.3% |
| Unknown | 1 | 2.1% |

### St. James Parish
**Total:** 74

| Race | Count | % |
|------|-------|---|
| Black | 62 | 83.8% |
| White | 12 | 16.2% |

### St. John the Baptist Parish
**Total:** 227

| Race | Count | % |
|------|-------|---|
| Unknown | 149 | 65.6% |
| White | 78 | 34.4% |

### St. Landry Parish
**Total:** 137

| Race | Count | % |
|------|-------|---|
| Black | 93 | 67.9% |
| White | 42 | 30.7% |
| Unknown | 2 | 1.5% |

### St. Martin Parish
**Total:** 224

| Race | Count | % |
|------|-------|---|
| Black | 113 | 50.4% |
| White | 103 | 46.0% |
| Unknown | 8 | 3.6% |

### St. Mary Parish
**Total:** 288

| Race | Count | % |
|------|-------|---|
| Black | 146 | 50.7% |
| White | 140 | 48.6% |
| Unknown | 1 | 0.3% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 872

| Race | Count | % |
|------|-------|---|
| White | 447 | 51.3% |
| Black | 384 | 44.0% |
| Unknown | 39 | 4.5% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 12 | 85.7% |
| Black | 2 | 14.3% |

### Tangipahoa Parish
**Total:** 708

| Race | Count | % |
|------|-------|---|
| Black | 464 | 65.5% |
| White | 241 | 34.0% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 567

| Race | Count | % |
|------|-------|---|
| Black | 382 | 67.4% |
| White | 171 | 30.2% |
| Unknown | 14 | 2.5% |

### Terrebonne Parish
**Total:** 586

| Race | Count | % |
|------|-------|---|
| Black | 336 | 57.3% |
| White | 237 | 40.4% |
| American Indian/Alaska Native | 12 | 2.0% |
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
**Total:** 182

| Race | Count | % |
|------|-------|---|
| Black | 94 | 51.6% |
| White | 87 | 47.8% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 446

| Race | Count | % |
|------|-------|---|
| Black | 230 | 51.6% |
| White | 209 | 46.9% |
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
**Total:** 199

| Race | Count | % |
|------|-------|---|
| Black | 128 | 64.3% |
| White | 71 | 35.7% |

### Winn Parish
**Total:** 149

| Race | Count | % |
|------|-------|---|
| Black | 77 | 51.7% |
| White | 72 | 48.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
