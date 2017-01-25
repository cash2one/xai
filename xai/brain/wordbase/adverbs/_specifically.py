

#calss header
class _SPECIFICALLY():
	def __init__(self,): 
		self.name = "SPECIFICALLY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
