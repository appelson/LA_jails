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

_Last updated: 2026-06-15 23:07 UTC_

**Total inmates (latest scrape):** 26,631 across 72 parishes/jails

### Acadia Parish
**Total:** 183

| Race | Count | % |
|------|-------|---|
| White | 99 | 54.1% |
| Black | 82 | 44.8% |
| Asian/PacificIslander | 1 | 0.5% |
| American Indian/Alaska Native | 1 | 0.5% |

### Allen Parish
**Total:** 117

| Race | Count | % |
|------|-------|---|
| White | 75 | 64.1% |
| Black | 40 | 34.2% |
| Unknown | 1 | 0.9% |
| American Indian/Alaska Native | 1 | 0.9% |

### Ascension Parish
**Total:** 544

| Race | Count | % |
|------|-------|---|
| Black | 289 | 53.1% |
| White | 218 | 40.1% |
| Unknown | 33 | 6.1% |
| Asian/PacificIslander | 4 | 0.7% |

### Assumption Parish
**Total:** 156

| Race | Count | % |
|------|-------|---|
| Unknown | 84 | 53.8% |
| White | 72 | 46.2% |

### Avoyelles Parish
**Total:** 360

| Race | Count | % |
|------|-------|---|
| Black | 204 | 56.7% |
| White | 152 | 42.2% |
| Unknown | 3 | 0.8% |
| Asian/PacificIslander | 1 | 0.3% |

### Beauregard Parish
**Total:** 159

| Race | Count | % |
|------|-------|---|
| White | 110 | 69.2% |
| Black | 49 | 30.8% |

### Bienville Parish
**Total:** 35

| Race | Count | % |
|------|-------|---|
| White | 22 | 62.9% |
| Unknown | 13 | 37.1% |

### Bogalusa Police Department
**Total:** 23

| Race | Count | % |
|------|-------|---|
| Black | 13 | 56.5% |
| White | 10 | 43.5% |

### Bossier City Police Department
**Total:** 37

| Race | Count | % |
|------|-------|---|
| Black | 21 | 56.8% |
| White | 15 | 40.5% |
| Asian/PacificIslander | 1 | 2.7% |

### Bossier Parish
**Total:** 1,107

| Race | Count | % |
|------|-------|---|
| Black | 608 | 54.9% |
| White | 498 | 45.0% |
| American Indian/Alaska Native | 1 | 0.1% |

### Caddo Parish
**Total:** 1,671

| Race | Count | % |
|------|-------|---|
| Black | 1,252 | 74.9% |
| White | 391 | 23.4% |
| Unknown | 26 | 1.6% |
| Asian/PacificIslander | 2 | 0.1% |

### Calcasieu Parish
**Total:** 1,085

| Race | Count | % |
|------|-------|---|
| Black | 604 | 55.7% |
| White | 440 | 40.6% |
| Unknown | 40 | 3.7% |
| Asian/PacificIslander | 1 | 0.1% |

### Caldwell Parish
**Total:** 611

| Race | Count | % |
|------|-------|---|
| Black | 390 | 63.8% |
| White | 201 | 32.9% |
| American Indian/Alaska Native | 19 | 3.1% |
| Unknown | 1 | 0.2% |

### Cameron Parish
**Total:** 25

| Race | Count | % |
|------|-------|---|
| White | 22 | 88.0% |
| Black | 2 | 8.0% |
| Unknown | 1 | 4.0% |

### Catahoula Parish
**Total:** 130

| Race | Count | % |
|------|-------|---|
| Black | 91 | 70.0% |
| White | 38 | 29.2% |
| Unknown | 1 | 0.8% |

### Claiborne Parish
**Total:** 664

| Race | Count | % |
|------|-------|---|
| Black | 413 | 62.2% |
| White | 251 | 37.8% |

### Concordia Parish
**Total:** 800

| Race | Count | % |
|------|-------|---|
| White | 452 | 56.5% |
| Black | 346 | 43.2% |
| Unknown | 2 | 0.2% |

### DeSoto Parish
**Total:** 126

| Race | Count | % |
|------|-------|---|
| Black | 72 | 57.1% |
| White | 52 | 41.3% |
| American Indian/Alaska Native | 1 | 0.8% |
| Asian/PacificIslander | 1 | 0.8% |

### East Baton Rouge Parish
**Total:** 1,336

| Race | Count | % |
|------|-------|---|
| Black | 1,054 | 78.9% |
| White | 215 | 16.1% |
| Unknown | 65 | 4.9% |
| Asian/PacificIslander | 2 | 0.1% |

### East Feliciana Parish
**Total:** 265

| Race | Count | % |
|------|-------|---|
| Black | 169 | 63.8% |
| White | 95 | 35.8% |
| Asian/PacificIslander | 1 | 0.4% |

### Evangeline Parish
**Total:** 151

| Race | Count | % |
|------|-------|---|
| Black | 80 | 53.0% |
| White | 69 | 45.7% |
| Unknown | 2 | 1.3% |

### Franklin Parish
**Total:** 821

| Race | Count | % |
|------|-------|---|
| Black | 529 | 64.4% |
| White | 281 | 34.2% |
| Unknown | 11 | 1.3% |

### Hammond Police Department
**Total:** 13

| Race | Count | % |
|------|-------|---|
| Black | 8 | 61.5% |
| White | 4 | 30.8% |
| Unknown | 1 | 7.7% |

### Iberia Parish
**Total:** 449

| Race | Count | % |
|------|-------|---|
| Black | 267 | 59.5% |
| White | 172 | 38.3% |
| Asian/PacificIslander | 5 | 1.1% |
| Unknown | 4 | 0.9% |
| American Indian/Alaska Native | 1 | 0.2% |

### Iberville Parish
**Total:** 99

| Race | Count | % |
|------|-------|---|
| Black | 64 | 64.6% |
| White | 34 | 34.3% |
| Unknown | 1 | 1.0% |

### Jackson Parish
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### Jefferson Davis Parish
**Total:** 155

| Race | Count | % |
|------|-------|---|
| White | 82 | 52.9% |
| Black | 69 | 44.5% |
| American Indian/Alaska Native | 3 | 1.9% |
| Unknown | 1 | 0.6% |

### Jefferson Parish
**Total:** 1,160

| Race | Count | % |
|------|-------|---|
| Black | 757 | 65.3% |
| White | 397 | 34.2% |
| Unknown | 6 | 0.5% |

### Kinder Police Department
**Total:** 1

| Race | Count | % |
|------|-------|---|
| Unknown | 1 | 100.0% |

### LaSalle Parish
**Total:** 71

| Race | Count | % |
|------|-------|---|
| White | 45 | 63.4% |
| Black | 25 | 35.2% |
| Unknown | 1 | 1.4% |

### Lafayette Parish
**Total:** 879

| Race | Count | % |
|------|-------|---|
| Black | 573 | 65.2% |
| White | 289 | 32.9% |
| Unknown | 17 | 1.9% |

### Lafourche Parish
**Total:** 746

| Race | Count | % |
|------|-------|---|
| Black | 383 | 51.3% |
| White | 357 | 47.9% |
| American Indian/Alaska Native | 4 | 0.5% |
| Unknown | 1 | 0.1% |
| Asian/PacificIslander | 1 | 0.1% |

### Leesville Police Department
**Total:** 3

| Race | Count | % |
|------|-------|---|
| White | 2 | 66.7% |
| Black | 1 | 33.3% |

### Lincoln Parish
**Total:** 373

| Race | Count | % |
|------|-------|---|
| Black | 285 | 76.4% |
| White | 85 | 22.8% |
| Unknown | 3 | 0.8% |

### Livingston Parish
**Total:** 795

| Race | Count | % |
|------|-------|---|
| White | 564 | 70.9% |
| Black | 220 | 27.7% |
| Unknown | 9 | 1.1% |
| Asian/PacificIslander | 1 | 0.1% |
| American Indian/Alaska Native | 1 | 0.1% |

### Madison Parish
**Total:** 144

| Race | Count | % |
|------|-------|---|
| Black | 114 | 79.2% |
| White | 28 | 19.4% |
| Unknown | 2 | 1.4% |

### Morehouse Parish
**Total:** 201

| Race | Count | % |
|------|-------|---|
| Black | 137 | 68.2% |
| White | 64 | 31.8% |

### Natchitoches Parish
**Total:** 192

| Race | Count | % |
|------|-------|---|
| Black | 145 | 75.5% |
| White | 45 | 23.4% |
| Unknown | 2 | 1.0% |

### Oakdale Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| White | 2 | 100.0% |

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
**Total:** 1,323

| Race | Count | % |
|------|-------|---|
| Black | 883 | 66.7% |
| White | 426 | 32.2% |
| Unknown | 14 | 1.1% |

### Plaquemines Parish
**Total:** 650

| Race | Count | % |
|------|-------|---|
| Black | 430 | 66.2% |
| White | 199 | 30.6% |
| Unknown | 13 | 2.0% |
| Asian/PacificIslander | 6 | 0.9% |
| American Indian/Alaska Native | 2 | 0.3% |

### Pointe Coupee Parish
**Total:** 106

| Race | Count | % |
|------|-------|---|
| Black | 66 | 62.3% |
| White | 37 | 34.9% |
| Unknown | 2 | 1.9% |
| American Indian/Alaska Native | 1 | 0.9% |

### Rapides Parish
**Total:** 1,024

| Race | Count | % |
|------|-------|---|
| Black | 652 | 63.7% |
| White | 353 | 34.5% |
| Unknown | 17 | 1.7% |
| Asian/PacificIslander | 2 | 0.2% |

### Red River Parish
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 28 | 58.3% |
| White | 19 | 39.6% |
| Asian/PacificIslander | 1 | 2.1% |

### Richland Parish
**Total:** 734

| Race | Count | % |
|------|-------|---|
| Black | 506 | 68.9% |
| White | 219 | 29.8% |
| Unknown | 6 | 0.8% |
| Asian/PacificIslander | 3 | 0.4% |

### Sabine Parish
**Total:** 195

| Race | Count | % |
|------|-------|---|
| White | 109 | 55.9% |
| Black | 83 | 42.6% |
| Unknown | 2 | 1.0% |
| American Indian/Alaska Native | 1 | 0.5% |

### Shreveport Police Department
**Total:** 54

| Race | Count | % |
|------|-------|---|
| Black | 40 | 74.1% |
| White | 13 | 24.1% |
| Unknown | 1 | 1.9% |

### St. Bernard Parish
**Total:** 225

| Race | Count | % |
|------|-------|---|
| Black | 134 | 59.6% |
| White | 87 | 38.7% |
| Asian/PacificIslander | 3 | 1.3% |
| Unknown | 1 | 0.4% |

### St. Charles Parish
**Total:** 187

| Race | Count | % |
|------|-------|---|
| Unknown | 112 | 59.9% |
| White | 75 | 40.1% |

### St. Helena Parish
**Total:** 48

| Race | Count | % |
|------|-------|---|
| Black | 33 | 68.8% |
| White | 14 | 29.2% |
| Unknown | 1 | 2.1% |

### St. James Parish
**Total:** 68

| Race | Count | % |
|------|-------|---|
| Black | 57 | 83.8% |
| White | 11 | 16.2% |

### St. John the Baptist Parish
**Total:** 203

| Race | Count | % |
|------|-------|---|
| Unknown | 130 | 64.0% |
| White | 73 | 36.0% |

### St. Landry Parish
**Total:** 120

| Race | Count | % |
|------|-------|---|
| Black | 78 | 65.0% |
| White | 40 | 33.3% |
| Unknown | 2 | 1.7% |

### St. Martin Parish
**Total:** 208

| Race | Count | % |
|------|-------|---|
| Black | 108 | 51.9% |
| White | 90 | 43.3% |
| Unknown | 9 | 4.3% |
| American Indian/Alaska Native | 1 | 0.5% |

### St. Mary Parish
**Total:** 280

| Race | Count | % |
|------|-------|---|
| Black | 147 | 52.5% |
| White | 132 | 47.1% |
| Asian/PacificIslander | 1 | 0.4% |

### St. Tammany Parish
**Total:** 884

| Race | Count | % |
|------|-------|---|
| White | 463 | 52.4% |
| Black | 380 | 43.0% |
| Unknown | 38 | 4.3% |
| Asian/PacificIslander | 2 | 0.2% |
| American Indian/Alaska Native | 1 | 0.1% |

### Sulphur Police Department
**Total:** 18

| Race | Count | % |
|------|-------|---|
| White | 16 | 88.9% |
| Black | 2 | 11.1% |

### Tangipahoa Parish
**Total:** 661

| Race | Count | % |
|------|-------|---|
| Black | 415 | 62.8% |
| White | 245 | 37.1% |
| Unknown | 1 | 0.2% |

### Tensas Parish
**Total:** 568

| Race | Count | % |
|------|-------|---|
| Black | 375 | 66.0% |
| White | 181 | 31.9% |
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
**Total:** 132

| Race | Count | % |
|------|-------|---|
| White | 68 | 51.5% |
| Black | 60 | 45.5% |
| Unknown | 3 | 2.3% |
| Asian/PacificIslander | 1 | 0.8% |

### Vernon Parish
**Total:** 160

| Race | Count | % |
|------|-------|---|
| White | 109 | 68.1% |
| Black | 48 | 30.0% |
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
**Total:** 188

| Race | Count | % |
|------|-------|---|
| White | 96 | 51.1% |
| Black | 92 | 48.9% |

### Webster Parish
**Total:** 448

| Race | Count | % |
|------|-------|---|
| Black | 237 | 52.9% |
| White | 205 | 45.8% |
| Unknown | 4 | 0.9% |
| Asian/PacificIslander | 2 | 0.4% |

### West Baton Rouge Parish
**Total:** 127

| Race | Count | % |
|------|-------|---|
| Black | 85 | 66.9% |
| White | 36 | 28.3% |
| Unknown | 5 | 3.9% |
| Asian/PacificIslander | 1 | 0.8% |

### West Carroll Parish
**Total:** 29

| Race | Count | % |
|------|-------|---|
| White | 24 | 82.8% |
| Black | 5 | 17.2% |

### West Felician Parish
**Total:** 188

| Race | Count | % |
|------|-------|---|
| Black | 123 | 65.4% |
| White | 65 | 34.6% |

### Winn Parish
**Total:** 145

| Race | Count | % |
|------|-------|---|
| Black | 79 | 54.5% |
| White | 66 | 45.5% |

### Winnfield Police Department
**Total:** 2

| Race | Count | % |
|------|-------|---|
| Black | 2 | 100.0% |
