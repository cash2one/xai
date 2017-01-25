

#calss header
class _HISTORICAL():
	def __init__(self,): 
		self.name = "HISTORICAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
