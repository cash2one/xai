

#calss header
class _POINT():
	def __init__(self,): 
		self.name = "POINT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
