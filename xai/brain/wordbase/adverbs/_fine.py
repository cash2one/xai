

#calss header
class _FINE():
	def __init__(self,): 
		self.name = "FINE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
