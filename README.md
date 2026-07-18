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

_Last updated: 2026-07-18 02:04 UTC_

**Total inmates (latest scrape):** 26,743 across 72 parishes/jails

### Acadia Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| White | 92 | 55.4% |
| Black | 73 | 44.0% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 123

| Race | Count | % |
|------|-------|---|
| White | 77 | 62.6% |
| Black | 43 | 35.0% |
| Unknown | 2 | 1.6% |
| American Indian/Alaska Native | 1 | 0.8% |

### Ascension Parish
**Total:** 504

| Race | Count | % |
|------|-------|---|
| Black | 268 | 53.2% |
| White | 200 | 39.7% |
| Unknown | 32 | 6.3% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| Unknown | 90 | 55.6% |
| White | 72 | 44.4% |

### Avoyelles Parish
**Total:** 346

| Race | Count | % |
|------|-------|---|
| Black | 192 | 55.5% |
| White | 150 | 43.4% |
| Unknown | 3 | 0.9% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 112 | 69.1% |
| Black | 50 | 30.9% |

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
| White | 16 | 57.1% |
| Black | 12 | 42.9% |

### Bossier City Police Department
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 27 | 57.4% |
| White | 20 | 42.6% |

### Bossier Parish
**Total:** 1,116

| Race | Count | % |
|------|-------|---|
| Black | 627 | 56.2% |
| White | 488 | 43.7% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,714

| Race | Count | % |
|------|-------|---|
| Black | 1,294 | 75.5% |
| White | 394 | 23.0% |
| Unknown | 25 | 1.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,098

| Race | Count | % |
|------|-------|---|
| Black | 613 | 55.8% |
| White | 441 | 40.2% |
| Unknown | 42 | 3.8% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 613

| Race | Count | % |
|------|-------|---|
| Black | 384 | 62.6% |
| White | 213 | 34.7% |
| American Indian/Alaska Native | 16 | 2.6% |

### Cameron Parish
**Total:** 16

| Race | Count | % |
|------|-------|---|
| White | 16 | 100.0% |

### Catahoula Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 92 | 70.8% |
| White | 37 | 28.5% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 657

| Race | Count | % |
|------|-------|---|
| Black | 405 | 61.6% |
| White | 252 | 38.4% |

### Concordia Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| White | 462 | 56.0% |
| Black | 363 | 44.0% |

### DeSoto Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 73 | 60.8% |
| White | 46 | 38.3% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,332

| Race | Count | % |
|------|-------|---|
| Black | 1,053 | 79.1% |
| White | 217 | 16.3% |
| Unknown | 60 | 4.5% |
| Asian/PacificIslander | 2 | 0.2% |

### East Feliciana Parish
**Total:** 270

| Race | Count | % |
|------|-------|---|
| Black | 174 | 64.4% |
| White | 94 | 34.8% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| Black | 89 | 57.8% |
| White | 64 | 41.6% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 837

| Race | Count | % |
|------|-------|---|
| Black | 552 | 65.9% |
| White | 279 | 33.3% |
| Unknown | 6 | 0.7% |

### Hammond Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| Black | 11 | 64.7% |
| White | 6 | 35.3% |

### Iberia Parish
**Total:** 463

| Race | Count | % |
|------|-------|---|
| Black | 276 | 59.6% |
| White | 177 | 38.2% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 37

| Race | Count | % |
|------|-------|---|
| Black | 21 | 56.8% |
| White | 16 | 43.2% |

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
| Black | 75 | 45.7% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,162

| Race | Count | % |
|------|-------|---|
| Black | 741 | 63.8% |
| White | 415 | 35.7% |
| Unknown | 6 | 0.5% |

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
**Total:** 814

| Race | Count | % |
|------|-------|---|
| Black | 541 | 66.5% |
| White | 259 | 31.8% |
| Unknown | 14 | 1.7% |

### Lafourche Parish
**Total:** 759

| Race | Count | % |
|------|-------|---|
| Black | 394 | 51.9% |
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
**Total:** 366

| Race | Count | % |
|------|-------|---|
| Black | 271 | 74.0% |
| White | 92 | 25.1% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 830

| Race | Count | % |
|------|-------|---|
| White | 587 | 70.7% |
| Black | 232 | 28.0% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Black | 116 | 81.1% |
| White | 26 | 18.2% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 206

| Race | Count | % |
|------|-------|---|
| Black | 149 | 72.3% |
| White | 57 | 27.7% |

### Natchitoches Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Black | 136 | 74.3% |
| White | 43 | 23.5% |
| Unknown | 4 | 2.2% |

### Oakdale Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 3 | 100.0% |

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
**Total:** 1,331

| Race | Count | % |
|------|-------|---|
| Black | 879 | 66.0% |
| White | 436 | 32.8% |
| Unknown | 16 | 1.2% |

### Plaquemines Parish
**Total:** 667

| Race | Count | % |
|------|-------|---|
| Black | 435 | 65.2% |
| White | 210 | 31.5% |
| Unknown | 13 | 1.9% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 71 | 60.2% |
| White | 44 | 37.3% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,039

| Race | Count | % |
|------|-------|---|
| Black | 653 | 62.8% |
| White | 369 | 35.5% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| Black | 20 | 51.3% |
| White | 18 | 46.2% |
| Asian/PacificIslander | 1 | 2.6% |

### Richland Parish
**Total:** 673

| Race | Count | % |
|------|-------|---|
| Black | 468 | 69.5% |
| White | 196 | 29.1% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 195

| Race | Count | % |
|------|-------|---|
| White | 109 | 55.9% |
| Black | 83 | 42.6% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 34 | 79.1% |
| White | 9 | 20.9% |

### St. Bernard Parish
**Total:** 217

| Race | Count | % |
|------|-------|---|
| Black | 131 | 60.4% |
| White | 82 | 37.8% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 181

| Race | Count | % |
|------|-------|---|
| Unknown | 103 | 56.9% |
| White | 78 | 43.1% |

### St. Helena Parish
**Total:** 54

| Race | Count | % |
|------|-------|---|
| Black | 35 | 64.8% |
| White | 17 | 31.5% |
| Unknown | 2 | 3.7% |

### St. James Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| Black | 63 | 84.0% |
| White | 12 | 16.0% |

### St. John the Baptist Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Unknown | 134 | 64.7% |
| White | 73 | 35.3% |

### St. Landry Parish
**Total:** 126

| Race | Count | % |
|------|-------|---|
| Black | 86 | 68.3% |
| White | 38 | 30.2% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 218

| Race | Count | % |
|------|-------|---|
| Black | 107 | 49.1% |
| White | 102 | 46.8% |
| Unknown | 8 | 3.7% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 286

| Race | Count | % |
|------|-------|---|
| Black | 151 | 52.8% |
| White | 134 | 46.9% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 872

| Race | Count | % |
|------|-------|---|
| White | 460 | 52.8% |
| Black | 370 | 42.4% |
| Unknown | 40 | 4.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| White | 11 | 84.6% |
| Black | 2 | 15.4% |

### Tangipahoa Parish
**Total:** 697

| Race | Count | % |
|------|-------|---|
| Black | 452 | 64.8% |
| White | 242 | 34.7% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 560

| Race | Count | % |
|------|-------|---|
| Black | 377 | 67.3% |
| White | 171 | 30.5% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 566

| Race | Count | % |
|------|-------|---|
| Black | 306 | 54.1% |
| White | 248 | 43.8% |
| American Indian/Alaska Native | 11 | 1.9% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 125

| Race | Count | % |
|------|-------|---|
| Black | 61 | 48.8% |
| White | 60 | 48.0% |
| Unknown | 3 | 2.4% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| White | 108 | 67.5% |
| Black | 50 | 31.2% |
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
| Black | 102 | 51.0% |
| White | 96 | 48.0% |
| Unknown | 2 | 1.0% |

### Webster Parish
**Total:** 470

| Race | Count | % |
|------|-------|---|
| Black | 249 | 53.0% |
| White | 214 | 45.5% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 83 | 64.8% |
| White | 41 | 32.0% |
| Unknown | 2 | 1.6% |
| Asian/PacificIslander | 2 | 1.6% |

### West Carroll Parish
**Total:** 29

| Race | Count | % |
|------|-------|---|
| White | 23 | 79.3% |
| Black | 6 | 20.7% |

### West Felician Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| Black | 126 | 64.3% |
| White | 70 | 35.7% |

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
