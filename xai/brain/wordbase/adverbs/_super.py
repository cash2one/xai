

#calss header
class _SUPER():
	def __init__(self,): 
		self.name = "SUPER"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
