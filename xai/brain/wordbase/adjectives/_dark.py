

#calss header
class _DARK():
	def __init__(self,): 
		self.name = "DARK"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
