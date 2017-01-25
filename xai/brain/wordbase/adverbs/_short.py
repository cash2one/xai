

#calss header
class _SHORT():
	def __init__(self,): 
		self.name = "SHORT"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
