

#calss header
class _LOWER():
	def __init__(self,): 
		self.name = "LOWER"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
