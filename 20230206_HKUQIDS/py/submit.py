import pandas as pd
import datetime
import os

currentDate = "".join(str(datetime.datetime.now())[:10].split("-"))


def submit(ret):
    dt = pd.read_csv("../sub/sample_submission.csv")["date_time"].values
    nextVersion = 1
    try:
        file_list = os.listdir(f'../sub/')
        if file_list:
            maxVersion = 0
            for _file in file_list:
                if f'submission_{currentDate}_' in _file:
                    maxVersion = max(maxVersion, int(
                        _file.split("_")[-1][:-4]))
            nextVersion = maxVersion + 1
        with open(f'../sub/submission_{currentDate}_{nextVersion}.csv', "w") as f:
            f.write('date_time,return\n')
            for i, y in enumerate(ret):
                f.write('{},{}\n'.format(dt[i], y))
    except:
        pass
