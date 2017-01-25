

#calss header
class _COOKING():
	def __init__(self,): 
		self.name = "COOKING"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
