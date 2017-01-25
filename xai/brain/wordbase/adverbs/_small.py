

#calss header
class _SMALL():
	def __init__(self,): 
		self.name = "SMALL"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
