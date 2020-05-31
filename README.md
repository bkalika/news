Run Docker: if you have installed the Docker: run the the terminal the command "docker-compose up --build",
else install docker and run this command.
f
Links for Postman collection and environments:

Collection: https://github.com/bkalika/news/blob/master/NEWS-API.postman_collection.json
TEST environment: https://github.com/bkalika/news/blob/master/TEST.postman_environment.json
PROD environment: https://github.com/bkalika/news/blob/master/PROD.postman_environment.json
Link to Heroku (but it does not work properly): https://yoursupernews.herokuapp.com/api/v1/post/

For recurring job running to reset post upvotes count you can use Cronetab. For activate cronetab
just need to call the command: "python crone/crone_file.py".
For more information about cronetab: https://code.tutsplus.com/tutorials/managing-cron-jobs-using-python--cms-28231