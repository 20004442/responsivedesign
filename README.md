# Design of Responsive Website
## AIM:
To design a responsive website with two break points.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:
### home.html
```
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <title>Responsive Aboutus Design</title>
</head>

<body>
    <div class="jumbotron">
        <div class="container text-center">
            <h1 class="display-3">Silicon Private Limited</h1>
            <h5 class="display-6">About Silicon Pvt Ltd</h5>
        </div>
    </div>
    <div class="homecontent">    
    <h1>About Us</h1>
    <img src="/static/img/building2.jpg" alt="Building">
    <div class="contenttext">
    Silicon Pvt Ltd, provides a broad range of semiconductor and infrastructure software applications that serve the data center, networking, software, broadband, wireless, and storage and industrial markets. Common applications for its products include: data center networking, home connectivity, broadband access, telecommunications equipment, smartphones, base stations, data center servers and storage, factory automation, power generation and alternative energy systems, displays, and mainframe operations and management, and application software development. Some of Silicon's core technologies and products include:
    <ul>
        <li>Memory Chips</li>
        <li>SATA HDD</li>
        <li>SATA SSD </li>
        <li>Broadband Modems</li>
        <li>Wifi Devices</li>
        <li>Switching Devices</li>
        <li>Optical Sensors</li>
    </ul> 
    </div>
    </div>
    <div class="row">
        <div class="col-12">
            <p>Copyright © 2021 Silicon Private Limited, Developed by kavya.</p>
        </div>
    </div>
   


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>

</body>

</html>
```
### productsresponsive.html
```
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Responsive Product Design</title>
</head>

<body>
    <div class="jumbotron">
        <div class="container text-center">
            <h1 class="display-3">Silicon Private Limited</h1>
            <h5 class="display-6">We Manufacture high quality electronic products</h5>
        </div>
    </div>
    <div class="container">
        <div class="row text-center">
            <div class="col-12 col-md-3 "><a href="/home">home</a></div>
            <div class="col-12 col-md-3 "><a href="/productsresponsive">productsresponsive</a></div>
            <div class="col-12 col-md-3 "><a href="/peopleresponsive">peopleresponsive</a></div>
            <div class="col-12 col-md-3 "><a href="/contactus">contactus</a></div>
        </div>
        <div class="row text-center">
            <div class="col-12">
                <h5 class="display-6">Our Premium Products</h5>
            </div>
        </div>
        <div class="row text-center">
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c1.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">4GB DDRA4 laptop memory</h5>
                    <p class="card-text">price: Rs.2000.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c2.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">1TB Laptop HDD</h5>
                    <p class="card-text">price: Rs.5000.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c3.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title"> Harddisk case </h5>
                    <p class="card-text">price: Rs.1800.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c4.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">Portable External Harddisk</h5>
                    <p class="card-text">price: Rs.5000.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c5.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">Waterproof SDD</h5>
                    <p class="card-text">price: Rs.5000.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c6.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">Harddrive Adapter</h5>
                    <p class="card-text">price: Rs.1000.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c7.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">Memory card for adapter</h5>
                    <p class="card-text">price: Rs.1000.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
            <div class="card col-12 col-md-6 col-lg-3">
                <img class="card-img-top" src="/static/img/c8.jpg" alt="card image cap">
                <div class="card-body">
                    <h5 class="card-title">2TB HDD</h5>
                    <p class="card-text">price: Rs.5000.00</p>
                    <a href="#" class="btn btn-primary">More Details</a>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <p>Copyright © 2021 Silicon Private Limited, Developed by kavya.</p>
            </div>
        </div>
    </div>


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>

</body>

</html>
```
### peopleresponsive.html
```
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Responsive People Design</title>
</head>

<body>
    <div class="jumbotron">
        <div class="container text-center">
            <h1 class="display-3">Silicon Private Limited</h1>
            <h5 class="display-6">crew </h5>
        </div>
    </div>
    <div class="row text-center">
        <div class="col-12">
            <h5 class="display-6">Our Crew </h5>
        </div>
    </div>
    <div class="row text-center">
        <div class="card col-12 col-md-6 col-lg-3">
            <img class="card-img-top" src="/static/img/p1.jpg" alt="card image cap">
            <div class="card-body">
                <h5 class="card-title">Angela Ahrendts </h5>
                <p class="card-text">Senior Vice President Retail</p>
                <a href="#" class="btn btn-primary">More Details</a>
            </div>
        </div>
        <div class="card col-12 col-md-6 col-lg-3">
            <img class="card-img-top" src="/static/img/p2.jpg" alt="card image cap">
            <div class="card-body">
                <h5 class="card-title">Jonathan Ive</h5>
                <p class="card-text">Senior Vice President Chief Design Officer </p>
                <a href="#" class="btn btn-primary">More Details</a>
            </div>
        </div>
        <div class="card col-12 col-md-6 col-lg-3">
            <img class="card-img-top" src="/static/img/p3.jpg" alt="card image cap">
            <div class="card-body">
                <h5 class="card-title">Luca Maestri </h5>
                <p class="card-text">Senior Vice President Chief Financial Officer</p>
                <a href="#" class="btn btn-primary">More Details</a>
            </div>
        </div>
        <div class="card col-12 col-md-6 col-lg-3">
            <img class="card-img-top" src="/static/img/p4.jpg" alt="card image cap">
            <div class="card-body">
                <h5 class="card-title">Dan Riccio</h5>
                <p class="card-text">Senior Vice President Hardware Engineering </p>
                <a href="#" class="btn btn-primary">More Details</a>
            </div>
        </div>
       <div class="card col-12 col-md-6 col-lg-3">
            <img class="card-img-top" src="/static/img/p5.jpg" alt="card image cap">
            <div class="card-body">
                <h5 class="card-title">Bruce Sewell</h5>
                <p class="card-text"> Senior Vice President General Counsel</p>
                <a href="#" class="btn btn-primary">More Details</a>
            </div>
        </div>
        <div class="card col-12 col-md-6 col-lg-3">
            <img class="card-img-top" src="/static/img/p6.jpg" alt="card image cap">
            <div class="card-body">
                <h5 class="card-title">Johny Srouji</h5>
                <p class="card-text"> Senior Vice President Hardware Technologies</p>
                <a href="#" class="btn btn-primary">More Details</a>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-12">
            <p>Copyright © 2021 Silicon Private Limited, Developed by kavya.</p>
        </div>
    </div>



    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
</body>

</html>
```
### contactus.html
```
<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <title>Responsive Contactus Design</title>   
</head>

<body>
    <div class="jumbotron">
        <div class="container text-center">
            <h1 class="display-3">Silicon Private Limited</h1>
            <h5 class="display-6">Contact Details of Silicon Private Limited</h5>
        </div>
    </div>

    <div class="contactuscontent">
    <h1>CONTACT US</h1>
    <div class="contactustext">
        <h1> Renuka (General Contact Manager),</h1>
        <h2> L. M. Silicon Products Private Limited,</h2>
        <h2>Anu Apartments-7th floor, Anna Nagar, Poonamalle, Chennai</h2>
        <h2> TamilNadu, India - 500081,</h2>
        <h2> contact number-9989596858</h2>
        <h3> Email address-Siliconprivatelimited@gmail.com</h3>

    </div>
    <div class="row">
        <div class="col-12">
            <p>Copyright © 2021 Silicon Private Limited, Developed by kavya.</p>
        </div>
    </div>
</div>


    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>

</body>

</html>
```

## OUTPUT:
![output](./static/img/output1.jpg)

![output](./static/img/output2.jpg)

![output](./static/img/output3.jpg)

![output](./static/img/output4.jpg)

![output](./static/img/output5.jpg)

![output](./static/img/output6.jpg)

![output](./static/img/output7.jpg)

![output](./static/img/output8.jpg)

### code validator report:
![output](./static/img/report1.jpg)

![output](./static/img/report2.jpg)

![output](./static/img/report3.jpg)

![output](./static/img/report4.jpg)
## RESULT:
Thus a responsive website is designed for the chip manufacturing company with two break points and is hosted in the URL http://kavya.student.saveetha.in:8000/. HTML code is validated.
