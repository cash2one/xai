

#calss header
class _BEDROOM():
	def __init__(self,): 
		self.name = "BEDROOM"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
