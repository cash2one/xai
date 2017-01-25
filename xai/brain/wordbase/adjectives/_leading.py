

#calss header
class _LEADING():
	def __init__(self,): 
		self.name = "LEADING"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
