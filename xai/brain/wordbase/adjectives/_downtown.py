

#calss header
class _DOWNTOWN():
	def __init__(self,): 
		self.name = "DOWNTOWN"
		self.jsondata = {}

	def run(self, obj):
		jsondata[obj] = {}
		jsondata[obj]['properties'] = self.name.lower()
		return jsondata
