

#calss header
class _OFF():
	def __init__(self,): 
		self.name = "OFF"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
