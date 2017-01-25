

#calss header
class _TRADE():
	def __init__(self,): 
		self.name = "TRADE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
