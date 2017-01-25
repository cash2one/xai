

#calss header
class _SEVERE():
	def __init__(self,): 
		self.name = "SEVERE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
