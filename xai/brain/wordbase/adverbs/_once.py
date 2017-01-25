

#calss header
class _ONCE():
	def __init__(self,): 
		self.name = "ONCE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
