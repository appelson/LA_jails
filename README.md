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

_Last updated: 2026-04-30 02:38 UTC_

**Total inmates (latest scrape):** 25,758 across 72 parishes/jails

### Acadia Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| White | 89 | 53.0% |
| Black | 77 | 45.8% |
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
**Total:** 505

| Race | Count | % |
|------|-------|---|
| Black | 268 | 53.1% |
| White | 200 | 39.6% |
| Unknown | 34 | 6.7% |
| Asian/PacificIslander | 3 | 0.6% |

### Assumption Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| Unknown | 74 | 51.0% |
| White | 71 | 49.0% |

### Avoyelles Parish
**Total:** 395

| Race | Count | % |
|------|-------|---|
| Black | 207 | 52.4% |
| White | 181 | 45.8% |
| Unknown | 6 | 1.5% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| White | 129 | 70.1% |
| Black | 54 | 29.3% |
| Unknown | 1 | 0.5% |

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
**Total:** 42

| Race | Count | % |
|------|-------|---|
| Black | 30 | 71.4% |
| White | 12 | 28.6% |

### Bossier Parish
**Total:** 1,122

| Race | Count | % |
|------|-------|---|
| Black | 616 | 54.9% |
| White | 503 | 44.8% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,577

| Race | Count | % |
|------|-------|---|
| Black | 1,169 | 74.1% |
| White | 372 | 23.6% |
| Unknown | 33 | 2.1% |
| Asian/PacificIslander | 3 | 0.2% |

### Calcasieu Parish
**Total:** 1,029

| Race | Count | % |
|------|-------|---|
| Black | 551 | 53.5% |
| White | 431 | 41.9% |
| Unknown | 44 | 4.3% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 605

| Race | Count | % |
|------|-------|---|
| Black | 393 | 65.0% |
| White | 191 | 31.6% |
| American Indian/Alaska Native | 20 | 3.3% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 21

| Race | Count | % |
|------|-------|---|
| White | 19 | 90.5% |
| Black | 2 | 9.5% |

### Catahoula Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 94 | 70.7% |
| White | 38 | 28.6% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 634

| Race | Count | % |
|------|-------|---|
| Black | 383 | 60.4% |
| White | 251 | 39.6% |

### Concordia Parish
**Total:** 823

| Race | Count | % |
|------|-------|---|
| White | 457 | 55.5% |
| Black | 362 | 44.0% |
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
**Total:** 266

| Race | Count | % |
|------|-------|---|
| Black | 161 | 60.5% |
| White | 104 | 39.1% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 82

| Race | Count | % |
|------|-------|---|
| White | 43 | 52.4% |
| Black | 38 | 46.3% |
| Unknown | 1 | 1.2% |

### Franklin Parish
**Total:** 846

| Race | Count | % |
|------|-------|---|
| Black | 553 | 65.4% |
| White | 281 | 33.2% |
| Unknown | 11 | 1.3% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| Black | 9 | 69.2% |
| White | 4 | 30.8% |

### Iberia Parish
**Total:** 441

| Race | Count | % |
|------|-------|---|
| Black | 272 | 61.7% |
| White | 163 | 37.0% |
| Asian/PacificIslander | 3 | 0.7% |
| Unknown | 2 | 0.5% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 100

| Race | Count | % |
|------|-------|---|
| Black | 63 | 63.0% |
| White | 34 | 34.0% |
| Unknown | 3 | 3.0% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| Black | 74 | 48.7% |
| White | 73 | 48.0% |
| American Indian/Alaska Native | 3 | 2.0% |
| Asian/PacificIslander | 1 | 0.7% |
| Unknown | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,158

| Race | Count | % |
|------|-------|---|
| Black | 768 | 66.3% |
| White | 377 | 32.6% |
| Unknown | 9 | 0.8% |
| Asian/PacificIslander | 4 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Black | 1 | 100.0% |

### LaSalle Parish
**Total:** 72

| Race | Count | % |
|------|-------|---|
| White | 51 | 70.8% |
| Black | 20 | 27.8% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 848

| Race | Count | % |
|------|-------|---|
| Black | 538 | 63.4% |
| White | 297 | 35.0% |
| Unknown | 13 | 1.5% |

### Lafourche Parish
**Total:** 752

| Race | Count | % |
|------|-------|---|
| Black | 386 | 51.3% |
| White | 357 | 47.5% |
| American Indian/Alaska Native | 5 | 0.7% |
| Asian/PacificIslander | 3 | 0.4% |
| Unknown | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 364

| Race | Count | % |
|------|-------|---|
| Black | 270 | 74.2% |
| White | 92 | 25.3% |
| Unknown | 2 | 0.5% |

### Livingston Parish
**Total:** 820

| Race | Count | % |
|------|-------|---|
| White | 587 | 71.6% |
| Black | 224 | 27.3% |
| Unknown | 7 | 0.9% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| Black | 111 | 78.2% |
| White | 30 | 21.1% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 209

| Race | Count | % |
|------|-------|---|
| Black | 143 | 68.4% |
| White | 66 | 31.6% |

### Natchitoches Parish
**Total:** 198

| Race | Count | % |
|------|-------|---|
| Black | 146 | 73.7% |
| White | 48 | 24.2% |
| Unknown | 3 | 1.5% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 7

| Race | Count | % |
|------|-------|---|
| White | 4 | 57.1% |
| Black | 3 | 42.9% |

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
| Black | 848 | 66.4% |
| White | 415 | 32.5% |
| Unknown | 15 | 1.2% |

### Plaquemines Parish
**Total:** 637

| Race | Count | % |
|------|-------|---|
| Black | 417 | 65.5% |
| White | 200 | 31.4% |
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
**Total:** 978

| Race | Count | % |
|------|-------|---|
| Black | 613 | 62.7% |
| White | 346 | 35.4% |
| Unknown | 17 | 1.7% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 24 | 58.5% |
| White | 16 | 39.0% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 716

| Race | Count | % |
|------|-------|---|
| Black | 494 | 69.0% |
| White | 212 | 29.6% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 177

| Race | Count | % |
|------|-------|---|
| White | 100 | 56.5% |
| Black | 77 | 43.5% |

### Shreveport Police Department
**Total:** 36

| Race | Count | % |
|------|-------|---|
| Black | 29 | 80.6% |
| White | 7 | 19.4% |

### St. Bernard Parish
**Total:** 225

| Race | Count | % |
|------|-------|---|
| Black | 128 | 56.9% |
| White | 94 | 41.8% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 179

| Race | Count | % |
|------|-------|---|
| Unknown | 104 | 58.1% |
| White | 75 | 41.9% |

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
**Total:** 198

| Race | Count | % |
|------|-------|---|
| Unknown | 126 | 63.6% |
| White | 72 | 36.4% |

### St. Landry Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 70 | 62.5% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Black | 102 | 51.0% |
| White | 91 | 45.5% |
| Unknown | 6 | 3.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 244

| Race | Count | % |
|------|-------|---|
| Black | 122 | 50.0% |
| White | 121 | 49.6% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 805

| Race | Count | % |
|------|-------|---|
| White | 410 | 50.9% |
| Black | 354 | 44.0% |
| Unknown | 36 | 4.5% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 2 | 0.2% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 14 | 93.3% |
| Black | 1 | 6.7% |

### Tangipahoa Parish
**Total:** 633

| Race | Count | % |
|------|-------|---|
| Black | 386 | 61.0% |
| White | 246 | 38.9% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 555

| Race | Count | % |
|------|-------|---|
| Black | 365 | 65.8% |
| White | 175 | 31.5% |
| Unknown | 15 | 2.7% |

### Terrebonne Parish
**Total:** 481

| Race | Count | % |
|------|-------|---|
| Black | 256 | 53.2% |
| White | 218 | 45.3% |
| American Indian/Alaska Native | 7 | 1.5% |

### Vermillion Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| White | 71 | 54.6% |
| Black | 57 | 43.8% |
| Unknown | 2 | 1.5% |

### Vernon Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| White | 112 | 70.0% |
| Black | 45 | 28.1% |
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
**Total:** 159

| Race | Count | % |
|------|-------|---|
| Black | 84 | 52.8% |
| White | 75 | 47.2% |

### Webster Parish
**Total:** 427

| Race | Count | % |
|------|-------|---|
| White | 213 | 49.9% |
| Black | 209 | 48.9% |
| Unknown | 3 | 0.7% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 136

| Race | Count | % |
|------|-------|---|
| Black | 83 | 61.0% |
| White | 48 | 35.3% |
| Unknown | 4 | 2.9% |
| Asian/PacificIslander | 1 | 0.7% |

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
