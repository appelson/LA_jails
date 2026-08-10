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

_Last updated: 2026-08-10 01:24 UTC_

**Total inmates (latest scrape):** 27,114 across 72 parishes/jails

### Acadia Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 89 | 54.9% |
| Black | 71 | 43.8% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| White | 73 | 61.9% |
| Black | 41 | 34.7% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 525

| Race | Count | % |
|------|-------|---|
| Black | 281 | 53.5% |
| White | 208 | 39.6% |
| Unknown | 31 | 5.9% |
| Asian/PacificIslander | 5 | 1.0% |

### Assumption Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| Unknown | 96 | 58.9% |
| White | 67 | 41.1% |

### Avoyelles Parish
**Total:** 353

| Race | Count | % |
|------|-------|---|
| Black | 198 | 56.1% |
| White | 152 | 43.1% |
| Unknown | 3 | 0.8% |

### Beauregard Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| White | 116 | 63.7% |
| Black | 66 | 36.3% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 22

| Race | Count | % |
|------|-------|---|
| White | 13 | 59.1% |
| Black | 9 | 40.9% |

### Bossier City Police Department
**Total:** 58

| Race | Count | % |
|------|-------|---|
| Black | 38 | 65.5% |
| White | 20 | 34.5% |

### Bossier Parish
**Total:** 1,127

| Race | Count | % |
|------|-------|---|
| Black | 635 | 56.3% |
| White | 490 | 43.5% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,720

| Race | Count | % |
|------|-------|---|
| Black | 1,305 | 75.9% |
| White | 386 | 22.4% |
| Unknown | 29 | 1.7% |

### Calcasieu Parish
**Total:** 1,102

| Race | Count | % |
|------|-------|---|
| Black | 600 | 54.4% |
| White | 458 | 41.6% |
| Unknown | 43 | 3.9% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 603

| Race | Count | % |
|------|-------|---|
| Black | 386 | 64.0% |
| White | 201 | 33.3% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 24

| Race | Count | % |
|------|-------|---|
| White | 23 | 95.8% |
| Black | 1 | 4.2% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 91 | 69.5% |
| White | 38 | 29.0% |
| Unknown | 2 | 1.5% |

### Claiborne Parish
**Total:** 655

| Race | Count | % |
|------|-------|---|
| Black | 405 | 61.8% |
| White | 250 | 38.2% |

### Concordia Parish
**Total:** 819

| Race | Count | % |
|------|-------|---|
| White | 466 | 56.9% |
| Black | 353 | 43.1% |

### DeSoto Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 76 | 57.6% |
| White | 56 | 42.4% |

### East Baton Rouge Parish
**Total:** 1,303

| Race | Count | % |
|------|-------|---|
| Black | 1,009 | 77.4% |
| White | 232 | 17.8% |
| Unknown | 58 | 4.5% |
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
**Total:** 161

| Race | Count | % |
|------|-------|---|
| Black | 95 | 59.0% |
| White | 65 | 40.4% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 853

| Race | Count | % |
|------|-------|---|
| Black | 567 | 66.5% |
| White | 281 | 32.9% |
| Unknown | 4 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| Black | 9 | 52.9% |
| White | 8 | 47.1% |

### Iberia Parish
**Total:** 470

| Race | Count | % |
|------|-------|---|
| Black | 281 | 59.8% |
| White | 177 | 37.7% |
| Unknown | 6 | 1.3% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 56

| Race | Count | % |
|------|-------|---|
| Black | 36 | 64.3% |
| White | 20 | 35.7% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 83 | 50.3% |
| Black | 80 | 48.5% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,221

| Race | Count | % |
|------|-------|---|
| Black | 800 | 65.5% |
| White | 414 | 33.9% |
| Unknown | 7 | 0.6% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 79

| Race | Count | % |
|------|-------|---|
| White | 48 | 60.8% |
| Black | 29 | 36.7% |
| Unknown | 2 | 2.5% |

### Lafayette Parish
**Total:** 833

| Race | Count | % |
|------|-------|---|
| Black | 553 | 66.4% |
| White | 270 | 32.4% |
| Unknown | 10 | 1.2% |

### Lafourche Parish
**Total:** 785

| Race | Count | % |
|------|-------|---|
| Black | 395 | 50.3% |
| White | 386 | 49.2% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 366

| Race | Count | % |
|------|-------|---|
| Black | 269 | 73.5% |
| White | 92 | 25.1% |
| Unknown | 4 | 1.1% |
| Asian/PacificIslander | 1 | 0.3% |

### Livingston Parish
**Total:** 837

| Race | Count | % |
|------|-------|---|
| White | 592 | 70.7% |
| Black | 236 | 28.2% |
| Unknown | 6 | 0.7% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| Black | 119 | 81.5% |
| White | 26 | 17.8% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 204

| Race | Count | % |
|------|-------|---|
| Black | 148 | 72.5% |
| White | 55 | 27.0% |
| Unknown | 1 | 0.5% |

### Natchitoches Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| Black | 144 | 77.0% |
| White | 39 | 20.9% |
| Unknown | 4 | 2.1% |

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
**Total:** 1,445

| Race | Count | % |
|------|-------|---|
| Black | 1,243 | 86.0% |
| White | 183 | 12.7% |
| Unknown | 15 | 1.0% |
| Asian/PacificIslander | 4 | 0.3% |

### Ouachita Parish
**Total:** 1,344

| Race | Count | % |
|------|-------|---|
| Black | 905 | 67.3% |
| White | 427 | 31.8% |
| Unknown | 12 | 0.9% |

### Plaquemines Parish
**Total:** 669

| Race | Count | % |
|------|-------|---|
| Black | 432 | 64.6% |
| White | 213 | 31.8% |
| Unknown | 13 | 1.9% |
| Asian/PacificIslander | 9 | 1.3% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 83 | 63.8% |
| White | 44 | 33.8% |
| Unknown | 2 | 1.5% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,053

| Race | Count | % |
|------|-------|---|
| Black | 672 | 63.8% |
| White | 365 | 34.7% |
| Unknown | 14 | 1.3% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 24 | 54.5% |
| White | 19 | 43.2% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 698

| Race | Count | % |
|------|-------|---|
| Black | 484 | 69.3% |
| White | 206 | 29.5% |
| Unknown | 5 | 0.7% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| White | 110 | 58.8% |
| Black | 75 | 40.1% |
| Unknown | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 32

| Race | Count | % |
|------|-------|---|
| Black | 23 | 71.9% |
| White | 8 | 25.0% |
| Unknown | 1 | 3.1% |

### St. Bernard Parish
**Total:** 226

| Race | Count | % |
|------|-------|---|
| Black | 130 | 57.5% |
| White | 92 | 40.7% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| Unknown | 101 | 57.4% |
| White | 75 | 42.6% |

### St. Helena Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 34 | 77.3% |
| White | 10 | 22.7% |

### St. James Parish
**Total:** 79

| Race | Count | % |
|------|-------|---|
| Black | 65 | 82.3% |
| White | 14 | 17.7% |

### St. John the Baptist Parish
**Total:** 225

| Race | Count | % |
|------|-------|---|
| Unknown | 148 | 65.8% |
| White | 77 | 34.2% |

### St. Landry Parish
**Total:** 136

| Race | Count | % |
|------|-------|---|
| Black | 91 | 66.9% |
| White | 43 | 31.6% |
| Unknown | 2 | 1.5% |

### St. Martin Parish
**Total:** 220

| Race | Count | % |
|------|-------|---|
| Black | 110 | 50.0% |
| White | 101 | 45.9% |
| Unknown | 9 | 4.1% |

### St. Mary Parish
**Total:** 286

| Race | Count | % |
|------|-------|---|
| White | 143 | 50.0% |
| Black | 142 | 49.7% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 885

| Race | Count | % |
|------|-------|---|
| White | 452 | 51.1% |
| Black | 390 | 44.1% |
| Unknown | 41 | 4.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 13 | 86.7% |
| Black | 2 | 13.3% |

### Tangipahoa Parish
**Total:** 713

| Race | Count | % |
|------|-------|---|
| Black | 469 | 65.8% |
| White | 241 | 33.8% |
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
| White | 233 | 40.5% |
| American Indian/Alaska Native | 13 | 2.3% |
| Asian/PacificIslander | 1 | 0.2% |

### Vermillion Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| White | 58 | 49.2% |
| Black | 57 | 48.3% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 177

| Race | Count | % |
|------|-------|---|
| White | 125 | 70.6% |
| Black | 50 | 28.2% |
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
| Black | 96 | 51.6% |
| White | 89 | 47.8% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 445

| Race | Count | % |
|------|-------|---|
| Black | 232 | 52.1% |
| White | 206 | 46.3% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.4% |

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
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Black | 128 | 63.1% |
| White | 75 | 36.9% |

### Winn Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| Black | 74 | 51.0% |
| White | 71 | 49.0% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
