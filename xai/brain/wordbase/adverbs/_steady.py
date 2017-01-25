

#calss header
class _STEADY():
	def __init__(self,): 
		self.name = "STEADY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
