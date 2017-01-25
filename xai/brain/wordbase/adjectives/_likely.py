

#calss header
class _LIKELY():
	def __init__(self,): 
		self.name = "LIKELY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
