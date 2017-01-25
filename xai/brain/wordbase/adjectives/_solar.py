

#calss header
class _SOLAR():
	def __init__(self,): 
		self.name = "SOLAR"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
