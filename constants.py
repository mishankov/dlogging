DEFAULT_CONFIG = {
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

STYLE_DICT = {
	"bold": "1",
	"cyan": "96",
	"yellow": "93",
	"red": "91",
	"red_background": "101"
}

LOG_LEVELS_DICT = {
	"DEBUG": 0,
	"INFO": 1,
	"WARNING": 2,
	"ERROR": 3,
	"CRITICAL": 4,
	"INFO_FORCED": 99
}