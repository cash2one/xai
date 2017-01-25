

#calss header
class _LANDSCAPE():
	def __init__(self,): 
		self.name = "LANDSCAPE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
