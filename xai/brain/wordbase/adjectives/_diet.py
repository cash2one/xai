

#calss header
class _DIET():
	def __init__(self,): 
		self.name = "DIET"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
