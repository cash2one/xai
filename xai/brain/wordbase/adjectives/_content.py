

#calss header
class _CONTENT():
	def __init__(self,): 
		self.name = "CONTENT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
