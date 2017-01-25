

#calss header
class _POPULAR():
	def __init__(self,): 
		self.name = "POPULAR"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
