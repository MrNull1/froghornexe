# froghorn.exe
### I'm too lazy to compile it so compile it yourself and submit a pr
## Usage
Download the executable from the releases page and run, best done on windows because of the name lol.
There's no actual malware, feel free to look at the code. All it does is open fullscreen and not close until the video has finished playing.
## Building
If you want to build it yourself, it's rather simple.

1. Set up a python venv however you see fit.
2. Clone the repository
3. Run this command to install the dependencies: ``` pip install -r requirements.txt ```
4. Test with `python3 froghorn.py` or build with `python -m PyInstaller --onefile --noconsole --add-data "video.mp4:." froghorn.py`
5. The built executable will be in the dist subdirectory.
