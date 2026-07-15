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

_Last updated: 2026-07-15 02:01 UTC_

**Total inmates (latest scrape):** 26,827 across 72 parishes/jails

### Acadia Parish
**Total:** 174

| Race | Count | % |
|------|-------|---|
| White | 102 | 58.6% |
| Black | 71 | 40.8% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| White | 77 | 64.7% |
| Black | 39 | 32.8% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.8% |

### Ascension Parish
**Total:** 523

| Race | Count | % |
|------|-------|---|
| Black | 274 | 52.4% |
| White | 213 | 40.7% |
| Unknown | 32 | 6.1% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| Unknown | 88 | 56.8% |
| White | 67 | 43.2% |

### Avoyelles Parish
**Total:** 353

| Race | Count | % |
|------|-------|---|
| Black | 194 | 55.0% |
| White | 155 | 43.9% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 161

| Race | Count | % |
|------|-------|---|
| White | 115 | 71.4% |
| Black | 46 | 28.6% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 28

| Race | Count | % |
|------|-------|---|
| White | 17 | 60.7% |
| Black | 11 | 39.3% |

### Bossier City Police Department
**Total:** 39

| Race | Count | % |
|------|-------|---|
| Black | 23 | 59.0% |
| White | 16 | 41.0% |

### Bossier Parish
**Total:** 1,129

| Race | Count | % |
|------|-------|---|
| Black | 630 | 55.8% |
| White | 498 | 44.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,701

| Race | Count | % |
|------|-------|---|
| Black | 1,286 | 75.6% |
| White | 388 | 22.8% |
| Unknown | 26 | 1.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,106

| Race | Count | % |
|------|-------|---|
| Black | 616 | 55.7% |
| White | 445 | 40.2% |
| Unknown | 42 | 3.8% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 601

| Race | Count | % |
|------|-------|---|
| Black | 376 | 62.6% |
| White | 207 | 34.4% |
| American Indian/Alaska Native | 17 | 2.8% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 15 | 88.2% |
| Black | 2 | 11.8% |

### Catahoula Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 91 | 70.5% |
| White | 37 | 28.7% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 659

| Race | Count | % |
|------|-------|---|
| Black | 410 | 62.2% |
| White | 249 | 37.8% |

### Concordia Parish
**Total:** 829

| Race | Count | % |
|------|-------|---|
| White | 464 | 56.0% |
| Black | 365 | 44.0% |

### DeSoto Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 73 | 58.9% |
| White | 50 | 40.3% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,329

| Race | Count | % |
|------|-------|---|
| Black | 1,052 | 79.2% |
| White | 213 | 16.0% |
| Unknown | 61 | 4.6% |
| Asian/PacificIslander | 3 | 0.2% |

### East Feliciana Parish
**Total:** 269

| Race | Count | % |
|------|-------|---|
| Black | 172 | 63.9% |
| White | 95 | 35.3% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| Black | 94 | 57.0% |
| White | 70 | 42.4% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 841

| Race | Count | % |
|------|-------|---|
| Black | 551 | 65.5% |
| White | 277 | 32.9% |
| Unknown | 13 | 1.5% |

### Hammond Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| Black | 9 | 52.9% |
| White | 8 | 47.1% |

### Iberia Parish
**Total:** 462

| Race | Count | % |
|------|-------|---|
| Black | 272 | 58.9% |
| White | 180 | 39.0% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 36

| Race | Count | % |
|------|-------|---|
| Black | 19 | 52.8% |
| White | 17 | 47.2% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 86 | 53.1% |
| Black | 73 | 45.1% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,169

| Race | Count | % |
|------|-------|---|
| Black | 758 | 64.8% |
| White | 405 | 34.6% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 1 | 50.0% |
| White | 1 | 50.0% |

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
| Black | 540 | 66.3% |
| White | 259 | 31.8% |
| Unknown | 16 | 2.0% |

### Lafourche Parish
**Total:** 756

| Race | Count | % |
|------|-------|---|
| Black | 393 | 52.0% |
| White | 359 | 47.5% |
| American Indian/Alaska Native | 3 | 0.4% |
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
| Black | 273 | 74.0% |
| White | 93 | 25.2% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 836

| Race | Count | % |
|------|-------|---|
| White | 588 | 70.3% |
| Black | 237 | 28.3% |
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
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 154 | 72.0% |
| White | 60 | 28.0% |

### Natchitoches Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Black | 138 | 75.4% |
| White | 41 | 22.4% |
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
**Total:** 1,347

| Race | Count | % |
|------|-------|---|
| Black | 892 | 66.2% |
| White | 440 | 32.7% |
| Unknown | 15 | 1.1% |

### Plaquemines Parish
**Total:** 664

| Race | Count | % |
|------|-------|---|
| Black | 436 | 65.7% |
| White | 206 | 31.0% |
| Unknown | 14 | 2.1% |
| Asian/PacificIslander | 7 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Pointe Coupee Parish
**Total:** 115

| Race | Count | % |
|------|-------|---|
| Black | 69 | 60.0% |
| White | 43 | 37.4% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,038

| Race | Count | % |
|------|-------|---|
| Black | 654 | 63.0% |
| White | 367 | 35.4% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 42

| Race | Count | % |
|------|-------|---|
| Black | 21 | 50.0% |
| White | 20 | 47.6% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 686

| Race | Count | % |
|------|-------|---|
| Black | 474 | 69.1% |
| White | 202 | 29.4% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| White | 109 | 55.6% |
| Black | 84 | 42.9% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 33 | 75.0% |
| White | 10 | 22.7% |
| Unknown | 1 | 2.3% |

### St. Bernard Parish
**Total:** 220

| Race | Count | % |
|------|-------|---|
| Black | 132 | 60.0% |
| White | 84 | 38.2% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| Unknown | 110 | 59.5% |
| White | 75 | 40.5% |

### St. Helena Parish
**Total:** 52

| Race | Count | % |
|------|-------|---|
| Black | 34 | 65.4% |
| White | 16 | 30.8% |
| Unknown | 2 | 3.8% |

### St. James Parish
**Total:** 74

| Race | Count | % |
|------|-------|---|
| Black | 61 | 82.4% |
| White | 13 | 17.6% |

### St. John the Baptist Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Unknown | 136 | 65.7% |
| White | 71 | 34.3% |

### St. Landry Parish
**Total:** 126

| Race | Count | % |
|------|-------|---|
| Black | 85 | 67.5% |
| White | 39 | 31.0% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 223

| Race | Count | % |
|------|-------|---|
| Black | 112 | 50.2% |
| White | 102 | 45.7% |
| Unknown | 8 | 3.6% |
| American Indian/Alaska Native | 1 | 0.4% |

### St. Mary Parish
**Total:** 294

| Race | Count | % |
|------|-------|---|
| Black | 152 | 51.7% |
| White | 141 | 48.0% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 868

| Race | Count | % |
|------|-------|---|
| White | 452 | 52.1% |
| Black | 374 | 43.1% |
| Unknown | 40 | 4.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| White | 14 | 87.5% |
| Black | 2 | 12.5% |

### Tangipahoa Parish
**Total:** 689

| Race | Count | % |
|------|-------|---|
| Black | 449 | 65.2% |
| White | 237 | 34.4% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 550

| Race | Count | % |
|------|-------|---|
| Black | 371 | 67.5% |
| White | 167 | 30.4% |
| Unknown | 12 | 2.2% |

### Terrebonne Parish
**Total:** 566

| Race | Count | % |
|------|-------|---|
| Black | 309 | 54.6% |
| White | 246 | 43.5% |
| American Indian/Alaska Native | 10 | 1.8% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 66 | 49.3% |
| White | 65 | 48.5% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.7% |

### Vernon Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 111 | 68.1% |
| Black | 50 | 30.7% |
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
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Black | 104 | 52.0% |
| White | 96 | 48.0% |

### Webster Parish
**Total:** 464

| Race | Count | % |
|------|-------|---|
| Black | 251 | 54.1% |
| White | 207 | 44.6% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 83 | 65.4% |
| White | 40 | 31.5% |
| Unknown | 2 | 1.6% |
| Asian/PacificIslander | 2 | 1.6% |

### West Carroll Parish
**Total:** 33

| Race | Count | % |
|------|-------|---|
| White | 27 | 81.8% |
| Black | 6 | 18.2% |

### West Felician Parish
**Total:** 198

| Race | Count | % |
|------|-------|---|
| Black | 127 | 64.1% |
| White | 71 | 35.9% |

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
