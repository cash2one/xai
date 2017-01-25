

#calss header
class _COLONIAL():
	def __init__(self,): 
		self.name = "COLONIAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
