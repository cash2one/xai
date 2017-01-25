

#calss header
class _LOW():
	def __init__(self,): 
		self.name = "LOW"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
