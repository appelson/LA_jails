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

_Last updated: 2026-05-06 02:23 UTC_

**Total inmates (latest scrape):** 25,817 across 72 parishes/jails

### Acadia Parish
**Total:** 173

| Race | Count | % |
|------|-------|---|
| White | 93 | 53.8% |
| Black | 78 | 45.1% |
| Asian/PacificIslander | 1 | 0.6% |
| American Indian/Alaska Native | 1 | 0.6% |

### Allen Parish
**Total:** 136

| Race | Count | % |
|------|-------|---|
| White | 85 | 62.5% |
| Black | 49 | 36.0% |
| Unknown | 1 | 0.7% |
| American Indian/Alaska Native | 1 | 0.7% |

### Ascension Parish
**Total:** 498

| Race | Count | % |
|------|-------|---|
| Black | 263 | 52.8% |
| White | 200 | 40.2% |
| Unknown | 31 | 6.2% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 148

| Race | Count | % |
|------|-------|---|
| Unknown | 77 | 52.0% |
| White | 71 | 48.0% |

### Avoyelles Parish
**Total:** 397

| Race | Count | % |
|------|-------|---|
| Black | 213 | 53.7% |
| White | 178 | 44.8% |
| Unknown | 5 | 1.3% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 190

| Race | Count | % |
|------|-------|---|
| White | 132 | 69.5% |
| Black | 58 | 30.5% |

### Bienville Parish
**Total:** 37

| Race | Count | % |
|------|-------|---|
| White | 22 | 59.5% |
| Unknown | 15 | 40.5% |

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
| Black | 32 | 66.7% |
| White | 16 | 33.3% |

### Bossier Parish
**Total:** 1,122

| Race | Count | % |
|------|-------|---|
| Black | 615 | 54.8% |
| White | 504 | 44.9% |
| Unknown | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,603

| Race | Count | % |
|------|-------|---|
| Black | 1,187 | 74.0% |
| White | 380 | 23.7% |
| Unknown | 33 | 2.1% |
| Asian/PacificIslander | 3 | 0.2% |

### Calcasieu Parish
**Total:** 1,028

| Race | Count | % |
|------|-------|---|
| Black | 557 | 54.2% |
| White | 427 | 41.5% |
| Unknown | 42 | 4.1% |
| Asian/PacificIslander | 2 | 0.2% |

### Caldwell Parish
**Total:** 611

| Race | Count | % |
|------|-------|---|
| Black | 398 | 65.1% |
| White | 193 | 31.6% |
| American Indian/Alaska Native | 20 | 3.3% |

### Cameron Parish
**Total:** 21

| Race | Count | % |
|------|-------|---|
| White | 19 | 90.5% |
| Black | 2 | 9.5% |

### Catahoula Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 92 | 70.8% |
| White | 37 | 28.5% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 659

| Race | Count | % |
|------|-------|---|
| Black | 401 | 60.8% |
| White | 258 | 39.2% |

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
| Black | 165 | 61.8% |
| White | 101 | 37.8% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 83

| Race | Count | % |
|------|-------|---|
| White | 43 | 51.8% |
| Black | 39 | 47.0% |
| Unknown | 1 | 1.2% |

### Franklin Parish
**Total:** 851

| Race | Count | % |
|------|-------|---|
| Black | 555 | 65.2% |
| White | 285 | 33.5% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |

### Hammond Police Department
**Total:** 8

| Race | Count | % |
|------|-------|---|
| Black | 6 | 75.0% |
| White | 2 | 25.0% |

### Iberia Parish
**Total:** 441

| Race | Count | % |
|------|-------|---|
| Black | 274 | 62.1% |
| White | 160 | 36.3% |
| Unknown | 3 | 0.7% |
| Asian/PacificIslander | 3 | 0.7% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 105

| Race | Count | % |
|------|-------|---|
| Black | 65 | 61.9% |
| White | 38 | 36.2% |
| Unknown | 2 | 1.9% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 153

| Race | Count | % |
|------|-------|---|
| White | 78 | 51.0% |
| Black | 70 | 45.8% |
| American Indian/Alaska Native | 3 | 2.0% |
| Asian/PacificIslander | 1 | 0.7% |
| Unknown | 1 | 0.7% |

### Jefferson Parish
**Total:** 1,183

| Race | Count | % |
|------|-------|---|
| Black | 771 | 65.2% |
| White | 399 | 33.7% |
| Unknown | 9 | 0.8% |
| Asian/PacificIslander | 4 | 0.3% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 72

| Race | Count | % |
|------|-------|---|
| White | 50 | 69.4% |
| Black | 21 | 29.2% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 839

| Race | Count | % |
|------|-------|---|
| Black | 526 | 62.7% |
| White | 299 | 35.6% |
| Unknown | 14 | 1.7% |

### Lafourche Parish
**Total:** 743

| Race | Count | % |
|------|-------|---|
| Black | 380 | 51.1% |
| White | 356 | 47.9% |
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
**Total:** 377

| Race | Count | % |
|------|-------|---|
| Black | 280 | 74.3% |
| White | 95 | 25.2% |
| Unknown | 2 | 0.5% |

### Livingston Parish
**Total:** 794

| Race | Count | % |
|------|-------|---|
| White | 570 | 71.8% |
| Black | 215 | 27.1% |
| Unknown | 7 | 0.9% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 141

| Race | Count | % |
|------|-------|---|
| Black | 110 | 78.0% |
| White | 30 | 21.3% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 205

| Race | Count | % |
|------|-------|---|
| Black | 139 | 67.8% |
| White | 66 | 32.2% |

### Natchitoches Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| Black | 143 | 74.5% |
| White | 45 | 23.4% |
| Unknown | 3 | 1.6% |
| Asian/PacificIslander | 1 | 0.5% |

### Oakdale Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

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
**Total:** 1,275

| Race | Count | % |
|------|-------|---|
| Black | 844 | 66.2% |
| White | 416 | 32.6% |
| Unknown | 15 | 1.2% |

### Plaquemines Parish
**Total:** 635

| Race | Count | % |
|------|-------|---|
| Black | 413 | 65.0% |
| White | 203 | 32.0% |
| Unknown | 11 | 1.7% |
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
**Total:** 993

| Race | Count | % |
|------|-------|---|
| Black | 622 | 62.6% |
| White | 353 | 35.5% |
| Unknown | 16 | 1.6% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 38

| Race | Count | % |
|------|-------|---|
| Black | 24 | 63.2% |
| White | 13 | 34.2% |
| Asian/PacificIslander | 1 | 2.6% |

### Richland Parish
**Total:** 716

| Race | Count | % |
|------|-------|---|
| Black | 492 | 68.7% |
| White | 214 | 29.9% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 178

| Race | Count | % |
|------|-------|---|
| White | 101 | 56.7% |
| Black | 77 | 43.3% |

### Shreveport Police Department
**Total:** 53

| Race | Count | % |
|------|-------|---|
| Black | 46 | 86.8% |
| White | 7 | 13.2% |

### St. Bernard Parish
**Total:** 219

| Race | Count | % |
|------|-------|---|
| Black | 129 | 58.9% |
| White | 87 | 39.7% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 172

| Race | Count | % |
|------|-------|---|
| Unknown | 98 | 57.0% |
| White | 74 | 43.0% |

### St. Helena Parish
**Total:** 77

| Race | Count | % |
|------|-------|---|
| Black | 56 | 72.7% |
| White | 16 | 20.8% |
| Unknown | 4 | 5.2% |
| American Indian/Alaska Native | 1 | 1.3% |

### St. James Parish
**Total:** 75

| Race | Count | % |
|------|-------|---|
| Black | 59 | 78.7% |
| White | 16 | 21.3% |

### St. John the Baptist Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| Unknown | 124 | 63.3% |
| White | 72 | 36.7% |

### St. Landry Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 70 | 62.5% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |

### St. Martin Parish
**Total:** 196

| Race | Count | % |
|------|-------|---|
| Black | 97 | 49.5% |
| White | 91 | 46.4% |
| Unknown | 7 | 3.6% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 242

| Race | Count | % |
|------|-------|---|
| Black | 124 | 51.2% |
| White | 117 | 48.3% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 807

| Race | Count | % |
|------|-------|---|
| White | 407 | 50.4% |
| Black | 359 | 44.5% |
| Unknown | 36 | 4.5% |
| Asian/PacificIslander | 3 | 0.4% |
| American Indian/Alaska Native | 2 | 0.2% |

### Sulphur Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| White | 12 | 85.7% |
| Black | 2 | 14.3% |

### Tangipahoa Parish
**Total:** 626

| Race | Count | % |
|------|-------|---|
| Black | 379 | 60.5% |
| White | 246 | 39.3% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 556

| Race | Count | % |
|------|-------|---|
| Black | 365 | 65.6% |
| White | 175 | 31.5% |
| Unknown | 16 | 2.9% |

### Terrebonne Parish
**Total:** 470

| Race | Count | % |
|------|-------|---|
| Black | 243 | 51.7% |
| White | 220 | 46.8% |
| American Indian/Alaska Native | 7 | 1.5% |

### Vermillion Parish
**Total:** 123

| Race | Count | % |
|------|-------|---|
| White | 64 | 52.0% |
| Black | 57 | 46.3% |
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
**Total:** 158

| Race | Count | % |
|------|-------|---|
| Black | 84 | 53.2% |
| White | 74 | 46.8% |

### Webster Parish
**Total:** 438

| Race | Count | % |
|------|-------|---|
| Black | 216 | 49.3% |
| White | 215 | 49.1% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 3 | 0.7% |

### West Baton Rouge Parish
**Total:** 137

| Race | Count | % |
|------|-------|---|
| Black | 86 | 62.8% |
| White | 47 | 34.3% |
| Unknown | 3 | 2.2% |
| Asian/PacificIslander | 1 | 0.7% |

### West Carroll Parish
**Total:** 31

| Race | Count | % |
|------|-------|---|
| White | 27 | 87.1% |
| Black | 3 | 9.7% |
| Unknown | 1 | 3.2% |

### West Felician Parish
**Total:** 178

| Race | Count | % |
|------|-------|---|
| Black | 111 | 62.4% |
| White | 67 | 37.6% |

### Winn Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| White | 77 | 51.0% |
| Black | 74 | 49.0% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
