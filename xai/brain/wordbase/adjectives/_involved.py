

#calss header
class _INVOLVED():
	def __init__(self,): 
		self.name = "INVOLVED"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
