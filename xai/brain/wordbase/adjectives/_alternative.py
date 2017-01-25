

#calss header
class _ALTERNATIVE():
	def __init__(self,): 
		self.name = "ALTERNATIVE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
