

#calss header
class _ALONG():
	def __init__(self,): 
		self.name = "ALONG"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
