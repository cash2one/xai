

#calss header
class _CHECK():
	def __init__(self,): 
		self.name = "CHECK"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
