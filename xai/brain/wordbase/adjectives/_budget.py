

#calss header
class _BUDGET():
	def __init__(self,): 
		self.name = "BUDGET"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
