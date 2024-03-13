# Sublime Text 4 JS Playground  
### Packages:
* terminus 
* origami 
* auto-save  

### Sublime building settings
```json
{  
  "target": "terminus_open",
	"shell_cmd": "C:/jsobserver.py \"$file\"",
  "post_window_hooks": [
    ["carry_file_to_pane", {"direction": "right"}]
  ],
}
```
