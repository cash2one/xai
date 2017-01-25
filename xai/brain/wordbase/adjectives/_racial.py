

#calss header
class _RACIAL():
	def __init__(self,): 
		self.name = "RACIAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
