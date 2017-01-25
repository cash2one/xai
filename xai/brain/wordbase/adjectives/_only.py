

#calss header
class _ONLY():
	def __init__(self,): 
		self.name = "ONLY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
