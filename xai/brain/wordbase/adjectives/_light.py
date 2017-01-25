

#calss header
class _LIGHT():
	def __init__(self,): 
		self.name = "LIGHT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
