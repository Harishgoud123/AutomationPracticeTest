implementation base on the http://automationpractice.com/index.php webpage.

**Tests were implemented and run on:**
Browsers: chrome, firefox
Selenium WebDriver: 3.4.2
Python: 3.8
pytest

**To Run Tests**
1. Clone/download the project
2. create virtual environment 
3. open terminal with created virtual environment and install the packages(using requirements.txt)

**Running tests**
Enter tests folder and use pytest command to run the tests(tests are categorized as positive and negative)
Ex: Use following command to run and generate html reports
pytest -v Test_DressesPage.py --html=Test_Dressespage.html
