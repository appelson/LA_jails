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

_Last updated: 2026-07-14 02:04 UTC_

**Total inmates (latest scrape):** 26,861 across 72 parishes/jails

### Acadia Parish
**Total:** 172

| Race | Count | % |
|------|-------|---|
| White | 102 | 59.3% |
| Black | 69 | 40.1% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 116

| Race | Count | % |
|------|-------|---|
| White | 74 | 63.8% |
| Black | 39 | 33.6% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 527

| Race | Count | % |
|------|-------|---|
| Black | 279 | 52.9% |
| White | 212 | 40.2% |
| Unknown | 32 | 6.1% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 157

| Race | Count | % |
|------|-------|---|
| Unknown | 88 | 56.1% |
| White | 69 | 43.9% |

### Avoyelles Parish
**Total:** 355

| Race | Count | % |
|------|-------|---|
| Black | 196 | 55.2% |
| White | 155 | 43.7% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 114 | 69.9% |
| Black | 49 | 30.1% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| White | 14 | 60.9% |
| Black | 9 | 39.1% |

### Bossier City Police Department
**Total:** 34

| Race | Count | % |
|------|-------|---|
| Black | 19 | 55.9% |
| White | 15 | 44.1% |

### Bossier Parish
**Total:** 1,131

| Race | Count | % |
|------|-------|---|
| Black | 630 | 55.7% |
| White | 500 | 44.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,709

| Race | Count | % |
|------|-------|---|
| Black | 1,292 | 75.6% |
| White | 389 | 22.8% |
| Unknown | 27 | 1.6% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,098

| Race | Count | % |
|------|-------|---|
| Black | 612 | 55.7% |
| White | 443 | 40.3% |
| Unknown | 40 | 3.6% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 602

| Race | Count | % |
|------|-------|---|
| Black | 377 | 62.6% |
| White | 207 | 34.4% |
| American Indian/Alaska Native | 17 | 2.8% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 15 | 88.2% |
| Black | 2 | 11.8% |

### Catahoula Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| Black | 94 | 70.1% |
| White | 39 | 29.1% |
| Unknown | 1 | 0.7% |

### Claiborne Parish
**Total:** 658

| Race | Count | % |
|------|-------|---|
| Black | 409 | 62.2% |
| White | 249 | 37.8% |

### Concordia Parish
**Total:** 820

| Race | Count | % |
|------|-------|---|
| White | 461 | 56.2% |
| Black | 359 | 43.8% |

### DeSoto Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 73 | 58.9% |
| White | 50 | 40.3% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,346

| Race | Count | % |
|------|-------|---|
| Black | 1,067 | 79.3% |
| White | 216 | 16.0% |
| Unknown | 61 | 4.5% |
| Asian/PacificIslander | 2 | 0.1% |

### East Feliciana Parish
**Total:** 273

| Race | Count | % |
|------|-------|---|
| Black | 176 | 64.5% |
| White | 95 | 34.8% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| Black | 92 | 56.1% |
| White | 71 | 43.3% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 842

| Race | Count | % |
|------|-------|---|
| Black | 552 | 65.6% |
| White | 278 | 33.0% |
| Unknown | 12 | 1.4% |

### Hammond Police Department
**Total:** 16

| Race | Count | % |
|------|-------|---|
| Black | 9 | 56.2% |
| White | 7 | 43.8% |

### Iberia Parish
**Total:** 463

| Race | Count | % |
|------|-------|---|
| Black | 272 | 58.7% |
| White | 180 | 38.9% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 35

| Race | Count | % |
|------|-------|---|
| Black | 18 | 51.4% |
| White | 17 | 48.6% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| White | 87 | 53.0% |
| Black | 74 | 45.1% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,176

| Race | Count | % |
|------|-------|---|
| Black | 761 | 64.7% |
| White | 409 | 34.8% |
| Unknown | 6 | 0.5% |

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
**Total:** 820

| Race | Count | % |
|------|-------|---|
| Black | 540 | 65.9% |
| White | 265 | 32.3% |
| Unknown | 15 | 1.8% |

### Lafourche Parish
**Total:** 761

| Race | Count | % |
|------|-------|---|
| Black | 395 | 51.9% |
| White | 362 | 47.6% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 375

| Race | Count | % |
|------|-------|---|
| Black | 277 | 73.9% |
| White | 95 | 25.3% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 830

| Race | Count | % |
|------|-------|---|
| White | 585 | 70.5% |
| Black | 234 | 28.2% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| Black | 117 | 82.4% |
| White | 24 | 16.9% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 213

| Race | Count | % |
|------|-------|---|
| Black | 152 | 71.4% |
| White | 61 | 28.6% |

### Natchitoches Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| Black | 138 | 75.4% |
| White | 41 | 22.4% |
| Unknown | 4 | 2.2% |

### Oakdale Police Department
**Total:** 4

| Race | Count | % |
|------|-------|---|
| White | 3 | 75.0% |
| Black | 1 | 25.0% |

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
**Total:** 1,360

| Race | Count | % |
|------|-------|---|
| Black | 898 | 66.0% |
| White | 446 | 32.8% |
| Unknown | 16 | 1.2% |

### Plaquemines Parish
**Total:** 677

| Race | Count | % |
|------|-------|---|
| Black | 441 | 65.1% |
| White | 214 | 31.6% |
| Unknown | 14 | 2.1% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 1 | 0.1% |

### Pointe Coupee Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| Black | 69 | 59.0% |
| White | 45 | 38.5% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,040

| Race | Count | % |
|------|-------|---|
| Black | 653 | 62.8% |
| White | 370 | 35.6% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 20 | 48.8% |
| White | 20 | 48.8% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 686

| Race | Count | % |
|------|-------|---|
| Black | 474 | 69.1% |
| White | 202 | 29.4% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 195

| Race | Count | % |
|------|-------|---|
| White | 108 | 55.4% |
| Black | 84 | 43.1% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 34 | 82.9% |
| White | 7 | 17.1% |

### St. Bernard Parish
**Total:** 215

| Race | Count | % |
|------|-------|---|
| Black | 130 | 60.5% |
| White | 81 | 37.7% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| Unknown | 111 | 59.4% |
| White | 76 | 40.6% |

### St. Helena Parish
**Total:** 50

| Race | Count | % |
|------|-------|---|
| Black | 33 | 66.0% |
| White | 15 | 30.0% |
| Unknown | 2 | 4.0% |

### St. James Parish
**Total:** 73

| Race | Count | % |
|------|-------|---|
| Black | 60 | 82.2% |
| White | 13 | 17.8% |

### St. John the Baptist Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Unknown | 137 | 66.2% |
| White | 70 | 33.8% |

### St. Landry Parish
**Total:** 125

| Race | Count | % |
|------|-------|---|
| Black | 85 | 68.0% |
| White | 38 | 30.4% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 222

| Race | Count | % |
|------|-------|---|
| Black | 113 | 50.9% |
| White | 100 | 45.0% |
| Unknown | 8 | 3.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 295

| Race | Count | % |
|------|-------|---|
| Black | 153 | 51.9% |
| White | 141 | 47.8% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 863

| Race | Count | % |
|------|-------|---|
| White | 451 | 52.3% |
| Black | 371 | 43.0% |
| Unknown | 39 | 4.5% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 12 | 85.7% |
| Black | 2 | 14.3% |

### Tangipahoa Parish
**Total:** 689

| Race | Count | % |
|------|-------|---|
| Black | 450 | 65.3% |
| White | 236 | 34.3% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 552

| Race | Count | % |
|------|-------|---|
| Black | 371 | 67.2% |
| White | 169 | 30.6% |
| Unknown | 12 | 2.2% |

### Terrebonne Parish
**Total:** 565

| Race | Count | % |
|------|-------|---|
| Black | 309 | 54.7% |
| White | 245 | 43.4% |
| American Indian/Alaska Native | 10 | 1.8% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 135

| Race | Count | % |
|------|-------|---|
| White | 66 | 48.9% |
| Black | 66 | 48.9% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.7% |

### Vernon Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 111 | 68.1% |
| Black | 50 | 30.7% |
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
| Black | 103 | 51.5% |
| White | 97 | 48.5% |

### Webster Parish
**Total:** 458

| Race | Count | % |
|------|-------|---|
| Black | 246 | 53.7% |
| White | 206 | 45.0% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 124

| Race | Count | % |
|------|-------|---|
| Black | 80 | 64.5% |
| White | 40 | 32.3% |
| Unknown | 2 | 1.6% |
| Asian/PacificIslander | 2 | 1.6% |

### West Carroll Parish
**Total:** 32

| Race | Count | % |
|------|-------|---|
| White | 26 | 81.2% |
| Black | 6 | 18.8% |

### West Felician Parish
**Total:** 199

| Race | Count | % |
|------|-------|---|
| Black | 126 | 63.3% |
| White | 73 | 36.7% |

### Winn Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| White | 78 | 50.6% |
| Black | 76 | 49.4% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
