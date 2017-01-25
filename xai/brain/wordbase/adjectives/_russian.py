

#calss header
class _RUSSIAN():
	def __init__(self,): 
		self.name = "RUSSIAN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
