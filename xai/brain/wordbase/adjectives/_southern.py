

#calss header
class _SOUTHERN():
	def __init__(self,): 
		self.name = "SOUTHERN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
