

#calss header
class _CURRENT():
	def __init__(self,): 
		self.name = "CURRENT"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
