

#calss header
class _ENGLISH():
	def __init__(self,): 
		self.name = "ENGLISH"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
