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

_Last updated: 2026-08-03 02:21 UTC_

**Total inmates (latest scrape):** 27,040 across 72 parishes/jails

### Acadia Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| White | 91 | 54.8% |
| Black | 73 | 44.0% |
| Unknown | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 122

| Race | Count | % |
|------|-------|---|
| White | 77 | 63.1% |
| Black | 41 | 33.6% |
| Unknown | 2 | 1.6% |
| American Indian/Alaska Native | 2 | 1.6% |

### Ascension Parish
**Total:** 515

| Race | Count | % |
|------|-------|---|
| Black | 275 | 53.4% |
| White | 203 | 39.4% |
| Unknown | 32 | 6.2% |
| Asian/PacificIslander | 5 | 1.0% |

### Assumption Parish
**Total:** 161

| Race | Count | % |
|------|-------|---|
| Unknown | 92 | 57.1% |
| White | 69 | 42.9% |

### Avoyelles Parish
**Total:** 350

| Race | Count | % |
|------|-------|---|
| Black | 199 | 56.9% |
| White | 148 | 42.3% |
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
**Total:** 20

| Race | Count | % |
|------|-------|---|
| White | 12 | 60.0% |
| Black | 8 | 40.0% |

### Bossier City Police Department
**Total:** 55

| Race | Count | % |
|------|-------|---|
| Black | 36 | 65.5% |
| White | 19 | 34.5% |

### Bossier Parish
**Total:** 1,125

| Race | Count | % |
|------|-------|---|
| Black | 633 | 56.3% |
| White | 490 | 43.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Caddo Parish
**Total:** 1,708

| Race | Count | % |
|------|-------|---|
| Black | 1,288 | 75.4% |
| White | 391 | 22.9% |
| Unknown | 29 | 1.7% |

### Calcasieu Parish
**Total:** 1,106

| Race | Count | % |
|------|-------|---|
| Black | 608 | 55.0% |
| White | 454 | 41.0% |
| Unknown | 43 | 3.9% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 617

| Race | Count | % |
|------|-------|---|
| Black | 395 | 64.0% |
| White | 206 | 33.4% |
| American Indian/Alaska Native | 15 | 2.4% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 21

| Race | Count | % |
|------|-------|---|
| White | 21 | 100.0% |

### Catahoula Parish
**Total:** 131

| Race | Count | % |
|------|-------|---|
| Black | 92 | 70.2% |
| White | 38 | 29.0% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 651

| Race | Count | % |
|------|-------|---|
| Black | 404 | 62.1% |
| White | 247 | 37.9% |

### Concordia Parish
**Total:** 824

| Race | Count | % |
|------|-------|---|
| White | 469 | 56.9% |
| Black | 355 | 43.1% |

### DeSoto Parish
**Total:** 125

| Race | Count | % |
|------|-------|---|
| Black | 73 | 58.4% |
| White | 51 | 40.8% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,259

| Race | Count | % |
|------|-------|---|
| Black | 979 | 77.8% |
| White | 223 | 17.7% |
| Unknown | 54 | 4.3% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### East Feliciana Parish
**Total:** 284

| Race | Count | % |
|------|-------|---|
| Black | 185 | 65.1% |
| White | 97 | 34.2% |
| Asian/PacificIslander | 2 | 0.7% |

### Evangeline Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| Black | 93 | 58.5% |
| White | 65 | 40.9% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 853

| Race | Count | % |
|------|-------|---|
| Black | 564 | 66.1% |
| White | 285 | 33.4% |
| Unknown | 4 | 0.5% |

### Hammond Police Department
**Total:** 22

| Race | Count | % |
|------|-------|---|
| Black | 10 | 45.5% |
| White | 9 | 40.9% |
| Unknown | 3 | 13.6% |

### Iberia Parish
**Total:** 482

| Race | Count | % |
|------|-------|---|
| Black | 288 | 59.8% |
| White | 181 | 37.6% |
| Unknown | 7 | 1.5% |
| Asian/PacificIslander | 5 | 1.0% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 49

| Race | Count | % |
|------|-------|---|
| Black | 29 | 59.2% |
| White | 20 | 40.8% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 166

| Race | Count | % |
|------|-------|---|
| White | 86 | 51.8% |
| Black | 77 | 46.4% |
| American Indian/Alaska Native | 2 | 1.2% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,208

| Race | Count | % |
|------|-------|---|
| Black | 780 | 64.6% |
| White | 421 | 34.9% |
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
**Total:** 848

| Race | Count | % |
|------|-------|---|
| Black | 555 | 65.4% |
| White | 282 | 33.3% |
| Unknown | 11 | 1.3% |

### Lafourche Parish
**Total:** 769

| Race | Count | % |
|------|-------|---|
| Black | 397 | 51.6% |
| White | 368 | 47.9% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 366

| Race | Count | % |
|------|-------|---|
| Black | 271 | 74.0% |
| White | 92 | 25.1% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 835

| Race | Count | % |
|------|-------|---|
| White | 587 | 70.3% |
| Black | 237 | 28.4% |
| Unknown | 8 | 1.0% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 152

| Race | Count | % |
|------|-------|---|
| Black | 122 | 80.3% |
| White | 29 | 19.1% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 202

| Race | Count | % |
|------|-------|---|
| Black | 148 | 73.3% |
| White | 54 | 26.7% |

### Natchitoches Parish
**Total:** 189

| Race | Count | % |
|------|-------|---|
| Black | 142 | 75.1% |
| White | 43 | 22.8% |
| Unknown | 4 | 2.1% |

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
| Black | 898 | 66.9% |
| White | 430 | 32.0% |
| Unknown | 14 | 1.0% |

### Plaquemines Parish
**Total:** 665

| Race | Count | % |
|------|-------|---|
| Black | 431 | 64.8% |
| White | 211 | 31.7% |
| Unknown | 12 | 1.8% |
| Asian/PacificIslander | 9 | 1.4% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 121

| Race | Count | % |
|------|-------|---|
| Black | 75 | 62.0% |
| White | 43 | 35.5% |
| Unknown | 2 | 1.7% |
| American Indian/Alaska Native | 1 | 0.8% |

### Rapides Parish
**Total:** 1,047

| Race | Count | % |
|------|-------|---|
| Black | 659 | 62.9% |
| White | 372 | 35.5% |
| Unknown | 14 | 1.3% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 42

| Race | Count | % |
|------|-------|---|
| Black | 21 | 50.0% |
| White | 20 | 47.6% |
| Asian/PacificIslander | 1 | 2.4% |

### Richland Parish
**Total:** 715

| Race | Count | % |
|------|-------|---|
| Black | 493 | 69.0% |
| White | 211 | 29.5% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 4 | 0.6% |

### Sabine Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| White | 109 | 57.4% |
| Black | 77 | 40.5% |
| Unknown | 3 | 1.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 41 | 85.4% |
| White | 6 | 12.5% |
| Unknown | 1 | 2.1% |

### St. Bernard Parish
**Total:** 232

| Race | Count | % |
|------|-------|---|
| Black | 134 | 57.8% |
| White | 93 | 40.1% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 2 | 0.9% |

### St. Charles Parish
**Total:** 175

| Race | Count | % |
|------|-------|---|
| Unknown | 102 | 58.3% |
| White | 73 | 41.7% |

### St. Helena Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| Black | 29 | 70.7% |
| White | 12 | 29.3% |

### St. James Parish
**Total:** 78

| Race | Count | % |
|------|-------|---|
| Black | 66 | 84.6% |
| White | 12 | 15.4% |

### St. John the Baptist Parish
**Total:** 232

| Race | Count | % |
|------|-------|---|
| Unknown | 156 | 67.2% |
| White | 76 | 32.8% |

### St. Landry Parish
**Total:** 132

| Race | Count | % |
|------|-------|---|
| Black | 87 | 65.9% |
| White | 43 | 32.6% |
| Unknown | 2 | 1.5% |

### St. Martin Parish
**Total:** 213

| Race | Count | % |
|------|-------|---|
| Black | 107 | 50.2% |
| White | 98 | 46.0% |
| Unknown | 8 | 3.8% |

### St. Mary Parish
**Total:** 290

| Race | Count | % |
|------|-------|---|
| Black | 151 | 52.1% |
| White | 138 | 47.6% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 912

| Race | Count | % |
|------|-------|---|
| White | 462 | 50.7% |
| Black | 406 | 44.5% |
| Unknown | 42 | 4.6% |
| American Indian/Alaska Native | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Sulphur Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 11 | 78.6% |
| Black | 3 | 21.4% |

### Tangipahoa Parish
**Total:** 703

| Race | Count | % |
|------|-------|---|
| Black | 468 | 66.6% |
| White | 232 | 33.0% |
| Unknown | 3 | 0.4% |

### Tensas Parish
**Total:** 572

| Race | Count | % |
|------|-------|---|
| Black | 386 | 67.5% |
| White | 174 | 30.4% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 571

| Race | Count | % |
|------|-------|---|
| Black | 317 | 55.5% |
| White | 242 | 42.4% |
| American Indian/Alaska Native | 12 | 2.1% |

### Vermillion Parish
**Total:** 114

| Race | Count | % |
|------|-------|---|
| Black | 56 | 49.1% |
| White | 55 | 48.2% |
| Unknown | 2 | 1.8% |
| Asian/PacificIslander | 1 | 0.9% |

### Vernon Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| White | 126 | 68.9% |
| Black | 55 | 30.1% |
| Asian/PacificIslander | 1 | 0.5% |
| Unknown | 1 | 0.5% |

### Ville Platte Police Department
**Total:** 31

| Race | Count | % |
|------|-------|---|
| Black | 18 | 58.1% |
| White | 12 | 38.7% |
| Unknown | 1 | 3.2% |

### Washington Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Black | 101 | 53.7% |
| White | 86 | 45.7% |
| Unknown | 1 | 0.5% |

### Webster Parish
**Total:** 453

| Race | Count | % |
|------|-------|---|
| Black | 236 | 52.1% |
| White | 210 | 46.4% |
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
**Total:** 204

| Race | Count | % |
|------|-------|---|
| Black | 131 | 64.2% |
| White | 73 | 35.8% |

### Winn Parish
**Total:** 146

| Race | Count | % |
|------|-------|---|
| Black | 74 | 50.7% |
| White | 72 | 49.3% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
