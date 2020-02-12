# Juniper Firmware Application - ***This Project has been shut down*** 
This program is web app that connects to a database and returns information about the recommended version level for a particular Juniper switch. The user can add new switches and their respective version levels.
<br><br>
The application is usable via: [this link](http://mscs621.rlyn.ch:5000).
<br><br>
This application was created by Robert Lynch for Marist College MSCS621 - Cloud Computing in Fall 2019. Information for this application is provided by Juniper Networks.
<br><br><br>
## Overview
This application consists of two services: a user interface, and a database. Users interact directly with the user interface (UI) in order to preform the basic functions of the application. When the user interacts with the UI, the UI then interacts with the database. Informations is either retrieved or added.

<br><br>
This application runs on a multi cloud consisting of services on Amazon Web Services (AWS) and IBM Cloud.
## How it Works
This applications consists of two functions: retrieving data and adding data.<br><br>


**Retrieving Data**<br>
To retrieve data, the user should go to the `Get Data` page. Once on this page, the user can select from a device list. When the user has selected the device they want information about, he or she should hit submit and the data will be retrieved.

<br><br>
**Adding Data**<br>
To add data, the user shouw go to the `Add Data` page. Once at the `Add Data` page, the user should fill in the blanks with basic information. The blanks are as follows:<br>
_Slug_ -  The slug is the ID the switch, this should not have any spaces in it.<br>
_Switch Name_ - The switch name is the name that is displayed to the user<br>
_Recommended Version_ - The recommended version is the firmware level that JTAC provides.<br>

<br>
Once these are filled in, the user can hit the submit button and he or she will see if the submit was successful.
