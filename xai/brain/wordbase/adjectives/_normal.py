

#calss header
class _NORMAL():
	def __init__(self,): 
		self.name = "NORMAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
