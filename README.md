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

_Last updated: 2026-08-08 01:17 UTC_

**Total inmates (latest scrape):** 26,927 across 72 parishes/jails

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
**Total:** 519

| Race | Count | % |
|------|-------|---|
| Black | 275 | 53.0% |
| White | 207 | 39.9% |
| Unknown | 32 | 6.2% |
| Asian/PacificIslander | 5 | 1.0% |

### Assumption Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| Unknown | 93 | 57.4% |
| White | 69 | 42.6% |

### Avoyelles Parish
**Total:** 348

| Race | Count | % |
|------|-------|---|
| Black | 194 | 55.7% |
| White | 151 | 43.4% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 174

| Race | Count | % |
|------|-------|---|
| White | 109 | 62.6% |
| Black | 65 | 37.4% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 11 | 61.1% |
| Black | 7 | 38.9% |

### Bossier City Police Department
**Total:** 65

| Race | Count | % |
|------|-------|---|
| Black | 42 | 64.6% |
| White | 23 | 35.4% |

### Bossier Parish
**Total:** 1,125

| Race | Count | % |
|------|-------|---|
| Black | 632 | 56.2% |
| White | 491 | 43.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,717

| Race | Count | % |
|------|-------|---|
| Black | 1,301 | 75.8% |
| White | 387 | 22.5% |
| Unknown | 29 | 1.7% |

### Calcasieu Parish
**Total:** 1,091

| Race | Count | % |
|------|-------|---|
| Black | 596 | 54.6% |
| White | 452 | 41.4% |
| Unknown | 42 | 3.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 605

| Race | Count | % |
|------|-------|---|
| Black | 388 | 64.1% |
| White | 201 | 33.2% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 22

| Race | Count | % |
|------|-------|---|
| White | 21 | 95.5% |
| Black | 1 | 4.5% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 91 | 68.9% |
| White | 39 | 29.5% |
| Unknown | 2 | 1.5% |

### Claiborne Parish
**Total:** 656

| Race | Count | % |
|------|-------|---|
| Black | 408 | 62.2% |
| White | 248 | 37.8% |

### Concordia Parish
**Total:** 817

| Race | Count | % |
|------|-------|---|
| White | 464 | 56.8% |
| Black | 353 | 43.2% |

### DeSoto Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 75 | 57.7% |
| White | 55 | 42.3% |

### East Baton Rouge Parish
**Total:** 1,269

| Race | Count | % |
|------|-------|---|
| Black | 985 | 77.6% |
| White | 225 | 17.7% |
| Unknown | 55 | 4.3% |
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
**Total:** 158

| Race | Count | % |
|------|-------|---|
| Black | 95 | 60.1% |
| White | 62 | 39.2% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 847

| Race | Count | % |
|------|-------|---|
| Black | 561 | 66.2% |
| White | 281 | 33.2% |
| Unknown | 4 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 10 | 52.6% |
| Black | 9 | 47.4% |

### Iberia Parish
**Total:** 468

| Race | Count | % |
|------|-------|---|
| Black | 280 | 59.8% |
| White | 176 | 37.6% |
| Unknown | 6 | 1.3% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 54

| Race | Count | % |
|------|-------|---|
| Black | 34 | 63.0% |
| White | 20 | 37.0% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 161

| Race | Count | % |
|------|-------|---|
| White | 82 | 50.9% |
| Black | 77 | 47.8% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,207

| Race | Count | % |
|------|-------|---|
| Black | 788 | 65.3% |
| White | 411 | 34.1% |
| Unknown | 7 | 0.6% |
| Asian/PacificIslander | 1 | 0.1% |

### Kinder Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| White | 1 | 50.0% |
| Black | 1 | 50.0% |

### LaSalle Parish
**Total:** 77

| Race | Count | % |
|------|-------|---|
| White | 48 | 62.3% |
| Black | 27 | 35.1% |
| Unknown | 2 | 2.6% |

### Lafayette Parish
**Total:** 827

| Race | Count | % |
|------|-------|---|
| Black | 548 | 66.3% |
| White | 269 | 32.5% |
| Unknown | 10 | 1.2% |

### Lafourche Parish
**Total:** 780

| Race | Count | % |
|------|-------|---|
| Black | 393 | 50.4% |
| White | 383 | 49.1% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 363

| Race | Count | % |
|------|-------|---|
| Black | 270 | 74.4% |
| White | 89 | 24.5% |
| Unknown | 4 | 1.1% |

### Livingston Parish
**Total:** 824

| Race | Count | % |
|------|-------|---|
| White | 587 | 71.2% |
| Black | 228 | 27.7% |
| Unknown | 6 | 0.7% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 147

| Race | Count | % |
|------|-------|---|
| Black | 119 | 81.0% |
| White | 26 | 17.7% |
| Unknown | 1 | 0.7% |
| American Indian/Alaska Native | 1 | 0.7% |

### Morehouse Parish
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Black | 147 | 73.5% |
| White | 52 | 26.0% |
| Unknown | 1 | 0.5% |

### Natchitoches Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| Black | 142 | 76.8% |
| White | 39 | 21.1% |
| Unknown | 4 | 2.2% |

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
**Total:** 1,444

| Race | Count | % |
|------|-------|---|
| Black | 1,243 | 86.1% |
| White | 181 | 12.5% |
| Unknown | 15 | 1.0% |
| Asian/PacificIslander | 5 | 0.3% |

### Ouachita Parish
**Total:** 1,336

| Race | Count | % |
|------|-------|---|
| Black | 900 | 67.4% |
| White | 425 | 31.8% |
| Unknown | 11 | 0.8% |

### Plaquemines Parish
**Total:** 662

| Race | Count | % |
|------|-------|---|
| Black | 429 | 64.8% |
| White | 210 | 31.7% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 9 | 1.4% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 81 | 63.8% |
| White | 43 | 33.9% |
| Unknown | 2 | 1.6% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,063

| Race | Count | % |
|------|-------|---|
| Black | 678 | 63.8% |
| White | 369 | 34.7% |
| Unknown | 14 | 1.3% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 22 | 53.7% |
| White | 18 | 43.9% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 700

| Race | Count | % |
|------|-------|---|
| Black | 486 | 69.4% |
| White | 206 | 29.4% |
| Unknown | 5 | 0.7% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| White | 112 | 58.9% |
| Black | 76 | 40.0% |
| Unknown | 1 | 0.5% |
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
| Black | 128 | 56.4% |
| White | 95 | 41.9% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 167

| Race | Count | % |
|------|-------|---|
| Unknown | 97 | 58.1% |
| White | 70 | 41.9% |

### St. Helena Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 34 | 77.3% |
| White | 10 | 22.7% |

### St. James Parish
**Total:** 77

| Race | Count | % |
|------|-------|---|
| Black | 66 | 85.7% |
| White | 11 | 14.3% |

### St. John the Baptist Parish
**Total:** 225

| Race | Count | % |
|------|-------|---|
| Unknown | 148 | 65.8% |
| White | 77 | 34.2% |

### St. Landry Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 89 | 66.4% |
| White | 43 | 32.1% |
| Unknown | 2 | 1.5% |

### St. Martin Parish
**Total:** 216

| Race | Count | % |
|------|-------|---|
| Black | 108 | 50.0% |
| White | 100 | 46.3% |
| Unknown | 8 | 3.7% |

### St. Mary Parish
**Total:** 282

| Race | Count | % |
|------|-------|---|
| Black | 143 | 50.7% |
| White | 138 | 48.9% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 875

| Race | Count | % |
|------|-------|---|
| White | 445 | 50.9% |
| Black | 389 | 44.5% |
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
**Total:** 704

| Race | Count | % |
|------|-------|---|
| Black | 464 | 65.9% |
| White | 237 | 33.7% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 564

| Race | Count | % |
|------|-------|---|
| Black | 381 | 67.6% |
| White | 171 | 30.3% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 576

| Race | Count | % |
|------|-------|---|
| Black | 329 | 57.1% |
| White | 232 | 40.3% |
| American Indian/Alaska Native | 13 | 2.3% |
| Asian/PacificIslander | 1 | 0.2% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| White | 58 | 49.6% |
| Black | 56 | 47.9% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.9% |

### Vernon Parish
**Total:** 172

| Race | Count | % |
|------|-------|---|
| White | 121 | 70.3% |
| Black | 49 | 28.5% |
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
**Total:** 186

| Race | Count | % |
|------|-------|---|
| Black | 95 | 51.1% |
| White | 90 | 48.4% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 441

| Race | Count | % |
|------|-------|---|
| Black | 229 | 51.9% |
| White | 205 | 46.5% |
| Unknown | 5 | 1.1% |
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
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Black | 128 | 64.0% |
| White | 72 | 36.0% |

### Winn Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| Black | 74 | 50.7% |
| White | 72 | 49.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
