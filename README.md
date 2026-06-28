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

_Last updated: 2026-06-28 03:01 UTC_

**Total inmates (latest scrape):** 26,602 across 72 parishes/jails

### Acadia Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| White | 102 | 54.5% |
| Black | 83 | 44.4% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| White | 70 | 62.5% |
| Black | 39 | 34.8% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 523

| Race | Count | % |
|------|-------|---|
| Black | 277 | 53.0% |
| White | 213 | 40.7% |
| Unknown | 29 | 5.5% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 150

| Race | Count | % |
|------|-------|---|
| Unknown | 83 | 55.3% |
| White | 67 | 44.7% |

### Avoyelles Parish
**Total:** 352

| Race | Count | % |
|------|-------|---|
| Black | 193 | 54.8% |
| White | 155 | 44.0% |
| Unknown | 3 | 0.9% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| White | 101 | 69.2% |
| Black | 45 | 30.8% |

### Bienville Parish
**Total:** 45

| Race | Count | % |
|------|-------|---|
| White | 26 | 57.8% |
| Unknown | 19 | 42.2% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 29 | 65.9% |
| White | 15 | 34.1% |

### Bossier Parish
**Total:** 1,116

| Race | Count | % |
|------|-------|---|
| Black | 621 | 55.6% |
| White | 494 | 44.3% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,698

| Race | Count | % |
|------|-------|---|
| Black | 1,276 | 75.1% |
| White | 393 | 23.1% |
| Unknown | 27 | 1.6% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,098

| Race | Count | % |
|------|-------|---|
| Black | 617 | 56.2% |
| White | 440 | 40.1% |
| Unknown | 38 | 3.5% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 623

| Race | Count | % |
|------|-------|---|
| Black | 392 | 62.9% |
| White | 210 | 33.7% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 18 | 94.7% |
| Black | 1 | 5.3% |

### Catahoula Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.2% |
| White | 40 | 30.1% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 681

| Race | Count | % |
|------|-------|---|
| Black | 420 | 61.7% |
| White | 261 | 38.3% |

### Concordia Parish
**Total:** 808

| Race | Count | % |
|------|-------|---|
| White | 454 | 56.2% |
| Black | 353 | 43.7% |
| Unknown | 1 | 0.1% |

### DeSoto Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 70 | 58.3% |
| White | 49 | 40.8% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,301

| Race | Count | % |
|------|-------|---|
| Black | 1,030 | 79.2% |
| White | 204 | 15.7% |
| Unknown | 65 | 5.0% |
| Asian/PacificIslander | 2 | 0.2% |

### East Feliciana Parish
**Total:** 273

| Race | Count | % |
|------|-------|---|
| Black | 174 | 63.7% |
| White | 98 | 35.9% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| Black | 92 | 56.8% |
| White | 69 | 42.6% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 845

| Race | Count | % |
|------|-------|---|
| Black | 556 | 65.8% |
| White | 279 | 33.0% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| Black | 10 | 66.7% |
| White | 4 | 26.7% |
| Unknown | 1 | 6.7% |

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
**Total:** 34

| Race | Count | % |
|------|-------|---|
| Black | 18 | 52.9% |
| White | 16 | 47.1% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| White | 86 | 52.4% |
| Black | 74 | 45.1% |
| American Indian/Alaska Native | 3 | 1.8% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,119

| Race | Count | % |
|------|-------|---|
| Black | 718 | 64.2% |
| White | 395 | 35.3% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| White | 2 | 100.0% |

### LaSalle Parish
**Total:** 72

| Race | Count | % |
|------|-------|---|
| White | 47 | 65.3% |
| Black | 24 | 33.3% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 833

| Race | Count | % |
|------|-------|---|
| Black | 537 | 64.5% |
| White | 281 | 33.7% |
| Unknown | 14 | 1.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 749

| Race | Count | % |
|------|-------|---|
| Black | 383 | 51.1% |
| White | 361 | 48.2% |
| American Indian/Alaska Native | 4 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 368

| Race | Count | % |
|------|-------|---|
| Black | 275 | 74.7% |
| White | 90 | 24.5% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 826

| Race | Count | % |
|------|-------|---|
| White | 588 | 71.2% |
| Black | 227 | 27.5% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 141

| Race | Count | % |
|------|-------|---|
| Black | 112 | 79.4% |
| White | 28 | 19.9% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 210

| Race | Count | % |
|------|-------|---|
| Black | 149 | 71.0% |
| White | 61 | 29.0% |

### Natchitoches Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| Black | 143 | 74.1% |
| White | 47 | 24.4% |
| Unknown | 3 | 1.6% |

### Oakdale Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

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
**Total:** 1,292

| Race | Count | % |
|------|-------|---|
| Black | 865 | 67.0% |
| White | 414 | 32.0% |
| Unknown | 13 | 1.0% |

### Plaquemines Parish
**Total:** 670

| Race | Count | % |
|------|-------|---|
| Black | 436 | 65.1% |
| White | 208 | 31.0% |
| Unknown | 16 | 2.4% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 3 | 0.4% |

### Pointe Coupee Parish
**Total:** 109

| Race | Count | % |
|------|-------|---|
| Black | 66 | 60.6% |
| White | 40 | 36.7% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,036

| Race | Count | % |
|------|-------|---|
| Black | 657 | 63.4% |
| White | 362 | 34.9% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 26 | 56.5% |
| White | 19 | 41.3% |
| Asian/PacificIslander | 1 | 2.2% |

### Richland Parish
**Total:** 716

| Race | Count | % |
|------|-------|---|
| Black | 495 | 69.1% |
| White | 211 | 29.5% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 189

| Race | Count | % |
|------|-------|---|
| White | 105 | 55.6% |
| Black | 81 | 42.9% |
| Unknown | 2 | 1.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 68

| Race | Count | % |
|------|-------|---|
| Black | 46 | 67.6% |
| White | 22 | 32.4% |

### St. Bernard Parish
**Total:** 218

| Race | Count | % |
|------|-------|---|
| Black | 127 | 58.3% |
| White | 88 | 40.4% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 186

| Race | Count | % |
|------|-------|---|
| Unknown | 113 | 60.8% |
| White | 73 | 39.2% |

### St. Helena Parish
**Total:** 50

| Race | Count | % |
|------|-------|---|
| Black | 35 | 70.0% |
| White | 14 | 28.0% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 64

| Race | Count | % |
|------|-------|---|
| Black | 54 | 84.4% |
| White | 10 | 15.6% |

### St. John the Baptist Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| Unknown | 129 | 65.8% |
| White | 67 | 34.2% |

### St. Landry Parish
**Total:** 126

| Race | Count | % |
|------|-------|---|
| Black | 81 | 64.3% |
| White | 43 | 34.1% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 220

| Race | Count | % |
|------|-------|---|
| Black | 113 | 51.4% |
| White | 97 | 44.1% |
| Unknown | 9 | 4.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 296

| Race | Count | % |
|------|-------|---|
| Black | 154 | 52.0% |
| White | 141 | 47.6% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 869

| Race | Count | % |
|------|-------|---|
| White | 465 | 53.5% |
| Black | 364 | 41.9% |
| Unknown | 37 | 4.3% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 15 | 88.2% |
| Black | 2 | 11.8% |

### Tangipahoa Parish
**Total:** 669

| Race | Count | % |
|------|-------|---|
| Black | 427 | 63.8% |
| White | 241 | 36.0% |
| Unknown | 1 | 0.1% |

### Tensas Parish
**Total:** 570

| Race | Count | % |
|------|-------|---|
| Black | 380 | 66.7% |
| White | 180 | 31.6% |
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
**Total:** 133

| Race | Count | % |
|------|-------|---|
| White | 69 | 51.9% |
| Black | 61 | 45.9% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| White | 116 | 69.0% |
| Black | 49 | 29.2% |
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
| White | 100 | 52.4% |
| Black | 91 | 47.6% |

### Webster Parish
**Total:** 444

| Race | Count | % |
|------|-------|---|
| Black | 235 | 52.9% |
| White | 203 | 45.7% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| Black | 83 | 68.0% |
| White | 35 | 28.7% |
| Unknown | 3 | 2.5% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 31

| Race | Count | % |
|------|-------|---|
| White | 25 | 80.6% |
| Black | 6 | 19.4% |

### West Felician Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| Black | 125 | 64.8% |
| White | 68 | 35.2% |

### Winn Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Black | 74 | 51.7% |
| White | 69 | 48.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
