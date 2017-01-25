

#calss header
class _BELOW():
	def __init__(self,): 
		self.name = "BELOW"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
