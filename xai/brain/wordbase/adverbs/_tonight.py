

#calss header
class _TONIGHT():
	def __init__(self,): 
		self.name = "TONIGHT"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
