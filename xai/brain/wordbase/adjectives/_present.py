

#calss header
class _PRESENT():
	def __init__(self,): 
		self.name = "PRESENT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
