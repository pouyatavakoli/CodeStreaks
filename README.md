# CodeStreaks 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/)
[![Codeforces API](https://img.shields.io/badge/Codeforces-API-success)](https://codeforces.com/apiHelp)

<!-- Hidden for now, uncomment when needed
[![GitHub Release](https://img.shields.io/github/v/release/pouyatavakoli/CodeStreaks)](https://github.com/pouyatavakoli/CodeStreaks/releases)
-->

A command-line tool to track competitive programming streaks on Codeforces for you and your friends. Compete on a leaderboard and visualize progress with emoji art!

## Features ✨

- 📅 Track daily problem-solving streaks on Codeforces  
- 🏆 Generate leaderboards for you and your friends  
- 🎨 Create customizable emoji art visualizations  
- ⚡ Lightweight CLI interface with quick setup  

---

## Installation 📦

Clone the repository:
```bash
git clone --depth 1 https://github.com/pouyatavakoli/CodeStreaks.git
cd CodeStreaks
```
## Configuration ⚙️
Before running the script:
- Add  all Codeforces handles to ```handles.txt``` (one per line) to track similar to this:
``` text
tourist
jiangly
orzdevinwang
```

## Usage 📟

### Basic Tracking 
this generates a basic leader board
```bash
python3 -m CodeStreaks.main
```
### Generate Emoji Art Visualization

```bash
python3 -m CodeStreaks.main --emoji-art
```

### Command Line Options

| Flag           | Description                                          |
|----------------|----------------------------------------------------- |
| --help         | Generate streak visualization using emoji patterns   |
| --emoji-art    | Show help message and available flags                |



## Testing 🧪
Run the test suite with:
```bash
python3 -m unittest discover -s tests
```
