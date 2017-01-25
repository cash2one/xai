

#calss header
class _STATE():
	def __init__(self,): 
		self.name = "STATE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
