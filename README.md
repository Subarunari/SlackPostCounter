# SlackPostCounter
[![Python](https://img.shields.io/badge/python-3.4-blue.svg)]
[![CircleCI](https://img.shields.io/circleci/project/github/RedSparr0w/node-csgo-parser.svg?style=flat&circle-token=01417825717dfd9978f6b1dbfe590c46066ab986)](https://circleci.com/gh/Subarunari/SlackPostCounter)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=svg)](https://github.com/Subarunari/SlackPostCounter/blob/master/LICENSE)

SlackPostCounter collect that number of posted message for each channel per day.

## Feature
* Python Scirpt
  * Executing SlackPostCounter　script whenever you want to.
  * `$ python cmd.py [csv | mongodb]`
* Saving Data Format
  * SlackPostCounter can save with following data format.
    * csv
    * MongoDB
* Differential Collecting
  * Recording the last collecting time. Next time, only collecting number of posted message from the last collecting time to the script execution time.
