

#calss header
class _STOCK():
	def __init__(self,): 
		self.name = "STOCK"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
