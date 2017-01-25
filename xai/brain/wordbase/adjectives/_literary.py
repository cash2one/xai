

#calss header
class _LITERARY():
	def __init__(self,): 
		self.name = "LITERARY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
