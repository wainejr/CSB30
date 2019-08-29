# Student's Dashboard

**Student's Dashboard** is a data mining/data visualization application that was implemented using a Flask backend, a Postgres Database, and an Angular frontend. 

The main goal is to show students what their class look like in terms of taste in music, movies and what they have in common.

## Database
Using a Postgres DBMS, data was stored. The main data was about movies, bands and relationship between students of the UTFPR’s database course. Most of the data was given to us by the students, but was later improved using using Spotify's API, Wikipedia's API and IMDb's API.

## Server side
A Python-powered RESTful API built from scratch using Flask. Serves the front-end with routes that get data from the database and preprocesses it before sending it.

## Client side
An Angular app built with TypeScript powers up the front-end. Using Chart.js we were able to show data in a beautiful and responsive way.

## What can be found in the app?
#### Most popular:
1. Music genres
1. Movie genres
1. Students
1. Hometowns
1. Movies
1. Bands

#### Trivia:
1. Degrees of separation (social connections away from each other)
1. Favorite movie decade 
1. Friends in commom
1. Etc 

## Folder structure
#### database/
    Files related to obtain and insert data in database. 

#### server/sandbox/server/
    Files related to database queries and routes.

#### client/src/app/
    Files related to Angular website.
    
## Members
* Giovanni Forastieri, @NEOGIGIO
* Ian Douglas Almeida Queros, @ianqueros
* Waine Barbosa de Oliveira Junior, @jr_waine

