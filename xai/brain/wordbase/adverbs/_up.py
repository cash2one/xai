

#calss header
class _UP():
	def __init__(self,): 
		self.name = "UP"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
