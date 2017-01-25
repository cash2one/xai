

#calss header
class _PERMANENT():
	def __init__(self,): 
		self.name = "PERMANENT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
