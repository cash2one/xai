

#calss header
class _AGRICULTURAL():
	def __init__(self,): 
		self.name = "AGRICULTURAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
