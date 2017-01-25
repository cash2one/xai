

#calss header
class _ONLINE():
	def __init__(self,): 
		self.name = "ONLINE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
