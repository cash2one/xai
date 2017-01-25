

#calss header
class _WIDE():
	def __init__(self,): 
		self.name = "WIDE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
