

#calss header
class _RURAL():
	def __init__(self,): 
		self.name = "RURAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
