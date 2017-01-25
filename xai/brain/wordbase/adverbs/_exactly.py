

#calss header
class _EXACTLY():
	def __init__(self,): 
		self.name = "EXACTLY"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
