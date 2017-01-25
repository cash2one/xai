

#calss header
class _EXISTING():
	def __init__(self,): 
		self.name = "EXISTING"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
