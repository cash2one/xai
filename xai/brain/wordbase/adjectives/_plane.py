

#calss header
class _PLANE():
	def __init__(self,): 
		self.name = "PLANE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
