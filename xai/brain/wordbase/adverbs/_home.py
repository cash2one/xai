

#calss header
class _HOME():
	def __init__(self,): 
		self.name = "HOME"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
