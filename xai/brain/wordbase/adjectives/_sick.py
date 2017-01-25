

#calss header
class _SICK():
	def __init__(self,): 
		self.name = "SICK"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
