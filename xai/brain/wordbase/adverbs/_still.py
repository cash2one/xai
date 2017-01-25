

#calss header
class _STILL():
	def __init__(self,): 
		self.name = "STILL"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
