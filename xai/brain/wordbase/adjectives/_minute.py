

#calss header
class _MINUTE():
	def __init__(self,): 
		self.name = "MINUTE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
