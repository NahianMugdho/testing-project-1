pip3 install selenium

pip install webdriver-manager


##a working Selenium script that:

Opens the site

Adds "Blackberry" to the cart

Proceeds to checkout

Completes the purchase

Takes a screenshot

Prints the success message

## PyTest-style test script and set up automated HTML report generation.

pip install pytest pytest-html selenium
pytest test_blackberry_purchase.py --html=report.html --self-contained-html
