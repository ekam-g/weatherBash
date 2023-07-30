# Welcome to Weather Bash


## How do I use it?

just do this and every hour it will give you the latest weather on your terminal (macos/linux only)

```
$  bash <( curl -s https://raw.githubusercontent.com/carghai/weatherBash/main/weather.sh)
```

or you can use the python version with advanced error handling and colors(needs requests library)


Unix Systems

```
$ python <(curl -s https://raw.githubusercontent.com/carghai/weatherBash/main/weather.py)
```

Windows Systems

```
Invoke-WebRequest -Uri https://raw.githubusercontent.com/carghai/weatherBash/main/weather.py -OutFile weather.py
python weather.py
```