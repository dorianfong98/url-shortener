


<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This is a URL Shortener application.

A URL shortener is a service that converts a provided long URL - https://some.domain.com/some-path-to/somewhere - into a shorter one like https://w.xyz/abcdef.

Built with Python, Django, with AJAX. This application was designed such that there is both a web-browser-accessible frontend web application, and a backend service which the frontend connects to via a HTTP-based API. 

As this project is purely MVP-scoped, I have not deployed it online. However, feel free to clone this project and run it locally on your computer. 

## Getting Started

To get started using the application, you can either simply head over to

Alternatively, if you would like to run this locally, you may download the .zip file, open the terminal, redirect to  the 'url_shortener' directory, and run `python manage.py runserver` in your terminal. 

Note: As this file runs on PORT 8000, make sure that it is not already in use. 
To check and kill processes running on the port:

For **Linux/Mac OS** search (sudo) run this in the terminal:

`$ lsof -i tcp:8000` <br />
`$ kill -9 PID`

On **Windows**:

`netstat -ano | findstr :8000`<br />
`tskill typeyourPIDhere` 



<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Dorian Fong - [My Website](https://dorianfong98.github.io/) | [My Email](mailto:dorianfong@u.nus.edu) | [My LinkedIn](https://www.linkedin.com/in/dorianfong/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

