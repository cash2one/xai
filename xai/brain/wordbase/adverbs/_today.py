

#calss header
class _TODAY():
	def __init__(self,): 
		self.name = "TODAY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
