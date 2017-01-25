

#calss header
class _PC():
	def __init__(self,): 
		self.name = "PC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
