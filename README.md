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

_Last updated: 2026-06-26 02:56 UTC_

**Total inmates (latest scrape):** 26,648 across 72 parishes/jails

### Acadia Parish
**Total:** 186

| Race | Count | % |
|------|-------|---|
| White | 100 | 53.8% |
| Black | 84 | 45.2% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 111

| Race | Count | % |
|------|-------|---|
| White | 69 | 62.2% |
| Black | 39 | 35.1% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 518

| Race | Count | % |
|------|-------|---|
| Black | 276 | 53.3% |
| White | 209 | 40.3% |
| Unknown | 29 | 5.6% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Unknown | 83 | 55.0% |
| White | 68 | 45.0% |

### Avoyelles Parish
**Total:** 354

| Race | Count | % |
|------|-------|---|
| Black | 193 | 54.5% |
| White | 157 | 44.4% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| White | 100 | 70.4% |
| Black | 42 | 29.6% |

### Bienville Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| White | 24 | 58.5% |
| Unknown | 17 | 41.5% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 44

| Race | Count | % |
|------|-------|---|
| Black | 29 | 65.9% |
| White | 15 | 34.1% |

### Bossier Parish
**Total:** 1,114

| Race | Count | % |
|------|-------|---|
| Black | 616 | 55.3% |
| White | 497 | 44.6% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,693

| Race | Count | % |
|------|-------|---|
| Black | 1,278 | 75.5% |
| White | 387 | 22.9% |
| Unknown | 26 | 1.5% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,103

| Race | Count | % |
|------|-------|---|
| Black | 617 | 55.9% |
| White | 445 | 40.3% |
| Unknown | 38 | 3.4% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 623

| Race | Count | % |
|------|-------|---|
| Black | 393 | 63.1% |
| White | 209 | 33.5% |
| American Indian/Alaska Native | 20 | 3.2% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 21

| Race | Count | % |
|------|-------|---|
| White | 18 | 85.7% |
| Black | 3 | 14.3% |

### Catahoula Parish
**Total:** 133

| Race | Count | % |
|------|-------|---|
| Black | 92 | 69.2% |
| White | 40 | 30.1% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 680

| Race | Count | % |
|------|-------|---|
| Black | 418 | 61.5% |
| White | 262 | 38.5% |

### Concordia Parish
**Total:** 809

| Race | Count | % |
|------|-------|---|
| White | 456 | 56.4% |
| Black | 351 | 43.4% |
| Unknown | 2 | 0.2% |

### DeSoto Parish
**Total:** 118

| Race | Count | % |
|------|-------|---|
| Black | 70 | 59.3% |
| White | 47 | 39.8% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,305

| Race | Count | % |
|------|-------|---|
| Black | 1,032 | 79.1% |
| White | 204 | 15.6% |
| Unknown | 67 | 5.1% |
| Asian/PacificIslander | 2 | 0.2% |

### East Feliciana Parish
**Total:** 269

| Race | Count | % |
|------|-------|---|
| Black | 171 | 63.6% |
| White | 97 | 36.1% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| Black | 91 | 56.9% |
| White | 68 | 42.5% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 843

| Race | Count | % |
|------|-------|---|
| Black | 550 | 65.2% |
| White | 281 | 33.3% |
| Unknown | 12 | 1.4% |

### Hammond Police Department
**Total:** 10

| Race | Count | % |
|------|-------|---|
| Black | 6 | 60.0% |
| White | 4 | 40.0% |

### Iberia Parish
**Total:** 457

| Race | Count | % |
|------|-------|---|
| Black | 264 | 57.8% |
| White | 182 | 39.8% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 87

| Race | Count | % |
|------|-------|---|
| Black | 56 | 64.4% |
| White | 30 | 34.5% |
| Unknown | 1 | 1.1% |

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
**Total:** 1,152

| Race | Count | % |
|------|-------|---|
| Black | 752 | 65.3% |
| White | 394 | 34.2% |
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
**Total:** 830

| Race | Count | % |
|------|-------|---|
| Black | 531 | 64.0% |
| White | 284 | 34.2% |
| Unknown | 14 | 1.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 746

| Race | Count | % |
|------|-------|---|
| Black | 383 | 51.3% |
| White | 358 | 48.0% |
| American Indian/Alaska Native | 4 | 0.5% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 361

| Race | Count | % |
|------|-------|---|
| Black | 271 | 75.1% |
| White | 87 | 24.1% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 823

| Race | Count | % |
|------|-------|---|
| White | 588 | 71.4% |
| Black | 224 | 27.2% |
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
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 152 | 71.0% |
| White | 62 | 29.0% |

### Natchitoches Parish
**Total:** 198

| Race | Count | % |
|------|-------|---|
| Black | 146 | 73.7% |
| White | 47 | 23.7% |
| Unknown | 5 | 2.5% |

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
**Total:** 1,310

| Race | Count | % |
|------|-------|---|
| Black | 876 | 66.9% |
| White | 420 | 32.1% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 689

| Race | Count | % |
|------|-------|---|
| Black | 454 | 65.9% |
| White | 210 | 30.5% |
| Unknown | 14 | 2.0% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 4 | 0.6% |

### Pointe Coupee Parish
**Total:** 106

| Race | Count | % |
|------|-------|---|
| Black | 65 | 61.3% |
| White | 38 | 35.8% |
| Unknown | 2 | 1.9% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,044

| Race | Count | % |
|------|-------|---|
| Black | 664 | 63.6% |
| White | 361 | 34.6% |
| Unknown | 17 | 1.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 27 | 57.4% |
| White | 19 | 40.4% |
| Asian/PacificIslander | 1 | 2.1% |

### Richland Parish
**Total:** 717

| Race | Count | % |
|------|-------|---|
| Black | 495 | 69.0% |
| White | 212 | 29.6% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| White | 106 | 55.8% |
| Black | 81 | 42.6% |
| Unknown | 2 | 1.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 59

| Race | Count | % |
|------|-------|---|
| Black | 40 | 67.8% |
| White | 19 | 32.2% |

### St. Bernard Parish
**Total:** 221

| Race | Count | % |
|------|-------|---|
| Black | 128 | 57.9% |
| White | 90 | 40.7% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| Unknown | 116 | 60.1% |
| White | 77 | 39.9% |

### St. Helena Parish
**Total:** 49

| Race | Count | % |
|------|-------|---|
| Black | 34 | 69.4% |
| White | 14 | 28.6% |
| Unknown | 1 | 2.0% |

### St. James Parish
**Total:** 63

| Race | Count | % |
|------|-------|---|
| Black | 53 | 84.1% |
| White | 10 | 15.9% |

### St. John the Baptist Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| Unknown | 126 | 65.3% |
| White | 67 | 34.7% |

### St. Landry Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 82 | 64.6% |
| White | 43 | 33.9% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 110 | 51.4% |
| White | 94 | 43.9% |
| Unknown | 9 | 4.2% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 287

| Race | Count | % |
|------|-------|---|
| Black | 148 | 51.6% |
| White | 138 | 48.1% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 855

| Race | Count | % |
|------|-------|---|
| White | 454 | 53.1% |
| Black | 362 | 42.3% |
| Unknown | 36 | 4.2% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 13 | 86.7% |
| Black | 2 | 13.3% |

### Tangipahoa Parish
**Total:** 663

| Race | Count | % |
|------|-------|---|
| Black | 418 | 63.0% |
| White | 244 | 36.8% |
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
| White | 67 | 50.4% |
| Black | 63 | 47.4% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 113 | 68.5% |
| Black | 49 | 29.7% |
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
**Total:** 187

| Race | Count | % |
|------|-------|---|
| White | 96 | 51.3% |
| Black | 91 | 48.7% |

### Webster Parish
**Total:** 442

| Race | Count | % |
|------|-------|---|
| Black | 234 | 52.9% |
| White | 202 | 45.7% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| Black | 84 | 68.9% |
| White | 34 | 27.9% |
| Unknown | 3 | 2.5% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 31

| Race | Count | % |
|------|-------|---|
| White | 25 | 80.6% |
| Black | 6 | 19.4% |

### West Felician Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| Black | 126 | 65.6% |
| White | 66 | 34.4% |

### Winn Parish
**Total:** 142

| Race | Count | % |
|------|-------|---|
| Black | 74 | 52.1% |
| White | 68 | 47.9% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
