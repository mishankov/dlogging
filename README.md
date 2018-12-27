# dlogging, what is it?
Python logging module

# Why?
To use it my own projects and practice decorators and console output styling

# How to use?

```python
import dlogging as log


log.debug('debug')
log.info('info')
log.warning('warning')
log.error('error')
log.critical('critical')
log.info_forced('info_forced')
``` 

# Can I configure it?
Yeah! First time you run programm with imported dlogging module, it will create `dlogging.json` file in your working directory. It will help you to configure your output.

## How does default `dlogging.json` file look like?
Like this
```json
{
  "log_template": "[{date}][{file}]{style}[{mode}]{endstyle} - {message}",
  "file_template": "{}:{}",
  "level": "DEBUG",
  "DEBUG": {
    "outputs": [
      {
        "type": "console",
        "style": [
          "bold"
        ]
      }
    ]
  },
  "INFO": {
    "outputs": [
      {
        "type": "console",
        "style": [
          "bold",
          "cyan"
        ]
      },
      {
        "type": "file",
        "path": "{wd}/LOGS",
        "name": "dloggingOut.log"
      }
    ]
  },
  "WARNING": {
    "outputs": [
      {
        "type": "console",
        "style": [
          "bold",
          "yellow"
        ]
      },
      {
        "type": "file",
        "path": "{wd}/LOGS",
        "name": "dloggingOut.log"
      }
    ]
  },
  "ERROR": {
    "outputs": [
      {
        "type": "console",
        "style": [
          "bold",
          "red"
        ]
      },
      {
        "type": "file",
        "path": "{wd}/LOGS",
        "name": "dloggingOut.log"
      }
    ]
  },
  "CRITICAL": {
    "outputs": [
      {
        "type": "console",
        "style": [
          "bold",
          "red_background"
        ]
      },
      {
        "type": "file",
        "path": "{wd}/LOGS",
        "name": "dloggingOut.log"
      },
      {
        "type": "file",
        "path": "{wd}/LOGS",
        "name": "dloggingOutCritical.log"
      }
    ]
  }
}
```

## What does it all means?
### log_template
String template for your logs. You can use this tags to put data in it:
- `{date}` - date-time in `YYYY-MM-DD hh:mm:ss` format
- `{file}` - file, from where logging was called
- `{style}` and `{endstyle}` - where style formatting for console output starts and ends
- `{message}` - logging message

### level
Logging level like `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL` or `INFO_FORCED`. How logging levels works? Simple example:

If your logging level set to `INFO`, only messages with logging level higher then `INFO` (`WARNING`, `ERROR`, `CRITICAL` or `INFO_FORCED`) would be written.

### DEBUG, INFO, WARNING, ERROR, CRITICAL
Then there is field for each logging level except of `INFO_FORCED`. In each that field you can configure outputs with **outputs** list

#### outputs > type
It can be `console` or `file` to write your logs to console or file respectively

#### outputs > style
If **type** field equals `console` this list represents which would be used in `{style}` tag in **log_template**. Can hold up to 2 strings

#### outputs > path
If **type** field equals `file` this field represents path to your log file. Tag `{wd}` means your working directory

#### outputs > name
If **type** field equals `file` this field represents name of your log file