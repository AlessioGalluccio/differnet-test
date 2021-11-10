FROM airlab404/dl:cuda10_pytorch_py36

WORKDIR /exp

# Install extras
COPY ../requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["bash"]


