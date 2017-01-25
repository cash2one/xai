

#calss header
class _RANK():
	def __init__(self,): 
		self.name = "RANK"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
