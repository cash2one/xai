

#calss header
class _FLAT():
	def __init__(self,): 
		self.name = "FLAT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
