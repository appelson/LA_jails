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

_Last updated: 2026-06-27 02:47 UTC_

**Total inmates (latest scrape):** 26,523 across 72 parishes/jails

### Acadia Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| White | 98 | 53.6% |
| Black | 83 | 45.4% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| White | 70 | 62.5% |
| Black | 39 | 34.8% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 524

| Race | Count | % |
|------|-------|---|
| Black | 280 | 53.4% |
| White | 211 | 40.3% |
| Unknown | 29 | 5.5% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| Unknown | 81 | 55.5% |
| White | 65 | 44.5% |

### Avoyelles Parish
**Total:** 351

| Race | Count | % |
|------|-------|---|
| Black | 192 | 54.7% |
| White | 155 | 44.2% |
| Unknown | 3 | 0.9% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| White | 99 | 69.2% |
| Black | 44 | 30.8% |

### Bienville Parish
**Total:** 42

| Race | Count | % |
|------|-------|---|
| White | 24 | 57.1% |
| Unknown | 18 | 42.9% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 30 | 65.2% |
| White | 16 | 34.8% |

### Bossier Parish
**Total:** 1,109

| Race | Count | % |
|------|-------|---|
| Black | 615 | 55.5% |
| White | 493 | 44.5% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,689

| Race | Count | % |
|------|-------|---|
| Black | 1,273 | 75.4% |
| White | 387 | 22.9% |
| Unknown | 27 | 1.6% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,096

| Race | Count | % |
|------|-------|---|
| Black | 618 | 56.4% |
| White | 438 | 40.0% |
| Unknown | 37 | 3.4% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 623

| Race | Count | % |
|------|-------|---|
| Black | 392 | 62.9% |
| White | 210 | 33.7% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 17 | 94.4% |
| Black | 1 | 5.6% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.7% |
| White | 39 | 29.5% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 678

| Race | Count | % |
|------|-------|---|
| Black | 417 | 61.5% |
| White | 261 | 38.5% |

### Concordia Parish
**Total:** 809

| Race | Count | % |
|------|-------|---|
| White | 455 | 56.2% |
| Black | 353 | 43.6% |
| Unknown | 1 | 0.1% |

### DeSoto Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| Black | 71 | 58.7% |
| White | 49 | 40.5% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,308

| Race | Count | % |
|------|-------|---|
| Black | 1,031 | 78.8% |
| White | 206 | 15.7% |
| Unknown | 68 | 5.2% |
| Asian/PacificIslander | 3 | 0.2% |

### East Feliciana Parish
**Total:** 272

| Race | Count | % |
|------|-------|---|
| Black | 173 | 63.6% |
| White | 98 | 36.0% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| Black | 91 | 56.9% |
| White | 68 | 42.5% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 845

| Race | Count | % |
|------|-------|---|
| Black | 554 | 65.6% |
| White | 279 | 33.0% |
| Unknown | 12 | 1.4% |

### Hammond Police Department
**Total:** 11

| Race | Count | % |
|------|-------|---|
| Black | 7 | 63.6% |
| White | 4 | 36.4% |

### Iberia Parish
**Total:** 460

| Race | Count | % |
|------|-------|---|
| Black | 267 | 58.0% |
| White | 182 | 39.6% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 32

| Race | Count | % |
|------|-------|---|
| Black | 16 | 50.0% |
| White | 16 | 50.0% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 162

| Race | Count | % |
|------|-------|---|
| White | 85 | 52.5% |
| Black | 73 | 45.1% |
| American Indian/Alaska Native | 3 | 1.9% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,116

| Race | Count | % |
|------|-------|---|
| Black | 721 | 64.6% |
| White | 389 | 34.9% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 70

| Race | Count | % |
|------|-------|---|
| White | 46 | 65.7% |
| Black | 23 | 32.9% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 827

| Race | Count | % |
|------|-------|---|
| Black | 530 | 64.1% |
| White | 281 | 34.0% |
| Unknown | 15 | 1.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 746

| Race | Count | % |
|------|-------|---|
| Black | 382 | 51.2% |
| White | 359 | 48.1% |
| American Indian/Alaska Native | 4 | 0.5% |
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
| Black | 274 | 75.1% |
| White | 88 | 24.1% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 822

| Race | Count | % |
|------|-------|---|
| White | 587 | 71.4% |
| Black | 224 | 27.3% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| Black | 113 | 79.6% |
| White | 28 | 19.7% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 211

| Race | Count | % |
|------|-------|---|
| Black | 150 | 71.1% |
| White | 61 | 28.9% |

### Natchitoches Parish
**Total:** 195

| Race | Count | % |
|------|-------|---|
| Black | 144 | 73.8% |
| White | 48 | 24.6% |
| Unknown | 3 | 1.5% |

### Oakdale Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| White | 1 | 50.0% |
| Black | 1 | 50.0% |

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
**Total:** 1,297

| Race | Count | % |
|------|-------|---|
| Black | 866 | 66.8% |
| White | 418 | 32.2% |
| Unknown | 13 | 1.0% |

### Plaquemines Parish
**Total:** 670

| Race | Count | % |
|------|-------|---|
| Black | 437 | 65.2% |
| White | 207 | 30.9% |
| Unknown | 16 | 2.4% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 3 | 0.4% |

### Pointe Coupee Parish
**Total:** 109

| Race | Count | % |
|------|-------|---|
| Black | 66 | 60.6% |
| White | 39 | 35.8% |
| Unknown | 3 | 2.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,036

| Race | Count | % |
|------|-------|---|
| Black | 658 | 63.5% |
| White | 361 | 34.8% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 26 | 56.5% |
| White | 19 | 41.3% |
| Asian/PacificIslander | 1 | 2.2% |

### Richland Parish
**Total:** 716

| Race | Count | % |
|------|-------|---|
| Black | 495 | 69.1% |
| White | 211 | 29.5% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| White | 104 | 55.3% |
| Black | 80 | 42.6% |
| Unknown | 3 | 1.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 67

| Race | Count | % |
|------|-------|---|
| Black | 46 | 68.7% |
| White | 21 | 31.3% |

### St. Bernard Parish
**Total:** 216

| Race | Count | % |
|------|-------|---|
| Black | 126 | 58.3% |
| White | 87 | 40.3% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| Unknown | 114 | 62.0% |
| White | 70 | 38.0% |

### St. Helena Parish
**Total:** 50

| Race | Count | % |
|------|-------|---|
| Black | 35 | 70.0% |
| White | 14 | 28.0% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 64

| Race | Count | % |
|------|-------|---|
| Black | 54 | 84.4% |
| White | 10 | 15.6% |

### St. John the Baptist Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| Unknown | 127 | 65.8% |
| White | 66 | 34.2% |

### St. Landry Parish
**Total:** 126

| Race | Count | % |
|------|-------|---|
| Black | 81 | 64.3% |
| White | 43 | 34.1% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 217

| Race | Count | % |
|------|-------|---|
| Black | 110 | 50.7% |
| White | 97 | 44.7% |
| Unknown | 9 | 4.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 296

| Race | Count | % |
|------|-------|---|
| Black | 153 | 51.7% |
| White | 142 | 48.0% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 865

| Race | Count | % |
|------|-------|---|
| White | 461 | 53.3% |
| Black | 364 | 42.1% |
| Unknown | 37 | 4.3% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 17

| Race | Count | % |
|------|-------|---|
| White | 15 | 88.2% |
| Black | 2 | 11.8% |

### Tangipahoa Parish
**Total:** 660

| Race | Count | % |
|------|-------|---|
| Black | 420 | 63.6% |
| White | 239 | 36.2% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 570

| Race | Count | % |
|------|-------|---|
| Black | 380 | 66.7% |
| White | 180 | 31.6% |
| Unknown | 10 | 1.8% |

### Terrebonne Parish
**Total:** 506

| Race | Count | % |
|------|-------|---|
| Black | 271 | 53.6% |
| White | 225 | 44.5% |
| American Indian/Alaska Native | 9 | 1.8% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| White | 69 | 51.9% |
| Black | 61 | 45.9% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 164

| Race | Count | % |
|------|-------|---|
| White | 113 | 68.9% |
| Black | 48 | 29.3% |
| Unknown | 2 | 1.2% |
| Asian/PacificIslander | 1 | 0.6% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| White | 99 | 51.6% |
| Black | 92 | 47.9% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 443

| Race | Count | % |
|------|-------|---|
| Black | 234 | 52.8% |
| White | 203 | 45.8% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| Black | 83 | 68.0% |
| White | 35 | 28.7% |
| Unknown | 3 | 2.5% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 31

| Race | Count | % |
|------|-------|---|
| White | 25 | 80.6% |
| Black | 6 | 19.4% |

### West Felician Parish
**Total:** 191

| Race | Count | % |
|------|-------|---|
| Black | 125 | 65.4% |
| White | 66 | 34.6% |

### Winn Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| Black | 74 | 51.4% |
| White | 70 | 48.6% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
