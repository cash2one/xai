

#calss header
class _ESSENTIAL():
	def __init__(self,): 
		self.name = "ESSENTIAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
