

#calss header
class _TRUE():
	def __init__(self,): 
		self.name = "TRUE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
