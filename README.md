# dlogging, what is it?
Python logging module

# Why?
To use it my own projects and practice decorators and console output styling

# How to use?

```python
import dlogging as log


log.debug('test_log')
log.info('test_log')
log.warning('test_log')
log.error('test_log')
log.critical('test_log')
log.info_forced('test_log')
``` 

# Can I configure it?
Yeah! First time you run programm with imported dlogging module, it will create `dlogging.json` file in your working directory. It will help you to configure your output.

## How does typical `dlogging.json` file look like?
Like this
```json
{
  "log_template": "[{date}][{file}]{style}[{mode}]{endstyle} - {message}",
  "file_template": "{}:{}",
  "level": "DEBUG",
  "DEBUG": {
    "output": [
      "console"
    ],
    "style": [
      "bold"
    ]
  },
  "INFO": {
    "output": [
      "console"
    ],
    "style": [
      "bold",
      "cyan"
    ]
  },
  "WARNING": {
    "output": [
      "console"
    ],
    "style": [
      "bold",
      "yellow"
    ]
  },
  "ERROR": {
    "output": [
      "console"
    ],
    "style": [
      "bold",
      "red"
    ]
  },
  "CRITICAL": {
    "output": [
      "console"
    ],
    "style": [
      "bold",
      "red_background"
    ]
  }
}
```
