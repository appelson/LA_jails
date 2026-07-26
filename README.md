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

_Last updated: 2026-07-26 02:20 UTC_

**Total inmates (latest scrape):** 26,897 across 72 parishes/jails

### Acadia Parish
**Total:** 169

| Race | Count | % |
|------|-------|---|
| White | 97 | 57.4% |
| Black | 71 | 42.0% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| White | 75 | 63.0% |
| Black | 40 | 33.6% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 503

| Race | Count | % |
|------|-------|---|
| Black | 264 | 52.5% |
| White | 203 | 40.4% |
| Unknown | 32 | 6.4% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| Unknown | 90 | 56.6% |
| White | 69 | 43.4% |

### Avoyelles Parish
**Total:** 350

| Race | Count | % |
|------|-------|---|
| Black | 196 | 56.0% |
| White | 151 | 43.1% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 171

| Race | Count | % |
|------|-------|---|
| White | 115 | 67.3% |
| Black | 55 | 32.2% |
| Unknown | 1 | 0.6% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 9 | 52.9% |
| Black | 8 | 47.1% |

### Bossier City Police Department
**Total:** 59

| Race | Count | % |
|------|-------|---|
| Black | 41 | 69.5% |
| White | 18 | 30.5% |

### Bossier Parish
**Total:** 1,128

| Race | Count | % |
|------|-------|---|
| Black | 640 | 56.7% |
| White | 486 | 43.1% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,705

| Race | Count | % |
|------|-------|---|
| Black | 1,285 | 75.4% |
| White | 394 | 23.1% |
| Unknown | 26 | 1.5% |

### Calcasieu Parish
**Total:** 1,112

| Race | Count | % |
|------|-------|---|
| Black | 621 | 55.8% |
| White | 449 | 40.4% |
| Unknown | 41 | 3.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 609

| Race | Count | % |
|------|-------|---|
| Black | 385 | 63.2% |
| White | 208 | 34.2% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 18 | 94.7% |
| Black | 1 | 5.3% |

### Catahoula Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 91 | 70.5% |
| White | 37 | 28.7% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 665

| Race | Count | % |
|------|-------|---|
| Black | 414 | 62.3% |
| White | 251 | 37.7% |

### Concordia Parish
**Total:** 808

| Race | Count | % |
|------|-------|---|
| White | 455 | 56.3% |
| Black | 353 | 43.7% |

### DeSoto Parish
**Total:** 115

| Race | Count | % |
|------|-------|---|
| Black | 72 | 62.6% |
| White | 42 | 36.5% |
| Asian/PacificIslander | 1 | 0.9% |

### East Baton Rouge Parish
**Total:** 1,324

| Race | Count | % |
|------|-------|---|
| Black | 1,036 | 78.2% |
| White | 226 | 17.1% |
| Unknown | 58 | 4.4% |
| Asian/PacificIslander | 3 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 275

| Race | Count | % |
|------|-------|---|
| Black | 177 | 64.4% |
| White | 96 | 34.9% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Black | 87 | 57.6% |
| White | 63 | 41.7% |
| Unknown | 1 | 0.7% |

### Franklin Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| Black | 546 | 66.2% |
| White | 274 | 33.2% |
| Unknown | 5 | 0.6% |

### Hammond Police Department
**Total:** 22

| Race | Count | % |
|------|-------|---|
| Black | 14 | 63.6% |
| White | 8 | 36.4% |

### Iberia Parish
**Total:** 468

| Race | Count | % |
|------|-------|---|
| Black | 281 | 60.0% |
| White | 176 | 37.6% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 29 | 61.7% |
| White | 18 | 38.3% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 84 | 50.9% |
| Black | 77 | 46.7% |
| Unknown | 2 | 1.2% |
| American Indian/Alaska Native | 2 | 1.2% |

### Jefferson Parish
**Total:** 1,198

| Race | Count | % |
|------|-------|---|
| Black | 770 | 64.3% |
| White | 422 | 35.2% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 1 | 50.0% |
| White | 1 | 50.0% |

### LaSalle Parish
**Total:** 77

| Race | Count | % |
|------|-------|---|
| White | 53 | 68.8% |
| Black | 23 | 29.9% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 821

| Race | Count | % |
|------|-------|---|
| Black | 545 | 66.4% |
| White | 264 | 32.2% |
| Unknown | 12 | 1.5% |

### Lafourche Parish
**Total:** 763

| Race | Count | % |
|------|-------|---|
| Black | 392 | 51.4% |
| White | 367 | 48.1% |
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
| Black | 274 | 74.1% |
| White | 93 | 25.1% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 827

| Race | Count | % |
|------|-------|---|
| White | 593 | 71.7% |
| Black | 223 | 27.0% |
| Unknown | 8 | 1.0% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 149

| Race | Count | % |
|------|-------|---|
| Black | 119 | 79.9% |
| White | 29 | 19.5% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 208

| Race | Count | % |
|------|-------|---|
| Black | 151 | 72.6% |
| White | 57 | 27.4% |

### Natchitoches Parish
**Total:** 180

| Race | Count | % |
|------|-------|---|
| Black | 136 | 75.6% |
| White | 41 | 22.8% |
| Unknown | 3 | 1.7% |

### Oakdale Police Department
**Total:** 6

| Race | Count | % |
|------|-------|---|
| White | 6 | 100.0% |

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
**Total:** 1,364

| Race | Count | % |
|------|-------|---|
| Black | 908 | 66.6% |
| White | 438 | 32.1% |
| Unknown | 18 | 1.3% |

### Plaquemines Parish
**Total:** 663

| Race | Count | % |
|------|-------|---|
| Black | 433 | 65.3% |
| White | 207 | 31.2% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 9 | 1.4% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| Black | 74 | 62.2% |
| White | 42 | 35.3% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,053

| Race | Count | % |
|------|-------|---|
| Black | 673 | 63.9% |
| White | 363 | 34.5% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| White | 20 | 48.8% |
| Black | 20 | 48.8% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 685

| Race | Count | % |
|------|-------|---|
| Black | 475 | 69.3% |
| White | 200 | 29.2% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| White | 108 | 56.2% |
| Black | 81 | 42.2% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 35

| Race | Count | % |
|------|-------|---|
| Black | 26 | 74.3% |
| White | 9 | 25.7% |

### St. Bernard Parish
**Total:** 222

| Race | Count | % |
|------|-------|---|
| Black | 129 | 58.1% |
| White | 89 | 40.1% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| Unknown | 109 | 58.9% |
| White | 76 | 41.1% |

### St. Helena Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 31 | 66.0% |
| White | 16 | 34.0% |

### St. James Parish
**Total:** 71

| Race | Count | % |
|------|-------|---|
| Black | 60 | 84.5% |
| White | 11 | 15.5% |

### St. John the Baptist Parish
**Total:** 217

| Race | Count | % |
|------|-------|---|
| Unknown | 143 | 65.9% |
| White | 74 | 34.1% |

### St. Landry Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 88 | 69.3% |
| White | 37 | 29.1% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 107 | 50.0% |
| White | 99 | 46.3% |
| Unknown | 8 | 3.7% |

### St. Mary Parish
**Total:** 289

| Race | Count | % |
|------|-------|---|
| Black | 156 | 54.0% |
| White | 131 | 45.3% |
| Asian/PacificIslander | 1 | 0.3% |
| American Indian/Alaska Native | 1 | 0.3% |

### St. Tammany Parish
**Total:** 880

| Race | Count | % |
|------|-------|---|
| White | 454 | 51.6% |
| Black | 381 | 43.3% |
| Unknown | 43 | 4.9% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 14 | 82.4% |
| Black | 3 | 17.6% |

### Tangipahoa Parish
**Total:** 709

| Race | Count | % |
|------|-------|---|
| Black | 467 | 65.9% |
| White | 239 | 33.7% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 566

| Race | Count | % |
|------|-------|---|
| Black | 384 | 67.8% |
| White | 170 | 30.0% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 579

| Race | Count | % |
|------|-------|---|
| Black | 314 | 54.2% |
| White | 253 | 43.7% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| White | 58 | 50.0% |
| Black | 55 | 47.4% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.9% |

### Vernon Parish
**Total:** 173

| Race | Count | % |
|------|-------|---|
| White | 117 | 67.6% |
| Black | 54 | 31.2% |
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
| Black | 97 | 52.7% |
| White | 86 | 46.7% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 462

| Race | Count | % |
|------|-------|---|
| Black | 247 | 53.5% |
| White | 208 | 45.0% |
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
**Total:** 28

| Race | Count | % |
|------|-------|---|
| White | 22 | 78.6% |
| Black | 6 | 21.4% |

### West Felician Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| Black | 126 | 64.0% |
| White | 71 | 36.0% |

### Winn Parish
**Total:** 153

| Race | Count | % |
|------|-------|---|
| White | 77 | 50.3% |
| Black | 76 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
