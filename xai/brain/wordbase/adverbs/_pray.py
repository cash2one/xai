

#calss header
class _PRAY():
	def __init__(self,): 
		self.name = "PRAY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
