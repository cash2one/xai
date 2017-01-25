

#calss header
class _PHYSICAL():
	def __init__(self,): 
		self.name = "PHYSICAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
