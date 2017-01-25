

#calss header
class _STRAIGHT():
	def __init__(self,): 
		self.name = "STRAIGHT"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
