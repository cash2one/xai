

#calss header
class _RIGHT():
	def __init__(self,): 
		self.name = "RIGHT"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
