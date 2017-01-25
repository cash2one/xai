

#calss header
class _CHANGING():
	def __init__(self,): 
		self.name = "CHANGING"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
