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

1. Clone the repository:

```bash
git clone --depth 1 https://github.com/pouyatavakoli/CodeStreaks.git
cd CodeStreaks
```
2. Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate 
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

**Note:** Python 3.6+ is required (comes pre-installed on most modern systems)
💡 You can deactivate the virtual environment anytime with ```deactivate```.

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
| --help         | Show help message and available flags                |
| --emoji-art    | Generate streak visualization using emoji patterns   |
| --only-accepted| Only count the accepted submissions                  |

## Testing 🧪

Run the test suite with:

```bash
python3 -m unittest discover -s tests
```

## Contributing 🤝

Contributions are welcome! Please follow these steps:

1. Check [TODO.md](TODO.md) for planned features
2. Open an issue to discuss proposed changes
3. Fork the repository
4. Create a feature branch
5. Submit a pull request with detailed description
