

#calss header
class _ABOUT():
	def __init__(self,): 
		self.name = "ABOUT"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
