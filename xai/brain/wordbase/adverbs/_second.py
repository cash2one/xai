

#calss header
class _SECOND():
	def __init__(self,): 
		self.name = "SECOND"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
