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

_Last updated: 2026-05-14 02:47 UTC_

**Total inmates (latest scrape):** 25,888 across 72 parishes/jails

### Acadia Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| White | 91 | 51.7% |
| Black | 82 | 46.6% |
| Unknown | 1 | 0.6% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| White | 76 | 62.3% |
| Black | 43 | 35.2% |
| American Indian/Alaska Native | 2 | 1.6% |
| Unknown | 1 | 0.8% |

### Ascension Parish
**Total:** 495

| Race | Count | % |
|------|-------|---|
| Black | 263 | 53.1% |
| White | 199 | 40.2% |
| Unknown | 29 | 5.9% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| Unknown | 78 | 53.4% |
| White | 68 | 46.6% |

### Avoyelles Parish
**Total:** 386

| Race | Count | % |
|------|-------|---|
| Black | 204 | 52.8% |
| White | 178 | 46.1% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 169

| Race | Count | % |
|------|-------|---|
| White | 118 | 69.8% |
| Black | 51 | 30.2% |

### Bienville Parish
**Total:** 38

| Race | Count | % |
|------|-------|---|
| White | 24 | 63.2% |
| Unknown | 14 | 36.8% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 52

| Race | Count | % |
|------|-------|---|
| Black | 34 | 65.4% |
| White | 18 | 34.6% |

### Bossier Parish
**Total:** 1,123

| Race | Count | % |
|------|-------|---|
| Black | 621 | 55.3% |
| White | 500 | 44.5% |
| American Indian/Alaska Native | 1 | 0.1% |
| Unknown | 1 | 0.1% |

### Caddo Parish
**Total:** 1,610

| Race | Count | % |
|------|-------|---|
| Black | 1,193 | 74.1% |
| White | 385 | 23.9% |
| Unknown | 30 | 1.9% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,037

| Race | Count | % |
|------|-------|---|
| Black | 571 | 55.1% |
| White | 425 | 41.0% |
| Unknown | 40 | 3.9% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 601

| Race | Count | % |
|------|-------|---|
| Black | 389 | 64.7% |
| White | 193 | 32.1% |
| American Indian/Alaska Native | 19 | 3.2% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 17 | 89.5% |
| Black | 2 | 10.5% |

### Catahoula Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.2% |
| White | 40 | 30.1% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 652

| Race | Count | % |
|------|-------|---|
| Black | 396 | 60.7% |
| White | 256 | 39.3% |

### Concordia Parish
**Total:** 806

| Race | Count | % |
|------|-------|---|
| White | 452 | 56.1% |
| Black | 350 | 43.4% |
| Unknown | 4 | 0.5% |

### DeSoto Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 73 | 60.8% |
| White | 46 | 38.3% |
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
**Total:** 265

| Race | Count | % |
|------|-------|---|
| Black | 165 | 62.3% |
| White | 99 | 37.4% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 98

| Race | Count | % |
|------|-------|---|
| Black | 49 | 50.0% |
| White | 48 | 49.0% |
| Unknown | 1 | 1.0% |

### Franklin Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| Black | 533 | 64.6% |
| White | 281 | 34.1% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 10

| Race | Count | % |
|------|-------|---|
| Black | 9 | 90.0% |
| White | 1 | 10.0% |

### Iberia Parish
**Total:** 452

| Race | Count | % |
|------|-------|---|
| Black | 279 | 61.7% |
| White | 165 | 36.5% |
| Asian/PacificIslander | 4 | 0.9% |
| Unknown | 3 | 0.7% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 115

| Race | Count | % |
|------|-------|---|
| Black | 73 | 63.5% |
| White | 40 | 34.8% |
| Unknown | 2 | 1.7% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| White | 72 | 49.3% |
| Black | 69 | 47.3% |
| American Indian/Alaska Native | 3 | 2.1% |
| Asian/PacificIslander | 1 | 0.7% |
| Unknown | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,190

| Race | Count | % |
|------|-------|---|
| Black | 781 | 65.6% |
| White | 397 | 33.4% |
| Unknown | 9 | 0.8% |
| Asian/PacificIslander | 3 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Black | 1 | 100.0% |

### LaSalle Parish
**Total:** 74

| Race | Count | % |
|------|-------|---|
| White | 52 | 70.3% |
| Black | 21 | 28.4% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 849

| Race | Count | % |
|------|-------|---|
| Black | 548 | 64.5% |
| White | 290 | 34.2% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 751

| Race | Count | % |
|------|-------|---|
| Black | 388 | 51.7% |
| White | 356 | 47.4% |
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
**Total:** 364

| Race | Count | % |
|------|-------|---|
| Black | 270 | 74.2% |
| White | 91 | 25.0% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 783

| Race | Count | % |
|------|-------|---|
| White | 555 | 70.9% |
| Black | 219 | 28.0% |
| Unknown | 7 | 0.9% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 104 | 78.2% |
| White | 28 | 21.1% |
| Unknown | 1 | 0.8% |

### Morehouse Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Black | 141 | 68.1% |
| White | 66 | 31.9% |

### Natchitoches Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| Black | 150 | 76.1% |
| White | 43 | 21.8% |
| Unknown | 3 | 1.5% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 8

| Race | Count | % |
|------|-------|---|
| White | 5 | 62.5% |
| Black | 2 | 25.0% |
| Unknown | 1 | 12.5% |

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
**Total:** 1,295

| Race | Count | % |
|------|-------|---|
| Black | 866 | 66.9% |
| White | 412 | 31.8% |
| Unknown | 17 | 1.3% |

### Plaquemines Parish
**Total:** 641

| Race | Count | % |
|------|-------|---|
| Black | 419 | 65.4% |
| White | 201 | 31.4% |
| Unknown | 13 | 2.0% |
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
**Total:** 997

| Race | Count | % |
|------|-------|---|
| Black | 617 | 61.9% |
| White | 362 | 36.3% |
| Unknown | 16 | 1.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 25 | 56.8% |
| White | 18 | 40.9% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 715

| Race | Count | % |
|------|-------|---|
| Black | 486 | 68.0% |
| White | 218 | 30.5% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sabine Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| White | 105 | 57.1% |
| Black | 79 | 42.9% |

### Shreveport Police Department
**Total:** 39

| Race | Count | % |
|------|-------|---|
| Black | 33 | 84.6% |
| White | 6 | 15.4% |

### St. Bernard Parish
**Total:** 225

| Race | Count | % |
|------|-------|---|
| Black | 128 | 56.9% |
| White | 94 | 41.8% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 178

| Race | Count | % |
|------|-------|---|
| Unknown | 102 | 57.3% |
| White | 76 | 42.7% |

### St. Helena Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 56 | 71.8% |
| White | 17 | 21.8% |
| Unknown | 4 | 5.1% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 76

| Race | Count | % |
|------|-------|---|
| Black | 59 | 77.6% |
| White | 17 | 22.4% |

### St. John the Baptist Parish
**Total:** 208

| Race | Count | % |
|------|-------|---|
| Unknown | 132 | 63.5% |
| White | 76 | 36.5% |

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
| White | 95 | 48.7% |
| Black | 92 | 47.2% |
| Unknown | 7 | 3.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 256

| Race | Count | % |
|------|-------|---|
| Black | 133 | 52.0% |
| White | 122 | 47.7% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 819

| Race | Count | % |
|------|-------|---|
| White | 426 | 52.0% |
| Black | 353 | 43.1% |
| Unknown | 35 | 4.3% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 2 | 0.2% |

### Sulphur Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| White | 14 | 87.5% |
| Black | 2 | 12.5% |

### Tangipahoa Parish
**Total:** 650

| Race | Count | % |
|------|-------|---|
| Black | 398 | 61.2% |
| White | 251 | 38.6% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 556

| Race | Count | % |
|------|-------|---|
| Black | 368 | 66.2% |
| White | 173 | 31.1% |
| Unknown | 15 | 2.7% |

### Terrebonne Parish
**Total:** 478

| Race | Count | % |
|------|-------|---|
| Black | 247 | 51.7% |
| White | 223 | 46.7% |
| American Indian/Alaska Native | 7 | 1.5% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| White | 73 | 56.6% |
| Black | 54 | 41.9% |
| Unknown | 2 | 1.6% |

### Vernon Parish
**Total:** 157

| Race | Count | % |
|------|-------|---|
| White | 105 | 66.9% |
| Black | 49 | 31.2% |
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
**Total:** 165

| Race | Count | % |
|------|-------|---|
| Black | 88 | 53.3% |
| White | 77 | 46.7% |

### Webster Parish
**Total:** 449

| Race | Count | % |
|------|-------|---|
| Black | 224 | 49.9% |
| White | 218 | 48.6% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 3 | 0.7% |

### West Baton Rouge Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 82 | 63.6% |
| White | 42 | 32.6% |
| Unknown | 4 | 3.1% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 27

| Race | Count | % |
|------|-------|---|
| White | 24 | 88.9% |
| Black | 3 | 11.1% |

### West Felician Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| Black | 115 | 63.2% |
| White | 67 | 36.8% |

### Winn Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| White | 73 | 50.3% |
| Black | 72 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
