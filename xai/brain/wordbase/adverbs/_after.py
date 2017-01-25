

#calss header
class _AFTER():
	def __init__(self,): 
		self.name = "AFTER"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
