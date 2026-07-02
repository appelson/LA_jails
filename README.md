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

_Last updated: 2026-07-02 02:52 UTC_

**Total inmates (latest scrape):** 26,662 across 72 parishes/jails

### Acadia Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| White | 102 | 54.5% |
| Black | 83 | 44.4% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| White | 69 | 61.6% |
| Black | 40 | 35.7% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 522

| Race | Count | % |
|------|-------|---|
| Black | 276 | 52.9% |
| White | 212 | 40.6% |
| Unknown | 30 | 5.7% |
| Asian/PacificIslander | 4 | 0.8% |

### Assumption Parish
**Total:** 153

| Race | Count | % |
|------|-------|---|
| Unknown | 86 | 56.2% |
| White | 67 | 43.8% |

### Avoyelles Parish
**Total:** 358

| Race | Count | % |
|------|-------|---|
| Black | 195 | 54.5% |
| White | 159 | 44.4% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| White | 100 | 69.4% |
| Black | 44 | 30.6% |

### Bienville Parish
**Total:** 41

| Race | Count | % |
|------|-------|---|
| White | 23 | 56.1% |
| Unknown | 18 | 43.9% |

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
| Black | 30 | 62.5% |
| White | 18 | 37.5% |

### Bossier Parish
**Total:** 1,127

| Race | Count | % |
|------|-------|---|
| Black | 623 | 55.3% |
| White | 503 | 44.6% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,697

| Race | Count | % |
|------|-------|---|
| Black | 1,281 | 75.5% |
| White | 386 | 22.7% |
| Unknown | 28 | 1.6% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,100

| Race | Count | % |
|------|-------|---|
| Black | 614 | 55.8% |
| White | 442 | 40.2% |
| Unknown | 41 | 3.7% |
| Asian/PacificIslander | 3 | 0.3% |

### Caldwell Parish
**Total:** 620

| Race | Count | % |
|------|-------|---|
| Black | 390 | 62.9% |
| White | 209 | 33.7% |
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
| Black | 419 | 61.8% |
| White | 259 | 38.2% |

### Concordia Parish
**Total:** 799

| Race | Count | % |
|------|-------|---|
| White | 451 | 56.4% |
| Black | 347 | 43.4% |
| Unknown | 1 | 0.1% |

### DeSoto Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 70 | 58.3% |
| White | 49 | 40.8% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,333

| Race | Count | % |
|------|-------|---|
| Black | 1,055 | 79.1% |
| White | 206 | 15.5% |
| Unknown | 70 | 5.3% |
| Asian/PacificIslander | 2 | 0.2% |

### East Feliciana Parish
**Total:** 272

| Race | Count | % |
|------|-------|---|
| Black | 174 | 64.0% |
| White | 97 | 35.7% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 168

| Race | Count | % |
|------|-------|---|
| Black | 95 | 56.5% |
| White | 72 | 42.9% |
| Unknown | 1 | 0.6% |

### Franklin Parish
**Total:** 842

| Race | Count | % |
|------|-------|---|
| Black | 552 | 65.6% |
| White | 280 | 33.3% |
| Unknown | 10 | 1.2% |

### Hammond Police Department
**Total:** 14

| Race | Count | % |
|------|-------|---|
| Black | 10 | 71.4% |
| White | 3 | 21.4% |
| Unknown | 1 | 7.1% |

### Iberia Parish
**Total:** 458

| Race | Count | % |
|------|-------|---|
| Black | 266 | 58.1% |
| White | 181 | 39.5% |
| Unknown | 5 | 1.1% |
| Asian/PacificIslander | 5 | 1.1% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 36

| Race | Count | % |
|------|-------|---|
| Black | 21 | 58.3% |
| White | 15 | 41.7% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| White | 84 | 52.8% |
| Black | 71 | 44.7% |
| American Indian/Alaska Native | 3 | 1.9% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,139

| Race | Count | % |
|------|-------|---|
| Black | 734 | 64.4% |
| White | 400 | 35.1% |
| Unknown | 5 | 0.4% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| White | 1 | 100.0% |

### LaSalle Parish
**Total:** 74

| Race | Count | % |
|------|-------|---|
| White | 47 | 63.5% |
| Black | 26 | 35.1% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 825

| Race | Count | % |
|------|-------|---|
| Black | 533 | 64.6% |
| White | 278 | 33.7% |
| Unknown | 13 | 1.6% |
| Asian/PacificIslander | 1 | 0.1% |

### Lafourche Parish
**Total:** 762

| Race | Count | % |
|------|-------|---|
| Black | 388 | 50.9% |
| White | 370 | 48.6% |
| American Indian/Alaska Native | 3 | 0.4% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 371

| Race | Count | % |
|------|-------|---|
| Black | 277 | 74.7% |
| White | 91 | 24.5% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 833

| Race | Count | % |
|------|-------|---|
| White | 587 | 70.5% |
| Black | 234 | 28.1% |
| Unknown | 10 | 1.2% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 143

| Race | Count | % |
|------|-------|---|
| Black | 115 | 80.4% |
| White | 27 | 18.9% |
| Unknown | 1 | 0.7% |

### Morehouse Parish
**Total:** 212

| Race | Count | % |
|------|-------|---|
| Black | 151 | 71.2% |
| White | 61 | 28.8% |

### Natchitoches Parish
**Total:** 186

| Race | Count | % |
|------|-------|---|
| Black | 138 | 74.2% |
| White | 45 | 24.2% |
| Unknown | 3 | 1.6% |

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
**Total:** 1,292

| Race | Count | % |
|------|-------|---|
| Black | 862 | 66.7% |
| White | 416 | 32.2% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 685

| Race | Count | % |
|------|-------|---|
| Black | 442 | 64.5% |
| White | 217 | 31.7% |
| Unknown | 15 | 2.2% |
| Asian/PacificIslander | 7 | 1.0% |
| American Indian/Alaska Native | 4 | 0.6% |

### Pointe Coupee Parish
**Total:** 112

| Race | Count | % |
|------|-------|---|
| Black | 69 | 61.6% |
| White | 40 | 35.7% |
| Unknown | 2 | 1.8% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,025

| Race | Count | % |
|------|-------|---|
| Black | 657 | 64.1% |
| White | 352 | 34.3% |
| Unknown | 14 | 1.4% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 45

| Race | Count | % |
|------|-------|---|
| Black | 22 | 48.9% |
| White | 22 | 48.9% |
| Asian/PacificIslander | 1 | 2.2% |

### Richland Parish
**Total:** 697

| Race | Count | % |
|------|-------|---|
| Black | 482 | 69.2% |
| White | 205 | 29.4% |
| Unknown | 7 | 1.0% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 193

| Race | Count | % |
|------|-------|---|
| White | 107 | 55.4% |
| Black | 83 | 43.0% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 54

| Race | Count | % |
|------|-------|---|
| Black | 40 | 74.1% |
| White | 14 | 25.9% |

### St. Bernard Parish
**Total:** 215

| Race | Count | % |
|------|-------|---|
| Black | 127 | 59.1% |
| White | 85 | 39.5% |
| Asian/PacificIslander | 2 | 0.9% |
| Unknown | 1 | 0.5% |

### St. Charles Parish
**Total:** 199

| Race | Count | % |
|------|-------|---|
| Unknown | 119 | 59.8% |
| White | 80 | 40.2% |

### St. Helena Parish
**Total:** 53

| Race | Count | % |
|------|-------|---|
| Black | 37 | 69.8% |
| White | 15 | 28.3% |
| Unknown | 1 | 1.9% |

### St. James Parish
**Total:** 63

| Race | Count | % |
|------|-------|---|
| Black | 53 | 84.1% |
| White | 10 | 15.9% |

### St. John the Baptist Parish
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Unknown | 134 | 66.0% |
| White | 69 | 34.0% |

### St. Landry Parish
**Total:** 125

| Race | Count | % |
|------|-------|---|
| Black | 80 | 64.0% |
| White | 43 | 34.4% |
| Unknown | 2 | 1.6% |

### St. Martin Parish
**Total:** 217

| Race | Count | % |
|------|-------|---|
| Black | 112 | 51.6% |
| White | 95 | 43.8% |
| Unknown | 9 | 4.1% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 292

| Race | Count | % |
|------|-------|---|
| Black | 156 | 53.4% |
| White | 135 | 46.2% |
| Asian/PacificIslander | 1 | 0.3% |

### St. Tammany Parish
**Total:** 868

| Race | Count | % |
|------|-------|---|
| White | 460 | 53.0% |
| Black | 368 | 42.4% |
| Unknown | 37 | 4.3% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 15

| Race | Count | % |
|------|-------|---|
| White | 13 | 86.7% |
| Black | 2 | 13.3% |

### Tangipahoa Parish
**Total:** 662

| Race | Count | % |
|------|-------|---|
| Black | 425 | 64.2% |
| White | 236 | 35.6% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 572

| Race | Count | % |
|------|-------|---|
| Black | 379 | 66.3% |
| White | 181 | 31.6% |
| Unknown | 12 | 2.1% |

### Terrebonne Parish
**Total:** 506

| Race | Count | % |
|------|-------|---|
| Black | 271 | 53.6% |
| White | 225 | 44.5% |
| American Indian/Alaska Native | 9 | 1.8% |
| Unknown | 1 | 0.2% |

### Vermillion Parish
**Total:** 134

| Race | Count | % |
|------|-------|---|
| White | 69 | 51.5% |
| Black | 62 | 46.3% |
| Unknown | 2 | 1.5% |
| Asian/PacificIslander | 1 | 0.7% |

### Vernon Parish
**Total:** 167

| Race | Count | % |
|------|-------|---|
| White | 118 | 70.7% |
| Black | 47 | 28.1% |
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
**Total:** 197

| Race | Count | % |
|------|-------|---|
| White | 99 | 50.3% |
| Black | 98 | 49.7% |

### Webster Parish
**Total:** 443

| Race | Count | % |
|------|-------|---|
| Black | 237 | 53.5% |
| White | 200 | 45.1% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.5% |

### West Baton Rouge Parish
**Total:** 128

| Race | Count | % |
|------|-------|---|
| Black | 87 | 68.0% |
| White | 35 | 27.3% |
| Unknown | 4 | 3.1% |
| Asian/PacificIslander | 2 | 1.6% |

### West Carroll Parish
**Total:** 30

| Race | Count | % |
|------|-------|---|
| White | 23 | 76.7% |
| Black | 7 | 23.3% |

### West Felician Parish
**Total:** 194

| Race | Count | % |
|------|-------|---|
| Black | 126 | 64.9% |
| White | 68 | 35.1% |

### Winn Parish
**Total:** 148

| Race | Count | % |
|------|-------|---|
| Black | 77 | 52.0% |
| White | 71 | 48.0% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
