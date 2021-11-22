1. To run test cases for first install all libraris which listed in requirements.txt :
pip install -r requirements.txt
2. Set up environments to run py files
3. Connect to your local DB using your personal data for connection. Name of DB "TRN" which was used in SQL module.
4. You can open test_db.py and run tests using "play" icon  separately for each test or all test using "play" icon near "class TestDB" or run test using command: pytest -s -v your_path\Orlianskaia\tests\test_db.py
5. To create a test report follow the instruction below:

In python terminal use command:
1. Check allure version.
2. Create a folder with test reports: pytest -s -v your_path\Orlianskaia\tests\test_db.py --alluredir=report. After this action check that file "report" was created.
3. Generate test report: allure serve report
4. Click on link and enjoy your test report!

.



