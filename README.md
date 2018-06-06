## Run using Docker
    * git clone https://github.com/arifcse77/hubstaff-test-51.git
    * cd hubstaff-test-51
    * docker build -t hubstaff .
    * docker run -itd -p 5000:5000 --name hubstaff -v $(pwd):/code hubstaff
    * Open browser and put http://localhost:5000/users
    
## Run using local
    * git clone https://github.com/arifcse77/hubstaff-test-51.git
    * cd hubstaff-test-51
    * pip3 install -r requirements.txt
    * python3 application.py
    * Open browser and put http://localhost:5000/users
