

#calss header
class _NOTHING():
	def __init__(self,): 
		self.name = "NOTHING"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
