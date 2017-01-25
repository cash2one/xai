

#calss header
class _POTENTIAL():
	def __init__(self,): 
		self.name = "POTENTIAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
