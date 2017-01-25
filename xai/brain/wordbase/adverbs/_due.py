

#calss header
class _DUE():
	def __init__(self,): 
		self.name = "DUE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
