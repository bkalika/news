1. Clone this repository.

2. After clonning this  repository:
- run the command "sudo lsof -i :5432"
- kill <pid:id>

3. Run Docker: if you have installed the Docker: run the the terminal the command "docker-compose up --build",
else install docker and run this command.

4. Go to the url: "http://127.0.0.1/api/v1/post/" and use this project as you need.

5. Links for Postman collection and environments:
  - Collection: https://github.com/bkalika/news/blob/master/NEWS-API.postman_collection.json
  - TEST environment: https://github.com/bkalika/news/blob/master/TEST.postman_environment.json
  - PROD environment: https://github.com/bkalika/news/blob/master/PROD.postman_environment.json

6. Link to Heroku (but it does not work properly):
  https://yoursupernews.herokuapp.com/api/v1/post/

7. For recurring job running to reset post upvotes count you can use Cronetab. For activate cronetab
just need to call the command: "python crone/crone_file.py".
For more information about cronetab: https://code.tutsplus.com/tutorials/managing-cron-jobs-using-python--cms-28231
