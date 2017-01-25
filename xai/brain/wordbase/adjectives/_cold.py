

#calss header
class _COLD():
	def __init__(self,): 
		self.name = "COLD"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
