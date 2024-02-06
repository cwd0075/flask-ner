# flask-ner
Python test driven development  
https://www.youtube.com/watch?v=eAPmXQ0dC7Q  
https://github.com/wesdoyle/flask-ner  

create the cheapest droplet on digitalocean  
login as root using putty, with privat.ppk key on evernote  

### ENVIRONMENT SETUP  
mkdir flask-ner  
cd flask-ner  
virtualenv env -p python3  
pip install spacy selenium pytest flask  
python -m spacy download en_core_web_sm  
mkdir static templates test  

vi setup.py and copy the file content from github  
:wq  
pip install -e .  

### WRITE TEST CODE  
cd test  
vi test_ner_client.py copy the file content from github  
:wq  
python -m pytest  

### WRITE PYTHON CODE  
cd ..  
vi ner_client.py  
:wq  
