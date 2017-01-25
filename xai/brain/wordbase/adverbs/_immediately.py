

#calss header
class _IMMEDIATELY():
	def __init__(self,): 
		self.name = "IMMEDIATELY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
