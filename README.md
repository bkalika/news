1. Run Docker:


2. Links for Postman collection and environments:
  - Collection:
    https://github.com/bkalika/news/blob/master/NEWS-API.postman_collection.json
  - TEST environment:
    https://github.com/bkalika/news/blob/master/TEST.postman_environment.json
  - PROD environment:
    https://github.com/bkalika/news/blob/master/PROD.postman_environment.json

4. Link to Heroku:


3. For recurring job running once a day to reset post upvotes count you can use Crone (schedule action).
For activate cronetab just need to call the command:
"python crone/crone_file.py"
For more information about cronetab:
https://code.tutsplus.com/tutorials/managing-cron-jobs-using-python--cms-28231
