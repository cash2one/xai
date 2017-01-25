

#calss header
class _CONVENTIONAL():
	def __init__(self,): 
		self.name = "CONVENTIONAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
