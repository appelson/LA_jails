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

_Last updated: 2026-07-08 02:16 UTC_

**Total inmates (latest scrape):** 26,807 across 72 parishes/jails

### Acadia Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| White | 96 | 57.8% |
| Black | 68 | 41.0% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 113

| Race | Count | % |
|------|-------|---|
| White | 69 | 61.1% |
| Black | 41 | 36.3% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 527

| Race | Count | % |
|------|-------|---|
| Black | 284 | 53.9% |
| White | 208 | 39.5% |
| Unknown | 31 | 5.9% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 157

| Race | Count | % |
|------|-------|---|
| Unknown | 86 | 54.8% |
| White | 71 | 45.2% |

### Avoyelles Parish
**Total:** 359

| Race | Count | % |
|------|-------|---|
| Black | 197 | 54.9% |
| White | 158 | 44.0% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| White | 112 | 70.4% |
| Black | 47 | 29.6% |

### Bienville Parish
**Total:** 40

| Race | Count | % |
|------|-------|---|
| White | 21 | 52.5% |
| Unknown | 19 | 47.5% |

### Bogalusa Police Department
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 13 | 68.4% |
| Black | 6 | 31.6% |

### Bossier City Police Department
**Total:** 42

| Race | Count | % |
|------|-------|---|
| Black | 24 | 57.1% |
| White | 18 | 42.9% |

### Bossier Parish
**Total:** 1,139

| Race | Count | % |
|------|-------|---|
| Black | 642 | 56.4% |
| White | 496 | 43.5% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,689

| Race | Count | % |
|------|-------|---|
| Black | 1,275 | 75.5% |
| White | 384 | 22.7% |
| Unknown | 29 | 1.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,114

| Race | Count | % |
|------|-------|---|
| Black | 610 | 54.8% |
| White | 460 | 41.3% |
| Unknown | 41 | 3.7% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 618

| Race | Count | % |
|------|-------|---|
| Black | 388 | 62.8% |
| White | 210 | 34.0% |
| American Indian/Alaska Native | 19 | 3.1% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 15 | 88.2% |
| Black | 2 | 11.8% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 91 | 69.5% |
| White | 39 | 29.8% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 666

| Race | Count | % |
|------|-------|---|
| Black | 413 | 62.0% |
| White | 253 | 38.0% |

### Concordia Parish
**Total:** 803

| Race | Count | % |
|------|-------|---|
| White | 451 | 56.2% |
| Black | 351 | 43.7% |
| Unknown | 1 | 0.1% |

### DeSoto Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 70 | 58.3% |
| White | 49 | 40.8% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,351

| Race | Count | % |
|------|-------|---|
| Black | 1,070 | 79.2% |
| White | 214 | 15.8% |
| Unknown | 65 | 4.8% |
| Asian/PacificIslander | 2 | 0.1% |

### East Feliciana Parish
**Total:** 271

| Race | Count | % |
|------|-------|---|
| Black | 174 | 64.2% |
| White | 96 | 35.4% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| Black | 92 | 55.4% |
| White | 73 | 44.0% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 842

| Race | Count | % |
|------|-------|---|
| Black | 554 | 65.8% |
| White | 278 | 33.0% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 19

| Race | Count | % |
|------|-------|---|
| Black | 14 | 73.7% |
| White | 4 | 21.1% |
| Unknown | 1 | 5.3% |

### Iberia Parish
**Total:** 472

| Race | Count | % |
|------|-------|---|
| Black | 273 | 57.8% |
| White | 189 | 40.0% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.8% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 35

| Race | Count | % |
|------|-------|---|
| White | 18 | 51.4% |
| Black | 17 | 48.6% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 167

| Race | Count | % |
|------|-------|---|
| White | 91 | 54.5% |
| Black | 73 | 43.7% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,142

| Race | Count | % |
|------|-------|---|
| Black | 734 | 64.3% |
| White | 402 | 35.2% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 72

| Race | Count | % |
|------|-------|---|
| White | 48 | 66.7% |
| Black | 23 | 31.9% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 812

| Race | Count | % |
|------|-------|---|
| Black | 539 | 66.4% |
| White | 257 | 31.7% |
| Unknown | 15 | 1.8% |
| Asian/PacificIslander | 1 | 0.1% |

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
**Total:** 373

| Race | Count | % |
|------|-------|---|
| Black | 278 | 74.5% |
| White | 92 | 24.7% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 821

| Race | Count | % |
|------|-------|---|
| White | 577 | 70.3% |
| Black | 232 | 28.3% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| Black | 114 | 80.3% |
| White | 27 | 19.0% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 216

| Race | Count | % |
|------|-------|---|
| Black | 156 | 72.2% |
| White | 60 | 27.8% |

### Natchitoches Parish
**Total:** 180

| Race | Count | % |
|------|-------|---|
| Black | 133 | 73.9% |
| White | 43 | 23.9% |
| Unknown | 4 | 2.2% |

### Oakdale Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| White | 2 | 100.0% |

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
**Total:** 1,337

| Race | Count | % |
|------|-------|---|
| Black | 890 | 66.6% |
| White | 432 | 32.3% |
| Unknown | 15 | 1.1% |

### Plaquemines Parish
**Total:** 684

| Race | Count | % |
|------|-------|---|
| Black | 440 | 64.3% |
| White | 218 | 31.9% |
| Unknown | 15 | 2.2% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 4 | 0.6% |

### Pointe Coupee Parish
**Total:** 114

| Race | Count | % |
|------|-------|---|
| Black | 71 | 62.3% |
| White | 40 | 35.1% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,039

| Race | Count | % |
|------|-------|---|
| Black | 658 | 63.3% |
| White | 365 | 35.1% |
| Unknown | 14 | 1.3% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 23 | 52.3% |
| White | 20 | 45.5% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 681

| Race | Count | % |
|------|-------|---|
| Black | 472 | 69.3% |
| White | 200 | 29.4% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| White | 111 | 56.3% |
| Black | 83 | 42.1% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 34 | 77.3% |
| White | 10 | 22.7% |

### St. Bernard Parish
**Total:** 230

| Race | Count | % |
|------|-------|---|
| Black | 136 | 59.1% |
| White | 90 | 39.1% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| Unknown | 119 | 62.0% |
| White | 73 | 38.0% |

### St. Helena Parish
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 35 | 72.9% |
| White | 12 | 25.0% |
| Unknown | 1 | 2.1% |

### St. James Parish
**Total:** 70

| Race | Count | % |
|------|-------|---|
| Black | 56 | 80.0% |
| White | 14 | 20.0% |

### St. John the Baptist Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Unknown | 134 | 64.7% |
| White | 73 | 35.3% |

### St. Landry Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 88 | 69.3% |
| White | 37 | 29.1% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 218

| Race | Count | % |
|------|-------|---|
| Black | 112 | 51.4% |
| White | 96 | 44.0% |
| Unknown | 9 | 4.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 294

| Race | Count | % |
|------|-------|---|
| Black | 155 | 52.7% |
| White | 138 | 46.9% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 875

| Race | Count | % |
|------|-------|---|
| White | 459 | 52.5% |
| Black | 376 | 43.0% |
| Unknown | 38 | 4.3% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 15 | 83.3% |
| Black | 3 | 16.7% |

### Tangipahoa Parish
**Total:** 663

| Race | Count | % |
|------|-------|---|
| Black | 436 | 65.8% |
| White | 226 | 34.1% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 565

| Race | Count | % |
|------|-------|---|
| Black | 376 | 66.5% |
| White | 177 | 31.3% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 556

| Race | Count | % |
|------|-------|---|
| Black | 301 | 54.1% |
| White | 242 | 43.5% |
| American Indian/Alaska Native | 11 | 2.0% |
| Unknown | 2 | 0.4% |

### Vermillion Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| White | 64 | 48.9% |
| Black | 64 | 48.9% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| White | 117 | 69.6% |
| Black | 49 | 29.2% |
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
**Total:** 205

| Race | Count | % |
|------|-------|---|
| Black | 104 | 50.7% |
| White | 101 | 49.3% |

### Webster Parish
**Total:** 450

| Race | Count | % |
|------|-------|---|
| Black | 241 | 53.6% |
| White | 203 | 45.1% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 94 | 70.1% |
| White | 35 | 26.1% |
| Unknown | 3 | 2.2% |
| Asian/PacificIslander | 2 | 1.5% |

### West Carroll Parish
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 24 | 80.0% |
| Black | 6 | 20.0% |

### West Felician Parish
**Total:** 194

| Race | Count | % |
|------|-------|---|
| Black | 126 | 64.9% |
| White | 68 | 35.1% |

### Winn Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| Black | 80 | 51.9% |
| White | 74 | 48.1% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
