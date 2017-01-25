

#calss header
class _SAME():
	def __init__(self,): 
		self.name = "SAME"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
