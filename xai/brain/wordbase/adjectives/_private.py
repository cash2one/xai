

#calss header
class _PRIVATE():
	def __init__(self,): 
		self.name = "PRIVATE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
