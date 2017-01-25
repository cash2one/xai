

#calss header
class _NUCLEAR():
	def __init__(self,): 
		self.name = "NUCLEAR"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
