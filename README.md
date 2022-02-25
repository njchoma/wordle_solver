# Wordle solver using information theory

This solver provides guesses based upon their expected information content, measured in bits. 
It assumes each word in the solution list is equally likely to be the hidden word.

## Operation

```
pip create -n /path/to/wordle_env
pip activate /path/to/wordle_env
pip install numpy tqdm
python wordle_solver.py
```
