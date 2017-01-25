

#calss header
class _OTHERWISE():
	def __init__(self,): 
		self.name = "OTHERWISE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
