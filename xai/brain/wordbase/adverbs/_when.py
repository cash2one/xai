

#calss header
class _WHEN():
	def __init__(self,): 
		self.name = "WHEN"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata