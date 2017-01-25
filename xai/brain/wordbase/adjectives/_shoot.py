

#calss header
class _SHOOT():
	def __init__(self,): 
		self.name = "SHOOT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
