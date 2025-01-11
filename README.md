**Features:**

* Schedules data scraping tasks at regular intervals (default: every 5 minutes).
* Checks for duplicate entries in MongoDB before uploading new data.
* Provides a modular and scalable workflow for data scraping and storage.

**Requirements:**

* Python 3.x)
* Bikroy_Dag library (custom library containing scraping and MongoDB functions)
* MongoDB instance (local or remote)

**Project Structure:**

* `Bikroy_Dag/`: Contains the custom Python library for scraping and MongoDB operations.
    * `src/`: Subdirectory for source code files within the library.
        * `getMobileData.py`: Script to scrape mobile data from Bikroy.com.
        * `checkMongoForDuplicates.py`: Script to check for duplicate entries in MongoDB.
        * `uploadToMongo.py`: Script to upload scraped data to MongoDB.

**Installation:**

## Step 1: Clone the repository
```bash
git clone <repo-url>
```

## Step 2: docker-compose up
```bash
docker-compose up
```

## Step 3: Open the browser
Open the browser and go to `http://localhost:2423/` to access the Airflow UI.
username: legacy
password: legacy


## Contributing:

**Feel free to fork this repository, make improvements, and submit pull requests!**
