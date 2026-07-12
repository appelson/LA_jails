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

_Last updated: 2026-07-12 02:18 UTC_

**Total inmates (latest scrape):** 26,840 across 72 parishes/jails

### Acadia Parish
**Total:** 175

| Race | Count | % |
|------|-------|---|
| White | 104 | 59.4% |
| Black | 69 | 39.4% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 115

| Race | Count | % |
|------|-------|---|
| White | 73 | 63.5% |
| Black | 39 | 33.9% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 527

| Race | Count | % |
|------|-------|---|
| Black | 278 | 52.8% |
| White | 213 | 40.4% |
| Unknown | 32 | 6.1% |
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
**Total:** 159

| Race | Count | % |
|------|-------|---|
| White | 113 | 71.1% |
| Black | 46 | 28.9% |

### Bienville Parish
**Total:** 38

| Race | Count | % |
|------|-------|---|
| White | 20 | 52.6% |
| Unknown | 18 | 47.4% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| White | 14 | 60.9% |
| Black | 9 | 39.1% |

### Bossier City Police Department
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 25 | 52.1% |
| White | 23 | 47.9% |

### Bossier Parish
**Total:** 1,130

| Race | Count | % |
|------|-------|---|
| Black | 628 | 55.6% |
| White | 501 | 44.3% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,708

| Race | Count | % |
|------|-------|---|
| Black | 1,293 | 75.7% |
| White | 387 | 22.7% |
| Unknown | 27 | 1.6% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,103

| Race | Count | % |
|------|-------|---|
| Black | 610 | 55.3% |
| White | 452 | 41.0% |
| Unknown | 38 | 3.4% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 614

| Race | Count | % |
|------|-------|---|
| Black | 386 | 62.9% |
| White | 210 | 34.2% |
| American Indian/Alaska Native | 17 | 2.8% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 17 | 89.5% |
| Black | 2 | 10.5% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.7% |
| White | 39 | 29.5% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 657

| Race | Count | % |
|------|-------|---|
| Black | 406 | 61.8% |
| White | 251 | 38.2% |

### Concordia Parish
**Total:** 817

| Race | Count | % |
|------|-------|---|
| White | 461 | 56.4% |
| Black | 356 | 43.6% |

### DeSoto Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 76 | 59.4% |
| White | 51 | 39.8% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,334

| Race | Count | % |
|------|-------|---|
| Black | 1,055 | 79.1% |
| White | 214 | 16.0% |
| Unknown | 63 | 4.7% |
| Asian/PacificIslander | 2 | 0.1% |

### East Feliciana Parish
**Total:** 272

| Race | Count | % |
|------|-------|---|
| Black | 176 | 64.7% |
| White | 94 | 34.6% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 170

| Race | Count | % |
|------|-------|---|
| Black | 95 | 55.9% |
| White | 74 | 43.5% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 842

| Race | Count | % |
|------|-------|---|
| Black | 554 | 65.8% |
| White | 278 | 33.0% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| Black | 8 | 61.5% |
| White | 5 | 38.5% |

### Iberia Parish
**Total:** 463

| Race | Count | % |
|------|-------|---|
| Black | 271 | 58.5% |
| White | 181 | 39.1% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 37

| Race | Count | % |
|------|-------|---|
| Black | 19 | 51.4% |
| White | 18 | 48.6% |

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
**Total:** 1,157

| Race | Count | % |
|------|-------|---|
| Black | 746 | 64.5% |
| White | 406 | 35.1% |
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
| Black | 534 | 65.9% |
| White | 261 | 32.2% |
| Unknown | 15 | 1.9% |

### Lafourche Parish
**Total:** 760

| Race | Count | % |
|------|-------|---|
| Black | 393 | 51.7% |
| White | 363 | 47.8% |
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
| Black | 270 | 73.8% |
| White | 93 | 25.4% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 826

| Race | Count | % |
|------|-------|---|
| White | 584 | 70.7% |
| Black | 231 | 28.0% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 140

| Race | Count | % |
|------|-------|---|
| Black | 115 | 82.1% |
| White | 24 | 17.1% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 153 | 71.5% |
| White | 61 | 28.5% |

### Natchitoches Parish
**Total:** 185

| Race | Count | % |
|------|-------|---|
| Black | 137 | 74.1% |
| White | 44 | 23.8% |
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
**Total:** 1,350

| Race | Count | % |
|------|-------|---|
| Black | 895 | 66.3% |
| White | 438 | 32.4% |
| Unknown | 17 | 1.3% |

### Plaquemines Parish
**Total:** 677

| Race | Count | % |
|------|-------|---|
| Black | 440 | 65.0% |
| White | 215 | 31.8% |
| Unknown | 14 | 2.1% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 1 | 0.1% |

### Pointe Coupee Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| Black | 69 | 59.5% |
| White | 44 | 37.9% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,053

| Race | Count | % |
|------|-------|---|
| Black | 663 | 63.0% |
| White | 373 | 35.4% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| Black | 21 | 48.8% |
| White | 21 | 48.8% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 678

| Race | Count | % |
|------|-------|---|
| Black | 466 | 68.7% |
| White | 202 | 29.8% |
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
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 36 | 76.6% |
| White | 11 | 23.4% |

### St. Bernard Parish
**Total:** 221

| Race | Count | % |
|------|-------|---|
| Black | 133 | 60.2% |
| White | 84 | 38.0% |
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
**Total:** 73

| Race | Count | % |
|------|-------|---|
| Black | 60 | 82.2% |
| White | 13 | 17.8% |

### St. John the Baptist Parish
**Total:** 205

| Race | Count | % |
|------|-------|---|
| Unknown | 135 | 65.9% |
| White | 70 | 34.1% |

### St. Landry Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 84 | 66.1% |
| White | 41 | 32.3% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 215

| Race | Count | % |
|------|-------|---|
| Black | 110 | 51.2% |
| White | 96 | 44.7% |
| Unknown | 8 | 3.7% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 298

| Race | Count | % |
|------|-------|---|
| Black | 155 | 52.0% |
| White | 142 | 47.7% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 868

| Race | Count | % |
|------|-------|---|
| White | 452 | 52.1% |
| Black | 377 | 43.4% |
| Unknown | 37 | 4.3% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 13 | 86.7% |
| Black | 2 | 13.3% |

### Tangipahoa Parish
**Total:** 682

| Race | Count | % |
|------|-------|---|
| Black | 441 | 64.7% |
| White | 238 | 34.9% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 562

| Race | Count | % |
|------|-------|---|
| Black | 376 | 66.9% |
| White | 174 | 31.0% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 559

| Race | Count | % |
|------|-------|---|
| Black | 305 | 54.6% |
| White | 243 | 43.5% |
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
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 113 | 68.5% |
| Black | 50 | 30.3% |
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
**Total:** 201

| Race | Count | % |
|------|-------|---|
| Black | 103 | 51.2% |
| White | 97 | 48.3% |
| Asian/PacificIslander | 1 | 0.5% |

### Webster Parish
**Total:** 444

| Race | Count | % |
|------|-------|---|
| Black | 240 | 54.1% |
| White | 198 | 44.6% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.5% |

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
**Total:** 200

| Race | Count | % |
|------|-------|---|
| Black | 127 | 63.5% |
| White | 73 | 36.5% |

### Winn Parish
**Total:** 156

| Race | Count | % |
|------|-------|---|
| White | 80 | 51.3% |
| Black | 76 | 48.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
