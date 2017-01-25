

#calss header
class _SMOOTH():
	def __init__(self,): 
		self.name = "SMOOTH"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
