

#calss header
class _ALL():
	def __init__(self,): 
		self.name = "ALL"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
