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

_Last updated: 2026-07-24 02:16 UTC_

**Total inmates (latest scrape):** 26,859 across 72 parishes/jails

### Acadia Parish
**Total:** 170

| Race | Count | % |
|------|-------|---|
| White | 97 | 57.1% |
| Black | 72 | 42.4% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| White | 75 | 63.6% |
| Black | 39 | 33.1% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 510

| Race | Count | % |
|------|-------|---|
| Black | 266 | 52.2% |
| White | 207 | 40.6% |
| Unknown | 33 | 6.5% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| Unknown | 90 | 57.0% |
| White | 68 | 43.0% |

### Avoyelles Parish
**Total:** 348

| Race | Count | % |
|------|-------|---|
| Black | 195 | 56.0% |
| White | 150 | 43.1% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 175

| Race | Count | % |
|------|-------|---|
| White | 119 | 68.0% |
| Black | 56 | 32.0% |

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
**Total:** 56

| Race | Count | % |
|------|-------|---|
| Black | 37 | 66.1% |
| White | 19 | 33.9% |

### Bossier Parish
**Total:** 1,114

| Race | Count | % |
|------|-------|---|
| Black | 630 | 56.6% |
| White | 482 | 43.3% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,696

| Race | Count | % |
|------|-------|---|
| Black | 1,278 | 75.4% |
| White | 393 | 23.2% |
| Unknown | 25 | 1.5% |

### Calcasieu Parish
**Total:** 1,104

| Race | Count | % |
|------|-------|---|
| Black | 615 | 55.7% |
| White | 447 | 40.5% |
| Unknown | 40 | 3.6% |
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
**Total:** 652

| Race | Count | % |
|------|-------|---|
| Black | 408 | 62.6% |
| White | 244 | 37.4% |

### Concordia Parish
**Total:** 806

| Race | Count | % |
|------|-------|---|
| White | 458 | 56.8% |
| Black | 348 | 43.2% |

### DeSoto Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| Black | 70 | 60.3% |
| White | 45 | 38.8% |
| Asian/PacificIslander | 1 | 0.9% |

### East Baton Rouge Parish
**Total:** 1,373

| Race | Count | % |
|------|-------|---|
| Black | 1,085 | 79.0% |
| White | 226 | 16.5% |
| Unknown | 58 | 4.2% |
| Asian/PacificIslander | 3 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 269

| Race | Count | % |
|------|-------|---|
| Black | 174 | 64.7% |
| White | 93 | 34.6% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| Black | 92 | 59.4% |
| White | 62 | 40.0% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 826

| Race | Count | % |
|------|-------|---|
| Black | 545 | 66.0% |
| White | 275 | 33.3% |
| Unknown | 6 | 0.7% |

### Hammond Police Department
**Total:** 18

| Race | Count | % |
|------|-------|---|
| Black | 10 | 55.6% |
| White | 8 | 44.4% |

### Iberia Parish
**Total:** 467

| Race | Count | % |
|------|-------|---|
| Black | 280 | 60.0% |
| White | 176 | 37.7% |
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
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 84 | 51.5% |
| Black | 76 | 46.6% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,197

| Race | Count | % |
|------|-------|---|
| Black | 762 | 63.7% |
| White | 427 | 35.7% |
| Unknown | 7 | 0.6% |
| Asian/PacificIslander | 1 | 0.1% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| White | 50 | 66.7% |
| Black | 24 | 32.0% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 823

| Race | Count | % |
|------|-------|---|
| Black | 548 | 66.6% |
| White | 262 | 31.8% |
| Unknown | 13 | 1.6% |

### Lafourche Parish
**Total:** 757

| Race | Count | % |
|------|-------|---|
| Black | 394 | 52.0% |
| White | 359 | 47.4% |
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
| Black | 275 | 74.3% |
| White | 92 | 24.9% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 828

| Race | Count | % |
|------|-------|---|
| White | 590 | 71.3% |
| Black | 227 | 27.4% |
| Unknown | 8 | 1.0% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| Black | 116 | 80.6% |
| White | 27 | 18.8% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 204

| Race | Count | % |
|------|-------|---|
| Black | 146 | 71.6% |
| White | 58 | 28.4% |

### Natchitoches Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| Black | 136 | 74.7% |
| White | 43 | 23.6% |
| Unknown | 3 | 1.6% |

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
**Total:** 1,343

| Race | Count | % |
|------|-------|---|
| Black | 894 | 66.6% |
| White | 430 | 32.0% |
| Unknown | 19 | 1.4% |

### Plaquemines Parish
**Total:** 667

| Race | Count | % |
|------|-------|---|
| Black | 435 | 65.2% |
| White | 210 | 31.5% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 8 | 1.2% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| Black | 72 | 60.5% |
| White | 44 | 37.0% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,046

| Race | Count | % |
|------|-------|---|
| Black | 663 | 63.4% |
| White | 364 | 34.8% |
| Unknown | 17 | 1.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| Black | 20 | 51.3% |
| White | 18 | 46.2% |
| Asian/PacificIslander | 1 | 2.6% |

### Richland Parish
**Total:** 684

| Race | Count | % |
|------|-------|---|
| Black | 474 | 69.3% |
| White | 201 | 29.4% |
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
**Total:** 32

| Race | Count | % |
|------|-------|---|
| Black | 25 | 78.1% |
| White | 7 | 21.9% |

### St. Bernard Parish
**Total:** 225

| Race | Count | % |
|------|-------|---|
| Black | 134 | 59.6% |
| White | 87 | 38.7% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| Unknown | 107 | 57.2% |
| White | 80 | 42.8% |

### St. Helena Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 32 | 68.1% |
| White | 15 | 31.9% |

### St. James Parish
**Total:** 71

| Race | Count | % |
|------|-------|---|
| Black | 60 | 84.5% |
| White | 11 | 15.5% |

### St. John the Baptist Parish
**Total:** 209

| Race | Count | % |
|------|-------|---|
| Unknown | 136 | 65.1% |
| White | 73 | 34.9% |

### St. Landry Parish
**Total:** 126

| Race | Count | % |
|------|-------|---|
| Black | 87 | 69.0% |
| White | 37 | 29.4% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 226

| Race | Count | % |
|------|-------|---|
| Black | 112 | 49.6% |
| White | 106 | 46.9% |
| Unknown | 8 | 3.5% |

### St. Mary Parish
**Total:** 288

| Race | Count | % |
|------|-------|---|
| Black | 151 | 52.4% |
| White | 135 | 46.9% |
| Asian/PacificIslander | 1 | 0.3% |
| American Indian/Alaska Native | 1 | 0.3% |

### St. Tammany Parish
**Total:** 887

| Race | Count | % |
|------|-------|---|
| White | 461 | 52.0% |
| Black | 382 | 43.1% |
| Unknown | 42 | 4.7% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| White | 13 | 81.2% |
| Black | 3 | 18.8% |

### Tangipahoa Parish
**Total:** 693

| Race | Count | % |
|------|-------|---|
| Black | 458 | 66.1% |
| White | 232 | 33.5% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 571

| Race | Count | % |
|------|-------|---|
| Black | 386 | 67.6% |
| White | 173 | 30.3% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 578

| Race | Count | % |
|------|-------|---|
| Black | 316 | 54.7% |
| White | 250 | 43.3% |
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
**Total:** 164

| Race | Count | % |
|------|-------|---|
| White | 110 | 67.1% |
| Black | 52 | 31.7% |
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
**Total:** 473

| Race | Count | % |
|------|-------|---|
| Black | 251 | 53.1% |
| White | 213 | 45.0% |
| Unknown | 7 | 1.5% |
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
**Total:** 195

| Race | Count | % |
|------|-------|---|
| Black | 125 | 64.1% |
| White | 70 | 35.9% |

### Winn Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| White | 76 | 50.0% |
| Black | 76 | 50.0% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
