

#calss header
class _ALIVE():
	def __init__(self,): 
		self.name = "ALIVE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
