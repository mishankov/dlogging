DEFAULT_CONFIG = {
	"log_template": "[{date}][{file}]{style}[{mode}]{endstyle} - {message}",
	"file_template": "{}:{}",
	"level": "DEBUG",
	"DEBUG": {
		"output": ["console"],
		"style": ["bold"]
	}, 
	"INFO": {
		"output": ["console"],
		"style": ["bold", "cyan"]
	}
	, 
	"WARNING": {
		"output": ["console"],
		"style": ["bold", "yellow"]
	}
	, 
	"ERROR": {
		"output": ["console"],
		"style": ["bold", "red"]
	}
	, 
	"CRITICAL": {
		"output": ["console"],
		"style": ["bold", "red_background"]
	}
}

STYLE_DICT = {
	"bold": "1",
	"cyan": "96",
	"yellow": "93",
	"red": "91",
	"red_background": "101"
}