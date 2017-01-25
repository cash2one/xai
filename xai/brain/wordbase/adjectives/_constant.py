

#calss header
class _CONSTANT():
	def __init__(self,): 
		self.name = "CONSTANT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
