# collect-diamonds
A simple script to be used with Windows Tash Scheduler to collect diamonds from coin market cap.

Create and fill a collectDiamonds.bat with the following:
    cd *replace with saved location of collect-diamonds repository*
    main.py

Create a loginDetails.yml file with the following:
    coinmarketcap_user:
        email: *replace with email*
        password: *replace with password*
Save this loginDetails.yml file in the collect-diamonds repository.

Download and save ChromeDriver (https://chromedriver.chromium.org/downloads) in the collect-diamonds repository.