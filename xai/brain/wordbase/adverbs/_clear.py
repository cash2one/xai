

#calss header
class _CLEAR():
	def __init__(self,): 
		self.name = "CLEAR"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
