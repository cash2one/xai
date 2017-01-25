

#calss header
class _EVERYWHERE():
	def __init__(self,): 
		self.name = "EVERYWHERE"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
