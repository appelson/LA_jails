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

_Last updated: 2026-07-23 02:19 UTC_

**Total inmates (latest scrape):** 26,876 across 72 parishes/jails

### Acadia Parish
**Total:** 169

| Race | Count | % |
|------|-------|---|
| White | 96 | 56.8% |
| Black | 72 | 42.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| White | 76 | 62.8% |
| Black | 41 | 33.9% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 514

| Race | Count | % |
|------|-------|---|
| Black | 270 | 52.5% |
| White | 206 | 40.1% |
| Unknown | 34 | 6.6% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| Unknown | 91 | 56.9% |
| White | 69 | 43.1% |

### Avoyelles Parish
**Total:** 351

| Race | Count | % |
|------|-------|---|
| Black | 197 | 56.1% |
| White | 151 | 43.0% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 170

| Race | Count | % |
|------|-------|---|
| White | 117 | 68.8% |
| Black | 53 | 31.2% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 8 | 53.3% |
| Black | 7 | 46.7% |

### Bossier City Police Department
**Total:** 50

| Race | Count | % |
|------|-------|---|
| Black | 33 | 66.0% |
| White | 16 | 32.0% |
| Asian/PacificIslander | 1 | 2.0% |

### Bossier Parish
**Total:** 1,109

| Race | Count | % |
|------|-------|---|
| Black | 630 | 56.8% |
| White | 478 | 43.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,702

| Race | Count | % |
|------|-------|---|
| Black | 1,281 | 75.3% |
| White | 395 | 23.2% |
| Unknown | 25 | 1.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,104

| Race | Count | % |
|------|-------|---|
| Black | 616 | 55.8% |
| White | 444 | 40.2% |
| Unknown | 42 | 3.8% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 613

| Race | Count | % |
|------|-------|---|
| Black | 387 | 63.1% |
| White | 211 | 34.4% |
| American Indian/Alaska Native | 15 | 2.4% |

### Cameron Parish
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 18 | 100.0% |

### Catahoula Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 92 | 71.3% |
| White | 36 | 27.9% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 650

| Race | Count | % |
|------|-------|---|
| Black | 403 | 62.0% |
| White | 247 | 38.0% |

### Concordia Parish
**Total:** 808

| Race | Count | % |
|------|-------|---|
| White | 460 | 56.9% |
| Black | 348 | 43.1% |

### DeSoto Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| Black | 71 | 61.2% |
| White | 44 | 37.9% |
| Asian/PacificIslander | 1 | 0.9% |

### East Baton Rouge Parish
**Total:** 1,350

| Race | Count | % |
|------|-------|---|
| Black | 1,066 | 79.0% |
| White | 222 | 16.4% |
| Unknown | 58 | 4.3% |
| Asian/PacificIslander | 3 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 269

| Race | Count | % |
|------|-------|---|
| Black | 172 | 63.9% |
| White | 95 | 35.3% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| Black | 89 | 57.8% |
| White | 64 | 41.6% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 832

| Race | Count | % |
|------|-------|---|
| Black | 548 | 65.9% |
| White | 278 | 33.4% |
| Unknown | 6 | 0.7% |

### Hammond Police Department
**Total:** 24

| Race | Count | % |
|------|-------|---|
| Black | 14 | 58.3% |
| White | 10 | 41.7% |

### Iberia Parish
**Total:** 465

| Race | Count | % |
|------|-------|---|
| Black | 277 | 59.6% |
| White | 177 | 38.1% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 26 | 60.5% |
| White | 17 | 39.5% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| White | 83 | 51.9% |
| Black | 74 | 46.2% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,216

| Race | Count | % |
|------|-------|---|
| Black | 780 | 64.1% |
| White | 429 | 35.3% |
| Unknown | 6 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| White | 53 | 67.9% |
| Black | 24 | 30.8% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 827

| Race | Count | % |
|------|-------|---|
| Black | 551 | 66.6% |
| White | 262 | 31.7% |
| Unknown | 14 | 1.7% |

### Lafourche Parish
**Total:** 755

| Race | Count | % |
|------|-------|---|
| Black | 395 | 52.3% |
| White | 356 | 47.2% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 365

| Race | Count | % |
|------|-------|---|
| Black | 272 | 74.5% |
| White | 90 | 24.7% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 830

| Race | Count | % |
|------|-------|---|
| White | 590 | 71.1% |
| Black | 229 | 27.6% |
| Unknown | 8 | 1.0% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| Black | 117 | 80.7% |
| White | 27 | 18.6% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 205

| Race | Count | % |
|------|-------|---|
| Black | 147 | 71.7% |
| White | 58 | 28.3% |

### Natchitoches Parish
**Total:** 180

| Race | Count | % |
|------|-------|---|
| Black | 136 | 75.6% |
| White | 41 | 22.8% |
| Unknown | 3 | 1.7% |

### Oakdale Police Department
**Total:** 4

| Race | Count | % |
|------|-------|---|
| White | 4 | 100.0% |

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
**Total:** 1,357

| Race | Count | % |
|------|-------|---|
| Black | 906 | 66.8% |
| White | 433 | 31.9% |
| Unknown | 18 | 1.3% |

### Plaquemines Parish
**Total:** 666

| Race | Count | % |
|------|-------|---|
| Black | 434 | 65.2% |
| White | 211 | 31.7% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 7 | 1.1% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 72 | 61.0% |
| White | 43 | 36.4% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,059

| Race | Count | % |
|------|-------|---|
| Black | 666 | 62.9% |
| White | 374 | 35.3% |
| Unknown | 17 | 1.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 40

| Race | Count | % |
|------|-------|---|
| Black | 20 | 50.0% |
| White | 19 | 47.5% |
| Asian/PacificIslander | 1 | 2.5% |

### Richland Parish
**Total:** 673

| Race | Count | % |
|------|-------|---|
| Black | 468 | 69.5% |
| White | 196 | 29.1% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| White | 109 | 55.6% |
| Black | 84 | 42.9% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 34

| Race | Count | % |
|------|-------|---|
| Black | 27 | 79.4% |
| White | 7 | 20.6% |

### St. Bernard Parish
**Total:** 228

| Race | Count | % |
|------|-------|---|
| Black | 138 | 60.5% |
| White | 86 | 37.7% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| Unknown | 107 | 57.8% |
| White | 78 | 42.2% |

### St. Helena Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 32 | 68.1% |
| White | 15 | 31.9% |

### St. James Parish
**Total:** 72

| Race | Count | % |
|------|-------|---|
| Black | 60 | 83.3% |
| White | 12 | 16.7% |

### St. John the Baptist Parish
**Total:** 205

| Race | Count | % |
|------|-------|---|
| Unknown | 136 | 66.3% |
| White | 69 | 33.7% |

### St. Landry Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 83 | 66.9% |
| White | 38 | 30.6% |
| Unknown | 3 | 2.4% |

### St. Martin Parish
**Total:** 225

| Race | Count | % |
|------|-------|---|
| Black | 111 | 49.3% |
| White | 105 | 46.7% |
| Unknown | 8 | 3.6% |
| American Indian/Alaska Native | 1 | 0.4% |

### St. Mary Parish
**Total:** 287

| Race | Count | % |
|------|-------|---|
| Black | 151 | 52.6% |
| White | 134 | 46.7% |
| Asian/PacificIslander | 1 | 0.3% |
| American Indian/Alaska Native | 1 | 0.3% |

### St. Tammany Parish
**Total:** 886

| Race | Count | % |
|------|-------|---|
| White | 460 | 51.9% |
| Black | 381 | 43.0% |
| Unknown | 43 | 4.9% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 12

| Race | Count | % |
|------|-------|---|
| White | 10 | 83.3% |
| Black | 2 | 16.7% |

### Tangipahoa Parish
**Total:** 686

| Race | Count | % |
|------|-------|---|
| Black | 451 | 65.7% |
| White | 232 | 33.8% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 573

| Race | Count | % |
|------|-------|---|
| Black | 387 | 67.5% |
| White | 174 | 30.4% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 573

| Race | Count | % |
|------|-------|---|
| Black | 315 | 55.0% |
| White | 246 | 42.9% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| White | 59 | 49.6% |
| Black | 57 | 47.9% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 110 | 67.5% |
| Black | 51 | 31.3% |
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
**Total:** 206

| Race | Count | % |
|------|-------|---|
| Black | 111 | 53.9% |
| White | 94 | 45.6% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 473

| Race | Count | % |
|------|-------|---|
| Black | 253 | 53.5% |
| White | 212 | 44.8% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 3 | 0.6% |

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
**Total:** 194

| Race | Count | % |
|------|-------|---|
| Black | 124 | 63.9% |
| White | 70 | 36.1% |

### Winn Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Black | 76 | 50.3% |
| White | 75 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
