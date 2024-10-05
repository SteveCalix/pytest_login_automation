Automated tests for https://practicetestautomation.com/practice-test-login were created using pytest
and selenium webdriver

Login tests are ran for chrome and firefox

Setup steps on local environment:
1. Install python. Latest version (3.12) is compatible.

2. Create a directory where all the code will be copied or downloaded to e.g. pytest_login_automation

3. Go to the directory cd /pytest_login_automation in this case

4. Create a virtual environment as not to mess up other python projects you may have by typing
    python -m venv .

5. Once the virtual environment is created, go to the created "Scripts" directory in windows or the "bin" directory in
   linux or mac and run the appropriate activate script
   source activate ->linux, mac
   activate.bat -> windows

6. Run the command below to install the required libraries
   pip install -r requirements.txt

7. To run the tests in the tests folder, run the following in the command line.
   pytest tests -sv
   The -sv flag would show the percent of the tests done in the console and the test currently running
