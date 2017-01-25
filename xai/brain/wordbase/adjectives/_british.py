

#calss header
class _BRITISH():
	def __init__(self,): 
		self.name = "BRITISH"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
