

#calss header
class _NORMALLY():
	def __init__(self,): 
		self.name = "NORMALLY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
