

#calss header
class _SURFACE():
	def __init__(self,): 
		self.name = "SURFACE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
