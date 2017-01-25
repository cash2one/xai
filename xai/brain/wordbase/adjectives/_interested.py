

#calss header
class _INTERESTED():
	def __init__(self,): 
		self.name = "INTERESTED"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
