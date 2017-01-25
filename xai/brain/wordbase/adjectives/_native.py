

#calss header
class _NATIVE():
	def __init__(self,): 
		self.name = "NATIVE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
