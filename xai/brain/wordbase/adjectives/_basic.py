

#calss header
class _BASIC():
	def __init__(self,): 
		self.name = "BASIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
