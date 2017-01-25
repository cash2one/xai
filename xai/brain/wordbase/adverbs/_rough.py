

#calss header
class _ROUGH():
	def __init__(self,): 
		self.name = "ROUGH"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
