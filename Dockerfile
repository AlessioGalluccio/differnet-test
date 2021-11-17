FROM airlab404/dl:cuda10_pytorch_py36

WORKDIR /exp

# Install extras
#COPY requirements.txt requirements.txt
COPY . .
RUN conda install -c anaconda python=3.8
RUN pip install -r requirements.txt
#COPY . .
CMD ["python", "main.py"]


