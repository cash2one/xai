

#calss header
class _UNDER():
	def __init__(self,): 
		self.name = "UNDER"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
