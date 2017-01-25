

#calss header
class _STRONG():
	def __init__(self,): 
		self.name = "STRONG"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
