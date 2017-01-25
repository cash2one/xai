

#calss header
class _LIVING():
	def __init__(self,): 
		self.name = "LIVING"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
