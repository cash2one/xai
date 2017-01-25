

#calss header
class _FAVORITE():
	def __init__(self,): 
		self.name = "FAVORITE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
