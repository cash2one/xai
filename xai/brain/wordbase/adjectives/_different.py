

#calss header
class _DIFFERENT():
	def __init__(self,): 
		self.name = "DIFFERENT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
