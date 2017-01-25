

#calss header
class _NOT():
	def __init__(self,): 
		self.name = "NOT"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
