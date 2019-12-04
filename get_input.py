import requests
import sys

day=sys.argv[1]

data = requests.get(f"https://adventofcode.com/2019/day/{day}/input", verify=False, headers={"Cookie": "session=53616c7465645f5f8c7a21749fff093f3e3aa755abcb6f9d3eed0a0b8b3a4fd8edac1c595e5abd00279d1400c81facbb"})

with open(f"inp{day}.txt","w") as file:
    file.write(data.text)
