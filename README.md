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

_Last updated: 2026-07-16 02:11 UTC_

**Total inmates (latest scrape):** 26,821 across 72 parishes/jails

### Acadia Parish
**Total:** 174

| Race | Count | % |
|------|-------|---|
| White | 98 | 56.3% |
| Black | 75 | 43.1% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| White | 75 | 63.6% |
| Black | 40 | 33.9% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.8% |

### Ascension Parish
**Total:** 520

| Race | Count | % |
|------|-------|---|
| Black | 276 | 53.1% |
| White | 208 | 40.0% |
| Unknown | 32 | 6.2% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| Unknown | 89 | 55.6% |
| White | 71 | 44.4% |

### Avoyelles Parish
**Total:** 351

| Race | Count | % |
|------|-------|---|
| Black | 195 | 55.6% |
| White | 152 | 43.3% |
| Unknown | 3 | 0.9% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| White | 111 | 69.8% |
| Black | 48 | 30.2% |

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
| White | 15 | 65.2% |
| Black | 8 | 34.8% |

### Bossier City Police Department
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 24 | 52.2% |
| White | 22 | 47.8% |

### Bossier Parish
**Total:** 1,131

| Race | Count | % |
|------|-------|---|
| Black | 630 | 55.7% |
| White | 500 | 44.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,705

| Race | Count | % |
|------|-------|---|
| Black | 1,291 | 75.7% |
| White | 387 | 22.7% |
| Unknown | 26 | 1.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Calcasieu Parish
**Total:** 1,106

| Race | Count | % |
|------|-------|---|
| Black | 619 | 56.0% |
| White | 441 | 39.9% |
| Unknown | 43 | 3.9% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 611

| Race | Count | % |
|------|-------|---|
| Black | 384 | 62.8% |
| White | 210 | 34.4% |
| American Indian/Alaska Native | 17 | 2.8% |

### Cameron Parish
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 16 | 94.1% |
| Black | 1 | 5.9% |

### Catahoula Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| Black | 92 | 71.3% |
| White | 36 | 27.9% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 656

| Race | Count | % |
|------|-------|---|
| Black | 407 | 62.0% |
| White | 249 | 38.0% |

### Concordia Parish
**Total:** 822

| Race | Count | % |
|------|-------|---|
| White | 462 | 56.2% |
| Black | 360 | 43.8% |

### DeSoto Parish
**Total:** 126

| Race | Count | % |
|------|-------|---|
| Black | 74 | 58.7% |
| White | 51 | 40.5% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,331

| Race | Count | % |
|------|-------|---|
| Black | 1,050 | 78.9% |
| White | 217 | 16.3% |
| Unknown | 61 | 4.6% |
| Asian/PacificIslander | 3 | 0.2% |

### East Feliciana Parish
**Total:** 260

| Race | Count | % |
|------|-------|---|
| Black | 167 | 64.2% |
| White | 91 | 35.0% |
| Asian/PacificIslander | 2 | 0.8% |

### Evangeline Parish
**Total:** 167

| Race | Count | % |
|------|-------|---|
| Black | 95 | 56.9% |
| White | 71 | 42.5% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 838

| Race | Count | % |
|------|-------|---|
| Black | 550 | 65.6% |
| White | 277 | 33.1% |
| Unknown | 11 | 1.3% |

### Hammond Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| Black | 8 | 57.1% |
| White | 6 | 42.9% |

### Iberia Parish
**Total:** 466

| Race | Count | % |
|------|-------|---|
| Black | 273 | 58.6% |
| White | 183 | 39.3% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 36

| Race | Count | % |
|------|-------|---|
| Black | 19 | 52.8% |
| White | 17 | 47.2% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 161

| Race | Count | % |
|------|-------|---|
| White | 85 | 52.8% |
| Black | 73 | 45.3% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,192

| Race | Count | % |
|------|-------|---|
| Black | 773 | 64.8% |
| White | 413 | 34.6% |
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
| White | 48 | 66.7% |
| Black | 23 | 31.9% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 821

| Race | Count | % |
|------|-------|---|
| Black | 540 | 65.8% |
| White | 265 | 32.3% |
| Unknown | 16 | 1.9% |

### Lafourche Parish
**Total:** 765

| Race | Count | % |
|------|-------|---|
| Black | 394 | 51.5% |
| White | 367 | 48.0% |
| American Indian/Alaska Native | 3 | 0.4% |
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
| Black | 272 | 74.7% |
| White | 89 | 24.5% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 836

| Race | Count | % |
|------|-------|---|
| White | 586 | 70.1% |
| Black | 239 | 28.6% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 141

| Race | Count | % |
|------|-------|---|
| Black | 115 | 81.6% |
| White | 25 | 17.7% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 212

| Race | Count | % |
|------|-------|---|
| Black | 151 | 71.2% |
| White | 61 | 28.8% |

### Natchitoches Parish
**Total:** 182

| Race | Count | % |
|------|-------|---|
| Black | 135 | 74.2% |
| White | 43 | 23.6% |
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
**Total:** 1,342

| Race | Count | % |
|------|-------|---|
| Black | 886 | 66.0% |
| White | 441 | 32.9% |
| Unknown | 15 | 1.1% |

### Plaquemines Parish
**Total:** 656

| Race | Count | % |
|------|-------|---|
| Black | 429 | 65.4% |
| White | 204 | 31.1% |
| Unknown | 14 | 2.1% |
| Asian/PacificIslander | 7 | 1.1% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| Black | 71 | 60.7% |
| White | 43 | 36.8% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,033

| Race | Count | % |
|------|-------|---|
| Black | 647 | 62.6% |
| White | 369 | 35.7% |
| Unknown | 15 | 1.5% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 42

| Race | Count | % |
|------|-------|---|
| Black | 21 | 50.0% |
| White | 20 | 47.6% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 680

| Race | Count | % |
|------|-------|---|
| Black | 471 | 69.3% |
| White | 199 | 29.3% |
| Unknown | 6 | 0.9% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 199

| Race | Count | % |
|------|-------|---|
| White | 112 | 56.3% |
| Black | 84 | 42.2% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 28 | 68.3% |
| White | 12 | 29.3% |
| Unknown | 1 | 2.4% |

### St. Bernard Parish
**Total:** 219

| Race | Count | % |
|------|-------|---|
| Black | 130 | 59.4% |
| White | 85 | 38.8% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 181

| Race | Count | % |
|------|-------|---|
| Unknown | 106 | 58.6% |
| White | 75 | 41.4% |

### St. Helena Parish
**Total:** 52

| Race | Count | % |
|------|-------|---|
| Black | 33 | 63.5% |
| White | 17 | 32.7% |
| Unknown | 2 | 3.8% |

### St. James Parish
**Total:** 74

| Race | Count | % |
|------|-------|---|
| Black | 61 | 82.4% |
| White | 13 | 17.6% |

### St. John the Baptist Parish
**Total:** 210

| Race | Count | % |
|------|-------|---|
| Unknown | 136 | 64.8% |
| White | 74 | 35.2% |

### St. Landry Parish
**Total:** 125

| Race | Count | % |
|------|-------|---|
| Black | 84 | 67.2% |
| White | 39 | 31.2% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 222

| Race | Count | % |
|------|-------|---|
| Black | 110 | 49.5% |
| White | 103 | 46.4% |
| Unknown | 8 | 3.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 291

| Race | Count | % |
|------|-------|---|
| Black | 153 | 52.6% |
| White | 137 | 47.1% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 863

| Race | Count | % |
|------|-------|---|
| White | 450 | 52.1% |
| Black | 371 | 43.0% |
| Unknown | 40 | 4.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 12

| Race | Count | % |
|------|-------|---|
| White | 10 | 83.3% |
| Black | 2 | 16.7% |

### Tangipahoa Parish
**Total:** 692

| Race | Count | % |
|------|-------|---|
| Black | 450 | 65.0% |
| White | 239 | 34.5% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 553

| Race | Count | % |
|------|-------|---|
| Black | 371 | 67.1% |
| White | 170 | 30.7% |
| Unknown | 12 | 2.2% |

### Terrebonne Parish
**Total:** 567

| Race | Count | % |
|------|-------|---|
| Black | 308 | 54.3% |
| White | 248 | 43.7% |
| American Indian/Alaska Native | 10 | 1.8% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 129

| Race | Count | % |
|------|-------|---|
| White | 63 | 48.8% |
| Black | 63 | 48.8% |
| Unknown | 2 | 1.6% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 163

| Race | Count | % |
|------|-------|---|
| White | 110 | 67.5% |
| Black | 51 | 31.3% |
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
| Black | 103 | 51.0% |
| White | 99 | 49.0% |

### Webster Parish
**Total:** 466

| Race | Count | % |
|------|-------|---|
| Black | 250 | 53.6% |
| White | 210 | 45.1% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 84 | 66.1% |
| White | 39 | 30.7% |
| Unknown | 2 | 1.6% |
| Asian/PacificIslander | 2 | 1.6% |

### West Carroll Parish
**Total:** 32

| Race | Count | % |
|------|-------|---|
| White | 26 | 81.2% |
| Black | 6 | 18.8% |

### West Felician Parish
**Total:** 198

| Race | Count | % |
|------|-------|---|
| Black | 127 | 64.1% |
| White | 71 | 35.9% |

### Winn Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| White | 79 | 51.0% |
| Black | 76 | 49.0% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
