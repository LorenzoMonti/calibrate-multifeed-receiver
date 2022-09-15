# Calibrate-multifeed-receiver


## Download

This project is written in Python3 (3.8 but also compatible with the newest versions), so make sure you have it installed in your machine.
After that you can download the repository, open terminal and type:

```bash
git clone https://github.com/LorenzoMonti/calibrate-multifeed-receiver.git
```

Or if you are a windows user, you can download the executable from [Releases section](https://github.com/LorenzoMonti/calibrate-multifeed-receiver/releases/download/v0.8.0/calibrate_receiver.exe). Remember that you must have the NI-VISA drivers installed in order to proceed. All testing was done with NI-488.2 (<=17.6 version) for backward compatibility with GPIB-B interfaces.

## Project's dependecies

```bash
sudo apt-get install python3-tk

cd calibrate-multifeed-receiver/
python3 setup.py install
```

## Install
```bash
python3 setup.py install
```

## Usage

Now you can run the project:

```bash
calibrate_receiver
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
