

#calss header
class _HEADLINE():
	def __init__(self,): 
		self.name = "HEADLINE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
