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

_Last updated: 2026-04-29 02:37 UTC_

**Total inmates (latest scrape):** 25,739 across 72 parishes/jails

### Acadia Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| White | 90 | 53.6% |
| Black | 76 | 45.2% |
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
**Total:** 513

| Race | Count | % |
|------|-------|---|
| Black | 266 | 51.9% |
| White | 208 | 40.5% |
| Unknown | 36 | 7.0% |
| Asian/PacificIslander | 3 | 0.6% |

### Assumption Parish
**Total:** 141

| Race | Count | % |
|------|-------|---|
| Unknown | 72 | 51.1% |
| White | 69 | 48.9% |

### Avoyelles Parish
**Total:** 386

| Race | Count | % |
|------|-------|---|
| Black | 201 | 52.1% |
| White | 178 | 46.1% |
| Unknown | 6 | 1.6% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 179

| Race | Count | % |
|------|-------|---|
| White | 127 | 70.9% |
| Black | 52 | 29.1% |

### Bienville Parish
**Total:** 40

| Race | Count | % |
|------|-------|---|
| White | 24 | 60.0% |
| Unknown | 16 | 40.0% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 42

| Race | Count | % |
|------|-------|---|
| Black | 29 | 69.0% |
| White | 13 | 31.0% |

### Bossier Parish
**Total:** 1,116

| Race | Count | % |
|------|-------|---|
| Black | 614 | 55.0% |
| White | 499 | 44.7% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,576

| Race | Count | % |
|------|-------|---|
| Black | 1,169 | 74.2% |
| White | 370 | 23.5% |
| Unknown | 34 | 2.2% |
| Asian/PacificIslander | 3 | 0.2% |

### Calcasieu Parish
**Total:** 1,031

| Race | Count | % |
|------|-------|---|
| Black | 552 | 53.5% |
| White | 432 | 41.9% |
| Unknown | 44 | 4.3% |
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
**Total:** 22

| Race | Count | % |
|------|-------|---|
| White | 20 | 90.9% |
| Black | 2 | 9.1% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 94 | 71.2% |
| White | 37 | 28.0% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 631

| Race | Count | % |
|------|-------|---|
| Black | 380 | 60.2% |
| White | 251 | 39.8% |

### Concordia Parish
**Total:** 806

| Race | Count | % |
|------|-------|---|
| White | 446 | 55.3% |
| Black | 356 | 44.2% |
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
**Total:** 849

| Race | Count | % |
|------|-------|---|
| Black | 556 | 65.5% |
| White | 282 | 33.2% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| Black | 10 | 62.5% |
| White | 6 | 37.5% |

### Iberia Parish
**Total:** 434

| Race | Count | % |
|------|-------|---|
| Black | 271 | 62.4% |
| White | 157 | 36.2% |
| Asian/PacificIslander | 3 | 0.7% |
| Unknown | 2 | 0.5% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 106

| Race | Count | % |
|------|-------|---|
| Black | 66 | 62.3% |
| White | 37 | 34.9% |
| Unknown | 3 | 2.8% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 153

| Race | Count | % |
|------|-------|---|
| Black | 75 | 49.0% |
| White | 73 | 47.7% |
| American Indian/Alaska Native | 3 | 2.0% |
| Asian/PacificIslander | 1 | 0.7% |
| Unknown | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,162

| Race | Count | % |
|------|-------|---|
| Black | 764 | 65.7% |
| White | 386 | 33.2% |
| Unknown | 8 | 0.7% |
| Asian/PacificIslander | 4 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 72

| Race | Count | % |
|------|-------|---|
| White | 51 | 70.8% |
| Black | 20 | 27.8% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 867

| Race | Count | % |
|------|-------|---|
| Black | 549 | 63.3% |
| White | 306 | 35.3% |
| Unknown | 12 | 1.4% |

### Lafourche Parish
**Total:** 752

| Race | Count | % |
|------|-------|---|
| Black | 385 | 51.2% |
| White | 357 | 47.5% |
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
**Total:** 360

| Race | Count | % |
|------|-------|---|
| Black | 265 | 73.6% |
| White | 94 | 26.1% |
| Unknown | 1 | 0.3% |

### Livingston Parish
**Total:** 819

| Race | Count | % |
|------|-------|---|
| White | 591 | 72.2% |
| Black | 220 | 26.9% |
| Unknown | 6 | 0.7% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 140

| Race | Count | % |
|------|-------|---|
| Black | 109 | 77.9% |
| White | 30 | 21.4% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Black | 143 | 70.4% |
| White | 60 | 29.6% |

### Natchitoches Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| Black | 142 | 72.1% |
| White | 51 | 25.9% |
| Unknown | 3 | 1.5% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 7

| Race | Count | % |
|------|-------|---|
| Black | 4 | 57.1% |
| White | 3 | 42.9% |

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
**Total:** 1,274

| Race | Count | % |
|------|-------|---|
| Black | 850 | 66.7% |
| White | 409 | 32.1% |
| Unknown | 15 | 1.2% |

### Plaquemines Parish
**Total:** 637

| Race | Count | % |
|------|-------|---|
| Black | 418 | 65.6% |
| White | 199 | 31.2% |
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
**Total:** 986

| Race | Count | % |
|------|-------|---|
| Black | 614 | 62.3% |
| White | 353 | 35.8% |
| Unknown | 17 | 1.7% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 42

| Race | Count | % |
|------|-------|---|
| Black | 25 | 59.5% |
| White | 16 | 38.1% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 719

| Race | Count | % |
|------|-------|---|
| Black | 493 | 68.6% |
| White | 216 | 30.0% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| White | 100 | 56.8% |
| Black | 76 | 43.2% |

### Shreveport Police Department
**Total:** 37

| Race | Count | % |
|------|-------|---|
| Black | 29 | 78.4% |
| White | 8 | 21.6% |

### St. Bernard Parish
**Total:** 224

| Race | Count | % |
|------|-------|---|
| Black | 127 | 56.7% |
| White | 94 | 42.0% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 177

| Race | Count | % |
|------|-------|---|
| Unknown | 104 | 58.8% |
| White | 73 | 41.2% |

### St. Helena Parish
**Total:** 76

| Race | Count | % |
|------|-------|---|
| Black | 55 | 72.4% |
| White | 16 | 21.1% |
| Unknown | 4 | 5.3% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 71

| Race | Count | % |
|------|-------|---|
| Black | 57 | 80.3% |
| White | 14 | 19.7% |

### St. John the Baptist Parish
**Total:** 194

| Race | Count | % |
|------|-------|---|
| Unknown | 124 | 63.9% |
| White | 70 | 36.1% |

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
**Total:** 246

| Race | Count | % |
|------|-------|---|
| White | 123 | 50.0% |
| Black | 122 | 49.6% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 805

| Race | Count | % |
|------|-------|---|
| White | 410 | 50.9% |
| Black | 355 | 44.1% |
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
**Total:** 635

| Race | Count | % |
|------|-------|---|
| Black | 386 | 60.8% |
| White | 248 | 39.1% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 559

| Race | Count | % |
|------|-------|---|
| Black | 367 | 65.7% |
| White | 177 | 31.7% |
| Unknown | 15 | 2.7% |

### Terrebonne Parish
**Total:** 476

| Race | Count | % |
|------|-------|---|
| Black | 252 | 52.9% |
| White | 218 | 45.8% |
| American Indian/Alaska Native | 6 | 1.3% |

### Vermillion Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| White | 69 | 53.5% |
| Black | 58 | 45.0% |
| Unknown | 2 | 1.6% |

### Vernon Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| White | 111 | 70.3% |
| Black | 44 | 27.8% |
| Unknown | 2 | 1.3% |
| Asian/PacificIslander | 1 | 0.6% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| Black | 85 | 52.5% |
| White | 77 | 47.5% |

### Webster Parish
**Total:** 427

| Race | Count | % |
|------|-------|---|
| White | 213 | 49.9% |
| Black | 209 | 48.9% |
| Unknown | 3 | 0.7% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 76 | 59.8% |
| White | 47 | 37.0% |
| Unknown | 3 | 2.4% |
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
**Total:** 143

| Race | Count | % |
|------|-------|---|
| White | 75 | 52.4% |
| Black | 68 | 47.6% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
