

#calss header
class _ELECTRONIC():
	def __init__(self,): 
		self.name = "ELECTRONIC"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
