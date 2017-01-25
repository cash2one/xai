

#calss header
class _OPPOSITE():
	def __init__(self,): 
		self.name = "OPPOSITE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
