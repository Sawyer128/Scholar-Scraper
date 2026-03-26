# Scholar-Scraper
![Yep](https://img.shields.io/badge/code-awesome-red) ![Oh yeah](https://img.shields.io/badge/project-coolest-indigo) ![One thousand percent](https://img.shields.io/badge/grade-highest-dark)

This is an awesome little project<sup id="a1">[1](#f1)</sup> that lets you search Google Scholar using SerpAPI, then it takes the sources you searched for and find the articles that **cited** the ones it searched for.!

Instructions to run are listed in the dropdown below!

<kbd>T</kbd> <kbd>H</kbd> <kbd>A</kbd> <kbd>N</kbd> <kbd>K</kbd> <kbd>S</kbd> <kbd>!</kbd>

---

<details>

<summary>In order to use...</summary>

Install the python packages: [serpapi](https://pypi.org/project/serpapi/), [rapidfuzz](https://pypi.org/project/RapidFuzz/), [dotenv](https://pypi.org/project/python-dotenv/), [requests](https://pypi.org/project/requests/).

Make sure to make a [SerpApi](https://serpapi.com/) Account, then **make a .env file and put your api key there** with the format `API_KEY=`.

Then you must **add the supposed titles of the articles your searching for into the `titles.txt`<sup id="a2">[2](#f2)</sup> file**.

Finally, run `main.py`.

_Heads up: The script will automatically create a folder named `output` in its directory, where it will place outputted files._

</details>

---

### Important

The journal article names in the texts files `titles.txt` and `titles2.txt` were taken from a database named [Academ-AI](https://www.academ-ai.info/).

### Footnotes

<b id="f1">1</b> <i>For AP Research.</i> [↩](#a1)<br>
<b id="f2">2</b> <i>Input file can be changed in the code when readwrite function is called in `main.py`.</i> [↩](#a2)