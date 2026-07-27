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

_Last updated: 2026-07-27 02:33 UTC_

**Total inmates (latest scrape):** 27,015 across 72 parishes/jails

### Acadia Parish
**Total:** 173

| Race | Count | % |
|------|-------|---|
| White | 100 | 57.8% |
| Black | 72 | 41.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| White | 75 | 62.5% |
| Black | 41 | 34.2% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 2 | 1.7% |

### Ascension Parish
**Total:** 505

| Race | Count | % |
|------|-------|---|
| Black | 265 | 52.5% |
| White | 204 | 40.4% |
| Unknown | 32 | 6.3% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| Unknown | 90 | 56.6% |
| White | 69 | 43.4% |

### Avoyelles Parish
**Total:** 352

| Race | Count | % |
|------|-------|---|
| Black | 199 | 56.5% |
| White | 150 | 42.6% |
| Unknown | 3 | 0.9% |

### Beauregard Parish
**Total:** 172

| Race | Count | % |
|------|-------|---|
| White | 116 | 67.4% |
| Black | 56 | 32.6% |

### Bienville Parish
**Total:** 43

| Race | Count | % |
|------|-------|---|
| White | 22 | 51.2% |
| Unknown | 21 | 48.8% |

### Bogalusa Police Department
**Total:** 20

| Race | Count | % |
|------|-------|---|
| White | 11 | 55.0% |
| Black | 9 | 45.0% |

### Bossier City Police Department
**Total:** 57

| Race | Count | % |
|------|-------|---|
| Black | 39 | 68.4% |
| White | 18 | 31.6% |

### Bossier Parish
**Total:** 1,129

| Race | Count | % |
|------|-------|---|
| Black | 640 | 56.7% |
| White | 487 | 43.1% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,716

| Race | Count | % |
|------|-------|---|
| Black | 1,294 | 75.4% |
| White | 397 | 23.1% |
| Unknown | 25 | 1.5% |

### Calcasieu Parish
**Total:** 1,112

| Race | Count | % |
|------|-------|---|
| Black | 621 | 55.8% |
| White | 448 | 40.3% |
| Unknown | 42 | 3.8% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 611

| Race | Count | % |
|------|-------|---|
| Black | 385 | 63.0% |
| White | 210 | 34.4% |
| American Indian/Alaska Native | 15 | 2.5% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 21

| Race | Count | % |
|------|-------|---|
| White | 20 | 95.2% |
| Black | 1 | 4.8% |

### Catahoula Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 90 | 70.3% |
| White | 37 | 28.9% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 666

| Race | Count | % |
|------|-------|---|
| Black | 415 | 62.3% |
| White | 251 | 37.7% |

### Concordia Parish
**Total:** 810

| Race | Count | % |
|------|-------|---|
| White | 458 | 56.5% |
| Black | 352 | 43.5% |

### DeSoto Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 76 | 63.3% |
| White | 43 | 35.8% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,339

| Race | Count | % |
|------|-------|---|
| Black | 1,048 | 78.3% |
| White | 228 | 17.0% |
| Unknown | 59 | 4.4% |
| Asian/PacificIslander | 3 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 276

| Race | Count | % |
|------|-------|---|
| Black | 178 | 64.5% |
| White | 96 | 34.8% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| Black | 87 | 57.2% |
| White | 64 | 42.1% |
| Unknown | 1 | 0.7% |

### Franklin Parish
**Total:** 824

| Race | Count | % |
|------|-------|---|
| Black | 546 | 66.3% |
| White | 273 | 33.1% |
| Unknown | 5 | 0.6% |

### Hammond Police Department
**Total:** 22

| Race | Count | % |
|------|-------|---|
| Black | 14 | 63.6% |
| White | 8 | 36.4% |

### Iberia Parish
**Total:** 467

| Race | Count | % |
|------|-------|---|
| Black | 281 | 60.2% |
| White | 175 | 37.5% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 29 | 60.4% |
| White | 19 | 39.6% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 165

| Race | Count | % |
|------|-------|---|
| White | 85 | 51.5% |
| Black | 77 | 46.7% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,207

| Race | Count | % |
|------|-------|---|
| Black | 776 | 64.3% |
| White | 425 | 35.2% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 1 | 50.0% |
| White | 1 | 50.0% |

### LaSalle Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| White | 54 | 69.2% |
| Black | 23 | 29.5% |
| Unknown | 1 | 1.3% |

### Lafayette Parish
**Total:** 827

| Race | Count | % |
|------|-------|---|
| Black | 549 | 66.4% |
| White | 264 | 31.9% |
| Unknown | 14 | 1.7% |

### Lafourche Parish
**Total:** 760

| Race | Count | % |
|------|-------|---|
| Black | 391 | 51.4% |
| White | 365 | 48.0% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 374

| Race | Count | % |
|------|-------|---|
| Black | 277 | 74.1% |
| White | 94 | 25.1% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 836

| Race | Count | % |
|------|-------|---|
| White | 599 | 71.7% |
| Black | 226 | 27.0% |
| Unknown | 8 | 1.0% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 150

| Race | Count | % |
|------|-------|---|
| Black | 120 | 80.0% |
| White | 29 | 19.3% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 208

| Race | Count | % |
|------|-------|---|
| Black | 152 | 73.1% |
| White | 56 | 26.9% |

### Natchitoches Parish
**Total:** 184

| Race | Count | % |
|------|-------|---|
| Black | 139 | 75.5% |
| White | 42 | 22.8% |
| Unknown | 3 | 1.6% |

### Oakdale Police Department
**Total:** 5

| Race | Count | % |
|------|-------|---|
| White | 5 | 100.0% |

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
| Black | 907 | 66.7% |
| White | 435 | 32.0% |
| Unknown | 18 | 1.3% |

### Plaquemines Parish
**Total:** 665

| Race | Count | % |
|------|-------|---|
| Black | 434 | 65.3% |
| White | 207 | 31.1% |
| Unknown | 13 | 2.0% |
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
**Total:** 1,055

| Race | Count | % |
|------|-------|---|
| Black | 674 | 63.9% |
| White | 364 | 34.5% |
| Unknown | 15 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 44

| Race | Count | % |
|------|-------|---|
| White | 21 | 47.7% |
| Black | 21 | 47.7% |
| Unknown | 1 | 2.3% |
| Asian/PacificIslander | 1 | 2.3% |

### Richland Parish
**Total:** 686

| Race | Count | % |
|------|-------|---|
| Black | 475 | 69.2% |
| White | 201 | 29.3% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| White | 108 | 56.2% |
| Black | 81 | 42.2% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 28

| Race | Count | % |
|------|-------|---|
| Black | 20 | 71.4% |
| White | 8 | 28.6% |

### St. Bernard Parish
**Total:** 226

| Race | Count | % |
|------|-------|---|
| Black | 131 | 58.0% |
| White | 90 | 39.8% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Unknown | 108 | 57.4% |
| White | 80 | 42.6% |

### St. Helena Parish
**Total:** 47

| Race | Count | % |
|------|-------|---|
| Black | 31 | 66.0% |
| White | 16 | 34.0% |

### St. James Parish
**Total:** 73

| Race | Count | % |
|------|-------|---|
| Black | 62 | 84.9% |
| White | 11 | 15.1% |

### St. John the Baptist Parish
**Total:** 219

| Race | Count | % |
|------|-------|---|
| Unknown | 144 | 65.8% |
| White | 75 | 34.2% |

### St. Landry Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 88 | 68.8% |
| White | 38 | 29.7% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 214

| Race | Count | % |
|------|-------|---|
| Black | 107 | 50.0% |
| White | 99 | 46.3% |
| Unknown | 8 | 3.7% |

### St. Mary Parish
**Total:** 291

| Race | Count | % |
|------|-------|---|
| Black | 156 | 53.6% |
| White | 133 | 45.7% |
| Asian/PacificIslander | 1 | 0.3% |
| American Indian/Alaska Native | 1 | 0.3% |

### St. Tammany Parish
**Total:** 889

| Race | Count | % |
|------|-------|---|
| White | 457 | 51.4% |
| Black | 388 | 43.6% |
| Unknown | 42 | 4.7% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 15 | 83.3% |
| Black | 3 | 16.7% |

### Tangipahoa Parish
**Total:** 714

| Race | Count | % |
|------|-------|---|
| Black | 470 | 65.8% |
| White | 241 | 33.8% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 567

| Race | Count | % |
|------|-------|---|
| Black | 385 | 67.9% |
| White | 170 | 30.0% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 579

| Race | Count | % |
|------|-------|---|
| Black | 312 | 53.9% |
| White | 255 | 44.0% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 119

| Race | Count | % |
|------|-------|---|
| White | 59 | 49.6% |
| Black | 57 | 47.9% |
| Unknown | 2 | 1.7% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 177

| Race | Count | % |
|------|-------|---|
| White | 120 | 67.8% |
| Black | 55 | 31.1% |
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
**Total:** 462

| Race | Count | % |
|------|-------|---|
| Black | 247 | 53.5% |
| White | 208 | 45.0% |
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
**Total:** 199

| Race | Count | % |
|------|-------|---|
| Black | 128 | 64.3% |
| White | 71 | 35.7% |

### Winn Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| White | 78 | 50.3% |
| Black | 77 | 49.7% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
