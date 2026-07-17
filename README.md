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

_Last updated: 2026-07-17 02:14 UTC_

**Total inmates (latest scrape):** 26,814 across 72 parishes/jails

### Acadia Parish
**Total:** 170

| Race | Count | % |
|------|-------|---|
| White | 95 | 55.9% |
| Black | 74 | 43.5% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| White | 76 | 62.8% |
| Black | 42 | 34.7% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.8% |

### Ascension Parish
**Total:** 514

| Race | Count | % |
|------|-------|---|
| Black | 274 | 53.3% |
| White | 204 | 39.7% |
| Unknown | 32 | 6.2% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| Unknown | 88 | 55.3% |
| White | 71 | 44.7% |

### Avoyelles Parish
**Total:** 349

| Race | Count | % |
|------|-------|---|
| Black | 194 | 55.6% |
| White | 151 | 43.3% |
| Unknown | 3 | 0.9% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| White | 115 | 70.1% |
| Black | 49 | 29.9% |

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
| White | 15 | 57.7% |
| Black | 11 | 42.3% |

### Bossier City Police Department
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 26 | 54.2% |
| White | 22 | 45.8% |

### Bossier Parish
**Total:** 1,122

| Race | Count | % |
|------|-------|---|
| Black | 629 | 56.1% |
| White | 492 | 43.9% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,700

| Race | Count | % |
|------|-------|---|
| Black | 1,283 | 75.5% |
| White | 391 | 23.0% |
| Unknown | 25 | 1.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,106

| Race | Count | % |
|------|-------|---|
| Black | 614 | 55.5% |
| White | 446 | 40.3% |
| Unknown | 43 | 3.9% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 611

| Race | Count | % |
|------|-------|---|
| Black | 384 | 62.8% |
| White | 211 | 34.5% |
| American Indian/Alaska Native | 16 | 2.6% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 17 | 89.5% |
| Black | 1 | 5.3% |
| Unknown | 1 | 5.3% |

### Catahoula Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 92 | 71.3% |
| White | 36 | 27.9% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 657

| Race | Count | % |
|------|-------|---|
| Black | 406 | 61.8% |
| White | 251 | 38.2% |

### Concordia Parish
**Total:** 815

| Race | Count | % |
|------|-------|---|
| White | 459 | 56.3% |
| Black | 356 | 43.7% |

### DeSoto Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| Black | 73 | 59.8% |
| White | 48 | 39.3% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,354

| Race | Count | % |
|------|-------|---|
| Black | 1,071 | 79.1% |
| White | 221 | 16.3% |
| Unknown | 60 | 4.4% |
| Asian/PacificIslander | 2 | 0.1% |

### East Feliciana Parish
**Total:** 261

| Race | Count | % |
|------|-------|---|
| Black | 168 | 64.4% |
| White | 91 | 34.9% |
| Asian/PacificIslander | 2 | 0.8% |

### Evangeline Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| Black | 95 | 57.6% |
| White | 69 | 41.8% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 837

| Race | Count | % |
|------|-------|---|
| Black | 552 | 65.9% |
| White | 279 | 33.3% |
| Unknown | 6 | 0.7% |

### Hammond Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| Black | 10 | 62.5% |
| White | 6 | 37.5% |

### Iberia Parish
**Total:** 465

| Race | Count | % |
|------|-------|---|
| Black | 274 | 58.9% |
| White | 181 | 38.9% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 38

| Race | Count | % |
|------|-------|---|
| Black | 21 | 55.3% |
| White | 17 | 44.7% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| White | 87 | 52.4% |
| Black | 76 | 45.8% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,176

| Race | Count | % |
|------|-------|---|
| Black | 756 | 64.3% |
| White | 414 | 35.2% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### LaSalle Parish
**Total:** 72

| Race | Count | % |
|------|-------|---|
| White | 48 | 66.7% |
| Black | 23 | 31.9% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 815

| Race | Count | % |
|------|-------|---|
| Black | 534 | 65.5% |
| White | 265 | 32.5% |
| Unknown | 16 | 2.0% |

### Lafourche Parish
**Total:** 758

| Race | Count | % |
|------|-------|---|
| Black | 393 | 51.8% |
| White | 361 | 47.6% |
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
| Black | 271 | 74.7% |
| White | 89 | 24.5% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 835

| Race | Count | % |
|------|-------|---|
| White | 588 | 70.4% |
| Black | 236 | 28.3% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 141

| Race | Count | % |
|------|-------|---|
| Black | 115 | 81.6% |
| White | 25 | 17.7% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 205

| Race | Count | % |
|------|-------|---|
| Black | 148 | 72.2% |
| White | 57 | 27.8% |

### Natchitoches Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| Black | 135 | 73.4% |
| White | 45 | 24.5% |
| Unknown | 4 | 2.2% |

### Oakdale Police Department
**Total:** 5

| Race | Count | % |
|------|-------|---|
| White | 4 | 80.0% |
| Black | 1 | 20.0% |

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
**Total:** 1,330

| Race | Count | % |
|------|-------|---|
| Black | 876 | 65.9% |
| White | 438 | 32.9% |
| Unknown | 16 | 1.2% |

### Plaquemines Parish
**Total:** 657

| Race | Count | % |
|------|-------|---|
| Black | 428 | 65.1% |
| White | 207 | 31.5% |
| Unknown | 13 | 2.0% |
| Asian/PacificIslander | 7 | 1.1% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 71 | 59.2% |
| White | 45 | 37.5% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Rapides Parish
**Total:** 1,039

| Race | Count | % |
|------|-------|---|
| Black | 652 | 62.8% |
| White | 370 | 35.6% |
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
**Total:** 677

| Race | Count | % |
|------|-------|---|
| Black | 467 | 69.0% |
| White | 201 | 29.7% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| White | 110 | 56.1% |
| Black | 83 | 42.3% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 33 | 76.7% |
| White | 9 | 20.9% |
| Unknown | 1 | 2.3% |

### St. Bernard Parish
**Total:** 218

| Race | Count | % |
|------|-------|---|
| Black | 132 | 60.6% |
| White | 82 | 37.6% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| Unknown | 105 | 56.8% |
| White | 80 | 43.2% |

### St. Helena Parish
**Total:** 52

| Race | Count | % |
|------|-------|---|
| Black | 33 | 63.5% |
| White | 17 | 32.7% |
| Unknown | 2 | 3.8% |

### St. James Parish
**Total:** 76

| Race | Count | % |
|------|-------|---|
| Black | 63 | 82.9% |
| White | 13 | 17.1% |

### St. John the Baptist Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Unknown | 134 | 64.7% |
| White | 73 | 35.3% |

### St. Landry Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 89 | 67.9% |
| White | 40 | 30.5% |
| Unknown | 2 | 1.5% |

### St. Martin Parish
**Total:** 221

| Race | Count | % |
|------|-------|---|
| Black | 110 | 49.8% |
| White | 102 | 46.2% |
| Unknown | 8 | 3.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 287

| Race | Count | % |
|------|-------|---|
| Black | 151 | 52.6% |
| White | 135 | 47.0% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 871

| Race | Count | % |
|------|-------|---|
| White | 458 | 52.6% |
| Black | 370 | 42.5% |
| Unknown | 41 | 4.7% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| White | 11 | 84.6% |
| Black | 2 | 15.4% |

### Tangipahoa Parish
**Total:** 695

| Race | Count | % |
|------|-------|---|
| Black | 449 | 64.6% |
| White | 243 | 35.0% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 555

| Race | Count | % |
|------|-------|---|
| Black | 373 | 67.2% |
| White | 170 | 30.6% |
| Unknown | 12 | 2.2% |

### Terrebonne Parish
**Total:** 571

| Race | Count | % |
|------|-------|---|
| Black | 311 | 54.5% |
| White | 248 | 43.4% |
| American Indian/Alaska Native | 11 | 1.9% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| White | 63 | 48.8% |
| Black | 63 | 48.8% |
| Unknown | 2 | 1.6% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 110 | 67.9% |
| Black | 50 | 30.9% |
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
**Total:** 201

| Race | Count | % |
|------|-------|---|
| Black | 102 | 50.7% |
| White | 98 | 48.8% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 474

| Race | Count | % |
|------|-------|---|
| Black | 252 | 53.2% |
| White | 215 | 45.4% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 82 | 64.6% |
| White | 41 | 32.3% |
| Unknown | 2 | 1.6% |
| Asian/PacificIslander | 2 | 1.6% |

### West Carroll Parish
**Total:** 32

| Race | Count | % |
|------|-------|---|
| White | 26 | 81.2% |
| Black | 6 | 18.8% |

### West Felician Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| Black | 128 | 65.0% |
| White | 69 | 35.0% |

### Winn Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| White | 79 | 51.0% |
| Black | 76 | 49.0% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
