

#calss header
class _NATIONAL():
	def __init__(self,): 
		self.name = "NATIONAL"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
