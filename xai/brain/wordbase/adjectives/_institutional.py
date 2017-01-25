

#calss header
class _INSTITUTIONAL():
	def __init__(self,): 
		self.name = "INSTITUTIONAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
