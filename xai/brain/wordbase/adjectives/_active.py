

#calss header
class _ACTIVE():
	def __init__(self,): 
		self.name = "ACTIVE"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
