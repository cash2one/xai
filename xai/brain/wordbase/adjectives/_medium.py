

#calss header
class _MEDIUM():
	def __init__(self,): 
		self.name = "MEDIUM"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
