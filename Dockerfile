FROM airlab404/dl:cuda10_pytorch_py36

WORKDIR /exp

# Install extras
COPY docker/requirements.txt /requirements.txt
#COPY . .
RUN pip install -r requirements.txt
COPY docker .
CMD ["python", "main.py"]


