import argparse
import shutil
import os
import time

ignore = [
    '.git',
    '.netlify',
    '.svelte-kit',
    'build',
    'node_modules',
    'scripts',
    'yarn.lock'
]

parser = argparse.ArgumentParser()

parser.add_argument("-in", "--entry", help="Entry")

args = parser.parse_args()

IN = args.entry

OUT = os.getcwd()

DIR = input("Type a writing dir: /")

shutil.copytree(IN, "{}/{}".format(OUT, DIR))

for name in ignore:

    if os.path.exists("{}/{}/{}".format(OUT, DIR, name)):

        os.system("rm -rf {}/{}/{}".format(OUT, DIR, name))

    else:

        print("Error when finding /{}".format(name))

print("Environment successfully ready ✨")

time.sleep(1)

print("Wait 2 seconds ...")

time.sleep(2)

os.system("code {}".format("{}/{}".format(OUT, DIR)))
