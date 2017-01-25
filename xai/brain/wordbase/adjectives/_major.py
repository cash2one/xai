

#calss header
class _MAJOR():
	def __init__(self,): 
		self.name = "MAJOR"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
