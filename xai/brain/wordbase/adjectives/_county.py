

#calss header
class _COUNTY():
	def __init__(self,): 
		self.name = "COUNTY"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
