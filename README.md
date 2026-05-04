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

_Last updated: 2026-05-04 02:25 UTC_

**Total inmates (latest scrape):** 25,836 across 72 parishes/jails

### Acadia Parish
**Total:** 171

| Race | Count | % |
|------|-------|---|
| White | 91 | 53.2% |
| Black | 78 | 45.6% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| White | 85 | 63.4% |
| Black | 47 | 35.1% |
| Unknown | 1 | 0.7% |
| American Indian/Alaska Native | 1 | 0.7% |

### Ascension Parish
**Total:** 512

| Race | Count | % |
|------|-------|---|
| Black | 271 | 52.9% |
| White | 203 | 39.6% |
| Unknown | 34 | 6.6% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| Unknown | 74 | 50.7% |
| White | 72 | 49.3% |

### Avoyelles Parish
**Total:** 397

| Race | Count | % |
|------|-------|---|
| Black | 213 | 53.7% |
| White | 177 | 44.6% |
| Unknown | 6 | 1.5% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 180

| Race | Count | % |
|------|-------|---|
| White | 126 | 70.0% |
| Black | 54 | 30.0% |

### Bienville Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| White | 23 | 59.0% |
| Unknown | 16 | 41.0% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 29 | 60.4% |
| White | 19 | 39.6% |

### Bossier Parish
**Total:** 1,132

| Race | Count | % |
|------|-------|---|
| Black | 619 | 54.7% |
| White | 510 | 45.1% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,596

| Race | Count | % |
|------|-------|---|
| Black | 1,181 | 74.0% |
| White | 377 | 23.6% |
| Unknown | 35 | 2.2% |
| Asian/PacificIslander | 3 | 0.2% |

### Calcasieu Parish
**Total:** 1,025

| Race | Count | % |
|------|-------|---|
| Black | 552 | 53.9% |
| White | 430 | 42.0% |
| Unknown | 41 | 4.0% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 604

| Race | Count | % |
|------|-------|---|
| Black | 391 | 64.7% |
| White | 193 | 32.0% |
| American Indian/Alaska Native | 20 | 3.3% |

### Cameron Parish
**Total:** 24

| Race | Count | % |
|------|-------|---|
| White | 23 | 95.8% |
| Black | 1 | 4.2% |

### Catahoula Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 93 | 70.5% |
| White | 38 | 28.8% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 655

| Race | Count | % |
|------|-------|---|
| Black | 392 | 59.8% |
| White | 263 | 40.2% |

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
**Total:** 267

| Race | Count | % |
|------|-------|---|
| Black | 164 | 61.4% |
| White | 102 | 38.2% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 83

| Race | Count | % |
|------|-------|---|
| White | 44 | 53.0% |
| Black | 38 | 45.8% |
| Unknown | 1 | 1.2% |

### Franklin Parish
**Total:** 842

| Race | Count | % |
|------|-------|---|
| Black | 548 | 65.1% |
| White | 283 | 33.6% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 9

| Race | Count | % |
|------|-------|---|
| Black | 6 | 66.7% |
| White | 3 | 33.3% |

### Iberia Parish
**Total:** 446

| Race | Count | % |
|------|-------|---|
| Black | 277 | 62.1% |
| White | 162 | 36.3% |
| Unknown | 3 | 0.7% |
| Asian/PacificIslander | 3 | 0.7% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 105

| Race | Count | % |
|------|-------|---|
| Black | 66 | 62.9% |
| White | 37 | 35.2% |
| Unknown | 2 | 1.9% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 154

| Race | Count | % |
|------|-------|---|
| White | 76 | 49.4% |
| Black | 73 | 47.4% |
| American Indian/Alaska Native | 3 | 1.9% |
| Asian/PacificIslander | 1 | 0.6% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,172

| Race | Count | % |
|------|-------|---|
| Black | 766 | 65.4% |
| White | 394 | 33.6% |
| Unknown | 8 | 0.7% |
| Asian/PacificIslander | 4 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 77

| Race | Count | % |
|------|-------|---|
| White | 54 | 70.1% |
| Black | 22 | 28.6% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 841

| Race | Count | % |
|------|-------|---|
| Black | 530 | 63.0% |
| White | 299 | 35.6% |
| Unknown | 12 | 1.4% |

### Lafourche Parish
**Total:** 741

| Race | Count | % |
|------|-------|---|
| Black | 376 | 50.7% |
| White | 358 | 48.3% |
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
**Total:** 372

| Race | Count | % |
|------|-------|---|
| Black | 275 | 73.9% |
| White | 95 | 25.5% |
| Unknown | 2 | 0.5% |

### Livingston Parish
**Total:** 805

| Race | Count | % |
|------|-------|---|
| White | 582 | 72.3% |
| Black | 213 | 26.5% |
| Unknown | 8 | 1.0% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Black | 111 | 77.6% |
| White | 31 | 21.7% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 207

| Race | Count | % |
|------|-------|---|
| Black | 142 | 68.6% |
| White | 65 | 31.4% |

### Natchitoches Parish
**Total:** 197

| Race | Count | % |
|------|-------|---|
| Black | 150 | 76.1% |
| White | 43 | 21.8% |
| Unknown | 3 | 1.5% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 6

| Race | Count | % |
|------|-------|---|
| Black | 3 | 50.0% |
| White | 3 | 50.0% |

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
**Total:** 1,273

| Race | Count | % |
|------|-------|---|
| Black | 845 | 66.4% |
| White | 414 | 32.5% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 638

| Race | Count | % |
|------|-------|---|
| Black | 418 | 65.5% |
| White | 200 | 31.3% |
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
**Total:** 979

| Race | Count | % |
|------|-------|---|
| Black | 611 | 62.4% |
| White | 350 | 35.8% |
| Unknown | 16 | 1.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 39

| Race | Count | % |
|------|-------|---|
| Black | 25 | 64.1% |
| White | 13 | 33.3% |
| Asian/PacificIslander | 1 | 2.6% |

### Richland Parish
**Total:** 717

| Race | Count | % |
|------|-------|---|
| Black | 494 | 68.9% |
| White | 213 | 29.7% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| White | 103 | 56.3% |
| Black | 80 | 43.7% |

### Shreveport Police Department
**Total:** 46

| Race | Count | % |
|------|-------|---|
| Black | 40 | 87.0% |
| White | 6 | 13.0% |

### St. Bernard Parish
**Total:** 228

| Race | Count | % |
|------|-------|---|
| Black | 133 | 58.3% |
| White | 92 | 40.4% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 180

| Race | Count | % |
|------|-------|---|
| Unknown | 110 | 61.1% |
| White | 70 | 38.9% |

### St. Helena Parish
**Total:** 76

| Race | Count | % |
|------|-------|---|
| Black | 56 | 73.7% |
| White | 15 | 19.7% |
| Unknown | 4 | 5.3% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 77

| Race | Count | % |
|------|-------|---|
| Black | 64 | 83.1% |
| White | 13 | 16.9% |

### St. John the Baptist Parish
**Total:** 199

| Race | Count | % |
|------|-------|---|
| Unknown | 125 | 62.8% |
| White | 74 | 37.2% |

### St. Landry Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 70 | 62.5% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| Black | 96 | 50.0% |
| White | 89 | 46.4% |
| Unknown | 6 | 3.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 237

| Race | Count | % |
|------|-------|---|
| Black | 121 | 51.1% |
| White | 115 | 48.5% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 810

| Race | Count | % |
|------|-------|---|
| White | 408 | 50.4% |
| Black | 361 | 44.6% |
| Unknown | 36 | 4.4% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 2 | 0.2% |

### Sulphur Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 12 | 85.7% |
| Black | 2 | 14.3% |

### Tangipahoa Parish
**Total:** 629

| Race | Count | % |
|------|-------|---|
| Black | 384 | 61.0% |
| White | 244 | 38.8% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 564

| Race | Count | % |
|------|-------|---|
| Black | 372 | 66.0% |
| White | 176 | 31.2% |
| Unknown | 16 | 2.8% |

### Terrebonne Parish
**Total:** 471

| Race | Count | % |
|------|-------|---|
| Black | 245 | 52.0% |
| White | 219 | 46.5% |
| American Indian/Alaska Native | 7 | 1.5% |

### Vermillion Parish
**Total:** 125

| Race | Count | % |
|------|-------|---|
| White | 66 | 52.8% |
| Black | 57 | 45.6% |
| Unknown | 2 | 1.6% |

### Vernon Parish
**Total:** 158

| Race | Count | % |
|------|-------|---|
| White | 108 | 68.4% |
| Black | 47 | 29.7% |
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
| Black | 80 | 53.0% |
| White | 71 | 47.0% |

### Webster Parish
**Total:** 442

| Race | Count | % |
|------|-------|---|
| Black | 219 | 49.5% |
| White | 216 | 48.9% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 3 | 0.7% |

### West Baton Rouge Parish
**Total:** 139

| Race | Count | % |
|------|-------|---|
| Black | 86 | 61.9% |
| White | 48 | 34.5% |
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
**Total:** 148

| Race | Count | % |
|------|-------|---|
| White | 76 | 51.4% |
| Black | 72 | 48.6% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
