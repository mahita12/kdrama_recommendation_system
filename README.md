# Kdrama Recommendation System
This project uses webscraping to get data from a Kdrama website and builds a content-based Kdrama recommendation system using the genre of a Kdrama. Python is the programming language used to code this project.

# Details
As an avid Kdrama viewer, I am always on the lookout for new dramas. It only made sense to automate this for me and that is how this project came to be. I broke down this project into two parts.

1. [Webscraping](#webscraping)
2. [Building the recommendation system](#building-the-recommendation-system)

## Webscraping 

The [website](https://mydramalist.com/shows/top_korean_dramas?page=1) I chose has a list of the top 100 Kdramas.

<img width="600" alt="image" src="https://user-images.githubusercontent.com/38627648/233736290-67d0a9df-70e5-4a2a-8f5f-ef14676a5362.png">

To extract information from each drama, I needed to have a list of all the links of all the dramas and then use each link to go the Kdramas' page.

<img width="600" alt="image" src="https://user-images.githubusercontent.com/38627648/233737185-6b3cee49-3e0b-4223-8c2a-15f42675b123.png">

To do this, I used webscraping and extracted all the links for each Kdrama page.

<img width="399" alt="image" src="https://user-images.githubusercontent.com/38627648/233736750-96269164-47e6-4acb-aeac-2921c8b9f463.png">

I then traversed through each link to obtain relevant information such as Title, Genre and Score.

<img width="399" alt="image" src="https://user-images.githubusercontent.com/38627648/233737478-b86916c4-17d5-46f4-a170-c60769621ce8.png">

<img width="399" alt="image" src="https://user-images.githubusercontent.com/38627648/233737857-28ea3281-dbd9-4c2a-bca5-6fdd87bc6434.png">

Once I had all the information I needed, I then loaded this into a DataFrame.

## Building the recommendation system

For the recommendation system itself, I decided a simple content-based system would work well with my data. I then tokenized my text column which is 'Genre' and then used cosine similarity to assign similarity to different Kdramas.

<img width="399" alt="image" src="https://user-images.githubusercontent.com/38627648/233738784-37c29d9f-28c9-42f8-951c-7105c55e748a.png">

To test, I printed out the recommendations for a Kdrama.

<img width="399" alt="image" src="https://user-images.githubusercontent.com/38627648/233739369-1969b82d-54d3-4e4e-8579-752e8879d18a.png">

# How to use

# Credits

1. [Kdrama Website](https://mydramalist.com/shows/top_korean_dramas?page=1)
2. [Webscraping Resource](https://realpython.com/beautiful-soup-web-scraper-python/)
3. [Regular Expressions Resource](https://regex101.com/)
4. [Recommendation System Resource](https://medium.com/mlearning-ai/basic-content-based-recommendation-system-with-python-code-be920b412067)
5. [ReadMe Resource](https://meakaakka.medium.com/a-beginners-guide-to-writing-a-kickass-readme-7ac01da88ab3)

# Author
🌸**Surya Mahita Datla**

<img width="25" alt="image" src="https://user-images.githubusercontent.com/38627648/233743258-d256aee9-80c8-44e2-a816-cb787818eb62.png"> https://github.com/mahita12

<img width="25" alt="image" src="https://user-images.githubusercontent.com/38627648/233743545-82b5e583-9dd6-4366-92d5-47952954d745.png"> https://www.linkedin.com/in/mahita-datla-baa45076

<img width="25" alt="image" src="https://user-images.githubusercontent.com/38627648/233743885-93caca41-1109-4f98-ba82-ea0e7ad8f17d.png"> mahitadatla@yahoo.com

Please share a ⭐ if you like this project.






