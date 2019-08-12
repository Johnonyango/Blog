# [Pitch]

## By John Onyango

## Description

The Blog web application is meant for users to create blogs by signing up, be able to view other blogs, delete, update and view comments on those blogs.

1. Health blogs
2. Educatinal blogs
3. Scientific blogs
4. Technology blogs

A user can select any of the categories from the navbar to view the blogs on these categories

##  User Stories
1. As a user one can create blogs after sign up and sign in.
2. As a user one can view, updtate and comment on blog posts
3. As a user one can be alerted when a new post is made by joining a subscription.
4. As a writer one can sign in to the blog.
5. As a writer one can create a blog from the application.
6. As a writer one can delete comments that they find insulting or degrading.
7. As a writer one can update or delete blogs they have created.


##  Behavior Driven Development
<table>
    <tr>
      <th>Behavior</th> 
      <th>Input</th> 
      <th>Output</th>   
    </tr>
    <tr>
        <td>Displaying various blog categories</td>
        <td>Click on a category</td>
        <td>The user lands to a page with several blogs on that category</td>
    </tr>
    <tr>
        <td>Subscribe</td>
        <td>User fills the subscribe form</td>
        <td>Redirects user to the home page to view posted blogs</td>
    </tr>
    <tr>
        <td>Sign up</td>
        <td>User fills the sign up form</td>
        <td>Redirects user to the login page</td>
    </tr>
    <tr>
        <td>Log in</td>
        <td>User fills the log in form</td>
        <td>Redirects user to home page in their profile accounts</td>
    </tr>
    <tr>
        <td>Add blog post</td>
        <td>The user clicks on the Add blog post button</td>
        <td>Redirects the user to the text area where they can add title then create their blog</td>
    </tr>
    <tr>
        <td>View recent blog posts</td>
        <td>The user scrolls down to the most recent blogs posted if any</td>
        <td>User sees posts with the options of update, comment on and delete post</td>
    </tr>
    <tr>
        <td>View profile</td>
        <td>Click on the user's name</td>
        <td>Redirects the user to the clicked user profile</td>
    </tr>
</table>

### Prerequisites

This web application requires the following software tools to operate
-Python version 3.6
-Flask
-Pip
-virtualenv
-A text  Editor
-SQLALCHEMY/Database


## Getting Started

* Clone this repository to your local computer.
* Ensure you have python3.6 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Create a virtual environment and access the folder via your virtual machine
 
 * run python3.6 manage.py server on the project directory

* Run ```chmod +x start.sh``` followed by ``` ./start.sh ``` while in the project folder to start the project.
* Once started, the project can be accessed on your localhost using the address: ``` localhost:5000 ```.
* This application can also be accessed by clicking the following link: 

## Technologies Used

* Python v3.6
* CSS(Boostrap/css.min)
* Flask
* Html

## Prepare environment variables
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/blog'

export SECRET_KEY='Your secret key'



## MIT License

Copyright (c) 2019 John Onyango

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 

Copyright (c) 2019 JOHN ONYANGO

