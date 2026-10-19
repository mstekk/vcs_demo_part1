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
		<html id='perspective-screenshot-dom' lang="en" data-html2canvas-ignore="true">
			<head>
				<style>
				    :root {
				        --button-color: """ + BUTTON_COLOR + """;
				        --icon-color: """ + ICON_COLOR + """;
				        --size: 40px;
				    }
				    
				    * {
				    	box-sizing: border-box;
				    	overflow: visible;
				    	height: var(--size);
				    	width: var(--size);
				    }
				    
				    body {
				        display: contents;
				        margin: 0px;
				        padding: 0px;
				        overflow: visible;
				    }
				    
				    #screenshot-button {
				    	display: flex;
				    	flex-wrap: wrap;
				    	justify-content: center;
				    	align-items: stretch;
				    	color: var(--icon-color);
				    	border: 1px solid var(--icon-color);
				    	border-radius: 4px;
				    	background-color: var(--button-color);
				        transition: box-shadow, filter 0.3s;
				        overflow: hidden;
				        cursor: pointer;
					
				        &:hover {
				            box-shadow: 0px 0px 6px 0px rgba(0, 0, 0, 0.5);
				            filter: brightness(95%);
				        }
				    }
				    
				    .material-symbols-outlined {
				    	height: calc(var(--size) - 8px);
				    	width: calc(var(--size) - 8px);
				    	font-size: calc(var(--size) - 8px) !important;
				        font-variation-settings:
				        	'FILL' 1
				        	, 'wght' 400
				        	, 'GRAD' 0
				        	, 'opsz' 24
					}
					
					
					
					@keyframes spinner {
						0% {transform: rotate(0deg);}
						100% {transform: rotate(360deg);}
					}
				</style>
				<script src='https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js'></script>
				<script src='https://cdnjs.cloudflare.com/ajax/libs/FileSaver.js/2.0.0/FileSaver.min.js'></script>
				<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
				<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
				<script blocking="render" async language="javascript">
				    function takeScreenshot() {
				    	function setLoadingStart() {
				    		// Get button element
					    	var buttonReady = document.getElementById('screenshot-button-ready');
					    	
					    	// Swap to loading icon
					    	buttonReady.innerHTML = 'autorenew';
					    	buttonReady.style.animation = '3s linear infinite spinner';
					    	
					    	return new Promise((resolve) => {
							    setTimeout(() => {
							      // Other things to do before completion of the promise
							      console.log("Set loading state.");
							      // The fulfillment value of the promise
							      resolve(123);
							    }, 10);
							  });
				    	};
				    	
				    	function setLoadingEnd() {
				    		// Get button element
					    	var buttonReady = document.getElementById('screenshot-button-ready');
					    	
					    	
				        	
				        	return new Promise((resolve) => {
							    setTimeout(() => {
									// Other things to do before completion of the promise
							        console.log("Set loading end.");
							      	// Return to normal loading icon
				        			buttonReady.innerHTML = 'photo_camera';
				        			buttonReady.style.animation = '';
							      // The fulfillment value of the promise
							      resolve(123);
							    }, 10);
							  });
				    	};
				    	
				    	function captureScreenshot() {
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
					        	, foreignObjectRendering: true
					        	, logging: true
					        	, removeContainer: true
					        	, timeout: 180000
					        	, useCORS: false
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
					        })
					        .then(() => {
					        	setLoadingEnd();
					        })
					        .catch((error) => {
					        	console.log(error);
					        });
				    	};
				    	
				    	setLoadingStart()
				    		.then((result) => {
				    			captureScreenshot();
				    		});
				        
				    };
				</script>
			</head>
			<body data-html2canvas-ignore="true">
				<button id='screenshot-button' type="button" onclick="takeScreenshot()" data-html2canvas-ignore="true">
					<span id='screenshot-button-ready' class="material-symbols-outlined" style="align-self: center; animation='';">photo_camera</span>
				</button>
			</body>
		</html>"""