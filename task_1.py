import pandas as pd
from collections import Counter

def main():
    lottery_df = pd.read_csv("lottery.csv")
    valid_columns = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
    all_numbers = []
    for col in valid_columns:
        all_numbers = all_numbers + list(lottery_df[col])
    counter = Counter(all_numbers)
    counter_keys = list(counter.keys())
    counter_keys = sorted(counter_keys, key=lambda x: (-counter[x]))
    for key in counter_keys:
        print("The count for key {} is : {}".format(key, counter[key]))

if __name__ == '__main__':
    main()
