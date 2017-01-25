

#calss header
class _ILL():
	def __init__(self,): 
		self.name = "ILL"
		self.jsondata = {}

	def run(self, verb):
		jsondata[verb] = {}
		jsondata[verb]['properties'] = self.name.lower()
		return jsondata
