

#calss header
class _FLAT():
	def __init__(self,): 
		self.name = "FLAT"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
