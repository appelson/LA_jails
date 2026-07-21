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

_Last updated: 2026-07-21 02:14 UTC_

**Total inmates (latest scrape):** 26,929 across 72 parishes/jails

### Acadia Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| White | 93 | 56.0% |
| Black | 72 | 43.4% |
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
**Total:** 511

| Race | Count | % |
|------|-------|---|
| Black | 272 | 53.2% |
| White | 203 | 39.7% |
| Unknown | 32 | 6.3% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| Unknown | 90 | 56.2% |
| White | 70 | 43.8% |

### Avoyelles Parish
**Total:** 355

| Race | Count | % |
|------|-------|---|
| Black | 198 | 55.8% |
| White | 154 | 43.4% |
| Unknown | 3 | 0.8% |

### Beauregard Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 116 | 70.3% |
| Black | 49 | 29.7% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| White | 15 | 65.2% |
| Black | 8 | 34.8% |

### Bossier City Police Department
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 26 | 56.5% |
| White | 20 | 43.5% |

### Bossier Parish
**Total:** 1,113

| Race | Count | % |
|------|-------|---|
| Black | 624 | 56.1% |
| White | 487 | 43.8% |
| American Indian/Alaska Native | 1 | 0.1% |
| Unknown | 1 | 0.1% |

### Caddo Parish
**Total:** 1,729

| Race | Count | % |
|------|-------|---|
| Black | 1,305 | 75.5% |
| White | 398 | 23.0% |
| Unknown | 25 | 1.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,104

| Race | Count | % |
|------|-------|---|
| Black | 614 | 55.6% |
| White | 446 | 40.4% |
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
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 17 | 100.0% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 93 | 71.0% |
| White | 37 | 28.2% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 648

| Race | Count | % |
|------|-------|---|
| Black | 401 | 61.9% |
| White | 247 | 38.1% |

### Concordia Parish
**Total:** 823

| Race | Count | % |
|------|-------|---|
| White | 463 | 56.3% |
| Black | 360 | 43.7% |

### DeSoto Parish
**Total:** 115

| Race | Count | % |
|------|-------|---|
| Black | 71 | 61.7% |
| White | 43 | 37.4% |
| Asian/PacificIslander | 1 | 0.9% |

### East Baton Rouge Parish
**Total:** 1,349

| Race | Count | % |
|------|-------|---|
| Black | 1,064 | 78.9% |
| White | 220 | 16.3% |
| Unknown | 61 | 4.5% |
| Asian/PacificIslander | 3 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 271

| Race | Count | % |
|------|-------|---|
| Black | 173 | 63.8% |
| White | 96 | 35.4% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| Black | 89 | 57.8% |
| White | 64 | 41.6% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 836

| Race | Count | % |
|------|-------|---|
| Black | 550 | 65.8% |
| White | 280 | 33.5% |
| Unknown | 6 | 0.7% |

### Hammond Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 15 | 65.2% |
| White | 8 | 34.8% |

### Iberia Parish
**Total:** 464

| Race | Count | % |
|------|-------|---|
| Black | 278 | 59.9% |
| White | 175 | 37.7% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 40

| Race | Count | % |
|------|-------|---|
| Black | 23 | 57.5% |
| White | 17 | 42.5% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 85 | 52.5% |
| Black | 74 | 45.7% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,201

| Race | Count | % |
|------|-------|---|
| Black | 767 | 63.9% |
| White | 427 | 35.6% |
| Unknown | 6 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 77

| Race | Count | % |
|------|-------|---|
| White | 52 | 67.5% |
| Black | 24 | 31.2% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 832

| Race | Count | % |
|------|-------|---|
| Black | 551 | 66.2% |
| White | 267 | 32.1% |
| Unknown | 14 | 1.7% |

### Lafourche Parish
**Total:** 760

| Race | Count | % |
|------|-------|---|
| Black | 398 | 52.4% |
| White | 358 | 47.1% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 367

| Race | Count | % |
|------|-------|---|
| Black | 273 | 74.4% |
| White | 91 | 24.8% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 828

| Race | Count | % |
|------|-------|---|
| White | 583 | 70.4% |
| Black | 234 | 28.3% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| Black | 116 | 80.6% |
| White | 27 | 18.8% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 208

| Race | Count | % |
|------|-------|---|
| Black | 150 | 72.1% |
| White | 58 | 27.9% |

### Natchitoches Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| Black | 140 | 74.9% |
| White | 43 | 23.0% |
| Unknown | 4 | 2.1% |

### Oakdale Police Department
**Total:** 5

| Race | Count | % |
|------|-------|---|
| White | 4 | 80.0% |
| Unknown | 1 | 20.0% |

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
**Total:** 1,362

| Race | Count | % |
|------|-------|---|
| Black | 904 | 66.4% |
| White | 440 | 32.3% |
| Unknown | 18 | 1.3% |

### Plaquemines Parish
**Total:** 668

| Race | Count | % |
|------|-------|---|
| Black | 434 | 65.0% |
| White | 212 | 31.7% |
| Unknown | 13 | 1.9% |
| Asian/PacificIslander | 7 | 1.0% |
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
**Total:** 1,050

| Race | Count | % |
|------|-------|---|
| Black | 660 | 62.9% |
| White | 373 | 35.5% |
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
**Total:** 677

| Race | Count | % |
|------|-------|---|
| Black | 470 | 69.4% |
| White | 198 | 29.2% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 195

| Race | Count | % |
|------|-------|---|
| White | 108 | 55.4% |
| Black | 84 | 43.1% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 32 | 74.4% |
| White | 11 | 25.6% |

### St. Bernard Parish
**Total:** 223

| Race | Count | % |
|------|-------|---|
| Black | 136 | 61.0% |
| White | 83 | 37.2% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| Unknown | 107 | 58.8% |
| White | 75 | 41.2% |

### St. Helena Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 32 | 68.1% |
| White | 15 | 31.9% |

### St. James Parish
**Total:** 73

| Race | Count | % |
|------|-------|---|
| Black | 62 | 84.9% |
| White | 11 | 15.1% |

### St. John the Baptist Parish
**Total:** 209

| Race | Count | % |
|------|-------|---|
| Unknown | 136 | 65.1% |
| White | 73 | 34.9% |

### St. Landry Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 83 | 66.9% |
| White | 39 | 31.5% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 221

| Race | Count | % |
|------|-------|---|
| Black | 107 | 48.4% |
| White | 105 | 47.5% |
| Unknown | 8 | 3.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 279

| Race | Count | % |
|------|-------|---|
| Black | 149 | 53.4% |
| White | 129 | 46.2% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 883

| Race | Count | % |
|------|-------|---|
| White | 461 | 52.2% |
| Black | 379 | 42.9% |
| Unknown | 41 | 4.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 11 | 78.6% |
| Black | 3 | 21.4% |

### Tangipahoa Parish
**Total:** 699

| Race | Count | % |
|------|-------|---|
| Black | 455 | 65.1% |
| White | 241 | 34.5% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 576

| Race | Count | % |
|------|-------|---|
| Black | 390 | 67.7% |
| White | 174 | 30.2% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 569

| Race | Count | % |
|------|-------|---|
| Black | 309 | 54.3% |
| White | 247 | 43.4% |
| American Indian/Alaska Native | 12 | 2.1% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| White | 60 | 49.2% |
| Black | 58 | 47.5% |
| Unknown | 3 | 2.5% |
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
**Total:** 208

| Race | Count | % |
|------|-------|---|
| Black | 107 | 51.4% |
| White | 100 | 48.1% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 470

| Race | Count | % |
|------|-------|---|
| Black | 250 | 53.2% |
| White | 213 | 45.3% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 85 | 64.9% |
| White | 41 | 31.3% |
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
| Black | 123 | 63.4% |
| White | 71 | 36.6% |

### Winn Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| White | 77 | 50.7% |
| Black | 75 | 49.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
