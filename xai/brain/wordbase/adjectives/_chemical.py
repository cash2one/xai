

#calss header
class _CHEMICAL():
	def __init__(self,): 
		self.name = "CHEMICAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
