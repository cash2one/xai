

#calss header
class _OPPOSITE():
	def __init__(self,): 
		self.name = "OPPOSITE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
