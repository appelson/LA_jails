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

_Last updated: 2026-07-25 02:15 UTC_

**Total inmates (latest scrape):** 26,790 across 72 parishes/jails

### Acadia Parish
**Total:** 169

| Race | Count | % |
|------|-------|---|
| White | 97 | 57.4% |
| Black | 71 | 42.0% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| White | 75 | 63.0% |
| Black | 40 | 33.6% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 504

| Race | Count | % |
|------|-------|---|
| Black | 261 | 51.8% |
| White | 204 | 40.5% |
| Unknown | 35 | 6.9% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| Unknown | 89 | 56.3% |
| White | 69 | 43.7% |

### Avoyelles Parish
**Total:** 350

| Race | Count | % |
|------|-------|---|
| Black | 196 | 56.0% |
| White | 151 | 43.1% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| White | 113 | 67.3% |
| Black | 55 | 32.7% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 9 | 52.9% |
| Black | 8 | 47.1% |

### Bossier City Police Department
**Total:** 62

| Race | Count | % |
|------|-------|---|
| Black | 37 | 59.7% |
| White | 25 | 40.3% |

### Bossier Parish
**Total:** 1,123

| Race | Count | % |
|------|-------|---|
| Black | 638 | 56.8% |
| White | 483 | 43.0% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,702

| Race | Count | % |
|------|-------|---|
| Black | 1,282 | 75.3% |
| White | 395 | 23.2% |
| Unknown | 25 | 1.5% |

### Calcasieu Parish
**Total:** 1,107

| Race | Count | % |
|------|-------|---|
| Black | 620 | 56.0% |
| White | 445 | 40.2% |
| Unknown | 40 | 3.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 607

| Race | Count | % |
|------|-------|---|
| Black | 385 | 63.4% |
| White | 207 | 34.1% |
| American Indian/Alaska Native | 15 | 2.5% |

### Cameron Parish
**Total:** 19

| Race | Count | % |
|------|-------|---|
| White | 18 | 94.7% |
| Black | 1 | 5.3% |

### Catahoula Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 91 | 71.1% |
| White | 36 | 28.1% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 665

| Race | Count | % |
|------|-------|---|
| Black | 414 | 62.3% |
| White | 251 | 37.7% |

### Concordia Parish
**Total:** 805

| Race | Count | % |
|------|-------|---|
| White | 455 | 56.5% |
| Black | 350 | 43.5% |

### DeSoto Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| Black | 70 | 60.3% |
| White | 45 | 38.8% |
| Asian/PacificIslander | 1 | 0.9% |

### East Baton Rouge Parish
**Total:** 1,327

| Race | Count | % |
|------|-------|---|
| Black | 1,040 | 78.4% |
| White | 226 | 17.0% |
| Unknown | 57 | 4.3% |
| Asian/PacificIslander | 3 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 274

| Race | Count | % |
|------|-------|---|
| Black | 176 | 64.2% |
| White | 96 | 35.0% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| Black | 88 | 57.9% |
| White | 63 | 41.4% |
| Unknown | 1 | 0.7% |

### Franklin Parish
**Total:** 826

| Race | Count | % |
|------|-------|---|
| Black | 546 | 66.1% |
| White | 275 | 33.3% |
| Unknown | 5 | 0.6% |

### Hammond Police Department
**Total:** 20

| Race | Count | % |
|------|-------|---|
| Black | 13 | 65.0% |
| White | 7 | 35.0% |

### Iberia Parish
**Total:** 467

| Race | Count | % |
|------|-------|---|
| Black | 280 | 60.0% |
| White | 176 | 37.7% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 30 | 62.5% |
| White | 18 | 37.5% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 84 | 50.9% |
| Black | 77 | 46.7% |
| Unknown | 2 | 1.2% |
| American Indian/Alaska Native | 2 | 1.2% |

### Jefferson Parish
**Total:** 1,197

| Race | Count | % |
|------|-------|---|
| Black | 772 | 64.5% |
| White | 418 | 34.9% |
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
| White | 50 | 67.6% |
| Black | 23 | 31.1% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 815

| Race | Count | % |
|------|-------|---|
| Black | 538 | 66.0% |
| White | 264 | 32.4% |
| Unknown | 13 | 1.6% |

### Lafourche Parish
**Total:** 765

| Race | Count | % |
|------|-------|---|
| Black | 394 | 51.5% |
| White | 366 | 47.8% |
| American Indian/Alaska Native | 4 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 368

| Race | Count | % |
|------|-------|---|
| Black | 272 | 73.9% |
| White | 93 | 25.3% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| White | 589 | 71.4% |
| Black | 224 | 27.2% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| Black | 117 | 81.2% |
| White | 26 | 18.1% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 206

| Race | Count | % |
|------|-------|---|
| Black | 149 | 72.3% |
| White | 57 | 27.7% |

### Natchitoches Parish
**Total:** 178

| Race | Count | % |
|------|-------|---|
| Black | 135 | 75.8% |
| White | 40 | 22.5% |
| Unknown | 3 | 1.7% |

### Oakdale Police Department
**Total:** 6

| Race | Count | % |
|------|-------|---|
| White | 6 | 100.0% |

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
| White | 437 | 32.4% |
| Unknown | 18 | 1.3% |

### Plaquemines Parish
**Total:** 663

| Race | Count | % |
|------|-------|---|
| Black | 434 | 65.5% |
| White | 207 | 31.2% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 8 | 1.2% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| Black | 72 | 61.5% |
| White | 42 | 35.9% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,044

| Race | Count | % |
|------|-------|---|
| Black | 665 | 63.7% |
| White | 362 | 34.7% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 38

| Race | Count | % |
|------|-------|---|
| Black | 19 | 50.0% |
| White | 18 | 47.4% |
| Asian/PacificIslander | 1 | 2.6% |

### Richland Parish
**Total:** 683

| Race | Count | % |
|------|-------|---|
| Black | 474 | 69.4% |
| White | 200 | 29.3% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| White | 108 | 56.0% |
| Black | 82 | 42.5% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 37

| Race | Count | % |
|------|-------|---|
| Black | 27 | 73.0% |
| White | 10 | 27.0% |

### St. Bernard Parish
**Total:** 222

| Race | Count | % |
|------|-------|---|
| Black | 130 | 58.6% |
| White | 88 | 39.6% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 179

| Race | Count | % |
|------|-------|---|
| Unknown | 105 | 58.7% |
| White | 74 | 41.3% |

### St. Helena Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 31 | 66.0% |
| White | 16 | 34.0% |

### St. James Parish
**Total:** 71

| Race | Count | % |
|------|-------|---|
| Black | 60 | 84.5% |
| White | 11 | 15.5% |

### St. John the Baptist Parish
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Unknown | 140 | 65.4% |
| White | 74 | 34.6% |

### St. Landry Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 87 | 68.5% |
| White | 38 | 29.9% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 215

| Race | Count | % |
|------|-------|---|
| Black | 107 | 49.8% |
| White | 100 | 46.5% |
| Unknown | 8 | 3.7% |

### St. Mary Parish
**Total:** 285

| Race | Count | % |
|------|-------|---|
| Black | 152 | 53.3% |
| White | 131 | 46.0% |
| Asian/PacificIslander | 1 | 0.4% |
| American Indian/Alaska Native | 1 | 0.4% |

### St. Tammany Parish
**Total:** 869

| Race | Count | % |
|------|-------|---|
| White | 451 | 51.9% |
| Black | 375 | 43.2% |
| Unknown | 41 | 4.7% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| White | 13 | 81.2% |
| Black | 3 | 18.8% |

### Tangipahoa Parish
**Total:** 702

| Race | Count | % |
|------|-------|---|
| Black | 462 | 65.8% |
| White | 237 | 33.8% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 566

| Race | Count | % |
|------|-------|---|
| Black | 384 | 67.8% |
| White | 170 | 30.0% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 576

| Race | Count | % |
|------|-------|---|
| Black | 312 | 54.2% |
| White | 252 | 43.8% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| White | 58 | 50.0% |
| Black | 55 | 47.4% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.9% |

### Vernon Parish
**Total:** 170

| Race | Count | % |
|------|-------|---|
| White | 116 | 68.2% |
| Black | 52 | 30.6% |
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
**Total:** 184

| Race | Count | % |
|------|-------|---|
| Black | 97 | 52.7% |
| White | 86 | 46.7% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 458

| Race | Count | % |
|------|-------|---|
| Black | 245 | 53.5% |
| White | 206 | 45.0% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 87 | 65.4% |
| White | 41 | 30.8% |
| Unknown | 3 | 2.3% |
| Asian/PacificIslander | 2 | 1.5% |

### West Carroll Parish
**Total:** 28

| Race | Count | % |
|------|-------|---|
| White | 22 | 78.6% |
| Black | 6 | 21.4% |

### West Felician Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| Black | 126 | 64.0% |
| White | 71 | 36.0% |

### Winn Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| White | 76 | 50.0% |
| Black | 76 | 50.0% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
