

#calss header
class _ABOVE():
	def __init__(self,): 
		self.name = "ABOVE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
