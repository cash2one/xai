

#calss header
class _CHAMPION():
	def __init__(self,): 
		self.name = "CHAMPION"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
