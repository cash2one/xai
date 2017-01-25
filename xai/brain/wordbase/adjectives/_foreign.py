

#calss header
class _FOREIGN():
	def __init__(self,): 
		self.name = "FOREIGN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
