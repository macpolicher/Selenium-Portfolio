# Selenium-Portfolio

INSTRUCTIONS ON HOW TO RUN TEST:

1. Download The Project.
2. Open on Pycharm or other Editors.
3. If there is a pop-up asking for you to "Create Virtual Environment", Just Click Okay. Then proceed to step 4.

3.1 If there is no pop up, follow this steps:
3.2 open terminal and navigate to root folder.
3.3 create virtual environment by typing: pip install virtualenv
3.4 type: virtualenv venv
3.5 (for Mac OS / Linux) type: source venv/bin/activate
3.6 (for Windows) type: venv\Scripts\activate
4. Install the requirements by typing: pip install -r requirements.txt
5. Run the test by typing: pytest --html=report/report.html

-- The test should open up a browser and run the tests -- 

(Done! This will generate an HTML report located at "report" folder)


INFO:
- Created using Selenium, Python, and pytest
- I use Page Object Model and my own created framework
