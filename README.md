## midi2microbit
midi2microbit is a tool that converts .mid files to an array of string, that can be played by the micro:bit board.

### Installation
1. Clone the repository with
```
git clone https://github.com/skill3472/midi2microbit.git
```
2. Install the required dependencies, with
```
pip3 install -r midi2microbit/requirements.txt
```
### Usage
The reccomended way to use this tool is to pipe the output to a text file, then copy the array from there. Once copied, it can be pasted into your micro:bit script and played with music.play(). Please note, that due to the limited memory of most micro:bit boards, you may need to use the -s and -e arguments, to specify a portion of the song you want to play, otherwise the script might not compile to .hex properly.
```
usage: midi2microbit [-h] [-s START] [-e END] file

This script converts midi files, to strings playable with micro:bit

positional arguments:
  file                  The path to the midi file you want to convert.

options:
  -h, --help            show this help message and exit
  -s START, --start START
                        Starting note to extract from.
  -e END, --end END     Last note to extract to.

Use music.play(), to play the string. The --start and --end arguments might be useful, due to the limited memory   
of most micro:bit models.
```