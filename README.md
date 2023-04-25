# TechNewsViaCourier

<img width="1117" alt="Screenshot 2023-04-25 at 3 55 41 PM" src="https://user-images.githubusercontent.com/38040515/234249616-ec2785c0-c56e-481e-ac4e-aada122b77da.png">



## Inspiration 
In our fast-paced lives, it can be difficult to keep up with the news by constantly browsing channels or websites. To address this, we have developed a project that collects tech news from various sources, condenses the information, and delivers it straight to your email inbox using the Courier API. #TechNewsViaCourier Get Tech news delivered to your mail inbox.

## What it does
The project gathers tech news information from websites through webscraping, then summarizes and delivers the information to your email inbox using the Courier API.

FLOW:

DATABRICKS(Python) ---**REST API**---> NEWS WEBSITES(source) ------> WEB SCRAPING ------> RAW DATA ---**TRANSFORMATION**---> SUMMARIZED NEWS ---**COURIER API**---> MAIL INBOX

## HOW TO RUN THE PROJECT
FOLLOW ANY ONE OF THESE STEPS:
1) create a free login in https://community.cloud.databricks.com/ website, download the two code files and import in the databricks workspace.
create cluster and now change the auth_token and email_address respectively in techconfigs.py file and run the TechNewsViaCourier.py file.
or
2) Download the code and in techconfigs.py file instead of %run ./techconfigs , directly assign the values of auth_token, api_link, email_address from the techconfigs file. Run the code in any of the python desktop editor.


## What's next for World News via Courier
Adding more news sources: Currently, the project collects news from a limited number of sources. Adding more news sources would provide a wider range of news for users to read.
Integrating with social media: Integrating the project with social media platforms such as Twitter or Facebook would allow users to share news articles and stay up-to-date on the latest news.
User feedback: Gathering user feedback to identify any areas for improvement and implementing those suggestions could make the project more user-friendly and enhance the user experience.

