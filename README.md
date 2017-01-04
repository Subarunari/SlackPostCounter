# SlackPostCounter

SlackPostCounter collect that number of posted message for each channel per day.

## Feature
* Python Scirpt
  * Executing SlackPostCounter　script whenever you want to.
* Differential Collecting
  * Recording the last collecting time. Next time, only collecting number of posted message from the last collecting time to the script execution time.
* Saving Data Format
  * SlackPostCounter can save with following data format.
    * csv
    * MongoDB

# ToDo
- [ ] enable execute with command.
- [ ] create setup.py.
- [ ] create docker image including script and MongoDB environment.
