FROM datajoint/jupyter:python3.6

RUN pip uninstall -y datajoint
RUN pip install "git+https://github.com/datajoint/datajoint-python.git@dev#egg=datajoint"
RUN pip install pynwb
ADD . /src/chen2017
RUN pip install -e /src/chen2017
