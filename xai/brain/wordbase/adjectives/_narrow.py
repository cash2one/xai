

#calss header
class _NARROW():
	def __init__(self,): 
		self.name = "NARROW"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
