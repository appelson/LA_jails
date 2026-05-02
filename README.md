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

_Last updated: 2026-05-02 02:18 UTC_

**Total inmates (latest scrape):** 25,671 across 72 parishes/jails

### Acadia Parish
**Total:** 173

| Race | Count | % |
|------|-------|---|
| White | 90 | 52.0% |
| Black | 81 | 46.8% |
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
**Total:** 507

| Race | Count | % |
|------|-------|---|
| Black | 268 | 52.9% |
| White | 201 | 39.6% |
| Unknown | 34 | 6.7% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| Unknown | 73 | 50.3% |
| White | 72 | 49.7% |

### Avoyelles Parish
**Total:** 397

| Race | Count | % |
|------|-------|---|
| Black | 210 | 52.9% |
| White | 180 | 45.3% |
| Unknown | 6 | 1.5% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| White | 128 | 70.3% |
| Black | 54 | 29.7% |

### Bienville Parish
**Total:** 37

| Race | Count | % |
|------|-------|---|
| White | 22 | 59.5% |
| Unknown | 15 | 40.5% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 28 | 65.1% |
| White | 15 | 34.9% |

### Bossier Parish
**Total:** 1,126

| Race | Count | % |
|------|-------|---|
| Black | 619 | 55.0% |
| White | 504 | 44.8% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,581

| Race | Count | % |
|------|-------|---|
| Black | 1,169 | 73.9% |
| White | 376 | 23.8% |
| Unknown | 33 | 2.1% |
| Asian/PacificIslander | 3 | 0.2% |

### Calcasieu Parish
**Total:** 1,022

| Race | Count | % |
|------|-------|---|
| Black | 549 | 53.7% |
| White | 429 | 42.0% |
| Unknown | 42 | 4.1% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 606

| Race | Count | % |
|------|-------|---|
| Black | 393 | 64.9% |
| White | 192 | 31.7% |
| American Indian/Alaska Native | 20 | 3.3% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 18 | 94.7% |
| Black | 1 | 5.3% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 93 | 70.5% |
| White | 38 | 28.8% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 649

| Race | Count | % |
|------|-------|---|
| Black | 386 | 59.5% |
| White | 263 | 40.5% |

### Concordia Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| White | 459 | 55.6% |
| Black | 362 | 43.9% |
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
| Black | 163 | 61.3% |
| White | 102 | 38.3% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 79

| Race | Count | % |
|------|-------|---|
| White | 41 | 51.9% |
| Black | 37 | 46.8% |
| Unknown | 1 | 1.3% |

### Franklin Parish
**Total:** 845

| Race | Count | % |
|------|-------|---|
| Black | 551 | 65.2% |
| White | 283 | 33.5% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 9

| Race | Count | % |
|------|-------|---|
| Black | 5 | 55.6% |
| White | 4 | 44.4% |

### Iberia Parish
**Total:** 443

| Race | Count | % |
|------|-------|---|
| Black | 272 | 61.4% |
| White | 164 | 37.0% |
| Unknown | 3 | 0.7% |
| Asian/PacificIslander | 3 | 0.7% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 101

| Race | Count | % |
|------|-------|---|
| Black | 64 | 63.4% |
| White | 35 | 34.7% |
| Unknown | 2 | 2.0% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| White | 75 | 49.7% |
| Black | 71 | 47.0% |
| American Indian/Alaska Native | 3 | 2.0% |
| Asian/PacificIslander | 1 | 0.7% |
| Unknown | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,172

| Race | Count | % |
|------|-------|---|
| Black | 765 | 65.3% |
| White | 395 | 33.7% |
| Unknown | 8 | 0.7% |
| Asian/PacificIslander | 4 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Black | 1 | 100.0% |

### LaSalle Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| White | 53 | 70.7% |
| Black | 21 | 28.0% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 837

| Race | Count | % |
|------|-------|---|
| Black | 528 | 63.1% |
| White | 297 | 35.5% |
| Unknown | 12 | 1.4% |

### Lafourche Parish
**Total:** 737

| Race | Count | % |
|------|-------|---|
| Black | 377 | 51.2% |
| White | 353 | 47.9% |
| American Indian/Alaska Native | 5 | 0.7% |
| Unknown | 1 | 0.1% |
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
| Black | 271 | 74.2% |
| White | 92 | 25.2% |
| Unknown | 2 | 0.5% |

### Livingston Parish
**Total:** 800

| Race | Count | % |
|------|-------|---|
| White | 580 | 72.5% |
| Black | 211 | 26.4% |
| Unknown | 7 | 0.9% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 141

| Race | Count | % |
|------|-------|---|
| Black | 110 | 78.0% |
| White | 30 | 21.3% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Black | 142 | 68.6% |
| White | 65 | 31.4% |

### Natchitoches Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Black | 143 | 76.1% |
| White | 41 | 21.8% |
| Unknown | 3 | 1.6% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 5

| Race | Count | % |
|------|-------|---|
| Black | 3 | 60.0% |
| White | 2 | 40.0% |

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
**Total:** 1,257

| Race | Count | % |
|------|-------|---|
| Black | 834 | 66.3% |
| White | 409 | 32.5% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 638

| Race | Count | % |
|------|-------|---|
| Black | 420 | 65.8% |
| White | 198 | 31.0% |
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
**Total:** 972

| Race | Count | % |
|------|-------|---|
| Black | 607 | 62.4% |
| White | 347 | 35.7% |
| Unknown | 16 | 1.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 38

| Race | Count | % |
|------|-------|---|
| Black | 24 | 63.2% |
| White | 13 | 34.2% |
| Asian/PacificIslander | 1 | 2.6% |

### Richland Parish
**Total:** 715

| Race | Count | % |
|------|-------|---|
| Black | 493 | 69.0% |
| White | 212 | 29.7% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 177

| Race | Count | % |
|------|-------|---|
| White | 101 | 57.1% |
| Black | 76 | 42.9% |

### Shreveport Police Department
**Total:** 42

| Race | Count | % |
|------|-------|---|
| Black | 35 | 83.3% |
| White | 7 | 16.7% |

### St. Bernard Parish
**Total:** 221

| Race | Count | % |
|------|-------|---|
| Black | 127 | 57.5% |
| White | 91 | 41.2% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| Unknown | 104 | 61.9% |
| White | 64 | 38.1% |

### St. Helena Parish
**Total:** 76

| Race | Count | % |
|------|-------|---|
| Black | 56 | 73.7% |
| White | 15 | 19.7% |
| Unknown | 4 | 5.3% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| Black | 62 | 82.7% |
| White | 13 | 17.3% |

### St. John the Baptist Parish
**Total:** 201

| Race | Count | % |
|------|-------|---|
| Unknown | 126 | 62.7% |
| White | 75 | 37.3% |

### St. Landry Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 70 | 62.5% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 195

| Race | Count | % |
|------|-------|---|
| Black | 97 | 49.7% |
| White | 91 | 46.7% |
| Unknown | 6 | 3.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 238

| Race | Count | % |
|------|-------|---|
| Black | 121 | 50.8% |
| White | 116 | 48.7% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 810

| Race | Count | % |
|------|-------|---|
| White | 410 | 50.6% |
| Black | 360 | 44.4% |
| Unknown | 35 | 4.3% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 2 | 0.2% |

### Sulphur Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| White | 11 | 84.6% |
| Black | 2 | 15.4% |

### Tangipahoa Parish
**Total:** 624

| Race | Count | % |
|------|-------|---|
| Black | 378 | 60.6% |
| White | 245 | 39.3% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 565

| Race | Count | % |
|------|-------|---|
| Black | 373 | 66.0% |
| White | 176 | 31.2% |
| Unknown | 16 | 2.8% |

### Terrebonne Parish
**Total:** 465

| Race | Count | % |
|------|-------|---|
| Black | 243 | 52.3% |
| White | 215 | 46.2% |
| American Indian/Alaska Native | 7 | 1.5% |

### Vermillion Parish
**Total:** 125

| Race | Count | % |
|------|-------|---|
| White | 67 | 53.6% |
| Black | 56 | 44.8% |
| Unknown | 2 | 1.6% |

### Vernon Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| White | 107 | 69.0% |
| Black | 45 | 29.0% |
| Unknown | 2 | 1.3% |
| Asian/PacificIslander | 1 | 0.6% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Black | 79 | 52.3% |
| White | 72 | 47.7% |

### Webster Parish
**Total:** 438

| Race | Count | % |
|------|-------|---|
| Black | 216 | 49.3% |
| White | 215 | 49.1% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 3 | 0.7% |

### West Baton Rouge Parish
**Total:** 136

| Race | Count | % |
|------|-------|---|
| Black | 83 | 61.0% |
| White | 48 | 35.3% |
| Unknown | 4 | 2.9% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 29

| Race | Count | % |
|------|-------|---|
| White | 26 | 89.7% |
| Black | 3 | 10.3% |

### West Felician Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Black | 111 | 60.7% |
| White | 72 | 39.3% |

### Winn Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| White | 75 | 51.4% |
| Black | 71 | 48.6% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
