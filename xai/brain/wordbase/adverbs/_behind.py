

#calss header
class _BEHIND():
	def __init__(self,): 
		self.name = "BEHIND"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
