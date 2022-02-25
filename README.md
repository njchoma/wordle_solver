# Wordle solver using information theory

This solver provides guesses based upon their expected information content, measured in bits. 
It assumes each word in the solution list is equally likely to be the hidden word.

## Operation

```
python3 -m venv /path/to/wordle_env
source /path/to/wordle_env/bin/activate
pip install numpy tqdm
python wordle_solver.py
```
