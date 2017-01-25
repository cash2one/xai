

#calss header
class _ONLY():
	def __init__(self,): 
		self.name = "ONLY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
