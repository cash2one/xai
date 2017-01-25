

#calss header
class _IN():
	def __init__(self,): 
		self.name = "IN"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
