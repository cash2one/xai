

#calss header
class _FORTH():
	def __init__(self,): 
		self.name = "FORTH"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
