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

_Last updated: 2026-07-13 02:19 UTC_

**Total inmates (latest scrape):** 26,955 across 72 parishes/jails

### Acadia Parish
**Total:** 175

| Race | Count | % |
|------|-------|---|
| White | 105 | 60.0% |
| Black | 69 | 39.4% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| White | 74 | 63.2% |
| Black | 40 | 34.2% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 529

| Race | Count | % |
|------|-------|---|
| Black | 279 | 52.7% |
| White | 213 | 40.3% |
| Unknown | 33 | 6.2% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| Unknown | 89 | 55.6% |
| White | 71 | 44.4% |

### Avoyelles Parish
**Total:** 357

| Race | Count | % |
|------|-------|---|
| Black | 198 | 55.5% |
| White | 155 | 43.4% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 114 | 69.9% |
| Black | 49 | 30.1% |

### Bienville Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| White | 20 | 51.3% |
| Unknown | 19 | 48.7% |

### Bogalusa Police Department
**Total:** 27

| Race | Count | % |
|------|-------|---|
| White | 17 | 63.0% |
| Black | 10 | 37.0% |

### Bossier City Police Department
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 26 | 63.4% |
| White | 15 | 36.6% |

### Bossier Parish
**Total:** 1,131

| Race | Count | % |
|------|-------|---|
| Black | 629 | 55.6% |
| White | 501 | 44.3% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,709

| Race | Count | % |
|------|-------|---|
| Black | 1,293 | 75.7% |
| White | 387 | 22.6% |
| Unknown | 28 | 1.6% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,107

| Race | Count | % |
|------|-------|---|
| Black | 614 | 55.5% |
| White | 450 | 40.7% |
| Unknown | 40 | 3.6% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 613

| Race | Count | % |
|------|-------|---|
| Black | 385 | 62.8% |
| White | 210 | 34.3% |
| American Indian/Alaska Native | 17 | 2.8% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 16 | 88.9% |
| Black | 2 | 11.1% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.7% |
| White | 39 | 29.5% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 660

| Race | Count | % |
|------|-------|---|
| Black | 409 | 62.0% |
| White | 251 | 38.0% |

### Concordia Parish
**Total:** 819

| Race | Count | % |
|------|-------|---|
| White | 463 | 56.5% |
| Black | 356 | 43.5% |

### DeSoto Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 78 | 59.5% |
| White | 52 | 39.7% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,346

| Race | Count | % |
|------|-------|---|
| Black | 1,065 | 79.1% |
| White | 216 | 16.0% |
| Unknown | 63 | 4.7% |
| Asian/PacificIslander | 2 | 0.1% |

### East Feliciana Parish
**Total:** 275

| Race | Count | % |
|------|-------|---|
| Black | 177 | 64.4% |
| White | 96 | 34.9% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 169

| Race | Count | % |
|------|-------|---|
| Black | 95 | 56.2% |
| White | 73 | 43.2% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 841

| Race | Count | % |
|------|-------|---|
| Black | 553 | 65.8% |
| White | 278 | 33.1% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| Black | 12 | 70.6% |
| White | 5 | 29.4% |

### Iberia Parish
**Total:** 464

| Race | Count | % |
|------|-------|---|
| Black | 273 | 58.8% |
| White | 180 | 38.8% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 36

| Race | Count | % |
|------|-------|---|
| Black | 18 | 50.0% |
| White | 18 | 50.0% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 86 | 52.1% |
| Black | 76 | 46.1% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,172

| Race | Count | % |
|------|-------|---|
| Black | 755 | 64.4% |
| White | 412 | 35.2% |
| Unknown | 5 | 0.4% |

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
| White | 49 | 68.1% |
| Black | 22 | 30.6% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 810

| Race | Count | % |
|------|-------|---|
| Black | 535 | 66.0% |
| White | 260 | 32.1% |
| Unknown | 15 | 1.9% |

### Lafourche Parish
**Total:** 761

| Race | Count | % |
|------|-------|---|
| Black | 394 | 51.8% |
| White | 363 | 47.7% |
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
**Total:** 831

| Race | Count | % |
|------|-------|---|
| White | 587 | 70.6% |
| Black | 233 | 28.0% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 139

| Race | Count | % |
|------|-------|---|
| Black | 114 | 82.0% |
| White | 24 | 17.3% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 215

| Race | Count | % |
|------|-------|---|
| Black | 154 | 71.6% |
| White | 61 | 28.4% |

### Natchitoches Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| Black | 138 | 73.8% |
| White | 45 | 24.1% |
| Unknown | 4 | 2.1% |

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
**Total:** 1,362

| Race | Count | % |
|------|-------|---|
| Black | 898 | 65.9% |
| White | 447 | 32.8% |
| Unknown | 17 | 1.2% |

### Plaquemines Parish
**Total:** 677

| Race | Count | % |
|------|-------|---|
| Black | 439 | 64.8% |
| White | 216 | 31.9% |
| Unknown | 14 | 2.1% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 1 | 0.1% |

### Pointe Coupee Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| Black | 70 | 59.8% |
| White | 44 | 37.6% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,057

| Race | Count | % |
|------|-------|---|
| Black | 666 | 63.0% |
| White | 374 | 35.4% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 42

| Race | Count | % |
|------|-------|---|
| White | 21 | 50.0% |
| Black | 20 | 47.6% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 678

| Race | Count | % |
|------|-------|---|
| Black | 468 | 69.0% |
| White | 200 | 29.5% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 198

| Race | Count | % |
|------|-------|---|
| White | 111 | 56.1% |
| Black | 84 | 42.4% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 51

| Race | Count | % |
|------|-------|---|
| Black | 40 | 78.4% |
| White | 11 | 21.6% |

### St. Bernard Parish
**Total:** 224

| Race | Count | % |
|------|-------|---|
| Black | 134 | 59.8% |
| White | 86 | 38.4% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Unknown | 112 | 59.6% |
| White | 76 | 40.4% |

### St. Helena Parish
**Total:** 49

| Race | Count | % |
|------|-------|---|
| Black | 34 | 69.4% |
| White | 13 | 26.5% |
| Unknown | 2 | 4.1% |

### St. James Parish
**Total:** 72

| Race | Count | % |
|------|-------|---|
| Black | 59 | 81.9% |
| White | 13 | 18.1% |

### St. John the Baptist Parish
**Total:** 206

| Race | Count | % |
|------|-------|---|
| Unknown | 136 | 66.0% |
| White | 70 | 34.0% |

### St. Landry Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 85 | 65.9% |
| White | 42 | 32.6% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 217

| Race | Count | % |
|------|-------|---|
| Black | 111 | 51.2% |
| White | 97 | 44.7% |
| Unknown | 8 | 3.7% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 300

| Race | Count | % |
|------|-------|---|
| Black | 157 | 52.3% |
| White | 142 | 47.3% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 871

| Race | Count | % |
|------|-------|---|
| White | 455 | 52.2% |
| Black | 377 | 43.3% |
| Unknown | 37 | 4.2% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 13 | 86.7% |
| Black | 2 | 13.3% |

### Tangipahoa Parish
**Total:** 695

| Race | Count | % |
|------|-------|---|
| Black | 451 | 64.9% |
| White | 241 | 34.7% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 562

| Race | Count | % |
|------|-------|---|
| Black | 376 | 66.9% |
| White | 174 | 31.0% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 563

| Race | Count | % |
|------|-------|---|
| Black | 307 | 54.5% |
| White | 245 | 43.5% |
| American Indian/Alaska Native | 10 | 1.8% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 137

| Race | Count | % |
|------|-------|---|
| White | 67 | 48.9% |
| Black | 67 | 48.9% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.7% |

### Vernon Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| White | 113 | 68.1% |
| Black | 51 | 30.7% |
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
**Total:** 202

| Race | Count | % |
|------|-------|---|
| Black | 104 | 51.5% |
| White | 98 | 48.5% |

### Webster Parish
**Total:** 445

| Race | Count | % |
|------|-------|---|
| Black | 241 | 54.2% |
| White | 198 | 44.5% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 81 | 65.3% |
| White | 39 | 31.5% |
| Unknown | 2 | 1.6% |
| Asian/PacificIslander | 2 | 1.6% |

### West Carroll Parish
**Total:** 31

| Race | Count | % |
|------|-------|---|
| White | 25 | 80.6% |
| Black | 6 | 19.4% |

### West Felician Parish
**Total:** 201

| Race | Count | % |
|------|-------|---|
| Black | 128 | 63.7% |
| White | 73 | 36.3% |

### Winn Parish
**Total:** 156

| Race | Count | % |
|------|-------|---|
| White | 79 | 50.6% |
| Black | 77 | 49.4% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
