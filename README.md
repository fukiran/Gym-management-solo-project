In order to use please download and install: Python3, Flask, Psycopg2, PostgreSQL. In the Terminal in gym directory: "createdb gym", "psql -d gym -f db/gym.sql", "flask run". In the browser's address bar type "http://localhost:5000/".

App is build for gym employee to allow customers and classes management.

Brief:

A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

MVP:

The app should allow the gym to create and edit Members.
The app should allow the gym to create and edit Classes.
The app should allow the gym to book members on specific classes.
The app should show a list of all upcoming classes.
The app should show all members that are booked in for a particular class.


Extensions:

Classes could have a maximum capacity, and users can only be added while there is space remaining.
The gym could be able to give its members Premium or Standard membership. Standard members can only be signed up for classes during off-peak hours.
The Gym could mark members and classes as active/deactivated. Deactivated members/classes will not appear when creating bookings.

![Screenshot 2021-02-05 at 22 57 03](https://user-images.githubusercontent.com/72009564/107099535-dd327d00-6809-11eb-9012-635c21a91b0c.png)

![Screenshot2.png](https://github.com/fukiran/Gym_management_app/blob/main/static/images/Screenshot2.png)
