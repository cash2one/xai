

#calss header
class _PRETEND():
	def __init__(self,): 
		self.name = "PRETEND"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
