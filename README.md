# Cell Serial Converter

This is just a collection of simple functions to convert cellular serial numbers from one format to another. The function `translate_serial` will take any format (ESN, HEX ESN, MEID or IMEI) and convert to all other appropriate formats.

## Web Front End

A simple Flask web application provides a user-friendly interface for these conversions.

### Installation

```bash
pip install -r requirements.txt
```

### Usage

```bash
python app.py
```

Then open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

No license -- feel free to use this however you want.
