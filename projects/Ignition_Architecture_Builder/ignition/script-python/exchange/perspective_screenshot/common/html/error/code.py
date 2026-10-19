class HtmlDocument(object):
	""" """
	_doc = """<!DOCTYPE html>
	<html lang="en">
		<head>
			<style>
				<style>
					:root {
				        --size: 40px;
				    }
				    
				    * {
				    	box-sizing: border-box;
				    	overflow: visible;
				    	height: var(--size) !important;
				    	width: var(--size) !important;
				    }
				    
				    body {
				        display: contents;
				        margin: 0px;
				        padding: 0px;
				        overflow: visible;
				        user-select: none;
				    }
				    
				    .error-container {
				    	display: flex;
				    	flex-wrap: wrap;
				    	justify-content: center;
				    	align-items: center;
				    	color: red;
				    }
				    
					.material-symbols-outlined {
						height: calc(var(--size) - 8px);
				    	width: calc(var(--size) - 8px);
				    	font-size: calc(var(--size) - 8px) !important;
						font-variation-settings:
					  		'FILL' 0
					  		, 'wght' 400
					  		, 'GRAD' 0
					  		, 'opsz' 24
					}
				</style>
			</style>
			<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
		</head>
		<body>
			<div class="error-container">
				<span class="material-symbols-outlined" style="align-self: center">warning</span>
			</div>
		</body>
	</html>"""
	def __init__(self):
		self.doc = self._doc[:]