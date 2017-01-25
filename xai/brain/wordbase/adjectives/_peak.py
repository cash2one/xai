

#calss header
class _PEAK():
	def __init__(self,): 
		self.name = "PEAK"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
