

#calss header
class _CONTEMPORARY():
	def __init__(self,): 
		self.name = "CONTEMPORARY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
