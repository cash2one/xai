

#calss header
class _THIN():
	def __init__(self,): 
		self.name = "THIN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
