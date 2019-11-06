# British Passport Checker
_Checks the status on your British Passport Application and fetches the latest update._

## Usage:
Open script and replace the following values with your details:

* ref_num - The reference number provided to you by Gov.UK after your passport application is accepted.
* email   - The email used to sign up for your passport
* day     - Your 'day' of birth, as on the application
* month   - Your 'month' of birth, as on the application
* year    - Your 'year' of birth, as on the application

### Example
```
ref_num = "PEX 111 222 333"
email = "last_dance_with@maryJane.com"
day = "15"
month = "12"
year = "1888"
```

### Run script as ```python3 passport-checker.py```

## Improvements:
* Use try/except
* Offer the ability to read info from a file instead of modifying the script directly
* Run headless (currently if you run headless it seems to have trouble fetching xpath)
* Run as a cron job, writing the latest state to a file. Then, check the state in the file against the retrieved state every time the script runs. If states are different, report, else quit silently.
  * Possibly run this serverless too, in the cloud with S3 to store state

