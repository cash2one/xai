

#calss header
class _KIND():
	def __init__(self,): 
		self.name = "KIND"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
