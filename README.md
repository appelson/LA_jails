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

_Last updated: 2026-04-28 02:35 UTC_

**Total inmates (latest scrape):** 25,735 across 72 parishes/jails

### Acadia Parish
**Total:** 167

| Race | Count | % |
|------|-------|---|
| White | 88 | 52.7% |
| Black | 77 | 46.1% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| White | 82 | 62.6% |
| Black | 47 | 35.9% |
| Unknown | 1 | 0.8% |
| American Indian/Alaska Native | 1 | 0.8% |

### Ascension Parish
**Total:** 510

| Race | Count | % |
|------|-------|---|
| Black | 267 | 52.4% |
| White | 205 | 40.2% |
| Unknown | 35 | 6.9% |
| Asian/PacificIslander | 3 | 0.6% |

### Assumption Parish
**Total:** 141

| Race | Count | % |
|------|-------|---|
| Unknown | 72 | 51.1% |
| White | 69 | 48.9% |

### Avoyelles Parish
**Total:** 388

| Race | Count | % |
|------|-------|---|
| Black | 202 | 52.1% |
| White | 179 | 46.1% |
| Unknown | 6 | 1.5% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 175

| Race | Count | % |
|------|-------|---|
| White | 123 | 70.3% |
| Black | 51 | 29.1% |
| Unknown | 1 | 0.6% |

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
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 29 | 67.4% |
| White | 14 | 32.6% |

### Bossier Parish
**Total:** 1,118

| Race | Count | % |
|------|-------|---|
| Black | 616 | 55.1% |
| White | 499 | 44.6% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,577

| Race | Count | % |
|------|-------|---|
| Black | 1,170 | 74.2% |
| White | 369 | 23.4% |
| Unknown | 35 | 2.2% |
| Asian/PacificIslander | 3 | 0.2% |

### Calcasieu Parish
**Total:** 1,037

| Race | Count | % |
|------|-------|---|
| Black | 555 | 53.5% |
| White | 434 | 41.9% |
| Unknown | 45 | 4.3% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 606

| Race | Count | % |
|------|-------|---|
| Black | 393 | 64.9% |
| White | 192 | 31.7% |
| American Indian/Alaska Native | 20 | 3.3% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 18 | 94.7% |
| Black | 1 | 5.3% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 94 | 71.2% |
| White | 37 | 28.0% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 629

| Race | Count | % |
|------|-------|---|
| Black | 380 | 60.4% |
| White | 249 | 39.6% |

### Concordia Parish
**Total:** 809

| Race | Count | % |
|------|-------|---|
| White | 446 | 55.1% |
| Black | 359 | 44.4% |
| Unknown | 4 | 0.5% |

### DeSoto Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| Black | 76 | 63.9% |
| White | 42 | 35.3% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,046

| Race | Count | % |
|------|-------|---|
| Black | 798 | 76.3% |
| White | 196 | 18.7% |
| Unknown | 51 | 4.9% |
| Asian/PacificIslander | 1 | 0.1% |

### East Feliciana Parish
**Total:** 274

| Race | Count | % |
|------|-------|---|
| Black | 166 | 60.6% |
| White | 107 | 39.1% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 79

| Race | Count | % |
|------|-------|---|
| White | 40 | 50.6% |
| Black | 38 | 48.1% |
| Unknown | 1 | 1.3% |

### Franklin Parish
**Total:** 848

| Race | Count | % |
|------|-------|---|
| Black | 555 | 65.4% |
| White | 282 | 33.3% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| Black | 11 | 73.3% |
| White | 4 | 26.7% |

### Iberia Parish
**Total:** 437

| Race | Count | % |
|------|-------|---|
| Black | 274 | 62.7% |
| White | 157 | 35.9% |
| Asian/PacificIslander | 3 | 0.7% |
| Unknown | 2 | 0.5% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 105

| Race | Count | % |
|------|-------|---|
| Black | 67 | 63.8% |
| White | 36 | 34.3% |
| Unknown | 2 | 1.9% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| Black | 75 | 48.7% |
| White | 74 | 48.1% |
| American Indian/Alaska Native | 3 | 1.9% |
| Asian/PacificIslander | 1 | 0.6% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,144

| Race | Count | % |
|------|-------|---|
| Black | 747 | 65.3% |
| White | 385 | 33.7% |
| Unknown | 8 | 0.7% |
| Asian/PacificIslander | 4 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 70

| Race | Count | % |
|------|-------|---|
| White | 48 | 68.6% |
| Black | 21 | 30.0% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 867

| Race | Count | % |
|------|-------|---|
| Black | 549 | 63.3% |
| White | 307 | 35.4% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 761

| Race | Count | % |
|------|-------|---|
| Black | 387 | 50.9% |
| White | 364 | 47.8% |
| American Indian/Alaska Native | 5 | 0.7% |
| Asian/PacificIslander | 3 | 0.4% |
| Unknown | 2 | 0.3% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 356

| Race | Count | % |
|------|-------|---|
| Black | 263 | 73.9% |
| White | 92 | 25.8% |
| Unknown | 1 | 0.3% |

### Livingston Parish
**Total:** 811

| Race | Count | % |
|------|-------|---|
| White | 585 | 72.1% |
| Black | 218 | 26.9% |
| Unknown | 6 | 0.7% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 141

| Race | Count | % |
|------|-------|---|
| Black | 109 | 77.3% |
| White | 31 | 22.0% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 206

| Race | Count | % |
|------|-------|---|
| Black | 145 | 70.4% |
| White | 61 | 29.6% |

### Natchitoches Parish
**Total:** 198

| Race | Count | % |
|------|-------|---|
| Black | 145 | 73.2% |
| White | 49 | 24.7% |
| Unknown | 3 | 1.5% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 8

| Race | Count | % |
|------|-------|---|
| Black | 5 | 62.5% |
| White | 3 | 37.5% |

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
**Total:** 1,278

| Race | Count | % |
|------|-------|---|
| Black | 849 | 66.4% |
| White | 413 | 32.3% |
| Unknown | 16 | 1.3% |

### Plaquemines Parish
**Total:** 642

| Race | Count | % |
|------|-------|---|
| Black | 420 | 65.4% |
| White | 202 | 31.5% |
| Unknown | 12 | 1.9% |
| Asian/PacificIslander | 7 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Pointe Coupee Parish
**Total:** 103

| Race | Count | % |
|------|-------|---|
| Black | 68 | 66.0% |
| White | 34 | 33.0% |
| Unknown | 1 | 1.0% |

### Rapides Parish
**Total:** 973

| Race | Count | % |
|------|-------|---|
| Black | 604 | 62.1% |
| White | 349 | 35.9% |
| Unknown | 18 | 1.8% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 40

| Race | Count | % |
|------|-------|---|
| Black | 24 | 60.0% |
| White | 15 | 37.5% |
| Asian/PacificIslander | 1 | 2.5% |

### Richland Parish
**Total:** 720

| Race | Count | % |
|------|-------|---|
| Black | 497 | 69.0% |
| White | 213 | 29.6% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 179

| Race | Count | % |
|------|-------|---|
| White | 101 | 56.4% |
| Black | 76 | 42.5% |
| Unknown | 2 | 1.1% |

### Shreveport Police Department
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 38 | 86.4% |
| White | 5 | 11.4% |
| Unknown | 1 | 2.3% |

### St. Bernard Parish
**Total:** 221

| Race | Count | % |
|------|-------|---|
| Black | 126 | 57.0% |
| White | 92 | 41.6% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 177

| Race | Count | % |
|------|-------|---|
| Unknown | 106 | 59.9% |
| White | 71 | 40.1% |

### St. Helena Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| Black | 54 | 72.0% |
| White | 16 | 21.3% |
| Unknown | 4 | 5.3% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 71

| Race | Count | % |
|------|-------|---|
| Black | 58 | 81.7% |
| White | 13 | 18.3% |

### St. John the Baptist Parish
**Total:** 194

| Race | Count | % |
|------|-------|---|
| Unknown | 122 | 62.9% |
| White | 72 | 37.1% |

### St. Landry Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 70 | 62.5% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 199

| Race | Count | % |
|------|-------|---|
| Black | 102 | 51.3% |
| White | 90 | 45.2% |
| Unknown | 6 | 3.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 240

| Race | Count | % |
|------|-------|---|
| White | 120 | 50.0% |
| Black | 119 | 49.6% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 806

| Race | Count | % |
|------|-------|---|
| White | 407 | 50.5% |
| Black | 359 | 44.5% |
| Unknown | 36 | 4.5% |
| American Indian/Alaska Native | 2 | 0.2% |
| Asian/PacificIslander | 2 | 0.2% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 14 | 93.3% |
| Black | 1 | 6.7% |

### Tangipahoa Parish
**Total:** 638

| Race | Count | % |
|------|-------|---|
| Black | 389 | 61.0% |
| White | 248 | 38.9% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 559

| Race | Count | % |
|------|-------|---|
| Black | 368 | 65.8% |
| White | 176 | 31.5% |
| Unknown | 15 | 2.7% |

### Terrebonne Parish
**Total:** 479

| Race | Count | % |
|------|-------|---|
| Black | 251 | 52.4% |
| White | 222 | 46.3% |
| American Indian/Alaska Native | 6 | 1.3% |

### Vermillion Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| White | 69 | 53.5% |
| Black | 58 | 45.0% |
| Unknown | 2 | 1.6% |

### Vernon Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| White | 105 | 69.5% |
| Black | 43 | 28.5% |
| Unknown | 2 | 1.3% |
| Asian/PacificIslander | 1 | 0.7% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 174

| Race | Count | % |
|------|-------|---|
| Black | 92 | 52.9% |
| White | 82 | 47.1% |

### Webster Parish
**Total:** 427

| Race | Count | % |
|------|-------|---|
| Black | 211 | 49.4% |
| White | 211 | 49.4% |
| Unknown | 3 | 0.7% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 76 | 58.5% |
| White | 49 | 37.7% |
| Unknown | 4 | 3.1% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 26 | 86.7% |
| Black | 4 | 13.3% |

### West Felician Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Black | 111 | 60.7% |
| White | 72 | 39.3% |

### Winn Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| White | 75 | 52.1% |
| Black | 69 | 47.9% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
