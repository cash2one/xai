

#calss header
class _WEAK():
	def __init__(self,): 
		self.name = "WEAK"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
