

#calss header
class _OUT():
	def __init__(self,): 
		self.name = "OUT"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
