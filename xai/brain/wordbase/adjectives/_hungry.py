

#calss header
class _HUNGRY():
	def __init__(self,): 
		self.name = "HUNGRY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
