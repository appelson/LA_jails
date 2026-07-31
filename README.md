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

_Last updated: 2026-07-31 02:20 UTC_

**Total inmates (latest scrape):** 26,871 across 72 parishes/jails

### Acadia Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 90 | 55.6% |
| Black | 70 | 43.2% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| White | 76 | 63.3% |
| Black | 40 | 33.3% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 506

| Race | Count | % |
|------|-------|---|
| Black | 271 | 53.6% |
| White | 198 | 39.1% |
| Unknown | 33 | 6.5% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| Unknown | 90 | 56.2% |
| White | 70 | 43.8% |

### Avoyelles Parish
**Total:** 340

| Race | Count | % |
|------|-------|---|
| Black | 194 | 57.1% |
| White | 143 | 42.1% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 176

| Race | Count | % |
|------|-------|---|
| White | 120 | 68.2% |
| Black | 56 | 31.8% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 8 | 57.1% |
| Black | 6 | 42.9% |

### Bossier City Police Department
**Total:** 63

| Race | Count | % |
|------|-------|---|
| Black | 45 | 71.4% |
| White | 18 | 28.6% |

### Bossier Parish
**Total:** 1,127

| Race | Count | % |
|------|-------|---|
| Black | 632 | 56.1% |
| White | 493 | 43.7% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,710

| Race | Count | % |
|------|-------|---|
| Black | 1,297 | 75.8% |
| White | 387 | 22.6% |
| Unknown | 26 | 1.5% |

### Calcasieu Parish
**Total:** 1,103

| Race | Count | % |
|------|-------|---|
| Black | 606 | 54.9% |
| White | 454 | 41.2% |
| Unknown | 41 | 3.7% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 609

| Race | Count | % |
|------|-------|---|
| Black | 390 | 64.0% |
| White | 203 | 33.3% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 21

| Race | Count | % |
|------|-------|---|
| White | 21 | 100.0% |

### Catahoula Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 92 | 70.8% |
| White | 37 | 28.5% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 653

| Race | Count | % |
|------|-------|---|
| Black | 406 | 62.2% |
| White | 247 | 37.8% |

### Concordia Parish
**Total:** 826

| Race | Count | % |
|------|-------|---|
| White | 472 | 57.1% |
| Black | 354 | 42.9% |

### DeSoto Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 75 | 60.5% |
| White | 48 | 38.7% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,267

| Race | Count | % |
|------|-------|---|
| Black | 974 | 76.9% |
| White | 230 | 18.2% |
| Unknown | 60 | 4.7% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 282

| Race | Count | % |
|------|-------|---|
| Black | 185 | 65.6% |
| White | 95 | 33.7% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| Black | 96 | 60.0% |
| White | 63 | 39.4% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 845

| Race | Count | % |
|------|-------|---|
| Black | 562 | 66.5% |
| White | 279 | 33.0% |
| Unknown | 4 | 0.5% |

### Hammond Police Department
**Total:** 18

| Race | Count | % |
|------|-------|---|
| Black | 10 | 55.6% |
| White | 7 | 38.9% |
| Unknown | 1 | 5.6% |

### Iberia Parish
**Total:** 474

| Race | Count | % |
|------|-------|---|
| Black | 284 | 59.9% |
| White | 178 | 37.6% |
| Unknown | 6 | 1.3% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 28 | 60.9% |
| White | 18 | 39.1% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 83 | 50.9% |
| Black | 77 | 47.2% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,200

| Race | Count | % |
|------|-------|---|
| Black | 776 | 64.7% |
| White | 417 | 34.8% |
| Unknown | 6 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 74

| Race | Count | % |
|------|-------|---|
| White | 49 | 66.2% |
| Black | 24 | 32.4% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 842

| Race | Count | % |
|------|-------|---|
| Black | 555 | 65.9% |
| White | 276 | 32.8% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 763

| Race | Count | % |
|------|-------|---|
| Black | 390 | 51.1% |
| White | 369 | 48.4% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 363

| Race | Count | % |
|------|-------|---|
| Black | 269 | 74.1% |
| White | 91 | 25.1% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 828

| Race | Count | % |
|------|-------|---|
| White | 592 | 71.5% |
| Black | 225 | 27.2% |
| Unknown | 8 | 1.0% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| Black | 121 | 79.6% |
| White | 30 | 19.7% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 204

| Race | Count | % |
|------|-------|---|
| Black | 150 | 73.5% |
| White | 54 | 26.5% |

### Natchitoches Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| Black | 137 | 75.3% |
| White | 41 | 22.5% |
| Unknown | 4 | 2.2% |

### Oakdale Police Department
**Total:** 5

| Race | Count | % |
|------|-------|---|
| White | 4 | 80.0% |
| Black | 1 | 20.0% |

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
**Total:** 1,334

| Race | Count | % |
|------|-------|---|
| Black | 893 | 66.9% |
| White | 426 | 31.9% |
| Unknown | 15 | 1.1% |

### Plaquemines Parish
**Total:** 659

| Race | Count | % |
|------|-------|---|
| Black | 427 | 64.8% |
| White | 209 | 31.7% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 9 | 1.4% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| Black | 74 | 62.2% |
| White | 42 | 35.3% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,036

| Race | Count | % |
|------|-------|---|
| Black | 652 | 62.9% |
| White | 368 | 35.5% |
| Unknown | 14 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| Black | 20 | 51.3% |
| White | 18 | 46.2% |
| Asian/PacificIslander | 1 | 2.6% |

### Richland Parish
**Total:** 706

| Race | Count | % |
|------|-------|---|
| Black | 490 | 69.4% |
| White | 208 | 29.5% |
| Unknown | 5 | 0.7% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 186

| Race | Count | % |
|------|-------|---|
| White | 107 | 57.5% |
| Black | 76 | 40.9% |
| Unknown | 2 | 1.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 36

| Race | Count | % |
|------|-------|---|
| Black | 26 | 72.2% |
| White | 10 | 27.8% |

### St. Bernard Parish
**Total:** 234

| Race | Count | % |
|------|-------|---|
| Black | 136 | 58.1% |
| White | 93 | 39.7% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 180

| Race | Count | % |
|------|-------|---|
| Unknown | 100 | 55.6% |
| White | 80 | 44.4% |

### St. Helena Parish
**Total:** 42

| Race | Count | % |
|------|-------|---|
| Black | 29 | 69.0% |
| White | 13 | 31.0% |

### St. James Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 66 | 84.6% |
| White | 12 | 15.4% |

### St. John the Baptist Parish
**Total:** 224

| Race | Count | % |
|------|-------|---|
| Unknown | 149 | 66.5% |
| White | 75 | 33.5% |

### St. Landry Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 84 | 66.1% |
| White | 41 | 32.3% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 211

| Race | Count | % |
|------|-------|---|
| Black | 106 | 50.2% |
| White | 97 | 46.0% |
| Unknown | 8 | 3.8% |

### St. Mary Parish
**Total:** 287

| Race | Count | % |
|------|-------|---|
| Black | 153 | 53.3% |
| White | 133 | 46.3% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 895

| Race | Count | % |
|------|-------|---|
| White | 459 | 51.3% |
| Black | 392 | 43.8% |
| Unknown | 42 | 4.7% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| White | 10 | 76.9% |
| Black | 3 | 23.1% |

### Tangipahoa Parish
**Total:** 703

| Race | Count | % |
|------|-------|---|
| Black | 467 | 66.4% |
| White | 233 | 33.1% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 569

| Race | Count | % |
|------|-------|---|
| Black | 383 | 67.3% |
| White | 174 | 30.6% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 577

| Race | Count | % |
|------|-------|---|
| Black | 320 | 55.5% |
| White | 245 | 42.5% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 58 | 49.2% |
| White | 57 | 48.3% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 179

| Race | Count | % |
|------|-------|---|
| White | 124 | 69.3% |
| Black | 53 | 29.6% |
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
**Total:** 185

| Race | Count | % |
|------|-------|---|
| Black | 97 | 52.4% |
| White | 87 | 47.0% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 451

| Race | Count | % |
|------|-------|---|
| Black | 236 | 52.3% |
| White | 208 | 46.1% |
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
**Total:** 28

| Race | Count | % |
|------|-------|---|
| White | 22 | 78.6% |
| Black | 6 | 21.4% |

### West Felician Parish
**Total:** 201

| Race | Count | % |
|------|-------|---|
| Black | 129 | 64.2% |
| White | 72 | 35.8% |

### Winn Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| Black | 75 | 51.4% |
| White | 71 | 48.6% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
