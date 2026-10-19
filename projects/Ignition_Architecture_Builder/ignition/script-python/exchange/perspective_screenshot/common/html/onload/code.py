# Imports
from exchange.perspective_screenshot.common.common import BUTTON_COLOR, ICON_COLOR, CAPTURE_MODE, IMAGE_TYPE, DISTRIBUTION_ENDPOINT

# HTML Document Class
class HtmlDocument(object):
	""" """
	def __init__(self, elementId, captureMode, imageName, imageType, distribute=False, gateway=None, project=None):
		# Simple input validation
		self.isValid = all([captureMode in CAPTURE_MODE, imageType in IMAGE_TYPE])
		
		# Reformat inputs for html/javascript
		filename = '{0}.{1}'.format(imageName, imageType)
		distribute = 'true' if distribute else 'false'
		distributionEndpoint = DISTRIBUTION_ENDPOINT.format(gatewayAddress=gateway, project=project)
		
		# Create html document
		self.doc = """<!DOCTYPE html>
		<html lang="en">
			<head>
				<script src='https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js'></script>
				<script src='https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.0/FileSaver.min.js'></script>
				<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
				<script language="javascript">
				    function takeScreenshot() {
				    	// Set local storage to in progress
				    	localStorage.setItem('screenshot', 'in-progress');
				    	
				    	// Element id to capture
				    	var elementId = '""" + elementId + """';
				    	
				    	// Flag to capture entire page or only visible portion
				    	var captureMode = '""" + captureMode + """';
				    	
				    	// Flag on whether to distribute the screenshot or save locally
				    	var distribute = """ + distribute + """;
				    	
				    	// Get image data and format filename
				    	var element = parent.document.getElementById(elementId);
				        var filename = '""" + filename + """';
				        
				        // Get element's current overflow & height
				        var _overflow = element.style.overflow;
				        var _height = element.style.height;
				        
				        // Hide app bars, action panels
				        var app_bar = element.getElementsByClassName("app-bar");
				        var app_modal = element.getElementsByClassName("app-modal");
				        var action_panel = element.getElementsByClassName("action-panel");
				        const app_bar_style = [];
				        const action_panel_style = [];
				        const app_modal_style = [];
				        
				        // Temporary document modification if captureFlag is enabled
				        if (captureMode === "entire-page") {
				        	element.style.overflow = 'visible';
				        	element.style.height = 'auto';
				        	
				        	for (let i=0; i < app_bar.length; i++) {
				        		app_bar_style[i] = app_bar[i].style.visibility;
				        		app_bar[i].style.visibility = 'hidden';
				        	}
				        	
				        	for (let j=0; j < action_panel.length; j++) {
				        		action_panel_style[j] = action_panel[j].style.visibility;
				        		action_panel[j].style.visibility = 'hidden';
				        	}
				        	
				        	for (let k=0; k < app_modal.length; k++) {
				        		app_modal_style[k] = app_modal[k].style.visibility;
				        		app_modal[k].style.visibility = 'hidden';
				        	}
				        } else {
				        	element.style.overflow = 'hidden';
				        }
				        
				        var clientRects = element.getClientRects()[0];
				        
				        // Convert screenshot and save to downloads folder
				        html2canvas(element, {
				        	allowTaint: true
				        	, taintTest: false
				        	, foreignObjectRendering: true
				        	, logging: true
				        	, removeContainer: true
				        	, timeout: 180000
				        	, useCORS: true
				        	, x: -clientRects['x']
				        	, y: -clientRects['y']
				        	, height: clientRects['height']
				        	, width: clientRects['width']
				        }).then((canvas) => {
				        	const img_data = canvas.toDataURL("image/png");
				        	if (distribute) {
				        		console.log("Distributing Screenshot");
				        		var distributor = new XMLHttpRequest();
				        		distributor.open("POST", '""" + distributionEndpoint + """', true);
        				    	distributor.setRequestHeader('Content-Type', 'application/json');
				        		distributor.send(JSON.stringify({filename: filename, data: img_data}));
        				    	distributor.onload = function() {
        				    		var response = JSON.parse(this.responseText);
        				    		console.log(response);
        				    		
        				    		// Remove local storage item
        				    		localStorage.removeItem('screenshot');
        				    	};
				        	} else {
				        		window.saveAs(img_data, filename);
				        	};
				        	
				        	// Reset document overflow & height if required
				        	element.style.overflow = _overflow
				        	if (captureMode === "entire-page") {
					        	element.style.height = _height
					        	
					        	for (let i=0; i < app_bar_style.length; i++) {
					        		app_bar[i].style.visibility = app_bar_style[i];
					        	}
					        	
					        	for (let j=0; j < action_panel_style.length; j++) {
					        		action_panel[j].style.visibility = action_panel_style[j];
					        	}
					        	
					        	for (let k=0; k < app_modal_style.length; k++) {
					        		app_modal[k].style.visibility = app_modal_style[k];
					        	}
					        };
				        });
				    };
				</script>
			</head>
			<body>
				<script language="javascript">
					if (localStorage['screenshot'] != 'in-progress') {
						document.addEventListener("load", takeScreenshot());
					};
				</script>
			</body>
		</html>"""